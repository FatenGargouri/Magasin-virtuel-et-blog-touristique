from django.shortcuts import render
#from django.template import loader
from django.http import HttpResponse
from .forms import ProduitForm
from .forms import FournisseurForm , CommandeForm 
from django.shortcuts import redirect
from .models import Produit , Fournisseur 


# Create your views here.
def index(request):
    #template=loader.get_template('mesProduits.html')
    list=Produit.objects.all()
    return render(request,'magasin/vitrine.html',{'list':list}) 
    
def index1(request):
    if request.method == "POST" :
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
        return render(request,'magasin/majProduits.html',{'form':form})

def index2(request):
    if request.method == "POST" :
        form1 = FournisseurForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/magasin')
    else :
        form1 = FournisseurForm() #créer formulaire vide
        return render(request,'magasin/fournisseursProd.html',{'form1':form1})

def index3(request):
    list1=Fournisseur.objects.all()
    return render(request,'magasin/fournisseurs.html',{'list1':list1})

def index4(request):
    if request.method == "POST" :
        form1 = FournisseurForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
            return redirect('/magasin')
    else :
        form2 = CommandeForm() #créer formulaire vide
        return render(request,'magasin/commande.html',{'form2':form2})

def index5(request):
    list3=Produit.objects.all()
    return render(request,'magasin/panier.html',{'list3':list3}) 

        

