"""Proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include
from . import views
urlpatterns = [
    path('form/' , views.form , name="form"),
    path('form2/' , views.form2 , name="form2"),
    path('form3/' , views.form3 , name="form3"),
    path('form4/' , views.form4 , name="form4"),
    path('form5/' , views.form5 , name="form5"),
    path('form6/' , views.form6 , name="form6"),
    path('form7/' , views.form7 , name="form7"),
    path('form8/' , views.form8 , name="form8"),
    path('form9/' , views.form9 , name="form9"),
    path('form10/' , views.form10 , name="form10"),
    path('form11/' , views.form11 , name="form11"),
    path('form12/' , views.form12 , name="form12"),
    path('form13/' , views.form13 , name="form13"),
    path('k2/' , views.k2 , name="k2"),
    path('k3/' , views.k3 , name="k3"),
    path('k4/' , views.k4 , name="k4"),
    path('k5/' , views.k5 , name="k5"),
    path('k6/' , views.k6 , name="k6"),
    path('k7/' , views.k7 , name="k7"),
    path('k8/' , views.k8 , name="k8"),
    path('k9/' , views.k9 , name="k9"),
    path('k10/' , views.k10 , name="k10"),
    path('k11/' , views.k11 , name="k11"),
    path('k12/' , views.k12 , name="k12"),
    path('k13/' , views.k13 , name="k13"),
    path('k14/' , views.k14 , name="k14"),
    path('k15/' , views.k15 , name="k15"),
    path('k16/' , views.k16 , name="k16"),
    path('k17/' , views.k17 , name="k17"),
    path('buy/' , views.buy , name="buy")
]
