from django.db import models

# Create your models here.

class Student(models.Model):
  name = models.CharField(max_length=30)
  document = models.CharField(max_length=11)
  email = models.EmailField()

  def __str__(self):
    return self.name
