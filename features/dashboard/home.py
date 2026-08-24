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

    return Panel(
        table,
        title="[bold cyan]SYSTÈME[/bold cyan]",
        border_style="cyan",
        padding=(1, 1)
    )


def afficher_dashboard():
    resume_tasks = obtenir_resume_task()
    resume_systeme = obtenir_resume_systeme()

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
    console.print(layout)
    console.print()