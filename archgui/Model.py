import re

from archgui.Printer import Printer
from archgui.Interpreter import Interpreter


# -------------------------------------------------------------------------
# / Converti une List en Tuple
# -------------------------------------------------------------------------


def list_to_tuple(ll):
    return tuple(list_to_tuple(x) for x in ll) if type(ll) is list else ll


# -------------------------------------------------------------------------
# / Vérifier qu'un paramètre de Size ou Location n’est pas vide
# / Retourne True ou False
# -------------------------------------------------------------------------


def pisnt_null(parameters):

    not_null = True
    if parameters["uniqid"] is None:
        not_null = False

    if parameters["lvl"] is not None:
        if parameters["model"] is not None:
            if parameters["wid"] is not None:
                not_null = True

    return not_null


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
#
#    Classe étant la surcouche de la Window de FreeSimpleGUI.
#    Elle génère le Layout de la Window et transmet les interactions issues
#    de la classe Windows à FreeSimpleGUI.
#
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------


class Model:

    def __init__(self, windows, lvl, model, specter):

        # -----------------------------------------------------------------

        self.windows = windows
        self.fsg = windows.fsg

        # -----------------------------------------------------------------

        self.is_hide = False
        self.reperc = re.compile(r"\d{2}%", re.IGNORECASE)

        # -----------------------------------------------------------------

        self.lvl = lvl
        self.model = model
        self.wid = None
        self.uniqid = None

        # -----------------------------------------------------------------

        self.title = ""

        # -----------------------------------------------------------------

        self.window = None

        # -----------------------------------------------------------------

        self.printer = Printer()
        self.interpreter = Interpreter(self.fsg, self.windows.config, self.window)

        # -----------------------------------------------------------------

        self.parameters = {
                "location_x": None,
                "location_y": None,
                "width": None,
                "height": None,
                "location_x_relative": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "location_y_relative": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "location_x_equal": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "location_y_equal": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "width_equal": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "height_equal": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "width_until": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "height_until": {
                    "lvl": None,
                    "model": None,
                    "wid": None,
                    "uniqid": None
                },
                "scrollable": False
            }

        # -----------------------------------------------------------------

        self.specter = specter
        self.items = self.specter["items"]

        # -----------------------------------------------------------------

        if len(self.specter["parameters"]) > 0:
            for parameter in self.specter["parameters"]:
                if isinstance(self.specter["parameters"][parameter], dict):
                    for sub_param in self.specter["parameters"][parameter]:
                        self.parameters[parameter][sub_param] = self.specter["parameters"][parameter][sub_param]
                else:
                    self.parameters[parameter] = self.specter["parameters"][parameter]

        # -----------------------------------------------------------------

        self.layout = None
        self.items_list = None

        # -----------------------------------------------------------------

        self.window_location = []
        self.window_size = []
        self.window_dpi = 80

    # ---------------------------------------------------------------------
    # / Définit la position de la fenêtre en X
    # ---------------------------------------------------------------------

    def set_location_x(self):

        if pisnt_null(self.parameters["location_x_relative"]):

            if not isinstance(self.window_location[0], int):
                self.window_location[0] = self.windows.wageo["x_min"]

            try:
                rel = self.parameters["location_x_relative"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    size = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_size()
                    location = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_location()
            except:
                self.printer.error("set_location_x()", "MODEL_SET_LOCATION_X")
                return False

            self.window_location[0] += size[0] + location[0]

        elif pisnt_null(self.parameters["location_x_equal"]):

            try:
                rel = self.parameters["location_x_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    location = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_location()
            except:
                self.printer.error("set_location_x()", "MODEL_SET_LOCATION_X")
                return False

            self.window_location[0] = location[0]

        elif self.parameters["location_x"] == 0 or self.parameters["location_x"] is None:
            self.window_location[0] = self.windows.wageo["x_min"]

        elif isinstance(self.parameters["location_x"], int):
            self.window_location[0] = self.windows.wageo["x_min"] + self.parameters["location_x"]

        elif self.reperc.match(str(self.parameters["location_x"])) and isinstance(self.parameters["width"], int):
            percent = int(self.parameters["location_x"].split("%")[0])
            self.window_location[0] = self.windows.wageo["x_min"]
            self.window_location[0] += int((self.windows.wageo["width"] / 100) * percent)
            self.window_location[0] -= int(self.parameters["width"] / 2)

        else:
            self.window_location[0] = 0

        return True

    # ---------------------------------------------------------------------
    # / Définit la position de la fenêtre en Y
    # ---------------------------------------------------------------------

    def set_location_y(self):

        if pisnt_null(self.parameters["location_y_relative"]):

            if not isinstance(self.window_location[1], int):
                self.window_location[1] = self.windows.wageo["y_min"]

            try:
                rel = self.parameters["location_y_relative"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    size = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_size()
                    location = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_location()
            except:
                self.printer.error("set_location_y()", "MODEL_SET_LOCATION_Y")
                return False

            self.window_location[1] += size[1] + location[1]
            self.window_location[1] += self.windows.wageo["titlebar_height"] + 1

        elif pisnt_null(self.parameters["location_y_equal"]):

            try:
                rel = self.parameters["location_y_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    location = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    location = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_location()
            except:
                self.printer.error("set_location_y()", "MODEL_SET_LOCATION_Y")
                return False

            self.window_location[1] = location[1]

        elif self.parameters["location_y"] == 0 or self.parameters["location_y"] is None:
            self.window_location[1] = self.windows.wageo["y_min"]

        elif isinstance(self.parameters["location_y"], int):
            self.window_location[1] = self.windows.wageo["y_min"] + self.parameters["location_y"]

        elif self.reperc.match(str(self.parameters["location_y"])) and isinstance(self.parameters["height"], int):
            percent = int(self.parameters["location_y"].split("%")[0])
            self.window_location[1] = self.windows.wageo["y_min"]
            self.window_location[1] += int((self.windows.wageo["height"] / 100) * percent)
            self.window_location[1] -= int(self.parameters["height"] / 2)

        else:
            self.window_location[1] = 0

        return True

    # ---------------------------------------------------------------------
    # / Définit la largeur de la fenêtre
    # ---------------------------------------------------------------------

    def set_size_width(self):

        if pisnt_null(self.parameters["width_equal"]):

            try:
                rel = self.parameters["width_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                else:
                    size = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_size()
            except:
                self.printer.error("set_size_width()", "MODEL_SET_SIZE_WIDTH")
                return False

            self.window_size[0] = size[0]

        elif pisnt_null(self.parameters["width_until"]):

            try:
                rel = self.parameters["width_until"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    size = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_location()
            except:
                self.printer.error("set_size_width()", "MODEL_SET_SIZE_WIDTH")
                return False

            self.window_size[0] = size[0]

        elif self.parameters["width"] is None:
            if self.parameters["height"] is None and not pisnt_null(self.parameters["height_equal"]):
                self.window_size[0] = None
            else:
                self.printer.error("set_size_width()", "MODEL_SET_SIZE_DUAL_NONE", tb=False)

        elif self.parameters["width"] == 0 or self.parameters["width"] == "100%":
            self.window_size[0] = self.windows.wageo["width"]
            self.window_size[0] -= self.window_location[0]

        elif isinstance(self.parameters["width"], int):
            self.window_size[0] = self.parameters["width"]

        elif self.reperc.match(str(self.parameters["width"])):
            percent = int(self.parameters["width"].split("%")[0])
            self.window_size[0] = int((self.windows.wageo["width"] / 100) * percent)

        else:
            self.window_size[0] = 0

        if self.window_size[0] is not None:
            self.window_size[0] = int(self.window_size[0])

        return True

    # ---------------------------------------------------------------------
    # / Définit la hauteur de la fenêtre
    # ---------------------------------------------------------------------

    def set_size_height(self):

        if pisnt_null(self.parameters["height_equal"]):

            try:
                rel = self.parameters["height_equal"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    size = self.windows.wds_uniqid[rel["uniqid"]].get_size()
                else:
                    size = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_size()
            except:
                self.printer.error("set_size_height()", "MODEL_SET_SIZE_HEIGHT")
                return False

            self.window_size[1] = size[1]

        elif pisnt_null(self.parameters["height_until"]):

            try:
                rel = self.parameters["height_until"]
                if rel["uniqid"] is not None and rel["uniqid"] in self.windows.wds_uniqid:
                    height_size = self.windows.wds_uniqid[rel["uniqid"]].get_location()
                else:
                    height_size = self.windows.wds_windows[rel["lvl"]][rel["model"]][rel["wid"]].get_location()
            except:
                self.printer.error("set_size_height()", "MODEL_SET_SIZE_HEIGHT")
                return False

            self.window_size[1] = height_size[1] - (2 * self.windows.wageo["titlebar_height"]) + 4

        elif self.parameters["height"] is None:
            if self.parameters["width"] is None and not pisnt_null(self.parameters["width_equal"]):
                self.window_size[1] = None
            else:
                self.printer.error("set_size_height()", "MODEL_SET_SIZE_DUAL_NONE", tb=False)

        elif self.parameters["height"] == 0 or self.parameters["height"] == "100%":
            self.window_size[1] = self.windows.wageo["height"]
            self.window_size[1] -= self.window_location[1]
            self.window_size[1] -= 6

        elif isinstance(self.parameters["height"], int):
            self.window_size[1] = self.parameters["height"]

        elif self.reperc.match(str(self.parameters["height"])):
            percent = int(self.parameters["height"].split("%")[0])
            self.window_size[1] = (self.windows.wageo["height"] / 100) * percent

        else:
            self.window_size[1] = 0

        if self.window_size[1] is not None:
            self.window_size[1] = int(self.window_size[1])

        return True

    # ---------------------------------------------------------------------
    # / Affiche la Window de FreeSimpleGUI
    # ---------------------------------------------------------------------

    def open(self, wid, title, location=None, size=None):

        self.wid = wid
        self.title = title

        # -----------------------------------------------------------------

        self.window_location = [0, 0]

        # -----------------------------------------------------------------

        self.window_size = [0, 0]

        # -----------------------------------------------------------------

        location_loaded = False
        if location is not None:
            if isinstance(location, list) and len(location) == 2:
                if isinstance(location[0], int) and isinstance(location[1], int):
                    self.window_location = [int(location[0]), int(location[1])]
                    location_loaded = True
                else:
                    self.printer.error("open()", "MODEL_OPEN_DYN_LOCATION_NOT_INT", tb=False)
            else:
                self.printer.error("open()", "MODEL_OPEN_DYN_LOCATION_LIST", tb=False)

        if not location_loaded:
            if not self.set_location_x():
                return False
            if not self.set_location_y():
                return False

        # -----------------------------------------------------------------

        size_loaded = False
        if size is not None:
            if isinstance(size, list) and len(size) == 2:
                if isinstance(size[0], int) and isinstance(size[1], int):
                    self.window_size = [int(size[0]), int(size[1])]
                    size_loaded = True
                else:
                    self.printer.error("open()", "MODEL_OPEN_DYN_SIZE_NOT_INT", tb=False)
            else:
                self.printer.error("open()", "MODEL_OPEN_DYN_SIZE_LIST", tb=False)

        if not size_loaded:
            if not self.set_size_width():
                return False
            if not self.set_size_height():
                return False

        # -----------------------------------------------------------------

        self.layout, self.items_list = self.interpreter.create_layout(self.items)

        # -----------------------------------------------------------------

        self.window = self.fsg.Window(self.title, self.layout,
                                              location=list_to_tuple(self.window_location),
                                              size=list_to_tuple(self.window_size))

        self.window.finalize()
        self.window_size = self.window.current_size_accurate()

        relocation = False
        if self.reperc.match(str(self.parameters["location_x"])) and not isinstance(self.parameters["width"], int):
            percent = int(self.parameters["location_x"].split("%")[0])
            self.window_location[0] = self.windows.wageo["x_min"]
            self.window_location[0] += int((self.windows.wageo["width"] / 100) * percent)
            self.window_location[0] -= int(self.window_size[0] / 2)
            relocation = True

        if self.reperc.match(str(self.parameters["location_y"])) and not isinstance(self.parameters["height"], int):
            percent = int(self.parameters["location_y"].split("%")[0])
            self.window_location[1] = self.windows.wageo["y_min"]
            self.window_location[1] += int((self.windows.wageo["height"] / 100) * percent)
            self.window_location[1] -= int(self.window_size[1] / 2)
            relocation = True

        if relocation:
            geometry = str(self.window_size[0]) + "x"
            geometry += str(self.window_size[1]) + "+"
            geometry += str(self.window_location[0]) + "+"
            geometry += str(self.window_location[1])

            self.window.TKroot.wm_geometry(newGeometry=geometry)
            self.window.TKroot.update()

            print("# -----------------------")
            print("# " + self.model)
            print("# width: " + str(self.window_size[0]))
            print("# height: " + str(self.window_size[1]))

        self.window_dpi = self.window.TKroot.winfo_fpixels('1i')

        # -----------------------------------------------------------------

        return self.window

    # ---------------------------------------------------------------------
    # / Affiche une fenêtre précédemment masquée
    # ---------------------------------------------------------------------

    def show(self):
        self.is_hide = False
        self.window.UnHide()

    # ---------------------------------------------------------------------
    # / Masque une fenêtre
    # ---------------------------------------------------------------------

    def hide(self):
        self.is_hide = True
        self.window.hide()

    # ---------------------------------------------------------------------
    # / Retourne la taille de la fenêtre
    # ---------------------------------------------------------------------

    def get_size(self):
        return self.window_size

    # ---------------------------------------------------------------------
    # / Retourne la position initiale de la fenêtre
    # ---------------------------------------------------------------------

    def get_location(self):
        return self.window_location

    # ---------------------------------------------------------------------
    # / Retourne le DPI de l'écran sur lequel est affiché la fenêtre
    # ---------------------------------------------------------------------

    def get_dpi(self):
        return self.window_dpi

    # ---------------------------------------------------------------------
    # / Retourne un Item de la fenêtre
    # ---------------------------------------------------------------------

    def get_item(self, item: str):
        return self.window[item].get()

    # ---------------------------------------------------------------------
    # / Modifie un Item de la fenêtre
    # ---------------------------------------------------------------------

    def update(self, items):

        error = False

        for item_updated in items:

            if all(k in item_updated for k in ("key", "mode")):

                key = item_updated["key"]
                mode = item_updated["mode"]

                if key in list(self.items_list.keys()):

                    key_type = self.items_list[key]["type"]

                    if mode in ["add", "replace", "clear"]:

                        if key_type == "column":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="column", tb=False)

                        if key_type == "frame":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="frame", tb=False)

                        if key_type == "canvas":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="canvas", tb=False)

                        if key_type == "label":

                            if "value" in item_updated:
                                value = item_updated["value"]

                                if mode == "add":
                                    self.window[item_updated["key"]].print(value)
                                elif mode == "replace":
                                    self.window[item_updated["key"]].update(value)

                            if mode == "clear":
                                self.window[item_updated["key"]].update()

                        if key_type == "in_line":

                            if "value" in item_updated:
                                value = item_updated["value"]

                                if mode == "add":
                                    value = self.window[item_updated["key"]].get() + value
                                    self.window[item_updated["key"]].update(value)
                                elif mode == "replace":
                                    self.window[item_updated["key"]].update(value)

                            if mode == "clear":
                                self.window[item_updated["key"]].update("")

                        if key_type == "in_lines":

                            if mode in ["add", "replace"]:

                                if mode == "replace":
                                    self.window[key].update("")

                                if "value" in item_updated:
                                    value = item_updated["value"]

                                    truncate_height = self.items_list[key]["truncate_height"]

                                    if truncate_height:
                                        truncate_width = True
                                    else:
                                        truncate_width = self.items_list[key]["truncate_width"]

                                    max_chars = self.window[item_updated["key"]].Size[0]
                                    max_lines = self.window[item_updated["key"]].Size[1]

                                    lines = ""
                                    lines_list = self.window[key].get().split("\n")

                                    if truncate_width:
                                        value = value[0:max_chars]

                                    if truncate_height:
                                        if len(lines_list) >= max_lines:
                                            dec = (len(lines_list) - max_lines) + 1
                                            lines_list = lines_list[dec:max_lines]

                                    for line in lines_list:
                                        if len(line) > 0:
                                            if truncate_height:
                                                lines += line[0: max_chars] + "\n"
                                            else:
                                                lines += line + "\n"

                                    lines += value

                                    self.window[key].update(lines)

                            elif mode == "clear":
                                self.window[key].update("")

                        if key_type == "button":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button", tb=False)

                        if key_type == "button_file":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button_file", tb=False)

                        if key_type == "button_files":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button_files", tb=False)

                        if key_type == "button_save":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button_save", tb=False)

                        if key_type == "button_folder":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button_folder", tb=False)

                        if key_type == "button_calendar":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button_calendar", tb=False)

                        if key_type == "button_color":
                            error = True
                            self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="button_color", tb=False)

                        if key_type == "combo":

                            if all(k in item_updated for k in ("value", "default_value")):

                                value = item_updated["value"]
                                default_value = item_updated["default_value"]

                                if mode == "add":

                                    if isinstance(value, str) and isinstance(default_value, str):
                                        value = self.window[item_updated["key"]].get().append(value)
                                        if default_value in value:
                                            self.window[item_updated["key"]].update(value, default_value)
                                        else:
                                            error = True
                                            self.printer.error("update()", "MODEL_COMBO_DEFAULT", tb=False)
                                    else:
                                        error = True
                                        self.printer.error("update()", "MODEL_COMBO_VALUE", tb=False)

                                elif mode == "replace":
                                    if isinstance(value, list) and isinstance(default_value, str):
                                        if default_value in value:
                                            self.window[item_updated["key"]].update(value, default_value)
                                        else:
                                            error = True
                                            self.printer.error("update()", "MODEL_COMBO_DEFAULT", tb=False)
                                    else:
                                        error = True
                                        self.printer.error("update()", "MODEL_COMBO_VALUE", tb=False)

                            else:
                                if mode == "clear":
                                    self.window[item_updated["key"]].update("", "")
                                else:
                                    error = True
                                    self.printer.error("update()", "MODEL_COMBO_UPDATE", tb=False)

                        if key_type == "progress_bar":

                            if "value" in item_updated:

                                max_value = self.window[item_updated["key"]].MaxValue
                                value = item_updated["value"]

                                if isinstance(value, int):

                                    if value <= max_value:

                                        if mode == "add":
                                            current_count = self.window[item_updated["key"]]
                                            current_count = current_count.TKProgressBar.TKProgressBarForReal['value']

                                            if current_count is None:
                                                current_count = 0

                                            value = current_count + value

                                            if value > max_value:
                                                value = max_value

                                            self.window[item_updated["key"]].update(value)

                                        elif mode == "replace":
                                            self.window[item_updated["key"]].update(value)

                                    else:
                                        error = True
                                        self.printer.error("update()", "MODEL_PROGRESS_BAR_SUP_MAX", tb=False)

                                else:
                                    error = True
                                    self.printer.error("update()", "MODEL_PROGRESS_BAR_INT", tb=False)

                            else:
                                if mode == "clear":
                                    self.window[item_updated["key"]].update(0)
                                else:
                                    error = True
                                    self.printer.error("update()", "MODEL_NO_UPDATE_ITEM", info="progress_bar", tb=False)

                    else:
                        error = True
                        self.printer.error("update()", "MODEL_UPDATE_MODE", tb=False)

        if error:
            return False
        else:
            self.windows.wds_simplegui[self.uniqid].refresh()
            return True

    # ---------------------------------------------------------------------
    # / Ferme la fenêtre
    # ---------------------------------------------------------------------

    def close(self):
        self.window.close()
