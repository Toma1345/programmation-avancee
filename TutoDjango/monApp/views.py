from django.shortcuts import render
# from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.views.generic import *
from monApp.forms import ContactUsForm
from monApp.models import *
from django.contrib.auth import *
from django.contrib.auth.views import *
from django.contrib.auth.models import *
from django.core.mail import send_mail
from django.shortcuts import redirect

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

# def ma_vue(request):
#     return JsonResponse({'foo': 'bar'})
    
# def accueil(request, param=None):
#     if request.GET and request.GET['name']:
#         param = request.GET['name']
#         return render(request, 'monApp/home.html', {'param':param})
#     return render(request, 'monApp/home.html', {'param':param})

# def contact(request):
#     return render(request, 'monApp/contact.html')

# def about(request):
#     return render(request, 'monApp/about.html')

# def ListProduits(request):
#     prdts = Produit.objects.all()
#     return render(request, 'monApp/list_produits.html', {'prdts':prdts})

# def ListCategorie(request):
#     cats = Categorie.objects.all()
#     return render(request, 'monApp/list_categories.html', {'cats':cats})

# def ListStatuts(request):
#     stats = Statut.objects.all()
#     return render(request, 'monApp/list_statut.html', {'stats':stats})

# def ListRayons(request):
#     rayons = Rayon.objects.all()
#     return render(request, 'monApp/list_rayons.html', {'rayons':rayons})

class HomeView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        
        if self.kwargs.get('param'):
            context['titreh1'] = "Bonjour " + self.kwargs.get('param') + ", vous êtes connecté !"
        else:
            context['titreh1'] = "Hello DJANGO"
        return context

    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
class AboutView(TemplateView):
    template_name = "monApp/page_home.html"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['titreh1'] = "About us ..."
        return context
    
    def post(self, request, **kwargs):
        return render(request, self.template_name)
    
# class ContactView(TemplateView):
#     template_name = "monApp/page_home.html"

#     def get_context_data(self, **kwargs):
#         context = super(ContactView, self).get_context_data(**kwargs)
#         context['titreh1']="Contact us ..."
#         return context
    
#     def post(self, request, **kwargs):
#         return render(request, self.template_name)

class ProduitListView(ListView):
    model = Produit
    template_name = "monApp/list_produits.html"
    context_object_name = "prdts"
    # queryset = Produit.objects.filter(refProd=2)

    def get_queryset(self):
        return Produit.objects.order_by("prixUnitaireProd")
    
    def get_context_data(self, **kwargs):
        context = super(ProduitListView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes produits"
        return context
    
class ProduitDetailView(DetailView):
    model = Produit
    template_name = "monApp/detail_produit.html"
    context_object_name = "prdt"

    def get_context_data(self, **kwargs):
        context = super(ProduitDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du produit"
        return context
    
class CategorieView(ListView):
    model = Categorie
    template_name = "monApp/list_categories.html"
    context_object_name = "cats"

    def get_context_data(self, **kwargs):
        context = super(CategorieView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context
    
class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        return context
     
class RayonsView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"

    def get_context_data(self, **kwargs):
        context = super(RayonsView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        return context
    
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"
        return context
    
class StatutView(ListView):
    model = Statut
    template_name = "monApp/list_statut.html"
    context_object_name = "stats"

    def get_context_data(self, **kwargs):
        context = super(StatutView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes status"
        return context
    
class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        return context
    
class ConnectView(LoginView):
    template_name = "monApp/page_login.html"

    def post(self, request, **kwargs):
        lgn = request.POST.get('username', False)
        pswrd = request.POST.get('password', False)
        user = authenticate(username=lgn, password=pswrd)
        if user is not None and user.is_active:
            login(request, user)
            return render(request, 'monApp/page_home.html', {'param': lgn, 'message': "You're connected"})
        else:
            return render(request, 'monApp/page_register.html')
        
class RegisterView(TemplateView):
    template_name = 'monApp/page_register.html'
    def post(self, request, **kwargs):
        username = request.POST.get('username', False)
        mail = request.POST.get('mail', False)
        password = request.POST.get('password', False)
        user = User.objects.create_user(username, mail, password)
        user.save()
        if user is not None and user.is_active:
            return render(request, 'monApp/page_login.html')
        else:
            return render(request, 'monApp/page_register.html')

class DisconnectView(TemplateView):
    template_name = 'monApp/page_logout.html'
    def get(self, request, **kwargs):
        logout(request)
        return render(request, self.template_name)
    
def ContactView(request):
    titreh1 = "Bienvenu sur la page Contact !"
    if request.method=='POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via TutoDjango Contact form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@monApp.com'],
            )
            return redirect('email-sent')
    else:
        form = ContactUsForm()
    return render(request, "monApp/page_home.html",{'titreh1':titreh1, 'form':form})

class EmailSentView(TemplateView):
    template_name = 'monApp/email-sent.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)