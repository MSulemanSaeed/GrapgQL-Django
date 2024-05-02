from django.db import models

class Restaurant(models.Model):
  name = models.CharField(max_length=100)
  staff_member = models.PositiveIntegerField()
  location = models.CharField(max_length=200)

  def __str__(self):
    return self.name

class Person(models.Model):
  name = models.CharField(max_length=20)
  age = models.PositiveIntegerField()

  def __str__(self) -> str:
    return self.name