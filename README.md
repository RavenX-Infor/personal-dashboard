# Personal Dashboard

Personal Dashboard est une application en ligne de commande développée en **Python** permettant de regrouper plusieurs outils utiles au quotidien depuis une seule interface.

Le projet est organisé en différentes fonctionnalités indépendantes afin de pouvoir facilement ajouter de nouveaux outils au fil du développement.

## ✨ Fonctionnalités

### 📁 Automatisation

Outils permettant d'effectuer différentes opérations sur les fichiers et dossiers :

* Organisation automatique de fichiers
* Renommage de fichiers
* Analyse de dossiers

### 💻 Système

Outils permettant de consulter différentes informations concernant l'ordinateur :

* Informations système
* Utilisation du processeur
* Utilisation de la mémoire RAM
* Informations sur les disques et le stockage

### ✅ Gestionnaire de tâches

Gestion simple de tâches depuis le terminal :

* Afficher les tâches
* Ajouter une tâche
* Terminer une tâche
* Supprimer une tâche

Les tâches sont sauvegardées localement dans un fichier JSON.

---

## 🚀 Installation

### 1. Cloner le projet

```bash
git clone URL_DU_REPOSITORY
cd personal-dashboard
```

### 2. Créer un environnement virtuel

```bash
python -m venv .venv
```

### 3. Activer l'environnement virtuel

#### Windows PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Installer les dépendances

```bash
python -m pip install -r requirements.txt
```

---

## ▶️ Utilisation

Une fois l'environnement virtuel activé, lancer l'application avec :

```bash
python main.py
```

Le menu principal permet ensuite d'accéder aux différentes fonctionnalités du dashboard.

---

## 📂 Structure du projet

```text
personal-dashboard/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   └── task.json
│
├── features/
│   │
│   ├── automation/
│   │   ├── analyzer.py
│   │   ├── menu.py
│   │   ├── organizer.py
│   │   ├── renamer.py
│   │   └── utils.py
│   │
│   ├── system/
│   │   ├── menu.py
│   │   └── monitor.py
│   │
│   └── tasks/
│       ├── manager.py
│       └── menu.py
│
└── utils/
    └── console.py
```

---

## 🛠️ Technologies

* **Python 3**
* **psutil** — récupération des informations système
* **JSON** — stockage des tâches
* **Git** — gestion des versions
* **GitHub** — hébergement du repository

---

## 🗺️ Roadmap

Personal Dashboard est encore en développement.

### Améliorations prévues

* [ ] Améliorer la gestion des erreurs
* [ ] Ajouter un système de logs
* [ ] Améliorer l'interface du terminal
* [ ] Ajouter de nouvelles informations système
* [ ] Améliorer le gestionnaire de tâches
* [ ] Ajouter de nouveaux outils d'automatisation
* [ ] Ajouter de nouvelles fonctionnalités au dashboard
* [ ] Ajouter des tests automatisés

---

## 🎯 Objectif du projet

L'objectif de Personal Dashboard est de construire progressivement une boîte à outils personnelle utilisable directement depuis le terminal.

Le projet sert également à expérimenter différentes fonctionnalités de Python, améliorer l'organisation du code et apprendre à développer une application de plus en plus complète et maintenable.
