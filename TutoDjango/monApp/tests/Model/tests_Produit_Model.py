from datetime import date
from django.test import TestCase
from monApp.models import Produit, Categorie, Statut
from decimal import Decimal

class ProduitModelTest(TestCase):
    def setUp(self):
        # Création des dépendances pour Produit
        self.categorie = Categorie.objects.create(nomCat="Test Catégorie")
        self.statut = Statut.objects.create(libelle="En ligne")
        
        # Création d'un objet Produit
        self.produit = Produit.objects.create(
            intituleProd="Iphone",
            prixUnitaireProd=Decimal("150.50"),
            dateFab=date(2025, 10, 14),
            categorie=self.categorie,
            statut=self.statut
        )
    
    def test_produit_creation(self):
        self.assertEqual(self.produit.intituleProd, "Iphone")
        self.assertEqual(self.produit.prixUnitaireProd, Decimal("150.50"))
        self.assertEqual(self.produit.dateFab, date(2025, 10, 14))
        self.assertEqual(self.produit.categorie.nomCat, "Test Catégorie")
        self.assertEqual(self.produit.statut.libelle, "En ligne")

    def test_string_representation(self):
        # Vérifie que la méthode __str__ retourne le format attendu
        self.assertEqual(str(self.produit), "Iphone")

    def test_produit_updating(self):
        new_intitule = "Tablette Samsung"
        new_price = Decimal("259.00")
        self.produit.intituleProd = new_intitule
        self.produit.prixUnitaireProd = new_price
        self.produit.save()
        
        updated_produit = Produit.objects.get(refProd=self.produit.refProd)
        self.assertEqual(updated_produit.intituleProd, new_intitule)
        self.assertEqual(updated_produit.prixUnitaireProd, new_price)

    def test_produit_deletion(self):
        self.produit.delete()
        self.assertEqual(Produit.objects.count(), 0)