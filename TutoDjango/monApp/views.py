from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from monApp.models import *

# def home(request, param=None):
#     #print(dir(request))
#     #print(request.__dict__)
#     # if request.GET and request.GET["test"]:
#     #     raise Http404
#     # return HttpResponse("Bonjour Monde !")
#     # return HttpResponseNotFound("Erreur fichier introuvable")
#     if request.GET and request.GET['name']:
#         string = request.GET['name']
#         return HttpResponse("Bonjour %s !" % string)
#     if param is None:
#         return HttpResponse("<h1>Bonjour !")
#     else:
#         return HttpResponse(f"<h1>Bonjour {param} !</h1>")

def ma_vue(request):
    return JsonResponse({'foo': 'bar'})
    
def accueil(request, param=None):
    if request.GET and request.GET['name']:
        param = request.GET['name']
        return render(request, 'monApp/home.html', {'param':param})
    return render(request, 'monApp/home.html', {'param':param})

def contact(request):
    return render(request, 'monApp/contact.html')

def about(request):
    return render(request, 'monApp/about.html')

def ListProduits(request):
    prdts = Produit.objects.all()
    return render(request, 'monApp/list_produits.html', {'prdts':prdts})

def ListCategorie(request):
    cats = Categorie.objects.all()
    return render(request, 'monApp/list_categories.html', {'cats':cats})

def ListStatuts(request):
    stats = Statut.objects.all()
    return render(request, 'monApp/list_statut.html', {'stats':stats})

def ListRayons(request):
    rayons = Rayon.objects.all()
    return render(request, 'monApp/list_rayons.html', {'rayons':rayons})
