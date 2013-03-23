from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
	headLine = models.CharField(max_length=50, blank=True)
	bodyText = models.CharField(max_length=300, blank=True)
	owner = models.ForeignKey(User)
	todoIsTicked = models.BooleanField(default=False)
