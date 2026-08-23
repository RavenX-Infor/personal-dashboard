import psutil
import platform
from datetime import datetime

def octets_vers_go(octest):
    return octest / (1024 ** 3)

def uptime():
    demarrage = datetime.fromtimestamp(psutil.boot_time())
    maintenant = datetime.now()
    
    uptime = maintenant - demarrage
    secondes = int(uptime.total_seconds())

    heures = secondes // 3600
    minutes = (secondes % 3600) // 60

    return heures, minutes

def vue_generale():
    systeme = platform.system()
    version_systeme = platform.release()
    
    cpu = platform.processor()
    cpu_percent = psutil.cpu_percent(interval=1)

    memoire_ram = psutil.virtual_memory()
    pourcent_ram = memoire_ram.percent

    heures, minutes = uptime()

    print("==== VUE GÉNÉRALE ====")
    print(f"Système : {systeme} {version_systeme}")
    print(f"Processeur : {cpu}")
    print(f"CPU : {cpu_percent:.1f} %")
    print(f"RAM : {pourcent_ram:.1f} %")
    print(f"Uptime : {heures}h {minutes}min")

def processeur():
    pourcent_cpu = psutil.cpu_percent(interval=1)
    coeur_cpu = psutil.cpu_count(logical=False)
    thread_cpu = psutil.cpu_count(logical=True)
    freq_cpu = psutil.cpu_freq()

    print("==== CPU ===")

    print(f"Utilisation : {pourcent_cpu} %")
    print(f"Coeurs physiques : {coeur_cpu}")
    print(f"Coeurs logiques : {thread_cpu}")

    if freq_cpu is not None:
      print(f"Fréquence actuelle : {freq_cpu.current:.0f} MHz")
    else:
        print("Fréquence actuelle : indisponible")

def memoire():
    memoire_ram = psutil.virtual_memory()
    total_ram = octets_vers_go(memoire_ram.total)
    use_ram = octets_vers_go(memoire_ram.used)
    dispo_ram = octets_vers_go(memoire_ram.available)
    pourcent_ram = memoire_ram.percent

    print("==== RAM ===")
    print(f"Total : {total_ram:.2f} Go")
    print(f"Utilisé : {use_ram:.2f} Go")
    print(f"Disponible : {dispo_ram:.2f} Go")
    print(f"Utilisation : {pourcent_ram:.1f} %")

def stockage():
    partitions = psutil.disk_partitions()

    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
        except (PermissionError, OSError):
            continue

        total = octets_vers_go(usage.total)
        utilise = octets_vers_go(usage.used)
        libre = octets_vers_go(usage.free)

        print(f"Lecteur : {partition.device}")
        print(f"Total : {total:.2f} Go")
        print(f"Utilisé : {utilise:.2f} Go")
        print(f"Libre : {libre:.2f} Go")
        print(f"Utilisation : {usage.percent:.1f} %")
        print()