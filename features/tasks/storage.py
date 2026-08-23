import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"
TASK_FILE = DATA_DIR / "task.json"


def initialiser_stockage():
    """Crée le dossier et le fichier de stockage s'ils n'existent pas."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not TASK_FILE.exists():
        with open(TASK_FILE, "w", encoding="utf-8") as fichier:
            json.dump([], fichier, indent=4, ensure_ascii=False)


def save_task(tasks):
    """Sauvegarde les tâches dans le fichier JSON."""
    initialiser_stockage()

    with open(TASK_FILE, "w", encoding="utf-8") as fichier:
        json.dump(
            tasks,
            fichier,
            indent=4,
            ensure_ascii=False
        )


def charger_tasks():
    """Charge et retourne les tâches enregistrées."""
    initialiser_stockage()

    try:
        with open(TASK_FILE, encoding="utf-8") as fichier:
            return json.load(fichier)

    except json.JSONDecodeError:
        return []