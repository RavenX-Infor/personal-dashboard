from rich import box
from rich.table import Table

from utils.console import effacer_ecran
from utils.ui import (
    console,
    titre,
    menu_options,
    succes,
    erreur,
    avertissement,
    info,
    pause
)

from features.tasks.manager import (
    voir_tasks,
    ajouter_task,
    terminer_task,
    supprimer_task,
    modif_tasks
)

def int_voir_task():
    tasks = voir_tasks()

    titre("MES TÂCHES")

    if not tasks:
        info("Aucune tâche.")
        return

    table = Table(
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
        expand=True
    )

    table.add_column("Statut", justify="center", width=8)
    table.add_column("ID", justify="center", width=5)
    table.add_column("Tâche")
    table.add_column("Priorité", justify="center")
    table.add_column("Créée le")
    table.add_column("Deadline")

    for task in tasks:
        priorite = task.get("priorite", "moyenne")
        date = task.get("date_creation", "Non renseignée")
        deadline = task.get("deadline", "Non renseignée")

        if task["terminee"]:
            statut = "[green]✓ Terminée[/green]"
        else:
            statut = "[yellow]○ En cours[/yellow]"

        if priorite == "haute":
            priorite_affichage = "[bold red]HAUTE[/bold red]"

        elif priorite == "moyenne":
            priorite_affichage = "[bold yellow]MOYENNE[/bold yellow]"

        else:
            priorite_affichage = "[bold green]FAIBLE[/bold green]"

        table.add_row(
            statut,
            str(task["id"]),
            task["titre"],
            priorite_affichage,
            date,
            deadline
        )

    console.print(table)
def int_ajouter_task():
    titre_task = input("Nouvelle tâche : ").strip()

    prio = input(
        "Ajouter une priorité (faible, moyenne ou haute) : "
    ).strip().lower()

    deadline = input(
        "Ajouter une deadline (JJ/MM/AAAA) : "
    ).strip()

    task, code_erreur = ajouter_task(
        titre_task,
        prio,
        deadline
    )

    if code_erreur == "titre_vide":
        erreur("Le titre ne peut pas être vide.")
        return

    if code_erreur == "priorite_invalide":
        erreur("La priorité est invalide.")
        return

    if code_erreur == "deadline_invalide":
        erreur("La deadline doit être au format JJ/MM/AAAA.")
        return

    if code_erreur == "deadline_passe":
        avertissement("La deadline est déjà passée.")
        return

    if code_erreur == "deadline_trop_loin":
        avertissement("La deadline est trop éloignée.")
        return

    succes(
        f'Tâche "{task["titre"]}" ajoutée '
        f'avec l\'ID {task["id"]} '
        f'et la priorité {task["priorite"].upper()}.'
    )


def int_terminer_task():
    tasks = voir_tasks()

    if not tasks:
        info("Aucune tâche.")
        return

    int_voir_task()

    try:
        id_task = int(
            input("\nID de la tâche à terminer : ")
        )
    except ValueError:
        erreur("L'ID doit être un nombre.")
        return

    resultat = terminer_task(id_task)

    if resultat is None:
        erreur(f"Aucune tâche avec l'ID {id_task}.")
        return

    if resultat is False:
        avertissement("Cette tâche est déjà terminée.")
        return

    succes(
        f'La tâche "{resultat["titre"]}" est terminée.'
    )


def int_supprimer_task():
    tasks = voir_tasks()

    if not tasks:
        info("Aucune tâche.")
        return

    int_voir_task()

    try:
        id_task = int(
            input("\nID de la tâche à supprimer : ")
        )
    except ValueError:
        erreur("L'ID doit être un nombre.")
        return

    resultat = supprimer_task(id_task)

    if resultat is None:
        erreur(f"Aucune tâche avec l'ID {id_task}.")
        return

    succes(
        f'La tâche "{resultat["titre"]}" a été supprimée.'
    )


def int_modif_task():
    tasks = voir_tasks()

    if not tasks:
        info("Aucune tâche.")
        return

    int_voir_task()

    try:
        id_task = int(
            input("\nID de la tâche à modifier : ")
        )
    except ValueError:
        erreur("L'ID doit être un nombre.")
        return

    options_modif = {
        "1": "Modifier le titre",
        "2": "Modifier la priorité",
        "3": "Modifier la deadline"
    }

    print()
    titre("MODIFIER UNE TÂCHE")
    menu_options(options_modif)

    choix = input("\n› Votre choix : ").strip()

    if choix == "0":
        info("Modification annulée.")
        return

    if choix == "1":
        nouveau_titre = input(
            "Nouveau titre : "
        ).strip()

        resultat, code_erreur = modif_tasks(
            id_task,
            new_titre=nouveau_titre
        )

        if code_erreur == "task_introuvable":
            erreur(f"Aucune tâche avec l'ID {id_task}.")
            return

        if code_erreur == "titre_vide":
            erreur("Le titre ne peut pas être vide.")
            return

        succes(
            f'Titre modifié : "{resultat["titre"]}"'
        )

    elif choix == "2":
        prio = input(
            "Nouvelle priorité "
            "(faible, moyenne ou haute) : "
        ).strip().lower()

        resultat, code_erreur = modif_tasks(
            id_task,
            new_prio=prio
        )

        if code_erreur == "task_introuvable":
            erreur(f"Aucune tâche avec l'ID {id_task}.")
            return

        if code_erreur == "priorite_invalide":
            erreur("Priorité invalide.")
            return

        succes(
            f'Priorité modifiée : '
            f'{resultat["priorite"].upper()}'
        )

    elif choix == "3":
        deadline = input(
            "Nouvelle deadline (JJ/MM/AAAA) : "
        ).strip()

        resultat, code_erreur = modif_tasks(
            id_task,
            new_deadline=deadline
        )

        if code_erreur == "task_introuvable":
            erreur(f"Aucune tâche avec l'ID {id_task}.")
            return

        if code_erreur == "deadline_invalide":
            erreur(
                "La deadline doit être au format JJ/MM/AAAA."
            )
            return

        if code_erreur == "deadline_passe":
            avertissement(
                "La deadline est déjà passée."
            )
            return

        if code_erreur == "deadline_trop_loin":
            avertissement(
                "La deadline est trop éloignée."
            )
            return

        succes(
            f'Deadline modifiée : '
            f'{resultat["deadline"]}'
        )

    else:
        erreur("Choix invalide.")


def menu_task():
    actions = {
        "1": int_voir_task,
        "2": int_ajouter_task,
        "3": int_terminer_task,
        "4": int_supprimer_task,
        "5": int_modif_task
    }

    options = {
        "1": "Voir les tâches",
        "2": "Ajouter une tâche",
        "3": "Terminer une tâche",
        "4": "Supprimer une tâche",
        "5": "Modifier une tâche"
    }

    while True:
        effacer_ecran()

        titre("GESTIONNAIRE DE TÂCHES")
        menu_options(options)

        choix = input("\n› Votre choix : ").strip()

        if choix == "0":
            return

        if choix in actions:
            effacer_ecran()
            actions[choix]()
            pause(
                "Appuyez sur Entrée pour revenir aux tâches..."
            )
        else:
            erreur("Choix invalide.")
            pause()