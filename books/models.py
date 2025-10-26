from django.db import models

# Create your models here.

from django.db import models

class BookCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publish_date = models.DateField()
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    distribution_expenses = models.DecimalField(max_digits=12, decimal_places=2)
    def __str__(self):
        return self.title

