from rich import print


def print_in(lbl: str, length: int, pos: str):

    label_length = len(lbl)

    if length - label_length > 0:

        if pos == "left":

            ret = lbl
            for _ in range(length - label_length):
                ret += " "

        elif pos == "right":

            ret = ""
            for _ in range(length - label_length):
                ret += " "
            ret += lbl

        else:
            print("ok1")
            sys.exit(0)

    else:
        print("ok2")
        sys.exit(0)

    return ret


if __name__ == "__main__":

    import os
    import sys
    import json

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
        sys.exit(0)

    # ---------------------------------------------------------------------
    # / Chargement des arguments
    # ---------------------------------------------------------------------

    cmd = "regular"
    args = {
        "windows": None,
        "events": None,
        "config": None
    }

    for arg in sys.argv:

        split_cmd_items = arg.split("--list-items")
        split_cmd_item = arg.split("--item=")

        if len(split_cmd_items) == 2:
            if split_cmd_items[0] == "" and split_cmd_items[1] == "":
                cmd = "list-items"

        elif len(split_cmd_item) > 1:
            if split_cmd_item[0] == "" and split_cmd_item[1] in list(interpreter.items()):
                cmd = "items"
                args = {
                    "item": split_cmd_item[1]
                }
            else:
                printer.error("__main__", "MAIN_CMD_ITEM_NOT_EXIST",
                              info=split_cmd_item[1],
                              tb=False)
                sys.exit(0)

        else:

            split_windows = arg.split("windows=")
            split_events = arg.split("events=")
            split_config = arg.split("config=")

            if len(split_windows) > 1:
                args["windows"] = split_windows[1]

            if len(split_events) > 1:
                args["events"] = split_events[1]

            if len(split_config) > 1:
                args["config"] = split_config[1]

    if cmd == "regular":

        # -----------------------------------------------------------------
        # / Création des Events
        # -----------------------------------------------------------------

        def create_events(model):

            global interpreter
            global args

            windows_folder = args["windows"] + "/"
            events_folder = args["events"] + "/"

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

            for itm in items_list:
                if items_list[itm] in list(interpreter.trigger_items()):
                    ce_inner += "        if event == \"" + itm + "\":\n"
                    ce_inner += "            print(self.model + \" / \" + self.wid + \" : \" + \"" + itm + "\")\n\n"

            try:
                with open(events_folder + model + ".py", "a") as ev_file:
                    ev_file.write(ce_inner)
            except:
                printer.error("__main__", "MAIN_CE_MODEL_EVENT")

        # -----------------------------------------------------------------

        if args["windows"] is None:
            printer.error("__main__", "MAIN_FLD_WIN_NONE",
                          tb=False)
            sys.exit(0)

        if args["events"] is None:
            printer.error("__main__", "MAIN_FLD_EVENT_NONE",
                          tb=False)
            sys.exit(0)

        if not os.path.isdir(args["windows"]):
            printer.error("__main__", "MAIN_FLD_WIN_NOT_FOUND",
                          info=args["windows"],
                          tb=False)
            sys.exit(0)

        if not os.path.isdir(args["events"]):
            printer.error("__main__", "MAIN_FLD_EVENT_NOT_FOUND",
                          info=args["events"],
                          tb=False)
            sys.exit(0)

        # -----------------------------------------------------------------

        if args["config"] is not None:
            if args["config"].endswith(".json"):
                config_user = json.load(open(args["config"]))
            else:
                printer.error("__main__", "MAIN_FILE_CONFIG_JSON", tb=False)
                sys.exit(0)

        # -----------------------------------------------------------------
        # / Création des fichiers event manquant
        # -----------------------------------------------------------------

        windows = os.listdir(args["windows"])
        windows_name = []

        try:
            for window in windows:
                if window.endswith(".json"):
                    name = window.replace(".json", "")
                    windows_name.append(name)
                    if not os.path.isfile("./" + args["events"] + "/" + name + ".py"):
                        create_events(name)
        except:
            printer.error("__main__", "MAIN_CR_EVENTS_FILES")
            sys.exit(0)

        # -----------------------------------------------------------------
        # / Chargement des parties du Loader
        # -----------------------------------------------------------------

        windows = os.listdir(args["windows"])
        events = os.listdir(args["events"])

        # -----------------------------------------------------------------

        inner = "import archgui as ag\n\n"

        for window in windows:
            if window.endswith(".json"):
                name = window.replace(".json", "")
                if name + ".py" not in events:
                    create_events(name)
                inner += "from " + args["events"].replace("/", "_") + "." + name + " import Events as " + name + "_events\n"

        # -----------------------------------------------------------------

        inner += "\nconfig = " + str(config) + "\n"
        inner += "config_user = " + str(config_user) + "\n\n"

        # -----------------------------------------------------------------

        inner += "specters = {" + "\n"

        try:
            for window in windows:
                if window.endswith(".json"):
                    name = window.replace(".json", "")
                    window = json.load(open(args["windows"] + "/" + window))
                    inner += "    \"" + name + "\": " + str(window) + ",\n"
        except:
            printer.error("__main__", "MAIN_READ_WIN_SYS")
            sys.exit(0)

        inner += "}" + "\n\n\n"

        # -----------------------------------------------------------------

        inner += "def archgui():\n\n"

        inner += "    for parameter in config:\n"
        inner += "        if parameter in list(config_user):\n"
        inner += "            for sub_parameter in config[parameter]:\n"
        inner += "                if sub_parameter in list(config_user[parameter]):\n"
        inner += "                    if config[parameter][sub_parameter] != config_user[parameter][sub_parameter]:\n"
        inner += "                        config[parameter][sub_parameter] = config_user[parameter][sub_parameter]\n"

        # -----------------------------------------------------------------

        inner += "\n    # ---------------------------------------------------------------------\n\n"
        inner += "    models_event = {\n"

        for window in windows:
            if window.endswith(".json"):
                name = window.replace(".json", "")
                event = "eval(\"" + name + "_events\")(),"
                inner += "        \"" + name + "\": " + event + " \n"

        inner += "    }\n"

        # -----------------------------------------------------------------

        inner += "\n    # ---------------------------------------------------------------------\n"
        inner += "\n    ag.init(config, specters, models_event)\n"
        inner += "\n    return ag\n"

        # -----------------------------------------------------------------
        # / Réécriture de Loader
        # -----------------------------------------------------------------

        try:
            with open("ag_loader.py", "w") as file:
                file.write(inner)
        except:
            printer.error("__main__", "MAIN_REWRITE_LOADER")
            sys.exit(0)

    else:

        if cmd == "list-items":

            print()
            print("    Liste des items:")
            print()

            for item in interpreter.items():
                if item in list(interpreter.trigger_items()):
                    label = print_in("- ", 8, "right") + "[bright_red]" + print_in(item, 18, "left") + "[/]"
                    label += "->   "
                    label += "[blue]trigger[/]"
                    print(label)
                else:
                    print(print_in("- ", 8, "right") + "[bright_red]" + item + "[/]")

            print()

        elif cmd == "items":

            print()
            print("    Items: [bright_blue]" + args["item"] + "[/]")
            print()

            parameters = interpreter.config["parameters"]
            item = interpreter.config["items"][args["item"]]

            for parameter in item:
                label = print_in("- ", 8, "right")
                label += "[bright_red]" + print_in(parameter, 8, "left") + "[/]"
                label += " ->   "
                label += "[bright_red]" + print_in(parameters[parameter][0], 24, "left") + "[/]"

                if type(parameters[parameter][1]) == list:
                    if len(parameters[parameter][1]) > 3:

                        label += " ->   "
                        ctr = 0
                        nbr = 0

                        for p in parameters[parameter][1]:

                            label += print_in("'" + p + "'", 14, "left")
                            ctr += 1
                            nbr += 1

                            if nbr > 2:
                                if ctr < len(parameters[parameter][1]):
                                    label += "\n"
                                    label += print_in("", 52, "left")
                                nbr = 0

                    else:

                        label += " ->   "
                        first = True
                        for p in parameters[parameter][1]:
                            if not first:
                                label += ", "
                            label += "'" + p + "'"
                            first = False

                else:
                    label += " ->   " + str(parameters[parameter][1])

                print(label)

            print()


