
from features.automation.utils import demander_dossier, formater



def analyser_dossier():
    path = demander_dossier()
    
    if path is None:
        return
        
    dossier = 0
    fichier = 0
    taille = 0
    extensions = {}

    fichier_gros = None
    fichier_gros_taille = 0

    for element in path.rglob("*"):
        if element.is_dir():
            dossier += 1
            continue

        if element.is_file():
            fichier += 1

            taille_fichier = element.stat().st_size
            taille += taille_fichier
            

            if taille_fichier > fichier_gros_taille:
                fichier_gros_taille = taille_fichier
                fichier_gros = element.name

            extension = element.suffix.lower()
            extensions[extension] = extensions.get(extension, 0) + 1
        

    print(f"Dossiers : {dossier} dans ce chemin")
    print(f"Fichiers : {fichier} dans ce chemin")
    print(f"Taille totale : {formater(taille)}")

    print("\nNombre de fichiers par extension :")

    for extension, nombre in extensions.items():
        print(f" - {extension} : {nombre}")

    if fichier_gros:
        print("\nFichier le plus lourd :")
        print(f" - {fichier_gros} ({formater(fichier_gros_taille)})")
    else:
        print("\nAucun fichier trouvé.")