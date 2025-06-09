# Gestion des Commandes et Paiements

Application de bureau en Python pour la gestion des commandes et des paiements clients.

## Fonctionnalités prévues

- Gestion de deux types de clients : revendeurs et particuliers
- Suivi des paiements (paiements en plusieurs fois)
- Configuration personnalisée des informations de l'entreprise
- Gestion des articles avec références et prix
- Création de bons de commande et bons de livraison
- Génération automatique de documents PDF

## Installation

1. Cloner le dépôt
2. Créer et activer un environnement virtuel Python
3. Installer les dépendances : `pip install -r requirements.txt`
4. Lancer l'application : `python main.py`

## Structure du projet

- `main.py` : Point d'entrée de l'application
- `src/` : Code source
  - `models/` : Modèles de données
  - `views/` : Interface utilisateur
  - `controllers/` : Logique métier
  - `utils/` : Fonctions utilitaires
- `data/` : Stockage des données
- `assets/` : Ressources graphiques