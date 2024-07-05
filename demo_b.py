import archgui
import numpy
import concurrent.futures
import time

# ###################################################################
# | Initialisation du module :                                      |
# ###################################################################

archgui.init()

# ###################################################################
# | Vous pouvez donner à vos events l’accès aux modules souhaitez   |
# | par l’utilisation de la variable "modules".                     |
# ###################################################################

modules = {
    "archgui": archgui,
    # "another_module": another-module,
}

archgui.define_modules(modules)

# ###################################################################
# | Affichage d'une fenêtre sur la base du model "demo_b" :         |
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

demo_b_uniqid = archgui.open(
    model="demo_b",
    wid="0",
    title="Archgui - Demo B")

# ###################################################################
# | Définition de la page principale :                              |
# | Lorsqu’une fenêtre principale est définie et que celle-ci est   |
# | fermé, la séquence d’arrêt du module est lancée.                |
# | Sans page principale de défini, la séquence d’arrêt est lancée  |
# | à la fermeture de la dernière fenêtre.                          |
# ###################################################################

archgui.define_main(demo_b_uniqid)

# ###################################################################
# | Update de la fenêtre dont l’uniqid est demo_b_uniqid :          |
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


def demo_b_create_graph(uniqid, container, gid):

    x1 = numpy.linspace(0, 10, 100)
    x2 = numpy.linspace(0, 10, 100)

    y1 = numpy.sin(x1)
    y2 = numpy.sin(x2 + 5)

    cx = 0
    data1 = []
    for xs in x1:
        data1.append([xs, y1[cx]])
        cx += 1

    cx = 0
    data2 = []
    for xs in x2:
        data2.append([xs, y2[cx]])
        cx += 1

    matrix = {
        "Label 1": {
            "data": data1
        },
        "Label 2": {
            "data": data2
        }
    }

    archgui.create_graph(
        uniqid=uniqid,
        container=container,
        gid=gid,
        matrix=matrix)

    return x1, x2


def demo_b_update_graph(uniqid, gid, x1, x2):

    for _ in range(20):

        y1 = numpy.sin(x1 - 0.1 * _)
        y2 = numpy.sin((x2 + 5) - 0.1 * _)

        cx = 0
        data1 = []
        for xs in x1:
            data1.append([xs, y1[cx]])
            cx += 1

        cx = 0
        data2 = []
        for xs in x2:
            data2.append([xs, y2[cx]])
            cx += 1

        matrix = {
            "Label 1": {
                "data": data1
            },
            "Label 2": {
                "data": data2
            }
        }

        archgui.update_graph(
            uniqid=uniqid,
            gid=gid,
            matrix=matrix)

        time.sleep(0.01)


def demo_b_update():

    container = "canvas_1"
    graph = "graph_1"

    x1, x2 = demo_b_create_graph(
        demo_b_uniqid,
        container,
        graph)

    demo_b_update_graph(demo_b_uniqid, graph, x1, x2)


pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
pool.submit(demo_b_update)

# ###################################################################
# | Lancement de l'écoute des events :                               |
# ###################################################################

archgui.run()

# ###################################################################
# | Aucune commande ne peut être lancée après .run()                |
# ###################################################################
