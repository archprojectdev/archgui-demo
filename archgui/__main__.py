if __name__ == "__main__":

    import os
    import sys
    import json
    import shutil

    import FreeSimpleGUI as fsg

    from archgui.Interpreter import Interpreter
    from archgui.Printer import Printer

    printer = Printer()

    # ---------------------------------------------------------------------
    # / Chargement de la configuration par défaut
    # ---------------------------------------------------------------------

    config = None
    config_user = {}

    try:
        config = json.load(open("archgui/config/default.json"))
        interpreter = Interpreter(fsg, config, None)
    except:
        printer.error("__main__", "MAIN_CFG_DEFAULT")

    user_folder_windows = None
    user_folder_events = None
    user_file_config = None

    # ---------------------------------------------------------------------
    # / Création des Events
    # ---------------------------------------------------------------------

    def create_events(lvl, model, user=False):

        global interpreter

        if user:

            global user_folder_windows
            global user_folder_events
            global user_file_config

            windows_folder = user_folder_windows + "/"
            events_folder = user_folder_events + "/"

        else:

            windows_folder = "archgui/windows/" + lvl + "/"
            events_folder = "archgui/events/" + lvl + "/"

        specter = None

        try:
            specter = json.load(open(windows_folder + model + ".json"))
        except:
            printer.error("__main__", "MAIN_CE_MODEL_WIN")

        items = specter["items"]
        layout, items_list = interpreter.create_layout(items)

        ce_inner = "class Events:\n\n"

        ce_inner += "    def __init__(self):\n\n"

        ce_inner += "        self.windows = None\n"
        ce_inner += "        self.window = None\n\n"

        ce_inner += "    def events(self, event, modules):\n\n"

        ce_inner += "        if self.windows.uniqid is None:\n"
        ce_inner += "            self.windows.uniqid = None\n\n"

        for item in items_list:
            if items_list[item] in list(interpreter.trigger_items()):
                ce_inner += "        if event == \"" + item + "\":\n"
                ce_inner += "            print(self.lvl + \" / \" + self.model + \" / \" + self.wid + \" : \" + \"" + item + "\")\n\n"

        try:
            with open(events_folder + model + ".py", "a") as ev_file:
                ev_file.write(ce_inner)
        except:
            printer.error("__main__", "MAIN_CE_MODEL_EVENT")

    # ---------------------------------------------------------------------
    # / Chargement des fichiers utilisateurs
    # ---------------------------------------------------------------------

    for arg in sys.argv:

        split_windows = arg.split("windows=")
        split_events = arg.split("events=")
        split_config = arg.split("config=")

        if len(split_windows) > 1:
            user_folder_windows = split_windows[1]

        if len(split_events) > 1:
            user_folder_events = split_events[1]

        if len(split_config) > 1:
            user_file_config = split_config[1]

    user_folder_windows_check = False
    user_folder_events_check = False

    if user_folder_windows is None:
        printer.error("__main__", "MAIN_FLD_WIN_NONE",
                      tb=False)

    if user_folder_events is None:
        printer.error("__main__", "MAIN_FLD_EVENT_NONE",
                      tb=False)

    if not os.path.isdir(user_folder_windows):
        printer.error("__main__", "MAIN_FLD_WIN_NOT_FOUND",
                      info=user_folder_windows,
                      tb=False)

    if not os.path.isdir(user_folder_events):
        printer.error("__main__", "MAIN_FLD_EVENT_NOT_FOUND",
                      info=user_folder_events,
                      tb=False)

    if user_file_config is not None:
        if user_file_config.endswith(".json"):

            if not os.path.isfile(user_file_config):
                shutil.copyfile("archgui/config/default.json", user_file_config)
            else:

                try:
                    shutil.copyfile(user_file_config, "archgui/config/user.json")
                    config_user = json.load(open("archgui/config/user.json"))
                except:
                    printer.error("__main__", "MAIN_CFG_DEFAULT")

        else:
            printer.error("__main__", "MAIN_FILE_CONFIG_JSON", tb=False)

    # ---------------------------------------------------------------------
    # / Création des fichiers event manquant
    # ---------------------------------------------------------------------

    user_windows = os.listdir(user_folder_windows)
    user_windows_name = []

    try:
        for window in user_windows:
            if window.endswith(".json"):
                name = window.replace(".json", "")
                user_windows_name.append(name)
                if not os.path.isfile("./" + user_folder_events + "/" + name + ".py"):
                    create_events("usr", name, True)
    except:
        printer.error("__main__", "MAIN_CR_EVENTS_FILES")

    # ---------------------------------------------------------------------
    # / Copie des fichiers utilisateurs vers le module
    # ---------------------------------------------------------------------

    try:
        for window in user_windows:
            if window.endswith(".json"):
                name = window.replace(".json", "")
                shutil.copyfile(user_folder_windows + "/" + name + ".json", "archgui/windows/usr/" + name + ".json")
                shutil.copyfile(user_folder_events + "/" + name + ".py", "archgui/events/usr/" + name + ".py")
    except:
        printer.error("__main__", "MAIN_CP_USER_FILES")

    # ---------------------------------------------------------------------
    # / Suppression des fichiers utilisateurs résiduels
    # ---------------------------------------------------------------------

    try:
        for window in os.listdir("archgui/windows/usr/"):
            if not window.endswith(".json"):
                if os.path.isfile("archgui/windows/usr/" + window):
                    os.remove("archgui/windows/usr/" + window)
            else:
                if window.replace(".json", "") not in user_windows_name:
                    if os.path.isfile("archgui/windows/usr/" + window):
                        os.remove("archgui/windows/usr/" + window)

        for window in os.listdir("archgui/events/usr/"):
            if not window.endswith(".py"):
                if os.path.isfile("archgui/events/usr/" + window):
                    os.remove("archgui/events/usr/" + window)
            else:
                if window.replace(".py", "") not in user_windows_name:
                    if os.path.isfile("archgui/events/usr/" + window):
                        os.remove("archgui/events/usr/" + window)
    except:
        printer.error("__main__", "MAIN_DEL_FILES")

    # ---------------------------------------------------------------------
    # / Chargement des parties du Loader
    # ---------------------------------------------------------------------

    try:
        with open("archgui/Loader.py", "r") as file:
            data = file.read()
    except:
        printer.error("__main__", "MAIN_READ_LOADER")

    events_start = "# - LOADING EVENTS ZONE START"
    events_end = "# - LOADING EVENTS ZONE END"
    events_before = data.split(events_start)[0]
    events_after = data.split(events_end)[1]

    windows_start = "# - LOADING WINDOWS ZONE START"
    windows_end = "# - LOADING WINDOWS ZONE END"
    windows_before = events_after.split(windows_start)[0]
    windows_after = events_after.split(windows_end)[1]

    config_start = "# - LOADING CONFIG ZONE START"
    config_end = "# - LOADING CONFIG ZONE END"
    config_before = windows_after.split(config_start)[0]
    config_after = windows_after.split(config_end)[1]

    models_start = "        # - LOADING MODELS LIST ZONE START"
    models_end = "        # - LOADING MODELS LIST ZONE END"
    models_list_before = config_after.split(models_start)[0]
    models_list_after = config_after.split(models_end)[1]

    # ---------------------------------------------------------------------

    windows_sys = os.listdir("archgui/windows/sys")
    windows_usr = os.listdir("archgui/windows/usr")

    events_sys = os.listdir("archgui/events/sys")
    events_usr = os.listdir("archgui/events/usr")

    # ---------------------------------------------------------------------

    inner = events_before
    inner += events_start + "\n"

    for window_sys in windows_sys:
        if window_sys.endswith(".json"):
            name = window_sys.replace(".json", "")
            if name + ".py" not in events_sys:
                create_events("sys", name)
            inner += "from archgui.events.sys." + name + " import Events as sys_" + name + "_events\n"

    for window_usr in windows_usr:
        if window_usr.endswith(".json"):
            name = window_usr.replace(".json", "")
            if name + ".py" not in events_usr:
                create_events("usr", name)
            inner += "from archgui.events.usr." + name + " import Events as usr_" + name + "_events\n"

    inner += events_end

    # ---------------------------------------------------------------------

    inner += windows_before
    inner += windows_start + "\n"

    inner += "specters = {" + "\n"
    inner += "    \"sys\": {" + "\n"

    try:
        for window_sys in windows_sys:
            if window_sys.endswith(".json"):
                name = window_sys.replace(".json", "")
                window = json.load(open("archgui/windows/sys/" + window_sys))
                inner += "        \"" + name + "\": " + str(window) + ",\n"
    except:
        printer.error("__main__", "MAIN_READ_WIN_SYS")

    inner += "    }," + "\n"
    inner += "    \"usr\": {" + "\n"

    try:
        for window_usr in windows_usr:
            if window_usr.endswith(".json"):
                name = window_usr.replace(".json", "")
                window = json.load(open("archgui/windows/usr/" + window_usr))
                inner += "        \"" + name + "\": " + str(window) + ",\n"
    except:
        printer.error("__main__", "MAIN_READ_WIN_USR")

    inner += "    }," + "\n"
    inner += "}" + "\n"

    inner += windows_end

    # ---------------------------------------------------------------------

    inner += config_before
    inner += config_start + "\n"

    inner += "config = " + str(config) + "\n"
    inner += "config_user = " + str(config_user) + "\n"

    inner += config_end

    # ---------------------------------------------------------------------

    inner += models_list_before
    inner += models_start + "\n"

    inner += "        self.models_list = {\n"
    inner += "            \"sys\": [\n"

    for window_sys in windows_sys:
        if window_sys.endswith(".json"):
            name = window_sys.replace(".json", "")
            inner += "                \"" + name + "\",\n"

    inner += "            ],\n"
    inner += "            \"usr\": [\n"

    for window_usr in windows_usr:
        if window_usr.endswith(".json"):
            name = window_usr.replace(".json", "")
            inner += "                \"" + name + "\",\n"

    inner += "            ]\n"
    inner += "        }\n"

    inner += models_end
    inner += models_list_after

    # ---------------------------------------------------------------------
    # / Réécriture de Loader
    # ---------------------------------------------------------------------

    try:
        with open("archgui/Loader.py", "w") as file:
            file.write(inner)
    except:
        printer.error("__main__", "MAIN_REWRITE_LOADER")
