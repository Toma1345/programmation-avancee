from monApp.forms import *
from monApp.models import *

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, Http404, JsonResponse
from django.views.generic import *

from django.contrib.auth import *
from django.contrib.auth.views import *
from django.contrib.auth.models import *

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.forms import BaseModelForm
from django.db.models import Count, Prefetch

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
        query = self.request.GET.get('search')
        if query:
            return Produit.objects.filter(intituleProd__icontains=query).select_related('categorie').select_related('statut').order_by("prixUnitaireProd")
        return Produit.objects.select_related('categorie').select_related('statut').order_by("prixUnitaireProd")
    
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

    def get_queryset(self):
        return Categorie.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(CategorieView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes catégories"
        return context
    
class CategorieDetailView(DetailView):
    model = Categorie
    template_name = "monApp/detail_categorie.html"
    context_object_name = "cat"

    def get_queryset(self):
        return Categorie.objects.annotate(nb_produits=Count('produits'))

    def get_context_data(self, **kwargs):
        context = super(CategorieDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail de la catégorie"
        context['prdts'] = self.object.produits.all()
        return context
     
class RayonsView(ListView):
    model = Rayon
    template_name = "monApp/list_rayons.html"
    context_object_name = "rayons"

    def get_queryset(self):
        return Rayon.objects.prefetch_related(
            Prefetch("contenirR", queryset=Contenir.objects.select_related("refProd"))
        )

    def get_context_data(self, **kwargs):
        context = super(RayonsView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes rayons"
        ryns_dt=[]
        for rayon in context['rayons']:
            total = 0
            for contenir in rayon.contenirR.all():
                total += contenir.refProd.prixUnitaireProd * contenir.Qte
            ryns_dt.append({'rayon': rayon, 'total_stock': total})
        context['ryns_dt'] = ryns_dt
        return context
    
class RayonDetailView(DetailView):
    model = Rayon
    template_name = "monApp/detail_rayon.html"
    context_object_name = "rayon"

    def get_context_data(self, **kwargs):
        context = super(RayonDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du rayon"

        prdts_dt = []
        total_rayon = 0
        total_nb_produit = 0

        for contenir in self.object.contenirR.all():
            total_produit = contenir.refProd.prixUnitaireProd * contenir.Qte
            prdts_dt.append({'produit': contenir.refProd,
                            'qte': contenir.Qte,
                            'prix_unitaire': contenir.refProd.prixUnitaireProd,
                            'total_produit': total_produit}
            )
            total_rayon += total_produit
            total_nb_produit += contenir.Qte

        context['prdts_dt'] = prdts_dt
        context['total_rayon'] = total_rayon
        context['total_nb_produit'] = total_nb_produit

        return context
    
class StatutView(ListView):
    model = Statut
    template_name = "monApp/list_statut.html"
    context_object_name = "stats"

    def get_queryset(self):
        return Statut.objects.annotate(nb_produits=Count('produitStatut'))

    def get_context_data(self, **kwargs):
        context = super(StatutView, self).get_context_data(**kwargs)
        context['titremenu'] = "Liste de mes status"
        return context
    
class StatutDetailView(DetailView):
    model = Statut
    template_name = "monApp/detail_statut.html"
    context_object_name = "stat"

    def get_queryset(self):
        return Statut.objects.annotate(nb_produits=Count('produitStatut'))

    def get_context_data(self, **kwargs):
        context = super(StatutDetailView, self).get_context_data(**kwargs)
        context['titremenu'] = "Détail du statut"
        context['prdts'] = self.object.produitStatut.all()
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
    if request.method == 'POST':
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
    
# def ProduitCreate(request):
#     if request.method == 'POST':
#         form = ProduitForm(request.POST)
#         if form.is_valid():
#             prdt = form.save()
#             return redirect('dtl_prdt', prdt.refProd)
#     else:
#         form = ProduitForm()
#     return render(request, "monApp/create_produit.html", {'form':form})

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')
class ProduitCreateView(CreateView):
    model = Produit
    form_class=ProduitForm
    template_name = "monApp/create_produit.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)
    
# def ProduitUpdate(request, id):
#     prdt = Produit.objects.get(id=id)
#     if request.method == 'POST':
#         form = ProduitForm(request.POST, instance=prdt)
#         if form.is_valid():
#             # mettre à jour le produit existant dans la base de données
#             form.save()
#             # rediriger vers la page détaillée du produit que nous venons de mettre à jour
#             return redirect('dtl_prdt', prdt.refProd)
#     else:
#         form = ProduitForm(instance=prdt)
#     return render(request,'monApp/update_produit.html', {'form': form})

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')    
class ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = "monApp/update_produit.html"

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        prdt = form.save()
        return redirect('dtl_prdt', prdt.refProd)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')        
class ProduitDeleteView(DeleteView):
    model = Produit
    template_name = "monApp/delete_produit.html"
    success_url = reverse_lazy('lst_prdts')


# Categorie

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')
class CategorieCreateView(CreateView):
    model = Categorie
    form_class=CategorieForm
    template_name = "monApp/create_categorie.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')    
class CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = "monApp/update_categorie.html"

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        cat = form.save()
        return redirect('dtl_cat', cat.idCat)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')        
class CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = "monApp/delete_categorie.html"
    success_url = reverse_lazy('lst_cats')

# Rayon

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')
class RayonCreateView(CreateView):
    model = Rayon
    form_class=RayonForm
    template_name = "monApp/create_rayon.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        r = form.save()
        return redirect('dtl_rayon', r.idRayon)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')    
class RayonUpdateView(UpdateView):
    model = Rayon
    form_class = RayonForm
    template_name = "monApp/update_rayon.html"

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        r = form.save()
        return redirect('dtl_rayon', r.idRayon)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')        
class RayonDeleteView(DeleteView):
    model = Rayon
    template_name = "monApp/delete_rayon.html"
    success_url = reverse_lazy('lst_rayons')

# Statut

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')
class StatutCreateView(CreateView):
    model = Statut
    form_class=StatutForm
    template_name = "monApp/create_statut.html"
    
    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        r = form.save()
        return redirect('dtl_statut', r.idStatut)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')    
class StatutUpdateView(UpdateView):
    model = Statut
    form_class = StatutForm
    template_name = "monApp/update_statut.html"

    def form_valid(self, form:BaseModelForm) -> HttpResponse:
        r = form.save()
        return redirect('dtl_statut', r.idStatut)

# Ajout du décorateur sur une CBV
@method_decorator(login_required, name='dispatch')        
class StatutDeleteView(DeleteView):
    model = Statut
    template_name = "monApp/delete_statut.html"
    success_url = reverse_lazy('lst_sts')

# @login_required(login_url='/monApp/login/')
# def my_view(request):
#     return render(request, 'monApp/home.html')