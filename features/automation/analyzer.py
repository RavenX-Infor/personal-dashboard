from features.automation.utils import (
    demander_dossier,
    formater
)

from utils.ui import (
    titre,
    info
)


def analyser_dossier():
    titre("ANALYSER UN DOSSIER")

    path = demander_dossier()

    if path is None:
        return

    nombre_dossiers = 0
    nombre_fichiers = 0
    taille_totale = 0

    extensions = {}

    fichier_gros = None
    fichier_gros_taille = 0

    for element in path.rglob("*"):
        if element.is_dir():
            nombre_dossiers += 1
            continue

        if element.is_file():
            nombre_fichiers += 1

            taille_fichier = element.stat().st_size
            taille_totale += taille_fichier

            if taille_fichier > fichier_gros_taille:
                fichier_gros_taille = taille_fichier
                fichier_gros = element.name

            extension = element.suffix.lower()

            if not extension:
                extension = "Sans extension"

            extensions[extension] = (
                extensions.get(extension, 0) + 1
            )

    print()
    titre("RÉSUMÉ")

    info(f"Dossiers      : {nombre_dossiers}")
    info(f"Fichiers      : {nombre_fichiers}")
    info(f"Taille totale : {formater(taille_totale)}")

    print()
    titre("EXTENSIONS")

    if extensions:
        for extension, nombre in sorted(
            extensions.items(),
            key=lambda item: item[1],
            reverse=True
        ):
            print(
                f" • {extension:<15} "
                f"{nombre} fichier"
                f"{'s' if nombre > 1 else ''}"
            )

    else:
        info("Aucune extension trouvée.")

    print()
    titre("PLUS GROS FICHIER")

    if fichier_gros:
        print(
            f" • {fichier_gros}"
        )

        print(
            f"   Taille : "
            f"{formater(fichier_gros_taille)}"
        )

    else:
        info("Aucun fichier trouvé.")