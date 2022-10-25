from django.db import models
from datetime import datetime
# from home.models import Contact

# Create your models here.
class contact(models.Model):
    name=models.CharField(max_length=122)
    mobile=models.CharField(max_length=12)
    pid=models.CharField(max_length=122)
    date=models.DateField()

