
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Emenitites(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name


class Book(models.Model):
    book_name = models.CharField(max_length=100)
    book_description = models.TextField()
    book_image = models.ImageField(upload_to='book_images/')
    book_file = models.FileField(upload_to='books/', null=True, blank=True)  # Optional based on your requirement
    price = models.IntegerField()
    emenities = models.ManyToManyField(Emenitites)

    def __str__(self):
        return self.book_name

from django.db import models

class PDF(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='pdfs/')

    def __str__(self):
        return self.title








