# Programmation Avancée
*par Thomas BROSSIER*

## TD1
- Création d'un environnement virtuel et installation de Django  
- Création d'un projet Django  
- Lancement du serveur de développement  
- Création de la base de données du projet  
- Création d’une application Django  
- Ajout d’une première page  
- Petit challenge : **Bonjour Cricri**

## TP1
- Utilisation des migrations Django
- Exercez-vous : 002 - 003 - 004 - 005 - 006
- Utilisation du shell Python pour insérer des données dans les modèles : Produits, Catégories, Statut  
- Petit challenge  

## TD2
- Introduction au site d’administration Django
- Application modifiable depuis l'interface admin
- Personnalisation de l’interface admin :  
    * `list_display`  
    * fichier `models.py` non modifié déjà OK
    * Calcul du prix unitaire produit (prix TTC - page 8) 
- Installation et utilisation de Django Debug Toolbar  
    - Exploration des URLs proposés dans le TD  

## TP2
- Mise en place du message dynamique : "Bonjour %s !" (méthode GET)  
- Création de templates pour :  
  - list_categories  
  - list_rayons  
  - list_statut  
  - list_produits  
  - about  
  - contact  
- Héritage de templates
- Application de styles CSS  
- Début d’intégration de Bootstrap :  
  - Documentation consultée : [W3Schools - Django et Bootstrap5](https://www.w3schools.com/django/django_add_bootstrap5.php)  
  - Installation de Bootstrap 5  
  - Ajout de menu, navigation et mise en forme tabulaire des listes

**Mise à jour du `models.py`**

## TD3
- Utilisation de `TemplateView` pour :  
  - Home  
  - About  
  - Contact  
  - Home avec paramètres (`Home/<param>`)
- Implémentation de `ListView` et `DetailView`
- Ajout de liens vers le détail du produit
- Création des vues Liste et Détail pour Statut, Catégorie et Rayon
- Intégration de liens vers les vues listes dans la barre de navigation  
- Mise en place des vues d’authentification :  
  - Login  
  - Register  
  - Logout  
- Création des pages HTML correspondantes (login, register)  
- Mise à jour de la navbar pour afficher les options Connexion / Inscription / Déconnexion selon l’état de l’utilisateur  
- Formulaire de contact avec :  
  - Envoi d’email  
  - Redirection vers une page de confirmation "email-sent" 
- Mise à jour de la navbar pour afficher les options Contact / A propos