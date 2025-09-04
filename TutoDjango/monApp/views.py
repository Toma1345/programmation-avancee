from django.shortcuts import render
from django.http import HttpResponse
from monApp.models import *

def home(request, param):
    return HttpResponse("<h1>Bonjour " + param + "!</h1>")

def home2(request):
    return HttpResponse("<h1>Bonjour !</h1>")

def contact(request):
    return HttpResponse("<h1>Contact us</h1><p>Texte...</p>")

def about(request):
    return HttpResponse("<h1>About us</h1><p>Texte...</p>")

def ListProduits(request):
    prdts = Produit.objects.all()
    reponse = "<ul>"
    for prod in prdts:
        reponse += f"<li>{prod.intituleProd}</li>"
    reponse += "</ul>"
    return HttpResponse(reponse)

def ListCategorie(request):
    cats = Categorie.objects.all()
    reponse = "<ul>"
    for cat in cats:
        reponse += f"<li>{cat.nomCat}</li>"
    reponse += "</ul>"
    return HttpResponse(reponse)

def ListStatuts(request):
    stats = Statut.objects.all()
    reponse = "<ul>"
    for stat in stats:
        reponse += f"<li>{stat.libelle}</li>"
    reponse += "</ul>"
    return HttpResponse(reponse)