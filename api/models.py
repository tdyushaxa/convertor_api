from django.db import models


class PDF_TO_WORD(models.Model):
    file_name = models.CharField(max_length=200, blank=True, null=True)
    pdf_file = models.FileField(upload_to="word")
    result = models.URLField(blank=True, null=True)
    word_file = models.FileField(upload_to="word", blank=True, null=True)

    def __str__(self) -> str:
        if self.file_name:
            return self.file_name
        if self.result:
            return str(self.result)
        return str(self.pdf_file)


class ImageOCR(models.Model):
    image = models.ImageField(upload_to="Image-ocr")
    lang = models.CharField(max_length=200, blank=True, null=True)
    file_name = models.CharField(max_length=200, blank=True, null=True)
    result = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        if self.file_name:
            return self.file_name
        return str(self.image)


class ImageToPdf(models.Model):
    image = models.ImageField(upload_to='image-pdf')
    file_name = models.CharField(max_length=200)
    result = models.URLField(blank=True, null=True)

    def __str__(self):
        if self.file_name:
            return self.file_name
        return str(self.image)


