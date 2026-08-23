def titre(texte):
    largeur = 40

    print("═" * largeur)
    print(texte.center(largeur))
    print("═" * largeur)


def succes(message):
    print(f"✓ {message}")


def erreur(message):
    print(f"✗ {message}")


def avertissement(message):
    print(f"⚠ {message}")


def info(message):
    print(f"ℹ {message}")


def pause(message="Appuyez sur Entrée pour continuer..."):
    input(f"\n{message}")

def menu_options(options, retour="Retour"):
    for cle, texte in options.items():
        print(f" [{cle}] {texte}")

    print(f"\n [0] {retour}")