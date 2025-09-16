from django.urls import path
from .import views
from django.views.generic import *

urlpatterns = [
    # path("home/", views.accueil, name="home"),
    # path("home", TemplateViews.as_view(template_name="monApp/page_home.html")),
    path("home/", views.HomeView.as_view()),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("home/<param>", views.accueil, name="accueil"),
    path("produits/", views.ListProduits, name="produits"),
    path("categories/", views.ListCategorie, name="categories"),
    path("statuts/", views.ListStatuts, name="statuts"),
    path("rayons/", views.ListRayons, name="rayons"),
]