from __future__ import unicode_literals

from django.db import models

# Create your models here.
class task(models.Model):
	myTask = models.CharField(max_length=20)
