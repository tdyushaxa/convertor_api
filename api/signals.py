from django.db.models.signals import post_save
from django.dispatch import receiver
from pdf2docx import Converter
from django.core.files import File as djangofile

from api.models import PDF_TO_WORD


@receiver(post_save, sender=PDF_TO_WORD)
def post_save_pdf_to_word(sender, instance, created, *args, **kwargs):
    if created:
        pdf_id = instance.id
        docx_path = f"media-files/{str(instance).split('.')[0]}.docx"
        conv = Converter(pdf_file="media-files/" + str(instance))
        conv.convert(docx_filename=docx_path)
        file_obj = djangofile(open(docx_path, 'rb'))
        instance.word_file = file_obj
