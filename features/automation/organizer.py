from features.automation.utils import demander_dossier


EXTENSIONS_PAR_CATEGORIE = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".webp"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Audio": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".7z"]
}


def trouver_categorie(extension):
    for categorie, extensions in EXTENSIONS_PAR_CATEGORIE.items():
        if extension in extensions:
            return categorie

    return "Autres"


def organiser_dossier():
    path = demander_dossier()

    if path is None:
        return

    fichiers = [fichier for fichier in path.iterdir() if fichier.is_file()]
    total = len(fichiers)

    if total == 0:
        print("Le dossier ne contient aucun fichier.")
        return

    suffixe = "s" if total > 1 else ""

    print(f"\n{total} fichier{suffixe} trouvé{suffixe} dans le dossier :\n")

    deplaces = 0
    ignores = 0
    categories_utilisees = set()

    for fichier in fichiers:
        extension = fichier.suffix.lower()
        categorie = trouver_categorie(extension)

        print(f" - {fichier.name}, {categorie}")

        dossier_destination = path / categorie
        dossier_destination.mkdir(exist_ok=True)

        destination = dossier_destination / fichier.name

        if destination.exists():
            ignores += 1
            print(f"   {fichier.name} existe déjà dans {categorie}.")
            continue

        fichier.rename(destination)
        deplaces += 1
        categories_utilisees.add(categorie)

        print(f"   {fichier.name} déplacé dans {categorie}.")

    print("\nOrganisation terminée.")
    print(f"{deplaces} fichier(s) déplacé(s).")
    print(f"{ignores} fichier(s) ignoré(s).")
    print(f"{len(categories_utilisees)} catégorie(s) utilisée(s).")