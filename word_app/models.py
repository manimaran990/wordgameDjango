from django.db import models

# Create your models here.
class WordGame(models.Model):
	word = models.TextField()
	score = models.FloatField()
	dateval = models.TextField()