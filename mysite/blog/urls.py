from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index),
    path('conseil/',views.index1),
    path('contactForm/',views.index2),
    path('plage/',views.index3)

]