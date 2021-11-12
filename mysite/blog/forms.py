from django.forms import ModelForm 
from .models import Contact

class contactForm(ModelForm):
    class Meta :
        model = Contact 
        fields = "__all__"  #pour tous les champs de la table 