from django.urls import path 
from . import views

urlpatterns = [

    path('',views.home,name='urdu/home'),
    path('index/',views.index,name='urdu/index'),
    

]

