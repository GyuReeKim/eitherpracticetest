from django.db import models

# Create your models here.
class Question(models.Model):
    title = models.CharField(max_length=100)
    choice_1 = models.CharField(max_length=100)
    choice_2 = models.CharField(max_length=100)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    pick = models.IntegerField()
    comment = models.CharField(max_length=100)