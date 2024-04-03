from django.db import models



class PDF_TO_WORD(models.Model):
    file_name = models.CharField(max_length=200,blank=True,null=True)
    pdf_file = models.FileField(upload_to="word")
    result = models.URLField(blank=True,null=True)
    word_file = models.FileField(upload_to="word",blank=True,null=True)
    
    def __str__(self) -> str:
        if self.file_name:
            return self.file_name
        if self.result:
            return str(self.result)
        return str(self.pdf_file)

    
