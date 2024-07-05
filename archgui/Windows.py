import copy
import uuid
import threading

from archgui.Printer import Printer

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pynput.keyboard import Key, Controller

# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
#
#    Classe gérant l'ouverture/fermeture et les interactions des fenêtres
#    Chaque fenêtre est issu d’un Model et possède ses propres Events
#
#    Chaque modèle peut etre appelé autant de fois que voulu à condition de
#    donner un nouvel wid pour chaque appel supplémentaire du meme Model
#
#    Chaque Model et Events sont chargé respectivement dans :
#     - self.wds_windows  copié dans  : self.wds_uniqid
#     - self.wds_events
#    La Window de FreeSimpleGUI est chargé dans : self.wds_simplegui
#
#    Les Events peuvent accéder à cette classe via la variable self.windows
#
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


class Windows:

    def __init__(self, platform, plt, fsg, workarea):

        self.modules = {}

        self.platform = platform
        self.plt = plt
        self.fsg = fsg
        self.wageo = workarea.geometry()

        # -----------------------------------------------------------------

        self.printer = Printer()
        self.lock = threading.Lock()

        # -----------------------------------------------------------------

        self.keyboard = Controller()
        self.key = Key

        # -----------------------------------------------------------------

        self.config = None
        self.window_main = None

        # -----------------------------------------------------------------

        self.models_window = {
            "sys": {},
            "usr": {}
        }
        self.models_event = {
            "sys": {},
            "usr": {}
        }

        # -----------------------------------------------------------------

        self.wds_simplegui = {}
        self.wds_windows = {}
        self.wds_uniqid = {}
        self.wds_events = {}
        self.wds_graphs = {}

    # ---------------------------------------------------------------------
    # / Chargement de la configuration de FreeSimpleGUI
    # ---------------------------------------------------------------------

    def load_config(self, config):
        self.config = config
        self.fsg.theme(self.config["general"]["theme"])

    # ---------------------------------------------------------------------
    # / Chargement des models et events
    # ---------------------------------------------------------------------

    def load_models(self, models_window, models_event):
        self.models_window = models_window
        self.models_event = models_event

    # ---------------------------------------------------------------------
    # / Chargement des modules de l’utilisateur
    # ---------------------------------------------------------------------

    def define_modules(self, modules) -> bool:
        self.modules = modules
        return True

    # ---------------------------------------------------------------------
    # / Définition de la fenêtre principale
    # ---------------------------------------------------------------------

    def define_main(self, uniqid: str) -> bool:
        if uniqid in self.wds_uniqid:
            self.window_main = uniqid
            return True
        else:
            self.printer.error("define_main()", "WINDOWS_DEFINE_MAIN", tb=False)
            return False

    # ---------------------------------------------------------------------
    # / Retourne l’UNIQID d’une fenêtre à partir du lvl + model + wid
    # ---------------------------------------------------------------------

    def uniqid(self, model: str, wid: str, lvl="usr"):

        uniqid = None
        if lvl in ["sys", "usr"]:
            if model in self.wds_windows[lvl]:
                if wid in self.wds_windows[lvl][model]:
                    uniqid = self.wds_windows[lvl][model][wid].uniqid

        if uniqid is not None:
            return uniqid
        else:
            return False

    # ---------------------------------------------------------------------
    # / Retourne l’UNIQID d’une fenêtre à partir du lvl + model + wid
    # ---------------------------------------------------------------------

    def window(self, uniqid: str) -> bool:
        if uniqid in self.wds_uniqid:
            return self.wds_uniqid[uniqid]
        else:
            self.printer.error("window()", "WINDOWS_WINDOW", tb=False)
            return False

    # ---------------------------------------------------------------------
    # / Retourne True ou False si la fenêtre existe ou non
    # ---------------------------------------------------------------------

    def exist(self, uniqid: str) -> bool:
        if uniqid in self.wds_uniqid:
            return True
        else:
            self.printer.error("exist()", "WINDOWS_EXIST", tb=False)
            return False

    # ---------------------------------------------------------------------
    # / Ouvre une nouvelle fenêtre
    # / Retourne l'UNIQID si la fenêtre n’existe pas deja
    # / Retourne False si la fenêtre existe déjà
    # ---------------------------------------------------------------------

    def open(self, model: str, wid: str, title: str, lvl="usr", uniqid=None, location=None, size=None):

        with self.lock:

            try:
                if lvl not in ["sys", "usr"]:
                    lvl = "usr"

                if lvl not in self.wds_windows:
                    self.wds_windows[lvl] = {}
                    self.wds_events[lvl] = {}

                if model not in self.wds_windows[lvl]:
                    self.wds_windows[lvl][model] = {}
                    self.wds_events[lvl][model] = {}

                if wid not in self.wds_windows[lvl][model]:
                    self.wds_windows[lvl][model][wid] = copy.copy(self.models_window[lvl][model])
                    self.wds_events[lvl][model][wid] = copy.copy(self.models_event[lvl][model])

                    simplegui = self.wds_windows[lvl][model][wid].open(
                        wid=wid,
                        title=title,
                        location=location,
                        size=size
                    )

                    if uniqid is None:
                        uniqid = uuid.uuid4()

                    self.wds_simplegui[uniqid] = simplegui
                    self.wds_uniqid[uniqid] = self.wds_windows[lvl][model][wid]
                    self.wds_graphs[uniqid] = {}

                    self.wds_windows[lvl][model][wid].uniqid = uniqid
                    self.wds_events[lvl][model][wid].uniqid = uniqid
                    self.wds_events[lvl][model][wid].wid = wid

                    self.wds_events[lvl][model][wid].windows = self
                    self.wds_events[lvl][model][wid].window = self.wds_windows[lvl][model][wid]

                    return uniqid

                else:
                    return False

            except:
                self.printer.error("open()", "WINDOWS_SHOW")
                return False

    # ---------------------------------------------------------------------
    # / Si la fenêtre est hide, la fenêtre est unhide et retourne True
    # / Si la fenêtre n’est pas hide, retourne False
    # ---------------------------------------------------------------------

    def show(self, uniqid: str) -> bool:

        try:

            if uniqid is not None and uniqid in self.wds_uniqid:
                if self.wds_uniqid[uniqid].is_hide:
                    self.wds_uniqid[uniqid].show()
                    return True
                else:
                    return False

        except:

            self.printer.error("show()", "WINDOWS_SHOW")
            return False

    # ---------------------------------------------------------------------
    # / Si la fenêtre n’est pas hide, la fenêtre est hide et retourne True
    # / Si la fenêtre est hide, retourne False
    # ---------------------------------------------------------------------

    def hide(self, uniqid: str):

        try:

            if uniqid is not None and uniqid in self.wds_uniqid:
                if self.wds_uniqid[uniqid].is_hide:
                    return False
                else:
                    self.wds_uniqid[uniqid].hide()
                    return True

        except:

            self.printer.error("hide()", "WINDOWS_SHOW")
            return False

    # ---------------------------------------------------------------------
    # / Modifie un item de la fenêtre ciblée et retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def update(self, uniqid: str, items: dict) -> bool:

        try:
            if uniqid is not None and uniqid in self.wds_uniqid:
                if self.wds_uniqid[uniqid].update(items):
                    return True
                else:
                    return False
        except:
            self.printer.error("update()", "WINDOWS_UPDATE")
            return False

    # ---------------------------------------------------------------------
    # / Ferme une fenêtre existante et retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def close(self, uniqid: str) -> bool:

        try:
            if uniqid is not None and uniqid in self.wds_uniqid:
                if self.wds_uniqid[uniqid].close():
                    self.close_and_purge(self.wds_simplegui[uniqid])
                    return True
                else:
                    return False
            else:
                return False

        except:
            self.printer.error("close()", "WINDOWS_CLOSE")
            return False

    # ---------------------------------------------------------------------
    # / Créé un graphique dans un conteneur (Canvas) dans la fenêtre ciblée
    # / Si l'ID du graphique n’est pas prédéfini il sera défini par un UUID
    # / Retourne l'ID du graphique
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def create_graph(self, uniqid: str, container=None, gid=None, matrix=None):

        try:

            dpi = self.wds_uniqid[uniqid].get_dpi()
            parent_size = self.wds_uniqid[uniqid].window[container].get_size()
            parent_pad = self.wds_uniqid[uniqid].window[container].Pad

            size_graph = [
                parent_size[0] - parent_pad[0][0] - parent_pad[1][0],
                parent_size[1] - parent_pad[0][1] - parent_pad[1][1],
            ]

            if size_graph[0] < 1 or size_graph[1] < 1:
                self.printer.error("create_graph()", "WINDOWS_CREATE_GRAPH_SIZE")
                return False

            fig = self.plt.Figure(
                figsize=(
                    size_graph[0] / dpi,
                    size_graph[1] / dpi
                ),
                dpi=dpi,
                facecolor=self.fsg.theme_background_color(),
                edgecolor=self.fsg.theme_text_color())

            self.plt.rcParams['text.color'] = self.fsg.theme_text_color()
            self.plt.rcParams['axes.labelcolor'] = self.fsg.theme_text_color()
            self.plt.rcParams['axes.edgecolor'] = self.fsg.theme_text_color()
            self.plt.rcParams['xtick.color'] = self.fsg.theme_text_color()
            self.plt.rcParams['ytick.color'] = self.fsg.theme_text_color()

            ax = fig.add_subplot(1, 1, 1)
            ax.set_facecolor(self.fsg.theme_button_color_background())

            colors = [
                self.fsg.theme_background_color(),
                self.fsg.theme_text_color()
            ]

            lines = {}
            colors_switch = 0

            xmins = []
            xmaxs = []
            ymins = []
            ymaxs = []

            for line in matrix:

                x = []
                y = []

                for data in matrix[line]["data"]:
                    x.append(data[0])
                    y.append(data[1])

                xmins.append(min(x))
                xmaxs.append(max(x))
                ymins.append(min(y))
                ymaxs.append(max(y))

                color = colors[colors_switch]

                if color in matrix[line]:
                    if matrix[line]["color"] is not None:
                        color = matrix[line]["color"]

                if color == colors[colors_switch]:
                    if colors_switch < len(colors) - 1:
                        colors_switch += 1
                    else:
                        colors_switch = 0

                lines[line] = ax.plot(x, y, label=line, color=color)

            ax.set_xlim(min(xmins), max(xmaxs))
            ax.set_ylim(min(ymins), max(ymaxs))

            legend = ax.legend(
                fontsize=self.config["general"]["font"][1],
                loc="upper left"
            ).get_frame()

            legend.set_facecolor(self.fsg.theme_button_color_background())
            legend.set_edgecolor(self.fsg.theme_background_color())

            canvas = FigureCanvasTkAgg(fig, self.wds_simplegui[uniqid][container].TKCanvas)
            canvas.get_tk_widget().forget()
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

            self.wds_simplegui[uniqid].refresh()

            self.wds_graphs[uniqid][gid] = {
                "matrix": matrix,
                "ax": ax,
                "lines": lines,
                "canvas": canvas
            }

            return gid

        except:
            self.printer.error("create_graph()", "WINDOWS_CREATE_GRAPH")
            return False

    # ---------------------------------------------------------------------
    # / Modification des données du graphique et rafraichissement
    # / Retourne True
    # / Sinon retourne False
    # ---------------------------------------------------------------------

    def update_graph(self, uniqid: str, gid=str, matrix=None) -> bool:

        try:

            xmins = []
            xmaxs = []
            ymins = []
            ymaxs = []

            for line in matrix:

                x = []
                y = []

                for data in matrix[line]["data"]:
                    x.append(data[0])
                    y.append(data[1])

                xmins.append(min(x))
                xmaxs.append(max(x))
                ymins.append(min(y))
                ymaxs.append(max(y))

                self.wds_graphs[uniqid][gid]["lines"][line][0].set_xdata(x)
                self.wds_graphs[uniqid][gid]["lines"][line][0].set_ydata(y)

            self.wds_graphs[uniqid][gid]["ax"].set_xlim(min(xmins), max(xmaxs))
            self.wds_graphs[uniqid][gid]["ax"].set_ylim(min(ymins), max(ymaxs))
            self.wds_graphs[uniqid][gid]["canvas"].draw()

            self.wds_simplegui[uniqid].refresh()
            return True

        except:

            self.printer.error("update_graph()", "WINDOWS_UPDATE_GRAPH")
            return False

    # ---------------------------------------------------------------------
    # / Purge les données lors da la fermeture d’une fenêtre
    # ---------------------------------------------------------------------

    def close_and_purge(self, window):

        wds_deleted = {}

        for uniqid in self.wds_simplegui:
            if self.wds_simplegui[uniqid] == window:
                wds_deleted[uniqid] = {
                    "lvl": self.wds_uniqid[uniqid].lvl,
                    "model": self.wds_uniqid[uniqid].model,
                    "wid": self.wds_uniqid[uniqid].wid
                }

        for uniqid in wds_deleted:

            del self.wds_graphs[uniqid]
            del self.wds_simplegui[uniqid]

            lvl = wds_deleted[uniqid]["lvl"]
            model = wds_deleted[uniqid]["model"]
            wid = wds_deleted[uniqid]["wid"]

            del self.wds_windows[lvl][model][wid]
            del self.wds_events[lvl][model][wid]

            if len(self.wds_windows[lvl][model]) == 0:
                del self.wds_windows[lvl][model]
                del self.wds_events[lvl][model]

            if len(self.wds_windows[lvl]) == 0:
                del self.wds_windows[lvl]
                del self.wds_events[lvl]

    # ---------------------------------------------------------------------
    # / Boucle d'écoute des Events
    # ---------------------------------------------------------------------

    def events_run(self):

        while True:

            window, event, values = self.fsg.read_all_windows()

            if event == self.fsg.WIN_CLOSED or event == 'Exit':

                if window is not None:
                    window.close()

                if self.window_main is not None:
                    if self.window_main in self.wds_uniqid:
                        if window == self.wds_uniqid[self.window_main].window:
                            break

                with self.lock:
                    self.close_and_purge(window)

            else:

                with self.lock:
                    wds_simplegui_cp = copy.copy(self.wds_simplegui)

                for uniqid in wds_simplegui_cp:
                    if uniqid in self.wds_simplegui:
                        if self.wds_simplegui[uniqid] == window:
                            lvl = self.wds_uniqid[uniqid].lvl
                            model = self.wds_uniqid[uniqid].model
                            wid = self.wds_uniqid[uniqid].wid
                            self.wds_events[lvl][model][wid].events(event, self.modules)

                del wds_simplegui_cp

            stop = True
            with self.lock:
                if len(self.wds_uniqid) > 0:
                    stop = False

            if stop:
                break
