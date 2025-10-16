from django.test import TestCase
from django.urls import reverse
from unittest.mock import patch
from monApp.models import Categorie, Statut
from monApp.forms import ContactUsForm
from django.contrib.auth.models import User

class SimpleFunctionViewsTest(TestCase):
    def test_accueil_view(self):
        response_anon = self.client.get('/monApp/home/Anon')
        self.assertEqual(response_anon.status_code, 200)
        self.assertContains(response_anon, "<h1>Hello Anon !!!</h1>")
        
        response_param = self.client.get('/monApp/home/TestUser')
        self.assertEqual(response_param.status_code, 200)
        self.assertContains(response_param, "<h1>Hello TestUser !!!</h1>")

    def test_list_status(self):
        Statut.objects.create(libelle="TestStatus1")
        response = self.client.get('/monApp/statuts/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "TestStatus1")


class GenericViewsTest(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='secret')
        self.client.login(username='testuser', password='secret')
        self.home_url = '/monApp/home/'
        self.home_param_url = '/monApp/home/UserParam'
        self.about_url = '/monApp/about/'

    def test_home_view_get_context_no_param(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Hello  !!!</h1>")

    def test_home_view_get_context_with_param(self):
        response = self.client.get(self.home_param_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>Hello UserParam !!!</h1>")

    def test_home_view_post(self):
        response = self.client.post(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')
        
    def test_about_view_get_context(self):
        response = self.client.get(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<h1>A propos de nous</h1>")

    def test_about_view_post(self):
        response = self.client.post(self.about_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/about.html')

    @patch('monApp.views.send_mail')
    def test_contact_view_post_valid(self, mock_send_mail):
        valid_data = {
            'name': 'TestName',
            'email': 'test@example.com',
            'message': 'Test message content.'
        }
        response = self.client.post(reverse('contact'), valid_data, follow=True)
        
        mock_send_mail.assert_called_once()
        self.assertRedirects(response, reverse('email-sent'))

    def test_contact_view_post_invalid(self):
        invalid_data = {
            'name': 'TestName',
            'email': 'invalid-email',
            'message': 'Test message content.'
        }
        response = self.client.post(reverse('contact'), invalid_data)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')

    def test_contact_view_get(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_home.html')

    def test_disconnect_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/page_logout.html')
        self.assertFalse(self.client.session.get('_auth_user_id'))

    def test_emailsent_view(self):
        response = self.client.get(reverse('email-sent'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'monApp/email-sent.html')