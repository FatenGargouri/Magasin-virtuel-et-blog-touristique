from django.urls import path,include
from django.conf.urls import url
from . import views
urlpatterns = [
    path('',views.index),
    path('FormProduit/',views.index1),
    path('FournisseurForm/',views.index2),
    path('fournisseurs/',views.index3),
    path('CommandeForm/',views.index4),
    path('panier/',views.index5)
    
    
]