from django.urls import path
from .import views

urlpatterns = [
    path("home/", views.accueil, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("home/<param>", views.accueil, name="accueil"),
    path("produits/", views.ListProduits, name="produits"),
    path("categories/", views.ListCategorie, name="categories"),
    path("statuts/", views.ListStatuts, name="statuts"),
    path("rayons/", views.ListRayons, name="rayons"),
]