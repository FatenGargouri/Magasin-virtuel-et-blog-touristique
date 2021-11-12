from django.db import models
from datetime import date
# Create your models here.
class Article(models.Model):
    titre=models.CharField(max_length=100)
    image=models.ImageField(blank=True,default='voyage.jpg')
    description=models.TextField(default='Non definie')
    
    def __str__(self):
        return self.titre+" "+self.description+" "

class Contact(models.Model):
    nom=models.CharField(max_length=100)
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    message=models.CharField(max_length=100,default='Non definie')
    Avis=models.CharField(max_length=100,default='Non definie')
    

    def __str__(self):
        return self.nom+" "+self.email+" "+str(self.telephone) +self.message+" "+self.Avis +" " 

class Plage(models.Model):
    nom=models.CharField(max_length=100)
    image=models.ImageField(blank=True,default='voyage.jpg')
    description=models.TextField(default='Non definie')

    def __str__(self):
        return self.nom+" "+self.description+" "

