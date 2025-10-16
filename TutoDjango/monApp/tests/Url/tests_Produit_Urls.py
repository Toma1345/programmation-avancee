from django.test import TestCase
from django.urls import reverse, resolve
from monApp.models import Produit, Categorie, Statut
from monApp.views import ProduitCreateView, ProduitDeleteView, ProduitListView, ProduitDetailView, ProduitUpdateView
from django.contrib.auth.models import User
from decimal import Decimal
from datetime import date

class ProduitUrlsTest(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(nomCat="TempCat")
        self.statut = Statut.objects.create(libelle="TempStatus")
        self.produit = Produit.objects.create(
            intituleProd="ProduitTest",
            prixUnitaireProd=Decimal("10.00"),
            dateFab=date.today(),
            categorie=self.categorie,
            statut=self.statut
        )
        # Nécessaire pour les tests des vues CRUD (qui ont @login_required)
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')

    def test_produit_list_url_is_resolved(self):
        url = reverse('lst_prdts')
        self.assertEqual(resolve(url).view_name, 'lst_prdts')
        self.assertEqual(resolve(url).func.view_class, ProduitListView)

    def test_produit_detail_url_is_resolved(self):
        url = reverse('dtl_prdt', args=[self.produit.refProd])
        self.assertEqual(resolve(url).view_name, 'dtl_prdt')
        self.assertEqual(resolve(url).func.view_class, ProduitDetailView)
        
    def test_produit_create_url_is_resolved(self):
        url = reverse('crt-prdt')
        self.assertEqual(resolve(url).view_name, 'crt-prdt')
        self.assertEqual(resolve(url).func.view_class, ProduitCreateView)

    def test_produit_update_url_is_resolved(self):
        url = reverse('prdt-chng', args=[self.produit.refProd])
        self.assertEqual(resolve(url).view_name, 'prdt-chng')
        self.assertEqual(resolve(url).func.view_class, ProduitUpdateView)
        
    def test_produit_delete_url_is_resolved(self):
        url = reverse('sup_prdt', args=[self.produit.refProd])
        self.assertEqual(resolve(url).view_name, 'sup_prdt')
        self.assertEqual(resolve(url).func.view_class, ProduitDeleteView)

    # Test de réponse simple pour les vues qui nécessitent une connexion
    def test_produit_create_response_code_OK(self):
        response = self.client.get(reverse('crt-prdt'))
        self.assertEqual(response.status_code, 200)

    def test_produit_update_response_code_OK(self):
        response = self.client.get(reverse('prdt-chng', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 200)

    def test_produit_delete_response_code_OK(self):
        response = self.client.get(reverse('sup_prdt', args=[self.produit.refProd]))
        self.assertEqual(response.status_code, 200)