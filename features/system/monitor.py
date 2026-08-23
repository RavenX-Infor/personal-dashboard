import platform
from datetime import datetime

import psutil

from utils.ui import (
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


def vue_generale():
    titre("VUE GÉNÉRALE")

    systeme = platform.system()
    version_systeme = platform.release()

    cpu = platform.processor()
    cpu_percent = psutil.cpu_percent(interval=1)

    memoire_ram = psutil.virtual_memory()
    pourcent_ram = memoire_ram.percent

    jours, heures, minutes = uptime()

    print()
    info(f"Système     : {systeme} {version_systeme}")
    info(f"Processeur  : {cpu}")
    info(f"CPU         : {cpu_percent:.1f} %")
    info(f"RAM         : {pourcent_ram:.1f} %")

    if jours > 0:
        info(
            f"Uptime      : "
            f"{jours}j {heures}h {minutes}min"
        )
    else:
        info(
            f"Uptime      : "
            f"{heures}h {minutes}min"
        )


def processeur():
    titre("PROCESSEUR")

    pourcent_cpu = psutil.cpu_percent(interval=1)
    coeur_cpu = psutil.cpu_count(logical=False)
    thread_cpu = psutil.cpu_count(logical=True)
    freq_cpu = psutil.cpu_freq()

    print()
    info(f"Utilisation      : {pourcent_cpu:.1f} %")
    info(f"Cœurs physiques  : {coeur_cpu}")
    info(f"Cœurs logiques   : {thread_cpu}")

    if freq_cpu is not None:
        info(
            f"Fréquence actuelle : "
            f"{freq_cpu.current:.0f} MHz"
        )
    else:
        avertissement(
            "Fréquence actuelle indisponible."
        )


def memoire():
    titre("MÉMOIRE RAM")

    memoire_ram = psutil.virtual_memory()

    total_ram = octets_vers_go(
        memoire_ram.total
    )

    utilise_ram = octets_vers_go(
        memoire_ram.used
    )

    disponible_ram = octets_vers_go(
        memoire_ram.available
    )

    pourcent_ram = memoire_ram.percent

    print()
    info(f"Total       : {total_ram:.2f} Go")
    info(f"Utilisée    : {utilise_ram:.2f} Go")
    info(f"Disponible  : {disponible_ram:.2f} Go")
    info(f"Utilisation : {pourcent_ram:.1f} %")


def stockage():
    titre("STOCKAGE")

    partitions = psutil.disk_partitions()

    partitions_affichees = 0

    for partition in partitions:
        try:
            usage = psutil.disk_usage(
                partition.mountpoint
            )

        except (PermissionError, OSError):
            continue

        total = octets_vers_go(
            usage.total
        )

        utilise = octets_vers_go(
            usage.used
        )

        libre = octets_vers_go(
            usage.free
        )

        partitions_affichees += 1

        print()
        print(f" Lecteur {partition.device}")
        print(" " + "─" * 30)

        info(f"Total       : {total:.2f} Go")
        info(f"Utilisé     : {utilise:.2f} Go")
        info(f"Libre       : {libre:.2f} Go")
        info(f"Utilisation : {usage.percent:.1f} %")

    if partitions_affichees == 0:
        avertissement(
            "Aucun lecteur accessible."
        )