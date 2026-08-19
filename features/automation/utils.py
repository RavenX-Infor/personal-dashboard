from pathlib import Path


def demander_dossier():
    saisie = input("Donner le chemin d'accès à votre dossier : ").strip().strip("'\"")

    if not saisie:
        print("Aucun chemin renseigné.")
        return None

    path = Path(saisie)

    if not path.is_dir():
        print("Le chemin spécifié n'existe pas ou n'est pas un dossier.")
        return None

    return path

def formater(taille):
    if taille >= 1024 ** 3:
        return f"{taille / (1024 ** 3):.2f} Go"
    elif taille >= 1024 ** 2:
        return f"{taille / (1024 ** 2):.2f} Mo"
    elif taille >= 1024:
        return f"{taille / 1024:.2f} Ko"
    else:
        return f"{taille} octets"
