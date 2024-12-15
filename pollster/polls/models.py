from django.db import models

# Create your models here.
class Questions(models.Model): #extends model
    #id automatically created
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')