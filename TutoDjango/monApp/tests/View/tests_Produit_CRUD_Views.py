# from django.test import TestCase
# from django.urls import reverse
# from monApp.models import Produit
# from django.contrib.auth.models import User

# class ProduitCreateViewTest(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', password='secret')
#         self.client.login(username='testuser', password='secret')
        
#     def test_produit_create_view_get(self):
#         response = self.client.get(reverse('crt-prdt'))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'monApp/create_produit.html')
        
#     def test_produit_create_view_post_valid(self):
#         data = {'intituleProd': 'ProduitPourTestCreation', 'prixUnitaireProd': 10.00, 'dateFab': '2024-01-01'}
#         response = self.client.post(reverse('crt-prdt'), data)
#         self.assertEqual(response.status_code, 302)  # Redirection après création
#         self.assertEqual(Produit.objects.count(), 1)
#         self.assertEqual(Produit.objects.last().intituleProd, 'ProduitPourTestCreation')
        
# class ProduitDetailViewTest(TestCase):
#     def setUp(self):
#         self.prdt = Produit.objects.create(intituleProd="ProduitPourTestDetail")
        
#     def test_produit_detail_view(self):
#         response = self.client.get(reverse('dtl_prdt', args=[self.prdt.refProd]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'monApp/detail_produit.html')
#         self.assertContains(response, 'ProduitPourTestDetail')
#         self.assertContains(response, "1")

# class ProduitUpdateViewTest(TestCase):
#     def setUp(self):
#         self.prdt = Produit.objects.create(intituleProd="ProduitPourTestUpdate")
#         self.user = User.objects.create_user(username='testuser', password='secret')
#         self.client.login(username='testuser', password='secret')
        
#     def test_produit_update_view_get(self):
#         response = self.client.get(reverse('prdt-chng', args=[self.prdt.refProd]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'monApp/update_produit.html')
        
#     def test_produit_update_view_post_valid(self):
#         self.assertEqual(self.prdt.intituleProd, "ProduitPourTestUpdate")
#         data = {'intituleProd': 'ProduitPourTestAferUpdate', 'prixUnitaireProd': 10.00, 'dateFab': '2024-01-01'}
#         response = self.client.post(reverse('prdt-chng', args=[self.prdt.refProd]), data)
#         self.assertEqual(response.status_code, 302)  # Redirection après mise à jour
#         self.prdt.refresh_from_db()
#         self.assertEqual(self.prdt.intituleProd, 'ProduitPourTestAferUpdate')
        
# class ProduitDeleteViewTest(TestCase):
#     def setUp(self):
#         self.prdt = Produit.objects.create(intituleProd="ProduitPourTestDelete")
#         self.user = User.objects.create_user(username='testuser', password='secret')
#         self.client.login(username='testuser', password='secret')
        
#     def test_produit_delete_view_get(self):
#         response = self.client.get(reverse('sup_prdt', args=[self.prdt.refProd]))
#         self.assertEqual(response.status_code, 200)
#         self.assertTemplateUsed(response, 'monApp/delete_produit.html')
        
#     def test_produit_delete_view_post(self):
#         response = self.client.post(reverse('sup_prdt', args=[self.prdt.refProd]))
#         self.assertEqual(response.status_code, 302)  # Redirection après suppression
#         self.assertFalse(Produit.objects.filter(refProd=self.prdt.refProd).exists())
#         self.assertRedirects(response, reverse('lst_prdts'))