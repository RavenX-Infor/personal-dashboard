from features.automation.utils import demander_dossier

from utils.ui import (
    titre,
    succes,
    erreur,
    avertissement,
    info
)


def renommer_fichiers():
    titre("RENOMMER DES FICHIERS")

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

    new_name = input(
        "\n› Nouveau nom : "
    ).strip()

    if not new_name:
        erreur("Le nouveau nom ne peut pas être vide.")
        return

    renommes = 0
    ignores = 0

    print()

    for index, fichier in enumerate(
        fichiers,
        start=1
    ):
        nouveau_nom = (
            f"{new_name}_{index:03d}"
            f"{fichier.suffix}"
        )

        destination = path / nouveau_nom

        if destination.exists():
            ignores += 1

            avertissement(
                f"{nouveau_nom} existe déjà."
            )

            continue

        ancien_nom = fichier.name

        fichier.rename(destination)

        renommes += 1

        succes(
            f"{ancien_nom} → {nouveau_nom}"
        )

    print()
    titre("RÉSUMÉ")

    info(f"Fichiers renommés : {renommes}")
    info(f"Fichiers ignorés  : {ignores}")