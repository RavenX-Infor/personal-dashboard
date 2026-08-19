import json
from pathlib import Path

base_dir = Path(__file__).resolve().parents[2]
task_folder = base_dir / "data" / "task.json"

def save_task(tasks):
  with open(task_folder, 'w', encoding="utf-8") as fichier:
     json.dump(tasks, fichier, indent=4, ensure_ascii=False)

def charger_tasks():
  try:
    with open(task_folder, encoding="utf-8") as fichier:
      return json.load(fichier)
  except FileNotFoundError:
     print("Fichier JSON non existant")
     return []
  except json.JSONDecodeError:
     print("Fichier conronpu")
     return []

def afficher_tasks(tasks):
  print("MES TACHES")

  if not tasks:
    print("Aucune tâches.")
    return

  for task in tasks:
    statut = "[X]" if task["terminee"] else "[ ]"
    print(f"{statut} {task["id"]} - {task["titre"]}")

def trouver_task(tasks, id_task):
  for task in tasks:
    if task["id"] == id_task:
      return task

  return None

def ajouter_task():

  new_task = input("Nouvelle tache : ").strip()

  if not new_task:
     print("Veuillez mettre un titre à vôtre tache")
     return

  tasks = charger_tasks()

  if tasks:
    id_task = max(task["id"] for task in tasks) + 1
  else:
      id_task = 1

  dict_task = dict(id=id_task, titre=new_task, terminee=False)

  tasks.append(dict_task)
  save_task(tasks)

  print(f'Tâche "{new_task}" ajoutée avec l\'ID {id_task}.')

def voir_tasks():
    tasks = charger_tasks()
    afficher_tasks(tasks)

def terminer_task():
    tasks = charger_tasks()
    afficher_tasks(tasks)

    if not tasks:
        return

    try:
        id_task = int(input("\nID de la tâche à terminer : "))
    except ValueError:
        print("Erreur : l'ID doit être un nombre.")
        return

    task = trouver_task(tasks, id_task)

    if task is None:
        print(f"Aucune tâche avec l'ID {id_task}.")
        return

    task["terminee"] = True
    save_task(tasks)

    print(f"La tâche ID {id_task} est terminée.")


def supprimer_task():
    tasks = charger_tasks()
    afficher_tasks(tasks)

    if not tasks:
        return

    try:
        id_task = int(input("\nID de la tâche à supprimer : "))
    except ValueError:
        print("Erreur : l'ID doit être un nombre.")
        return

    task = trouver_task(tasks, id_task)

    if task is None:
        print(f"Aucune tâche avec l'ID {id_task}.")
        return

    tasks.remove(task)
    save_task(tasks)

    print(f"La tâche ID {id_task} a été supprimée.")
  

