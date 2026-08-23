from features.tasks.storage import save_task, charger_tasks


def trouver_task(tasks, id_task):
    for task in tasks:
        if task["id"] == id_task:
            return task

    return None


def ajouter_task(titre):
    if not titre:
        return None

    tasks = charger_tasks()

    if tasks:
        id_task = max(task["id"] for task in tasks) + 1
    else:
        id_task = 1

    dict_task = dict(
        id=id_task,
        titre=titre,
        terminee=False
    )

    tasks.append(dict_task)
    save_task(tasks)

    return dict_task


def voir_tasks():
    return charger_tasks()


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