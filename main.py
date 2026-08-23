from features.automation.menu import menu_automation
from features.tasks.menu import menu_task
from features.system.menu import menu_system

from utils.console import effacer_ecran
from utils.ui import titre, menu_options, erreur, succes, pause


def main_menu():
    actions = {
        "1": menu_automation,
        "2": menu_task,
        "3": menu_system
    }

    options = {
        "1": "Automation Center",
        "2": "Gestionnaire de tâches",
        "3": "Information système"
    }

    while True:
        effacer_ecran()

        titre("PERSONAL DASHBOARD")
        menu_options(options, retour="Quitter")

        choix = input("\n› Votre choix : ").strip()

        if choix == "0":
            effacer_ecran()
            succes("À bientôt !")
            break

        if choix in actions:
            effacer_ecran()
            actions[choix]()
        else:
            erreur("Choix invalide.")
            pause()


if __name__ == "__main__":
    main_menu()