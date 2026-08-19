from features.automation.menu import menu_automation
from features.tasks.menu import menu_task

from utils.console import effacer_ecran


def main_menu():
    actions = {
        "1": (menu_automation),
        "2": (menu_task)
    }

    while True:
        effacer_ecran()
        
        print("=" * 35)
        print("        Personal Dashboard      ")
        print("=" * 35)
        print(" [1] Automation Center")
        print(" [2] Gestionnaire de tâches")
        print(" [0] Quitter")
        print("-" * 35)

        choix = input("Votre choix : ").strip()

        if choix == "0":
            effacer_ecran()
            print("Au revoir !")
            break

        elif choix in actions:
            effacer_ecran()
            actions[choix]()
        else: 
            input("\nChoix Invalide. Appuyez sur Entrée pour réesayer...")

if __name__ == "__main__":
    main_menu()