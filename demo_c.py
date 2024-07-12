from ag_loader import archgui
import concurrent.futures
import time

# ###################################################################
# | Initialisation du module :                                      |
# ###################################################################

ag = archgui()

# ###################################################################
# | Vous pouvez donner à vos events l’accès aux modules souhaitez   |
# | par l’utilisation de la variable "modules".                     |
# ###################################################################

modules = {
    "archgui": archgui,
    # "another_module": another-module,
}

ag.define_modules(modules)

# ###################################################################
# | Affichage d'une fenêtre sur la base du model "demo_c" :         |
# | L’argument "wid" différencie les fenêtres d’un meme model.      |
# | La commande show retourne l’id unique "uniqid" de la fenêtre.   |
# | "uniqid" est différent de "wid".                                |
# | Il peut être défini manuellement via l’argument : uniqid        |
# | Cela est nécessaire pour cibler une fenêtre lors d’un update    |
# | à partir d’un event                                             |
# ###################################################################

# ###################################################################
# | L’uniqid est utilisé pour cibler une fenêtre lors des cmds :    |
# |    .update()                                                    |
# |    .close()                                                     |
# |    .create_graph()                                              |
# |    .update_graph()                                              |
# ###################################################################

demo_c_uniqid = ag.open(
    model="demo_c",
    wid="0",
    title="Archgui - Demo C")

# ###################################################################
# | Définition de la page principale :                              |
# | Lorsqu’une fenêtre principale est définie et que celle-ci est   |
# | fermé, la séquence d’arrêt du module est lancée.                |
# | Sans page principale de défini, la séquence d’arrêt est lancée  |
# | à la fermeture de la dernière fenêtre.                          |
# ###################################################################

ag.define_main(demo_c_uniqid)

# ###################################################################
# | Update de la fenêtre dont l’uniqid est demo_c_uniqid :          |
# | Cette commande est lancée dans un thread parallèle pour ne pas  |
# | bloquer execution du .run()                                     |
# | Les deux composants updated dans cette commande sont :          |
# |    "label_1"                                                    |
# |    "in_line_1"                                                  |
# | Trois modes sont disponibles dans .update() :                   |
# |    "add"                                                        |
# |    "replace"                                                    |
# |    "clear"                                                      |
# ###################################################################


def demo_c_update():

    for _ in range(10):
        status = ag.update(uniqid=demo_c_uniqid, items=[
            {
                "key": "progress_bar_1",
                "mode": "add",
                "value": 10
            }
        ])
        if status is False:
            break
        time.sleep(1)


pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
pool.submit(demo_c_update)

# ###################################################################
# | Lancement de l'écoute des events :                               |
# ###################################################################

ag.run()

# ###################################################################
# | Aucune commande ne peut être lancée après .run()                |
# ###################################################################
