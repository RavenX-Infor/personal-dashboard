from utils.console import effacer_ecran

from features.system.monitor import vue_generale, memoire, processeur, stockage

def menu_system():
    actions = {
      "1": vue_generale,
      "2": processeur,
      "3": memoire,
      "4": stockage
    }

    while True:
          effacer_ecran()
            
          print("=" * 35)
          print("        SYSTEM MONITOR          ")
          print("=" * 35)
          print(" [1] Vue général")
          print(" [2] Voir CPU")
          print(" [3] Voir mémoire")
          print(" [4] Voir stockage")
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
    
          input("\nAppuyez sur Entrée pour revenir au System Monitor...")