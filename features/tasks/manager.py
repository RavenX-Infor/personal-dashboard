from datetime import datetime, timedelta

from features.tasks.storage import save_task, charger_tasks


def trouver_task(tasks, id_task):
    for task in tasks:
        if task["id"] == id_task:
            return task

    return None


def valider_deadline(deadline):
    if not deadline:
        return None, "deadline_invalide"

    try:
        deadline_date = datetime.strptime(deadline, "%d/%m/%Y")
    except ValueError:
        return None, "deadline_invalide"

    maintenant = datetime.now()
    date_limite = maintenant + timedelta(days=365)

    if deadline_date.date() < maintenant.date():
        return None, "deadline_passe"

    if deadline_date > date_limite:
        return None, "deadline_trop_loin"

    return deadline_date, None


def ajouter_task(titre, priorite, deadline):
    priorites_valides = ["faible", "moyenne", "haute"]

    if not titre:
        return None, "titre_vide"

    if priorite not in priorites_valides:
        return None, "priorite_invalide"

    deadline_date, erreur = valider_deadline(deadline)

    if erreur:
        return None, erreur

    tasks = charger_tasks()

    if tasks:
        id_task = max(task["id"] for task in tasks) + 1
    else:
        id_task = 1

    date_creation = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    dict_task = {
        "id": id_task,
        "titre": titre,
        "priorite": priorite,
        "date_creation": date_creation,
        "deadline": deadline,
        "terminee": False
    }

    tasks.append(dict_task)
    save_task(tasks)

    return dict_task, None


def voir_tasks():
    return charger_tasks()


def modif_tasks(id_task, new_titre=None, new_prio=None, new_deadline=None):
    tasks = charger_tasks()
    priorites_valides = ["faible", "moyenne", "haute"]

    task = trouver_task(tasks, id_task)

    if task is None:
        return None, "task_introuvable"

    if new_titre is not None:
        new_titre = new_titre.strip()

        if not new_titre:
            return None, "titre_vide"

        task["titre"] = new_titre

    if new_prio is not None:
        new_prio = new_prio.strip().lower()

        if new_prio not in priorites_valides:
            return None, "priorite_invalide"

        task["priorite"] = new_prio

    if new_deadline is not None:
        deadline_date, erreur = valider_deadline(new_deadline)

        if erreur:
            return None, erreur

        task["deadline"] = new_deadline

    save_task(tasks)

    return task, None


def terminer_task(id_task):
    tasks = charger_tasks()

    task = trouver_task(tasks, id_task)

    if task is None:
        return None

    if task["terminee"]:
        return False

    task["terminee"] = True
    save_task(tasks)

    return task


def supprimer_task(id_task):
    tasks = charger_tasks()

    task = trouver_task(tasks, id_task)

    if task is None:
        return None

    tasks.remove(task)
    save_task(tasks)

    return task