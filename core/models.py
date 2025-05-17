from django.db import models

class Book(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    Description = models.TextField()
    Image_Url = models.URLField()
    Country = models.CharField(max_length=100)  # Qo‘shilgan maydon
    def __str__(self):
        return self.Title

class Books_seller(models.Model):
    Title = models.CharField(max_length=200)
    Author = models.CharField(max_length=100)
    Description = models.TextField()
    Image_Url = models.URLField()

    def __str__(self):
        return self.Title
