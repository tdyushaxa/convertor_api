from django.db.models.signals import post_save
from django.dispatch import receiver
from pdf2docx import Converter
from django.core.files import File as djangofile
from api.models import PDF_TO_WORD, ImageOCR
from easyocr import Reader
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

@receiver(post_save, sender=PDF_TO_WORD)
def post_save_pdf_to_word(sender, instance, created, *args, **kwargs):
    if created:
        pdf_id = instance.id
        docx_path = f"media-files/{str(instance).split('.')[0]}.docx"
        conv = Converter(pdf_file="media-files/" + str( instance))
        conv.convert(docx_filename=docx_path)
        file_obj = djangofile(open(docx_path, 'rb'))
        instance.word_file = file_obj
        instance.save()



@receiver(post_save,sender=ImageOCR)
def post_save_image_to_text(sender,instance,created,*args, **kwargs):
    if created:
        reader = Reader([instance.lang,'en'],gpu=False)
        text = reader.readtext(image=f"media-files/{str(instance)}",detail=0)
        instance.file_name = str(instance)
        instance.result = " ".join(text)
        instance.save()