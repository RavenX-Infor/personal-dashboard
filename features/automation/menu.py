from features.automation.organizer import organiser_dossier
from features.automation.renamer import renommer_fichiers
from features.automation.analyzer import analyser_dossier

from utils.console import effacer_ecran

from utils.ui import (
    titre,
    menu_options,
    erreur,
    pause
)


def menu_automation():
    actions = {
        "1": organiser_dossier,
        "2": renommer_fichiers,
        "3": analyser_dossier
    }

    options = {
        "1": "Organiser un dossier",
        "2": "Renommer des fichiers",
        "3": "Analyser un dossier"
    }

    while True:
        effacer_ecran()

        titre("AUTOMATION CENTER")
        menu_options(options)

        choix = input("\n› Votre choix : ").strip()

        if choix == "0":
            return

        if choix in actions:
            effacer_ecran()
            actions[choix]()

            pause(
                "Appuyez sur Entrée pour revenir "
                "à Automation Center..."
            )

        else:
            erreur("Choix invalide.")
            pause()