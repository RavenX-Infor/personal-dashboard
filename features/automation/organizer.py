from features.automation.utils import demander_dossier

from utils.ui import (
    titre,
    succes,
    avertissement,
    info
)


EXTENSIONS_PAR_CATEGORIE = {
    "Images": [
        ".png",
        ".jpg",
        ".jpeg",
        ".gif",
        ".bmp",
        ".webp"
    ],

    "Videos": [
        ".mp4",
        ".mkv",
        ".avi",
        ".mov"
    ],

    "Documents": [
        ".pdf",
        ".txt",
        ".docx"
    ],

    "Audio": [
        ".mp3",
        ".wav",
        ".flac"
    ],

    "Archives": [
        ".zip",
        ".rar",
        ".7z"
    ]
}


def trouver_categorie(extension):
    for categorie, extensions in EXTENSIONS_PAR_CATEGORIE.items():
        if extension in extensions:
            return categorie

    return "Autres"


def organiser_dossier():
    titre("ORGANISER UN DOSSIER")

    path = demander_dossier()

    if path is None:
        return

    fichiers = [
        fichier
        for fichier in path.iterdir()
        if fichier.is_file()
    ]

    total = len(fichiers)

    if total == 0:
        info("Le dossier ne contient aucun fichier.")
        return

    info(
        f"{total} fichier"
        f"{'s' if total > 1 else ''} trouvé"
        f"{'s' if total > 1 else ''}."
    )

    deplaces = 0
    ignores = 0
    categories_utilisees = set()

    print()

    for fichier in fichiers:
        extension = fichier.suffix.lower()
        categorie = trouver_categorie(extension)

        dossier_destination = path / categorie
        dossier_destination.mkdir(exist_ok=True)

        destination = dossier_destination / fichier.name

        if destination.exists():
            ignores += 1

            avertissement(
                f"{fichier.name} existe déjà "
                f"dans {categorie}."
            )

            continue

        fichier.rename(destination)

        deplaces += 1
        categories_utilisees.add(categorie)

        succes(
            f"{fichier.name} → {categorie}"
        )

    print()
    titre("RÉSUMÉ")

    info(f"Fichiers déplacés : {deplaces}")
    info(f"Fichiers ignorés  : {ignores}")
    info(
        f"Catégories utilisées : "
        f"{len(categories_utilisees)}"
    )