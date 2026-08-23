from pathlib import Path

from utils.ui import erreur


def demander_dossier():
    saisie = input(
        "› Chemin du dossier : "
    ).strip().strip("'\"")

    if not saisie:
        erreur("Aucun chemin renseigné.")
        return None

    path = Path(saisie).expanduser()

    if not path.is_dir():
        erreur(
            "Le chemin spécifié n'existe pas "
            "ou n'est pas un dossier."
        )
        return None

    return path


def formater(taille):
    if taille >= 1024 ** 3:
        return f"{taille / (1024 ** 3):.2f} Go"

    if taille >= 1024 ** 2:
        return f"{taille / (1024 ** 2):.2f} Mo"

    if taille >= 1024:
        return f"{taille / 1024:.2f} Ko"

    return f"{taille} octets"