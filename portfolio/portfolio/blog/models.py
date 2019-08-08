from django.db import models


# Create your models here.

class visiter(models.Model):
    first_name = models.CharField(max_length=40)
    second_name = models.CharField(max_length=40)

    def str__(self):
        return self.first_name


class contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    messages = models.TextField()

    def str__(self):
        return self.email
