from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Article , Contact , Plage
from .forms import contactForm
# Create your views here.
def index(request):
    list=Article.objects.all()
    return render(request,'blog/contenu.html',{'list':list}) 

def index1(request):
    list1=Article.objects.all()
    return render(request,'blog/conseil.html',{'list1':list1})

def index2(request):
    if request.method == "POST" :
        form = contactForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/blog')
    else :
        form = contactForm() #créer formulaire vide
        return render(request,'blog/contact.html',{'form':form})

def index3(request):
    list2=Plage.objects.all()
    return render(request,'blog/plage.html',{'list2':list2})         





       
