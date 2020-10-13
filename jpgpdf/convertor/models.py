from django.db import models

# Create your models here.
class taking_img(models.Model):
    name = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images', blank=True)
    #file_name = models.CharField(max_length=55555555555555555555)
    #file = models.FileField(upload_to='converted', blank=True)



class convention(models.Model):
    name = models.CharField(max_length=256)
    file = models.FileField(upload_to='converted', blank=False)