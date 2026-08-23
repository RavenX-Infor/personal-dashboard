# Personal Dashboard

Personal Dashboard est une application terminal développée en Python regroupant plusieurs outils personnels dans une seule interface.

Le projet est actuellement en développement.

## Fonctionnalités

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
- Affichage sous forme de tableau

### System Monitor

Informations et statistiques sur le système.

- Vue générale
- Utilisation CPU
- Informations processeur
- Utilisation RAM
- Stockage et espace disponible
- Uptime du système

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

## Structure

```text
personal-dashboard/
├── data/
├── features/
│   ├── automation/
│   ├── system/
│   └── tasks/
├── utils/
│   ├── console.py
│   └── ui.py
├── main.py
├── requirements.txt
└── README.md
```

## Statut

🚧 Projet en cours de développement.