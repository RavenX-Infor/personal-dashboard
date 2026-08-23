from utils.console import effacer_ecran

from features.tasks.manager import (
    voir_tasks,
    ajouter_task,
    terminer_task,
    supprimer_task
)


def menu_task():
    actions = {
        "1": (voir_tasks),
        "2": (ajouter_task),
        "3": (terminer_task),
        "4": (supprimer_task)
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

