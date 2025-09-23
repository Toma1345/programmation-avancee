from django.urls import path
from .import views
from django.views.generic import *

urlpatterns = [
    # path("home/", views.accueil, name="home"),
    # path("home", TemplateViews.as_view(template_name="monApp/page_home.html")),
    path("home/", views.HomeView.as_view(), name="home"),
    # path("about/", views.about, name="about"),
    path("about/", views.AboutView.as_view(), name="about"),
    # path("contact/", views.contact, name="contact"),
    # path("contact/", views.ContactView.as_view(), name="contact"),
    path("contact/", views.ContactView, name="contact"),
    path("email-sent/", views.EmailSentView.as_view(), name="email-sent"),
    # path("home/<param>", views.accueil, name="accueil"),
    path("home/<param>", views.HomeView.as_view(), name="accueil"),
    # path("produits/", views.ListProduits, name="produits"),
    path("produits/", views.ProduitListView.as_view(), name="lst_prdts"),
    path("produit/<pk>/", views.ProduitDetailView.as_view(), name="dtl_prdt"),
    # path("categories/", views.ListCategorie, name="categories"),
    path("categories/", views.CategorieView.as_view(), name="lst_cats"),
    path("categorie/<pk>/", views.CategorieDetailView.as_view(), name="dtl_cat"),
    # path("statuts/", views.ListStatuts, name="statuts"),
    path("statuts/", views.StatutView.as_view(), name="lst_sts"),
    path("statut/<pk>/", views.StatutDetailView.as_view(), name="dtl_statut"),
    # path("rayons/", views.ListRayons, name="rayons"),
    path("rayons/", views.RayonsView.as_view(), name="lst_rayons"),
    path("rayon/<pk>/", views.RayonDetailView.as_view(), name="dtl_rayon"),
    path('login/', views.ConnectView.as_view(), name='login'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.DisconnectView.as_view(), name='logout'),
]