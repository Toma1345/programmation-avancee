from django.test import TestCase
from django.urls import reverse, resolve
from monApp.views import CategorieView, CategorieDetailView, CategorieCreateView, CategorieUpdateView, CategorieDeleteView

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