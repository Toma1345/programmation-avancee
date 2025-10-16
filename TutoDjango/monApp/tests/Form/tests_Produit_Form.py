from django.test import TestCase
from datetime import date
from decimal import Decimal
from monApp.models import Produit
from monApp.forms import ProduitForm

class ProduitFormTest(TestCase):
    def test_form_valid_data(self):
        # Le formulaire exclut 'categorie' et 'statut' qui sont optionnels
        form = ProduitForm(data={
            'intituleProd': 'Iphone',
            'prixUnitaireProd': '0.75',
            'dateFab': date.today(),
        })
        self.assertTrue(form.is_valid(), f"Form errors: {form.errors}")

    def test_form_invalid_data_missing_name(self):
        form = ProduitForm(data={
            'intituleProd': '', 
            'prixUnitaireProd': '0.75',
            'dateFab': date.today(),
        })
        self.assertFalse(form.is_valid())
        self.assertIn('intituleProd', form.errors)
        self.assertEqual(form.errors['intituleProd'], ['Ce champ est obligatoire.'])

    def test_form_invalid_data_price_too_many_decimals(self):
        # Le champ DecimalField a 2 décimales maximum
        form = ProduitForm(data={
            'intituleProd': 'Huawei',
            'prixUnitaireProd': '0.755', 
            'dateFab': date.today(),
        })
        self.assertFalse(form.is_valid())
        self.assertIn('prixUnitaireProd', form.errors)
        self.assertIn('pas plus de 2 chiffres', str(form.errors['prixUnitaireProd']))
        
    def test_form_save(self):
        data = {
            'intituleProd': 'Xiaomi',
            'prixUnitaireProd': '50.50',
            'dateFab': date.today(),
        }
        form = ProduitForm(data=data)
        self.assertTrue(form.is_valid())
        
        produit = form.save()
        self.assertEqual(Produit.objects.count(), 1)
        self.assertEqual(produit.intituleProd, 'Xiaomi')
        self.assertEqual(produit.prixUnitaireProd, Decimal('50.50'))