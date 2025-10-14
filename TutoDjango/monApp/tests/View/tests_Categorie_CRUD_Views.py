from django.test import TestCase
from django.urls import reverse
from monApp.models import Categorie
from django.contrib.auth.models import User

class CategorieCreateViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_categorie_create_view_get(self):
        response = self.client.get(reverse('crt-cat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/create_categorie.html')
        
    def test_categorie_create_view_post_valid(self):
        data = {'nomCat': 'CategoriePourTestCreation'}
        response = self.client.post(reverse('crt-cat'), data)
        self.assertEqual(response.status_code, 302)  # Redirection après création
        self.assertEqual(Categorie.objects.count(), 1)
        self.assertEqual(Categorie.objects.last().nomCat, 'CategoriePourTestCreation')
        
class CategorieDetailViewTest(TestCase):
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTestDetail")
        
    def test_categorie_detail_view(self):
        response = self.client.get(reverse('dtl_cat', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/detail_categorie.html')
        self.assertContains(response, 'CategoriePourTestDetail')
        self.assertContains(response, "1")

class CategorieUpdateViewTest(TestCase):
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTestUpdate")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_categorie_update_view_get(self):
        response = self.client.get(reverse('cat-chng', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/update_categorie.html')
        
    def test_categorie_update_view_post_valid(self):
        self.assertEqual(self.ctgr.nomCat, "CategoriePourTestUpdate")
        data = {'nomCat': 'CategoriePourTestAferUpdate'}
        response = self.client.post(reverse('cat-chng', args=[self.ctgr.idCat]), data)
        self.assertEqual(response.status_code, 302)  # Redirection après mise à jour
        self.ctgr.refresh_from_db()
        self.assertEqual(self.ctgr.nomCat, 'CategoriePourTestAferUpdate')
        
class CategorieDeleteViewTest(TestCase):
    def setUp(self):
        self.ctgr = Categorie.objects.create(nomCat="CategoriePourTestDelete")
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        
    def test_categorie_delete_view_get(self):
        response = self.client.get(reverse('sup_cat', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/delete_categorie.html')
        
    def test_categorie_delete_view_post(self):
        response = self.client.post(reverse('sup_cat', args=[self.ctgr.idCat]))
        self.assertEqual(response.status_code, 302)  # Redirection après suppression
        self.assertFalse(Categorie.objects.filter(idCat=self.ctgr.idCat).exists())
        self.assertRedirects(response, reverse('lst_cats'))