from django.db import models

class blog(models.Model):
    title = models.CharField(max_length= 20)
    publish_date = models.DateField()
    image = models.ImageField(upload_to = 'images/')
    body = models.CharField(max_length= 20)
