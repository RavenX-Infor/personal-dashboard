from features.automation.organizer import organiser_dossier

from features.automation.renamer import renommer_fichiers

from features.automation.analyzer import analyser_dossier

from utils.console import effacer_ecran

def menu_automation():
    actions = {
        "1": (organiser_dossier),
        "2": (renommer_fichiers),
        "3": (analyser_dossier)
    }

    while True:
        effacer_ecran()
        
        print("=" * 35)
        print("        AUTOMATION CENTER        ")
        print("=" * 35)
        print(" [1] Organiser un dossier")
        print(" [2] Renommer des fichiers")
        print(" [3] Analyser un dossier")
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

        input("\nPresser Entrée pour revenir au menu Automation Center...")
