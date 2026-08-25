from rich.panel import Panel
from rich.progress_bar import ProgressBar
from rich.table import Table

from features.system.monitor import obtenir_resume_systeme
from features.tasks.manager import obtenir_resume_task

from utils.ui import console

def couleur_utilisation(pourcentage):
    if pourcentage >= 85:
        return "red"

    if pourcentage >= 60:
        return "yellow"

    return "green"

def creer_panel_tasks(resume):
    prochaine = resume.get("prochaine")
    progression = resume.get("progression")

    if progression >= 100:
        couleur_progression = "green"
    else:
        couleur_progression = "cyan"

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        expand=True
    )

    table.add_column()
    table.add_column(justify="right")
    table.add_column()
    table.add_column(justify="right")

    table.add_row(
        "Total",
        str(resume["total"]),
        "En cours",
        f'[yellow]{resume["en_cours"]}[/yellow]'
    )

    table.add_row(
        "Terminées",
        f'[green]{resume["terminees"]}[/green]',
        "Priorité haute",
        f'[red]{resume["hautes"]}[/red]'
    )

    if resume["en_retard"] > 0:
        retard = f'[bold red]{resume["en_retard"]}[/bold red]'
    else:
        retard = f'[green]{resume["en_retard"]}[/green]'

    table.add_row(
        "En retard",
        retard,
        "",
        ""
    )


    table.add_row("", "", "", "")

    table.add_row(
        "Progression",
        ProgressBar(
            total=100,
            completed=progression,
            width=20,
            complete_style=couleur_progression,
            finished_style="green"
        ),
        "",
        f"[{couleur_progression}]{progression:.1f}%[/{couleur_progression}]"
    )

    if prochaine:
        jours = prochaine["jours_restant"]

        if jours == 0:
            texte_jours = "[bold red]Aujourd'hui[/bold red]"

        elif jours == 1:
            texte_jours = "[bold yellow]Demain[/bold yellow]"

        else:
            texte_jours = (
                f"[cyan]Dans {jours} jours[/cyan]"
            )

        table.add_row("", "", "", "")

        table.add_row(
            "[bold]Prochaine[/bold]",
            prochaine["titre"],
            "Deadline",
            f'[cyan]{prochaine["deadline"]}[/cyan]'
        )

        table.add_row(
            "",
            "",
            "",
            texte_jours
        )

    else:
        table.add_row("", "", "", "")

        table.add_row(
            "[dim]Aucune deadline à venir[/dim]",
            "",
            "",
            ""
        )

    return Panel(
        table,
        title="[bold cyan]TÂCHES[/bold cyan]",
        border_style="cyan",
        padding=(1, 1)
    )

def creer_panel_systeme(resume):
    cpu = resume["cpu"]
    ram = resume["ram"]
    etat = resume["etat"]

    if etat == "Critique":
        couleur_etat = "red"
    elif etat == "Élevé":
        couleur_etat = "yellow"
    else:
        couleur_etat = "green"

    couleur_cpu = couleur_utilisation(cpu)
    couleur_ram = couleur_utilisation(ram)

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 1),
        expand=True
    )

    table.add_column(
        width=5
    )

    table.add_column(
        ratio=1
    )

    table.add_column(
        width=8,
        justify="right"
    )

    table.add_row(
        "CPU",
        ProgressBar(
            total=100,
            completed=cpu,
            width=20,
            complete_style=couleur_cpu,
            finished_style=couleur_cpu
        ),
        f"[{couleur_cpu}]{cpu:.1f}%[/{couleur_cpu}]"
    )

    table.add_row(
        "RAM",
        ProgressBar(
            total=100,
            completed=ram,
            width=20,
            complete_style=couleur_ram,
            finished_style=couleur_ram
        ),
        f"[{couleur_ram}]{ram:.1f}%[/{couleur_ram}]"
    )

    table.add_row(
    "",
    "",
    ""
)

    table.add_row(
        "État",
        f"[bold {couleur_etat}]● {etat}[/bold {couleur_etat}]",
        ""
    )

    return Panel(
        table,
        title="[bold cyan]SYSTÈME[/bold cyan]",
        border_style="cyan",
        padding=(1, 1)
    )

def generer_alertes(resume_tasks, resume_systeme):
    alertes = []

    nb_retard = resume_tasks.get("en_retard", 0)

    if nb_retard > 0:
        s = "s" if nb_retard > 1 else ""

        alertes.append({
            "niveau": "danger",
            "message": f"Attention : {nb_retard} tâche{s} en retard !"
        })

    prochaine = resume_tasks.get("prochaine")

    if prochaine and prochaine.get("jours_restant") is not None:
        jours = prochaine["jours_restant"]

        if jours == 0:
            alertes.append({
                "niveau": "danger",
                "message": (
                    f"Urgent : La tâche '{prochaine['titre']}' "
                    "arrive à échéance aujourd'hui !"
                )
            })

        elif jours == 1:
            alertes.append({
                "niveau": "warning",
                "message": (
                    f"Rappel : La tâche '{prochaine['titre']}' "
                    "arrive à échéance demain."
                )
            })

    etat = resume_systeme.get("etat")

    if etat == "Critique":
        alertes.append({
            "niveau": "danger",
            "message": "L'utilisation du système est critique."
        })

    elif etat == "Élevé":
        alertes.append({
            "niveau": "warning",
            "message": "L'utilisation du système est élevée."
        })

    if not alertes:
        alertes.append({
            "niveau": "success",
            "message": "Tout va bien : aucune alerte à signaler."
        })

    return alertes

def creer_panel_alertes(alertes):
    lignes = []

    niveau_global = "success"

    for alerte in alertes:
        niveau = alerte["niveau"]
        message = alerte["message"]

        if niveau == "danger":
            lignes.append(f"[bold red]✖ {message}[/bold red]")
            niveau_global = "danger"

        elif niveau == "warning":
            lignes.append(f"[bold yellow]⚠ {message}[/bold yellow]")

            if niveau_global != "danger":
                niveau_global = "warning"

        else:
            lignes.append(f"[bold green]✓ {message}[/bold green]")

    contenu = "\n".join(lignes)

    if niveau_global == "danger":
        couleur_bordure = "red"
    elif niveau_global == "warning":
        couleur_bordure = "yellow"
    else:
        couleur_bordure = "green"

    return Panel(
        contenu,
        title="[bold]ALERTES[/bold]",
        border_style=couleur_bordure,
        padding=(0, 1)
    )
    
def afficher_dashboard():
    resume_tasks = obtenir_resume_task()
    resume_systeme = obtenir_resume_systeme()

    alertes = generer_alertes(
        resume_tasks,
        resume_systeme
    )

    panel_alertes = creer_panel_alertes(
        alertes
    )

    panel_tasks = creer_panel_tasks(
        resume_tasks
    )

    panel_systeme = creer_panel_systeme(
        resume_systeme
    )

    layout = Table.grid(
        expand=True,
        padding=(0, 1)
    )

    layout.add_column(
        ratio=3
    )

    layout.add_column(
        ratio=2
    )

    layout.add_row(
        panel_tasks,
        panel_systeme
    )

    console.print()
    console.print(panel_alertes)
    console.print(layout)
    console.print()