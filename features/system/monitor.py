import platform
from datetime import datetime

import psutil

from rich.table import Table
from rich.progress_bar import ProgressBar
from rich import box

from utils.ui import (
    console,
    titre,
    info,
    avertissement
)


def octets_vers_go(octets):
    return octets / (1024 ** 3)


def uptime():
    demarrage = datetime.fromtimestamp(
        psutil.boot_time()
    )

    maintenant = datetime.now()
    duree = maintenant - demarrage

    secondes = int(duree.total_seconds())

    jours = secondes // 86400
    heures = (secondes % 86400) // 3600
    minutes = (secondes % 3600) // 60

    return jours, heures, minutes


def couleur_utilisation(pourcentage):
    if pourcentage >= 85:
        return "red"

    if pourcentage >= 60:
        return "yellow"

    return "green"


def afficher_barre(pourcentage):
    couleur = couleur_utilisation(pourcentage)

    return ProgressBar(
        total=100,
        completed=pourcentage,
        width=30,
        complete_style=couleur,
        finished_style=couleur
    )


def vue_generale():
    titre("VUE GÉNÉRALE")

    systeme = platform.system()
    version_systeme = platform.release()

    cpu = platform.processor()
    cpu_percent = psutil.cpu_percent(interval=1)

    memoire_ram = psutil.virtual_memory()
    ram_percent = memoire_ram.percent

    jours, heures, minutes = uptime()

    table = Table(
        box=box.ROUNDED,
        show_header=False,
        expand=True
    )

    table.add_column("Information", style="bold cyan")
    table.add_column("Valeur")

    table.add_row(
        "Système",
        f"{systeme} {version_systeme}"
    )

    table.add_row(
        "Processeur",
        cpu if cpu else "Non renseigné"
    )

    table.add_row(
        "Uptime",
        f"{jours}j {heures}h {minutes}min"
    )

    console.print(table)

    console.print("\n[bold]CPU[/bold]")
    console.print(
        afficher_barre(cpu_percent),
        f" {cpu_percent:.1f}%"
    )

    console.print("\n[bold]RAM[/bold]")
    console.print(
        afficher_barre(ram_percent),
        f" {ram_percent:.1f}%"
    )


def processeur():
    titre("PROCESSEUR")

    pourcent_cpu = psutil.cpu_percent(interval=1)
    coeur_cpu = psutil.cpu_count(logical=False)
    thread_cpu = psutil.cpu_count(logical=True)
    freq_cpu = psutil.cpu_freq()

    table = Table(
        box=box.ROUNDED,
        show_header=False,
        expand=True
    )

    table.add_column(
        "Information",
        style="bold cyan"
    )

    table.add_column("Valeur")

    table.add_row(
        "Cœurs physiques",
        str(coeur_cpu)
    )

    table.add_row(
        "Cœurs logiques",
        str(thread_cpu)
    )

    if freq_cpu is not None:
        table.add_row(
            "Fréquence actuelle",
            f"{freq_cpu.current:.0f} MHz"
        )
    else:
        table.add_row(
            "Fréquence actuelle",
            "Indisponible"
        )

    console.print(table)

    console.print("\n[bold]Utilisation CPU[/bold]")

    console.print(
        afficher_barre(pourcent_cpu),
        f" {pourcent_cpu:.1f}%"
    )


def memoire():
    titre("MÉMOIRE RAM")

    ram = psutil.virtual_memory()

    total = octets_vers_go(ram.total)
    utilise = octets_vers_go(ram.used)
    disponible = octets_vers_go(ram.available)

    table = Table(
        box=box.ROUNDED,
        show_header=True,
        header_style="bold cyan",
        expand=True
    )

    table.add_column("Total")
    table.add_column("Utilisée")
    table.add_column("Disponible")
    table.add_column("Utilisation")

    table.add_row(
        f"{total:.2f} Go",
        f"{utilise:.2f} Go",
        f"{disponible:.2f} Go",
        f"{ram.percent:.1f}%"
    )

    console.print(table)

    console.print("\n[bold]Utilisation RAM[/bold]")

    console.print(
        afficher_barre(ram.percent),
        f" {ram.percent:.1f}%"
    )


def stockage():
    titre("STOCKAGE")

    partitions = psutil.disk_partitions()

    table = Table(
        box=box.ROUNDED,
        header_style="bold cyan",
        expand=True
    )

    table.add_column("Lecteur")
    table.add_column("Total", justify="right")
    table.add_column("Utilisé", justify="right")
    table.add_column("Libre", justify="right")
    table.add_column("Utilisation", justify="right")

    partitions_affichees = 0

    for partition in partitions:
        try:
            usage = psutil.disk_usage(
                partition.mountpoint
            )
        except (PermissionError, OSError):
            continue

        total = octets_vers_go(usage.total)
        utilise = octets_vers_go(usage.used)
        libre = octets_vers_go(usage.free)

        couleur = couleur_utilisation(
            usage.percent
        )

        table.add_row(
            partition.device,
            f"{total:.2f} Go",
            f"{utilise:.2f} Go",
            f"{libre:.2f} Go",
            f"[{couleur}]{usage.percent:.1f}%[/{couleur}]"
        )

        partitions_affichees += 1

    if partitions_affichees == 0:
        avertissement(
            "Aucun lecteur accessible."
        )
        return

    console.print(table)