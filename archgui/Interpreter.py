# -------------------------------------------------------------------------
# / Converti une List en Tuple
# -------------------------------------------------------------------------


def list_to_tuple(ll):
    return tuple(list_to_tuple(x) for x in ll) if type(ll) is list else ll


# -------------------------------------------------------------------------
# -------------------------------------------------------------------------
#
#    Classe permettant de convertir le model.json en item FreeSimpleGUI
#
# -------------------------------------------------------------------------
# -------------------------------------------------------------------------

class Interpreter:

    def __init__(self, fsg, config, window):

        # -----------------------------------------------------------------

        self.fsg = fsg
        self.window = window
        self.config = config

        # -----------------------------------------------------------------

        self.config["parameters"] = {
            "t": ["type", "'str'"],
            "v": ["value", "'str'"],
            "k": ["key", "'str'"],
            "p": ["pad", (("int", "int"), ("int", "int"))],
            "s": ["size", ("int", "int")],
            "d": ["disabled", "'bool'"],
            "f": ["font", ("str", "int")],
            "g": ["group", "'str'"],
            "df": ["default", "'bool'"],
            "dv": ["default_value", "'str'"],
            "tl": ["tab_location", ["top", "topleft", "topright", "left", "lefttop", "leftbottom", "right", "righttop", "rightbottom", "bottom", "bottomleft", "bottomright"]],
            "ro": ["readonly", "'bool'"],
            "av": ["vertical_alignment", ["top", "center", "bottom"]],
            "ae": ["element_justification", ["left", "center", "right"]],
            "tg": ["target", "'str'"],
            "sc": ["scrollable", "'bool'"],
            "scvo": ["vertical_scroll_only", "'bool'"],
            "ns": ["no_scrollbar", "'bool'"],
            "xx": ["expand_x", "'bool'"],
            "xy": ["expand_y", "'bool'"],
            "tw": ["truncate_height", "'bool'"],
            "th": ["truncate_width", "'bool'"]
        }

        # -----------------------------------------------------------------

        self.config["items"] = {
            "column": ["k", "p", "s", "sc", "scvo", "av", "ae", "xx", "xy"],
            "tab_group": ["k", "p", "s", "f", "tl", "xx", "xy"],
            "tab": ["k", "p", "d", "ae", "xx", "xy"],
            "frame": ["k", "p", "s", "av", "ae", "f", "xx", "xy"],
            "canvas": ["k", "p", "s", "f", "xx", "xy"],
            "label": ["k", "p", "s", "f", "xx", "xy", "v"],
            "progress_bar": ["k", "p", "s", "xx", "xy", "v"],
            "in_line": ["k", "p", "s", "ro", "f", "xx", "xy", "v"],
            "in_lines": ["k", "p", "s", "f", "d", "ns", "xx", "xy", "v"],
            "in_radio": ["k", "p", "s", "ro", "f", "xx", "xy", "v", "g"],
            "in_checkbox": ["k", "p", "d", "s", "xx", "xy", "v"],
            "in_combo": ["k", "p", "d", "s", "xx", "xy", "dv", "v"],
            "button": ["k", "p", "s", "d", "f", "v"],
            "button_file": ["k", "tg", "p", "s", "d", "f", "v"],
            "button_files": ["k", "tg", "p", "s", "d", "f", "v"],
            "button_save": ["k", "tg", "p", "s", "d", "f", "v"],
            "button_folder": ["k", "tg", "p", "s", "d", "f", "v"],
            "button_calendar": ["k", "tg", "p", "s", "d", "f", "v"],
            "button_color": ["k", "tg", "p", "s", "d", "f", "v"],
        }

        # -----------------------------------------------------------------

        self.config["trigger_items"] = {
            "in_line": self.config["items"]["in_line"],
            "in_lines": self.config["items"]["in_lines"],
            "in_radio": self.config["items"]["in_radio"],
            "in_checkbox": self.config["items"]["in_checkbox"],
            "in_combo": self.config["items"]["in_combo"],
            "button": self.config["items"]["button"],
            "button_file": self.config["items"]["button_file"],
            "button_files": self.config["items"]["button_files"],
            "button_save": self.config["items"]["button_save"],
            "button_folder": self.config["items"]["button_folder"],
            "button_calendar": self.config["items"]["button_calendar"],
            "button_color": self.config["items"]["button_color"]
        }

    # ---------------------------------------------------------------------
    # / Agrège les paramètres par défaut et les paramètres spécifiés
    # / pour chaque item du model
    # ---------------------------------------------------------------------

    def create_parameters(self, item):

        parameters = {}
        if "k" in item[0]:
            parameters["t"] = item[0]["t"]

        for parameter in self.config[item[0]["t"]]:
            if parameter in self.config["parameters"]:

                parameters[parameter] = self.config[item[0]["t"]][parameter]

                if parameter in item[0]:
                    parameters[parameter] = item[0][parameter]

                if isinstance(parameters[parameter], list):
                    parameters[parameter] = list_to_tuple(parameters[parameter])

        return parameters

    # ---------------------------------------------------------------------
    # / Créé le layout du model pour FreeSimpleGUI
    # ---------------------------------------------------------------------

    def create_layout(self, items):

        items_list = {}
        layout, items_list = self.create_items(items, items_list)

        return layout, items_list

    # ---------------------------------------------------------------------
    # / Liste des items
    # ---------------------------------------------------------------------

    def items(self):
        return self.config["items"]

    # ---------------------------------------------------------------------
    # / Liste des items pouvant etre trigger dans un event
    # ---------------------------------------------------------------------

    def trigger_items(self):
        return self.config["trigger_items"]

    # ---------------------------------------------------------------------
    # / Créé les items pour le layout
    # ---------------------------------------------------------------------

    def create_items(self, items=None, items_list=None):

        layout = []

        row_c = 0
        for row in items:

            layout.append([])

            for item in row:

                if item[0]["t"] == "column":
                    rl, items_list = self.add_column(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "tab_group":
                    rl, items_list = self.add_tab_group(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "tab":
                    rl, items_list = self.add_tab(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "frame":
                    rl, items_list = self.add_frame(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "canvas":
                    rl, items_list = self.add_canvas(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "label":
                    rl, items_list = self.add_label(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "in_line":
                    rl, items_list = self.add_in_line(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "in_lines":
                    rl, items_list = self.add_in_lines(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "in_radio":
                    rl, items_list = self.add_in_radio(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "in_checkbox":
                    rl, items_list = self.add_in_checkbox(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "in_combo":
                    rl, items_list = self.add_in_combo(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button":
                    rl, items_list = self.add_button(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button_file":
                    rl, items_list = self.add_button_file(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button_files":
                    rl, items_list = self.add_button_files(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button_save":
                    rl, items_list = self.add_button_save(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button_folder":
                    rl, items_list = self.add_button_folder(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button_calendar":
                    rl, items_list = self.add_button_calendar(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "button_color":
                    rl, items_list = self.add_button_color(item, items_list)
                    layout[row_c].append(rl)
                elif item[0]["t"] == "progress_bar":
                    rl, items_list = self.add_progress_bar(item, items_list)
                    layout[row_c].append(rl)

            row_c += 1

        return layout, items_list

    # ---------------------------------------------------------------------
    # / Les items pouvant etre utilisé dans un model :
    # ---------------------------------------------------------------------

    def add_column(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        items, items_list = self.create_items(
            items=item[1],
            items_list=items_list)

        new_item = self.fsg.Column(
            items,
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            scrollable=parameters["sc"],
            vertical_scroll_only=parameters["scvo"],
            vertical_alignment=parameters["av"],
            element_justification=parameters["ae"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_tab_group(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        items, items_list = self.create_items(
            items=item[1],
            items_list=items_list)

        new_item = self.fsg.TabGroup(
            items,
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            font=parameters["f"],
            enable_events=True,
            tab_location=parameters["tl"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_tab(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        items, items_list = self.create_items(
            items=item[1],
            items_list=items_list)

        new_item = self.fsg.Tab(
            parameters["v"],
            items,
            key=parameters["k"],
            pad=parameters["p"],
            disabled=parameters["d"],
            element_justification=parameters["ae"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_frame(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        items, items_list = self.create_items(
            items=item[1],
            items_list=items_list)

        new_item = self.fsg.Frame(
            parameters["v"],
            items,
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            vertical_alignment=parameters["av"],
            element_justification=parameters["ae"],
            font=parameters["f"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_canvas(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.Canvas(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        new_item.BackgroundColor = self.fsg.theme_background_color()

        return new_item, items_list

    def add_label(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.Text(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            font=parameters["f"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_progress_bar(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.ProgressBar(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_in_line(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.InputText(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            readonly=parameters["ro"],
            font=parameters["f"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_in_lines(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"],
                "truncate_width": parameters["tw"],
                "truncate_height": parameters["th"]
            }

        new_item = self.fsg.Multiline(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            font=parameters["f"],
            disabled=parameters["d"],
            no_scrollbar=parameters["ns"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_in_radio(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.Radio(
            parameters["v"],
            parameters["g"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"],
            group_id=parameters["g"]
        )

        return new_item, items_list

    def add_in_checkbox(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.Checkbox(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            disabled=parameters["d"],
            size=parameters["s"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"]
        )

        return new_item, items_list

    def add_in_combo(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.Combo(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            disabled=parameters["d"],
            size=parameters["s"],
            expand_x=parameters["xx"],
            expand_y=parameters["xy"],
            default_value=parameters["dv"]
        )

        return new_item, items_list

    def add_button(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.Button(
            parameters["v"],
            key=parameters["k"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"]
        )

        return new_item, items_list

    def add_button_file(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.FileBrowse(
            key=parameters["k"],
            target=parameters["tg"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"],
            button_text=parameters["v"],
        )

        return new_item, items_list

    def add_button_files(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.FilesBrowse(
            key=parameters["k"],
            target=parameters["tg"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"],
            button_text=parameters["v"],
        )

        return new_item, items_list

    def add_button_save(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.FileSaveAs(
            key=parameters["k"],
            target=parameters["tg"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"],
            button_text=parameters["v"],
        )

        return new_item, items_list

    def add_button_folder(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.FolderBrowse(
            key=parameters["k"],
            target=parameters["tg"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"],
            button_text=parameters["v"],
        )

        return new_item, items_list

    def add_button_calendar(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.CalendarButton(
            key=parameters["k"],
            target=parameters["tg"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"],
            button_text=parameters["v"],
        )

        return new_item, items_list

    def add_button_color(self, item, items_list):

        items_list = items_list
        parameters = self.create_parameters(item)

        if "t" in parameters:
            items_list[parameters["k"]] = {
                "type": parameters["t"]
            }

        new_item = self.fsg.ColorChooserButton(
            key=parameters["k"],
            target=parameters["tg"],
            pad=parameters["p"],
            size=parameters["s"],
            disabled=parameters["d"],
            font=parameters["f"],
            button_text=parameters["v"],
        )

        return new_item, items_list
