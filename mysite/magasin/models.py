from django.db import models
from datetime import date
# Create your models here.
class  Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballe')]
    libelle=models.CharField(max_length=100)
    description=models.TextField(default='Non definie')
    type = models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    img=models.ImageField(blank=True,default='aliment.jpg')
    Emballage=models.OneToOneField('Emballage',on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libelle+" "+self.description+" "+str(self.prix)

class Emballage(models.Model):
    COUL_CHOICES=[('bl','blanc'),('rg','rouge'),('ble','bleur'),('vr','vert'),('mulli','multicolore')]
    matiere=models.CharField(max_length=100)
    couleur=models.CharField(max_length=10,default='transparent',choices=COUL_CHOICES)

    def __str__(self):
        return self.matiere+" "+self.couleur  

class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)

    def __str__(self):
        return self.nom+" "+self.adresse+" "+self.email+" "+str(self.telephone)

class ProduitC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.Duree_garantie   

class Commande(models.Model):
    Duree_garantie=models.CharField(max_length=100)
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    Produits=models.ManyToManyField('Produit')

    def __dtr__(self):
        return self.Duree_garantie+" "+self.dateCde+" "+self.totalCde             


      




