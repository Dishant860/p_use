"""dishant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views


urlpatterns = [
    
    path('', views.index, name='index'),
    path('saveenquiry', views.saveEnquiry, name='saveenquiry'), 
    path('jecalc', views.jecalc, name='jecalc'), 
    path('newtest', views.newtest, name='newtest'), 
    path('vdata', views.vdata, name='vdata'),
    path('dele/<int:id>', views.dele, name='dele'),
    path('bill', views.bill, name='bill'),
    path('billdata', views.billdata, name='billdata'),
    path('prints', views.prints, name='prints'),
    path('qrdecoder', views.qrdecoder, name='qrdecoder'),
    path('decodefun', views.decodefun, name='decodefun'),
    path('all_bills', views.all_bills, name='all_bills'),
    path('vieww/<int:id>', views.vieww, name='vieww'),
    path('searchbar', views.searchbar, name='searchbar'),
    path('dvieww/<int:id>', views.dvieww, name='dvieww'),
    path('vocabs', views.vocabs, name='vocabs'),
    path('vocab_check', views.vocab_check, name='vocab_check'),



    


 

]