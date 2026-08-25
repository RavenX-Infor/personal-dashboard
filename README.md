# Personal Dashboard

Personal Dashboard est une application terminal développée en Python regroupant plusieurs outils personnels dans une seule interface.

Le projet propose un tableau de bord central permettant de consulter rapidement ses tâches, l'état du système et les informations importantes.

## Fonctionnalités

### Dashboard

Accueil central affichant un résumé des informations importantes.

- Résumé des tâches
- Nombre de tâches en cours et terminées
- Nombre de tâches en retard
- Nombre de tâches à priorité haute
- Progression globale des tâches
- Prochaine deadline
- Nombre de jours avant la prochaine deadline
- Résumé de l'utilisation CPU et RAM
- État global du système
- Système d'alertes dynamiques
- Date et heure

Les alertes possèdent plusieurs niveaux :

- 🟢 Succès
- 🟡 Avertissement
- 🔴 Danger

### Automation Center

Outils permettant d'automatiser certaines tâches liées aux fichiers.

- Organisation automatique d'un dossier par type de fichier
- Renommage automatique de plusieurs fichiers
- Analyse d'un dossier
- Analyse des extensions et de l'espace utilisé

### Gestionnaire de tâches

Gestion de tâches persistantes enregistrées localement.

- Ajouter une tâche
- Modifier une tâche
- Supprimer une tâche
- Terminer une tâche
- Priorités : faible, moyenne et haute
- Date de création
- Deadline
- Détection des tâches en retard
- Calcul de la prochaine deadline
- Progression globale
- Affichage sous forme de tableau

### System Monitor

Informations et statistiques sur le système.

- Vue générale
- Utilisation CPU
- Informations processeur
- Utilisation RAM
- Stockage et espace disponible
- Uptime du système
- État du système : Normal, Élevé ou Critique

## Technologies

- Python
- Rich
- psutil
- JSON

## Installation

Cloner le projet :

```bash
git clone <URL_DU_REPO>
cd personal-dashboard
```

Créer un environnement virtuel :

```bash
python -m venv .venv
```

Activer l'environnement sous Windows :

```powershell
.venv\Scripts\Activate.ps1
```

Installer les dépendances :

```bash
pip install -r requirements.txt
```

## Lancement

```bash
python main.py
```

Afficher la version installée :

```bash
python main.py --version
```

## Structure

```text
personal-dashboard/
├── data/
├── features/
│   ├── automation/
│   ├── dashboard/
│   ├── system/
│   └── tasks/
├── utils/
│   ├── console.py
│   └── ui.py
├── config.py
├── main.py
├── requirements.txt
├── CHANGELOG.md
└── README.md
```

## Version

Version actuelle : **v0.2.0**

Consultez [CHANGELOG.md](CHANGELOG.md) pour suivre l'évolution du projet.

## Statut

🚧 Personal Dashboard est actuellement en développement.