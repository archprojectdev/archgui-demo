from rich import print
import os
import sys
import traceback


class Printer:

    def __init__(self):

        self.interpreter = None
        self.model = None

    @staticmethod
    def error_info(code, info):

        filename = ""
        exception = ""

        if code == "MAIN_CMD_ITEM_NOT_EXIST":
            filename = "__main__.py"
            exception = "L'item '" + info + "' sélectionné n'existe pas."

        if code == "MAIN_FLD_WIN_NONE":
            filename = "__main__.py"
            exception = "L'argument 'windows' n'est pas défini."

        if code == "MAIN_FLD_EVENT_NONE":
            filename = "__main__.py"
            exception = "L'argument 'events' n'est pas défini."

        if code == "MAIN_FLD_WIN_NOT_FOUND":
            filename = "__main__.py"
            exception = "Le dossier '" + info + "' n'existe pas."

        if code == "MAIN_FLD_EVENT_NOT_FOUND":
            filename = "__main__.py"
            exception = "Le dossier '" + info + "' n'existe pas."

        if code == "MAIN_FILE_CONFIG_JSON":
            filename = "__main__.py"
            exception = "Le fichier 'config' ciblé doit avoir une extension '.json'"

        if code in ["INIT_DEFINE_MODULES", "INIT_DEFINE_MAIN",
                    "INIT_OPEN", "INIT_UPDATE", "INIT_CLOSE",
                    "INIT_CREATE_GRAPH", "INIT_UPDATE_GRAPH",
                    "INIT_RUN"]:
            filename = "__init__.py"
            exception = "Archgui n'est pas initialisé."

        if code == "INIT_DEFINE_MODULES_RETURN":
            filename = "__init__.py"
            exception = "Impossible de charger les modules dans Archgui."

        if code == "INIT_DEFINE_MAIN_RETURN":
            filename = "__init__.py"
            exception = "Impossible de définir la fenêtre main dans Archgui."

        if code == "INIT_OPEN_RETURN":
            filename = "__init__.py"
            exception = "Impossible d'ouvrir la fenêtre."

        if code == "INIT_UPDATE_RETURN":
            filename = "__init__.py"
            exception = "Impossible de mettre à jour les items la fenêtre."

        if code == "INIT_CLOSE_RETURN":
            filename = "__init__.py"
            exception = "Impossible de fermer la fenêtre."

        if code == "INIT_CREATE_GRAPH_RETURN":
            filename = "__init__.py"
            exception = "Impossible de créer le graphique."

        if code == "INIT_UPDATE_GRAPH_RETURN":
            filename = "__init__.py"
            exception = "Impossible de mettre à jour le graphique."

        if code in ["WINDOWS_DEFINE_MAIN", "WINDOWS_WINDOW", "WINDOWS_EXIST"]:
            filename = "Windows.py"
            exception = "Uniqid introuvable. La fenêtre cible n'est probablement pas encore ouverte."

        if code == "WINDOWS_CREATE_GRAPH_SIZE":
            filename = "Windows.py"
            exception = "La taille du graphique ne permet pas sa création."

        if code in ["MODEL_OPEN_DYN_LOCATION_NOT_INT", "MODEL_OPEN_DYN_LOCATION_LIST"]:
            filename = "Model.py"
            exception = "Si une position (location) dynamique de fenêtre est définie lors d'un open().\n" \
                        "Elle doit etre sous cette forme: list(int, int)"

        if code in ["MODEL_OPEN_DYN_SIZE_NOT_INT", "MODEL_OPEN_DYN_SIZE_LIST"]:
            filename = "Model.py"
            exception = "Si une taille (size) dynamique de fenêtre est définie lors d'un open().\n" \
                        "Elle doit etre sous cette forme: list(int, int)"

        if code in ["MODEL_SET_SIZE_DUAL_NONE"]:
            filename = "Model.py"
            exception = "Si la largeur (width) ou la hauteur (height) sont en 'null',\n" \
                        "les deux doivent etre en 'null'."

        if code in ["MODEL_UPDATE_MODE"]:
            filename = "Model.py"
            exception = "Les modes de mise à jour (update) doivent etre: \n"
            exception += "      - add\n"
            exception += "      - replace\n"
            exception += "      - clear"

        if code in ["MODEL_NO_UPDATE_ITEM"]:
            filename = "Model.py"
            exception = "Pas de mise à jour (update) possible sur l'item: " + info

        if code in ["MODEL_COMBO_DEFAULT"]:
            filename = "Model.py"
            exception = "Le paramètre 'default_value' doit etre défini."

        if code in ["MODEL_COMBO_VALUE"]:
            filename = "Model.py"
            exception = "Le paramètre 'default_value' ainsi que 'value' doit etre défini."

        if code in ["MODEL_COMBO_UPDATE"]:
            filename = "Model.py"
            exception = "Pour effectuer une mise à jour (update),\n" \
                        "Le paramètre 'default_value' ainsi que 'value' doit etre défini."

        if code in ["MODEL_PROGRESS_BAR_SUP_MAX"]:
            filename = "Model.py"
            exception = "Pour effectuer une mise à jour (update) sur un item 'progress_bar',\n" \
                        "La valeur doit etre inférieur ou égale a la valeur max."

        if code in ["MODEL_PROGRESS_BAR_INT"]:
            filename = "Model.py"
            exception = "Pour effectuer une mise à jour (update) sur un item 'progress_bar',\n" \
                        "La valeur doit etre un INT."

        return filename, exception

    def resolve(self, code, exception):

        if code == "MAIN_CMD_ITEM_NOT_EXIST":
            print("[purple4]Info[/]:  La liste des items est disponible via la commande suivant:")
            print("[purple4]Retry[/]: python -m archgui --list-items\n")

        if code in ["MAIN_FLD_WIN_NONE", "MAIN_FLD_EVENT_NONE",
                    "MAIN_FLD_WIN_NOT_FOUND", "MAIN_FLD_EVENT_NOT_FOUND"]:

            print("[purple4]Info[/]:  Les arguments suivant doivent être passé:")
            print("      - windows")
            print("      - events")
            print("      - config\n")
            print("[purple4]Retry[/]: python -m archgui "
                  "windows=YOUR_WINDOWS_FOLDER "
                  "events=YOUR_EVENTS_FOLDER "
                  "config=YOUR_CONFIG.JSON\n")

        if code in ["WINDOWS_SHOW", "WINDOWS_UPDATE", "WINDOWS_CLOSE"]:
            print("[purple4]Info[/]:  Vous tentez probablement d'accéder à une fenêtre")
            print("       ou à un model de fenêtre qui n'existe pas.\n")

    def error(self, fnc, code, info=None, tb=True):

        if tb:

            exc_type, exc_obj, exc_tb = sys.exc_info()
            filename = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            formatted_lines = traceback.format_exc().splitlines()

            exception = formatted_lines[-1]
            script = formatted_lines[2].lstrip()

            print("\n[bright_red]Error[/]: In file [bright_blue]" + filename + "[/] line " + "[bright_blue]" + str(exc_tb.tb_lineno) + "[/]")
            print("[bright_yellow]       Exception[/]: " + exception)
            print("[bright_yellow]        Function[/]: [dim white]" + fnc + "[/]")
            print("[bright_yellow]          Script[/]: " + script + "\n")
            self.resolve(code, exception)

        else:

            filename, exception = self.error_info(code, info)
            print("\n[bright_red]Error[/]: In file [bright_blue]" + filename + "[/]")
            print("[bright_yellow]       Exception[/]: " + exception)
            print("[bright_yellow]        Function[/]: [dim white]" + fnc + "[/]\n")
            self.resolve(code, exception)
