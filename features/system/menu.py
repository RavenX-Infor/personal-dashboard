from utils.console import effacer_ecran

from features.system.monitor import (
    vue_generale,
    memoire,
    processeur,
    stockage
)

from utils.ui import (
    titre,
    menu_options,
    erreur,
    pause
)


def menu_system():
    actions = {
        "1": vue_generale,
        "2": processeur,
        "3": memoire,
        "4": stockage
    }

    options = {
        "1": "Vue générale",
        "2": "Processeur",
        "3": "Mémoire RAM",
        "4": "Stockage"
    }

    while True:
        effacer_ecran()

        titre("SYSTEM MONITOR")
        menu_options(options)

        choix = input("\n› Votre choix : ").strip()

        if choix == "0":
            return

        if choix in actions:
            effacer_ecran()
            actions[choix]()

            pause(
                "Appuyez sur Entrée pour revenir "
                "au System Monitor..."
            )

        else:
            erreur("Choix invalide.")
            pause()