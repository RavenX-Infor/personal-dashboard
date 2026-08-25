import argparse

from config import (
    APP_NAME,
    VERSION,
    DESCRIPTION
)

from features.automation.menu import menu_automation
from features.tasks.menu import menu_task
from features.system.menu import menu_system
from features.dashboard.home import afficher_dashboard
from utils.console import effacer_ecran
from datetime import datetime

from utils.ui import (
    console,
    titre,
    menu_options,
    erreur,
    succes,
    pause
)


def creer_parser():
    parser = argparse.ArgumentParser(
        prog="personal-dashboard",
        description=DESCRIPTION
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"{APP_NAME} v{VERSION}"
    )

    return parser


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

        titre(APP_NAME.upper())

        console.print(
            f"[dim]v{VERSION}[/dim]",
            justify="center"
        )

        date_heure = datetime.now().strftime("%d/%m/%Y • %H:%M")

        console.print(
            f"[dim]{date_heure}[/dim]",
            justify="center"
        )

        afficher_dashboard()

        menu_options(
            options,
            retour="Quitter"
        )

        choix = input("\n› Votre choix : ").strip()

        if choix == "0":
            effacer_ecran()
            succes("À bientôt !")
            return

        if choix in actions:
            effacer_ecran()
            actions[choix]()

        else:
            erreur("Choix invalide.")
            pause()


def main():
    parser = creer_parser()

    parser.parse_args()

    try:
        main_menu()

    except KeyboardInterrupt:
        effacer_ecran()

        console.print()

        succes("À bientôt !")


if __name__ == "__main__":
    main()