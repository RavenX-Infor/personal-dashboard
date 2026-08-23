import json
from pathlib import Path

base_dir = Path(__file__).resolve().parents[2]
task_file = base_dir / "data" / "task.json"



def save_task(tasks):
  with open(task_file, 'w', encoding="utf-8") as fichier:
     json.dump(tasks, fichier, indent=4, ensure_ascii=False)

def charger_tasks():
    try:
        with open(task_file, encoding="utf-8") as fichier:
            return json.load(fichier)

    except (FileNotFoundError, json.JSONDecodeError):
        return []