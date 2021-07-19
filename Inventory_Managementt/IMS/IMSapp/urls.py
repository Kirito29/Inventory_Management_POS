from django.urls import path 
from . import views 

urlpatterns = [
    path("", views.index, name= "Home"),
    path("page2/", views.page2, name= "This is the second page"),
]
