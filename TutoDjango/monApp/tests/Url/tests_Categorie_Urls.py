from django.test import TestCase
from django.urls import reverse, resolve
from monApp.views import CategorieView, CategorieDetailView, CategorieCreateView, CategorieUpdateView, CategorieDeleteView
from monApp.models import Categorie
from django.contrib.auth.models import User

class CategorieUrlsTest(TestCase):

    def test_categorie_list_url_is_resolved(self):
        url = reverse('lst_cats')
        self.assertEqual(resolve(url).view_name, 'lst_cats')
        self.assertEqual(resolve(url).func.view_class,CategorieView)
    
    def test_categorie_detail_url_is_resolved(self):
        url = reverse('dtl_cat', args=[1])
        self.assertEqual(resolve(url).view_name, 'dtl_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDetailView)
    
    def test_categorie_create_url_is_resolved(self):
        url = reverse('crt-cat')
        self.assertEqual(resolve(url).view_name, 'crt-cat')
        self.assertEqual(resolve(url).func.view_class, CategorieCreateView)
    
    def test_categorie_update_url_is_resolved(self):
        url = reverse('cat-chng', args=[1])
        self.assertEqual(resolve(url).view_name, 'cat-chng')
        self.assertEqual(resolve(url).func.view_class, CategorieUpdateView)
    
    def test_categorie_delete_url_is_resolved(self):
        url = reverse('sup_cat', args=[1])
        self.assertEqual(resolve(url).view_name, 'sup_cat')
        self.assertEqual(resolve(url).func.view_class, CategorieDeleteView)
        
    def test_categorie_list_response_code(self):
        response = self.client.get(reverse('lst_cats'))
        self.assertEqual(response.status_code, 200)
        
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTest")
        self.user = User.objects.create_user(username="testuser", password="secret")
        self.client.login(username="testuser", password="secret")
        
    def test_categorie_detail_response_code(self):
        url = reverse('dtl_cat', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_categorie_detail_response_code_404(self):
        url = reverse('dtl_cat', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_categorie_create_response_code_OK(self):
        response = self.client.get(reverse('crt-cat'))
        self.assertEqual(response.status_code, 200)
        
    def test_categorie_update_response_code_OK(self):
        url = reverse('cat-chng', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_categorie_update_response_code_404(self):
        url = reverse('cat-chng', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_categorie_delete_response_code_OK(self):
        url = reverse('sup_cat', args=[self.ctgr.idCat])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_categorie_delete_response_code_404(self):
        url = reverse('sup_cat', args=[9999])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
    
    def test_redirect_after_categorie_creation(self):
        response = self.client.post(reverse('crt-cat'), {'nomCat': 'CategoriePourTestRedirectionCreation'})
        self.assertEqual(response.status_code, 302)  # statut 302 = redirection
        self.assertRedirects(response, '/monApp/categorie/2/')
        
    def test_redirect_after_categorie_updating(self):
        response = self.client.post(reverse('cat-chng', args=[self.ctgr.idCat]), data={'nomCat': 'CategoriePourTestRedirectionMAJ'})
        self.assertEqual(response.status_code, 302)  # statut 302 = redirection
        self.assertRedirects(response, f'/monApp/categorie/{self.ctgr.idCat}/')
        
    def test_redirect_after_categorie_deletion(self):
        response = self.client.post(reverse('sup_cat', args=[self.ctgr.pk]))
        self.assertEqual(response.status_code, 302)  # statut 302 = redirection
        self.assertRedirects(response, reverse('lst_cats'))
        self.assertFalse(Categorie.objects.filter(pk=self.ctgr.pk).exists())