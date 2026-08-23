from utils.console import effacer_ecran

from features.tasks.manager import (
    voir_tasks,
    ajouter_task,
    terminer_task,
    supprimer_task
)
def int_voir_task():
    tasks = voir_tasks()

    print("MES TACHES")

    if not tasks:
        print("Aucune tâche.")
        return

    for task in tasks:
        statut = "[X]" if task["terminee"] else "[ ]"
        print(f'{statut} {task["id"]} - {task["titre"]}')


def int_ajouter_task():
    titre = input("Nouvelle tâche : ").strip()

    task = ajouter_task(titre)

    if task is None:
        print("Veuillez mettre un titre à votre tâche.")
        return

    print(f'Tâche "{task["titre"]}" ajoutée avec l\'ID {task["id"]}.')

def int_terminer_task():
    tasks = voir_tasks()

    if not tasks:
        print("Aucune tâche.")
        return

    int_voir_task()

    try:
        id_task = int(input("\nID de la tâche à terminer : "))
    except ValueError:
        print("Erreur : l'ID doit être un nombre.")
        return

    resultat = terminer_task(id_task)

    if resultat is None:
        print(f"Aucune tâche avec l'ID {id_task}.")
    elif resultat is False:
        print("Cette tâche est déjà terminée.")
    else:
        print(f'La tâche "{resultat["titre"]}" est terminée.')

def int_supprimer_task():
    tasks = voir_tasks()

    if not tasks:
        print("Aucune tâche.")
        return

    int_voir_task()

    try:
        id_task = int(input("\nID de la tâche à supprimer : "))
    except ValueError:
        print("Erreur : l'ID doit être un nombre.")
        return

    resultat = supprimer_task(id_task)

    if resultat is None:
        print(f"Aucune tâche avec l'ID {id_task}.")
    else:
        print(f'La tâche "{resultat["titre"]}" a été supprimée.')

def menu_task():
    actions = {
        "1": int_voir_task,
        "2": int_ajouter_task,
        "3": int_terminer_task,
        "4": int_supprimer_task
    }

    while True:
        effacer_ecran()
        
        print("=" * 35)
        print("        Task Gestionnaire       ")
        print("=" * 35)
        print(" [1] Voir les tâches")
        print(" [2] Ajouter une tâche")
        print(" [3] Terminer une tâche")
        print(" [4] Supprimer une tâche")
        print(" [0] Retour")
        print("-" * 35)

        choix = input("Votre choix : ").strip()

        if choix == "0":
            return
        if choix in actions:
            effacer_ecran()
            actions[choix]()

            
        else: 
            input("\nChoix Invalide. Appuyez sur Entrée pour réesayer...")
            continue

        input("\nPresser Entrée pour revenir au menu Task Gestionnaire...")

