from django.db import models
from django.contrib.auth.models import User
import os 
# Create your models here.


class Book(models.Model):
    book_name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/')
    pdf = models.FileField(upload_to='pdf/')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.book_name
    
    def delete(self, *args, **kwargs):
        if self.cover and os.path.isfile(self.cover.path):
            os.remove(self.cover.path)
        if self.pdf and os.path.isfile(self.pdf.path):
            os.remove(self.pdf.path)
        super().delete(*args, **kwargs)


class DownloadCount(models.Model):

    book= models.ForeignKey(Book, on_delete=models.CASCADE)
    download_count = models.PositiveIntegerField(default=0)