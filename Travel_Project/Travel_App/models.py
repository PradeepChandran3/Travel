from django.db import models

# Create your models here.
class Place(models.Model):
    Name=models.CharField(max_length=250)
    Image=models.ImageField(upload_to='pics')
    Description=models.TextField()

    def __str__(self):
        return self.Name

class Team(models.Model):
    Surname=models.CharField(max_length=250)
    Picture=models.ImageField(upload_to='pics')
    Details=models.TextField()

    def __str__(self):
        return self.Surname