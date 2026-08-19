from features.automation.utils import demander_dossier

def renommer_fichiers():
    path = demander_dossier()
    
    if path is None:
        return
    

    
    fichiers = [f for f in path.iterdir() if f.is_file()]
    total = len(fichiers)
    
    if total == 0:
        print("Le dossier ne contient aucun fichier.")
        return
    
    s = "s" if total > 1 else ""


    print(f"\n {total} fichier{s} trouvé{s} dans le dossier : \n")

    new_name = input("Nouveau nom : ").strip()

    if not new_name:
        print("Le nouveau nom ne peut pas être vide")
        return

    renommes = 0
    ignores = 0
    

    for index, fichier in enumerate(fichiers, start=1):

        nouveau_name = f"{new_name}_{index:03d}{fichier.suffix}"

        destination = path / nouveau_name

        if destination.exists():
            ignores += 1
            print(f"⚠️ {nouveau_name} existe déjà, fichier ignoré.")
            continue
        
        
        ancien_nom = fichier.name
        fichier.rename(destination)
        renommes += 1
        
        print(f"✅ {ancien_nom} -> {nouveau_name}")

    s_renommes = "s" if renommes > 1 else ""
    s_ignores = "s" if ignores > 1 else ""  

    print("\nRenommage terminé.")
    print(f"{renommes} fichier{s_renommes} renommé{s_renommes}.")
    print(f"{ignores} fichier{s_ignores} ignoré{s_ignores}.")