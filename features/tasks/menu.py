import os

from features.tasks.manager import (
    voir_tasks,
    ajouter_task,
    terminer_task,
    supprimer_task
)


def effacer_ecran():
    """Efface la console selon le système d'exploitation."""
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_task():
    actions = {
        "1": (voir_tasks, "--- Menu voir ---"),
        "2": (ajouter_task, "--- Menu add ---"),
        "3": (terminer_task, "--- Menu terminer ---"),
        "4": (supprimer_task, "--- Menu delete ---")
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
        elif choix in actions:
            effacer_ecran()
            fonction, en_tete = actions[choix]
            if en_tete:
                print(f"{en_tete}\n")
            fonction()
        else: 
            input("\nChoix Invalide. Appuyez sur Entrée pour réesayer...")
            continue

        input("\nPresser Entrée pour revenir au menu Task Gestionnaire...")

if __name__ == "__main__":
    menu_task()