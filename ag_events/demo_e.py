class Events:

    def __init__(self):

        self.windows = None
        self.window = None

        # ---------------------------------------------------------------------
        # / Ajout de l'utilisateur
        # / La 'self.uniqids = {}' n'est pas généré automatique lors
        # / de la création des fichiers 'event.py'
        # ---------------------------------------------------------------------

        self.uniqids = {}

    def events(self, event, modules):

        if self.windows.uniqid is None:
            self.windows.uniqid = None

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_1'
        # / Ouverture de la fenêtre sur le model 'demo_e_1'
        # / Update des labels de la fenêtre précédemment ouverte
        # ---------------------------------------------------------------------

        if event == "button_1":

            # -----------------------------------------------------------------
            # Ouverture via 'self.windows'
            # -----------------------------------------------------------------

            demo_e_1 = self.windows.open(
                model="demo_e_1",
                wid="0",
                title="Archgui - Demo E 1")

            # -----------------------------------------------------------------
            # On vérifie que l'on n’a pas déjà ouvert la fenêtre
            # Si la fenêtre est déjà ouverte, la fonction self.windows.open
            # retournera False ce qui provoquera une erreur pour la suite
            # -----------------------------------------------------------------

            if demo_e_1:
                self.uniqids["demo_e_1"] = demo_e_1

            # -----------------------------------------------------------------
            # Mise à jour des valeurs des labels
            # - Contrôle de la présence de l'item 'demo_e_1' dans 'self.uniqids'
            # - Contrôle de l'existence de la fenêtre
            # -----------------------------------------------------------------

            if "demo_e_1" in self.uniqids:
                if self.windows.exist(self.uniqids["demo_e_1"]):

                    lvl = self.windows.window(self.uniqids["demo_e_1"]).lvl
                    model = self.windows.window(self.uniqids["demo_e_1"]).model
                    wid = self.windows.window(self.uniqids["demo_e_1"]).wid

                    label_1 = "Fenêtre actuelle:"
                    label_2 = "- Lvl: " + lvl
                    label_3 = "- Model: " + model
                    label_4 = "- Wid: " + wid

                    lvl = self.window.lvl
                    model = self.window.model
                    wid = self.window.wid

                    label_5 = "Fenêtre mère:"
                    label_6 = "- Lvl: " + lvl
                    label_7 = "- Model: " + model
                    label_8 = "- Wid: " + wid

                    self.windows.update(
                        uniqid=self.uniqids["demo_e_1"],
                        items=[
                            {"key": "label_1", "mode": "replace", "value": label_1},
                            {"key": "label_2", "mode": "replace", "value": label_2},
                            {"key": "label_3", "mode": "replace", "value": label_3},
                            {"key": "label_4", "mode": "replace", "value": label_4},
                            {"key": "label_5", "mode": "replace", "value": label_5},
                            {"key": "label_6", "mode": "replace", "value": label_6},
                            {"key": "label_7", "mode": "replace", "value": label_7},
                            {"key": "label_8", "mode": "replace", "value": label_8}
                        ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_2'
        # / Ouverture de la fenêtre sur le model 'demo_e_2'
        # / Utilisation de la variation 'modules' et non 'self.windows'
        # / Reste du script identique que pour le 'button_1'
        # ---------------------------------------------------------------------

        if event == "button_2":

            demo_e_2 = modules["archgui"].open(
                model="demo_e_2",
                wid="0",
                title="Archgui - Demo E 2")

            if demo_e_2:
                self.uniqids["demo_e_2"] = demo_e_2

            if "demo_e_2" in self.uniqids:
                if self.windows.exist(self.uniqids["demo_e_2"]):

                    lvl = self.windows.window(self.uniqids["demo_e_2"]).lvl
                    model = self.windows.window(self.uniqids["demo_e_2"]).model
                    wid = self.windows.window(self.uniqids["demo_e_2"]).wid

                    label_1 = "Fenêtre actuelle:"
                    label_2 = "- Lvl: " + lvl
                    label_3 = "- Model: " + model
                    label_4 = "- Wid: " + wid

                    lvl = self.window.lvl
                    model = self.window.model
                    wid = self.window.wid

                    label_5 = "Fenêtre mère:"
                    label_6 = "- Lvl: " + lvl
                    label_7 = "- Model: " + model
                    label_8 = "- Wid: " + wid

                    self.windows.update(
                        uniqid=self.uniqids["demo_e_2"],
                        items=[
                            {"key": "label_1", "mode": "replace", "value": label_1},
                            {"key": "label_2", "mode": "replace", "value": label_2},
                            {"key": "label_3", "mode": "replace", "value": label_3},
                            {"key": "label_4", "mode": "replace", "value": label_4},
                            {"key": "label_5", "mode": "replace", "value": label_5},
                            {"key": "label_6", "mode": "replace", "value": label_6},
                            {"key": "label_7", "mode": "replace", "value": label_7},
                            {"key": "label_8", "mode": "replace", "value": label_8}
                        ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_3'
        # / Ouverture de la fenêtre sur le model 'demo_e_3'
        # / Masquage de la fenêtre précédemment ouverte si l'on re-clique
        # / sur le 'button_3' et inversement
        # / Reste du script identique que pour le 'button_1'
        # / Suppression des contrôles inutiles et du stockage de l'uniqid
        # / dans le self.
        # ---------------------------------------------------------------------

        if event == "button_3":

            demo_e_3_id = self.windows.uniqid(model="demo_e_3", wid="0")

            if demo_e_3_id:
                if not self.windows.hide(demo_e_3_id):
                    self.windows.show(demo_e_3_id)
            else:

                demo_e_3_id = self.windows.open(
                    model="demo_e_3",
                    wid="0",
                    title="Archgui - Demo E 3")

                lvl = self.windows.window(demo_e_3_id).lvl
                model = self.windows.window(demo_e_3_id).model
                wid = self.windows.window(demo_e_3_id).wid

                label_1 = "Fenêtre actuelle:"
                label_2 = "- Lvl: " + lvl
                label_3 = "- Model: " + model
                label_4 = "- Wid: " + wid

                lvl = self.window.lvl
                model = self.window.model
                wid = self.window.wid

                label_5 = "Fenêtre mère:"
                label_6 = "- Lvl: " + lvl
                label_7 = "- Model: " + model
                label_8 = "- Wid: " + wid

                self.windows.update(
                    uniqid=demo_e_3_id,
                    items=[
                        {"key": "label_1", "mode": "replace", "value": label_1},
                        {"key": "label_2", "mode": "replace", "value": label_2},
                        {"key": "label_3", "mode": "replace", "value": label_3},
                        {"key": "label_4", "mode": "replace", "value": label_4},
                        {"key": "label_5", "mode": "replace", "value": label_5},
                        {"key": "label_6", "mode": "replace", "value": label_6},
                        {"key": "label_7", "mode": "replace", "value": label_7},
                        {"key": "label_8", "mode": "replace", "value": label_8}
                    ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_4'
        # / Ouverture de la fenêtre sur le model 'demo_e_4'
        # / Fermeture de la fenêtre précédemment ouverte si l'on re-clique
        # / sur le 'button_4' et inversement
        # / Reste du script identique que pour le 'button_1'
        # / Suppression des contrôles inutiles
        # ---------------------------------------------------------------------

        if event == "button_4":

            demo_e_4_id = self.windows.uniqid(model="demo_e_4", wid="0")

            if demo_e_4_id:
                self.windows.close(demo_e_4_id)
            else:
                demo_e_4_id = self.windows.open(
                    model="demo_e_4",
                    wid="0",
                    title="Archgui - Demo E 4")

                lvl = self.windows.window(demo_e_4_id).lvl
                model = self.windows.window(demo_e_4_id).model
                wid = self.windows.window(demo_e_4_id).wid

                label_1 = "Fenêtre actuelle:"
                label_2 = "- Lvl: " + lvl
                label_3 = "- Model: " + model
                label_4 = "- Wid: " + wid

                lvl = self.window.lvl
                model = self.window.model
                wid = self.window.wid

                label_5 = "Fenêtre mère:"
                label_6 = "- Lvl: " + lvl
                label_7 = "- Model: " + model
                label_8 = "- Wid: " + wid

                self.windows.update(
                    uniqid=demo_e_4_id,
                    items=[
                        {"key": "label_1", "mode": "replace", "value": label_1},
                        {"key": "label_2", "mode": "replace", "value": label_2},
                        {"key": "label_3", "mode": "replace", "value": label_3},
                        {"key": "label_4", "mode": "replace", "value": label_4},
                        {"key": "label_5", "mode": "replace", "value": label_5},
                        {"key": "label_6", "mode": "replace", "value": label_6},
                        {"key": "label_7", "mode": "replace", "value": label_7},
                        {"key": "label_8", "mode": "replace", "value": label_8}
                    ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_5'
        # / Ouverture de la fenêtre sur le model 'demo_e_5'
        # / Script identique au 'button_1'
        # ---------------------------------------------------------------------

        if event == "button_5":

            demo_e_5 = self.windows.open(
                model="demo_e_5",
                wid="0",
                title="Archgui - Demo E 5")

            if demo_e_5:
                self.uniqids["demo_e_5"] = demo_e_5

            if "demo_e_5" in self.uniqids:
                if self.windows.exist(self.uniqids["demo_e_5"]):

                    lvl = self.windows.window(self.uniqids["demo_e_5"]).lvl
                    model = self.windows.window(self.uniqids["demo_e_5"]).model
                    wid = self.windows.window(self.uniqids["demo_e_5"]).wid

                    label_1 = "Fenêtre actuelle:"
                    label_2 = "- Lvl: " + lvl
                    label_3 = "- Model: " + model
                    label_4 = "- Wid: " + wid

                    lvl = self.window.lvl
                    model = self.window.model
                    wid = self.window.wid

                    label_5 = "Fenêtre mère:"
                    label_6 = "- Lvl: " + lvl
                    label_7 = "- Model: " + model
                    label_8 = "- Wid: " + wid

                    self.windows.update(
                        uniqid=self.uniqids["demo_e_5"],
                        items=[
                            {"key": "label_1", "mode": "replace", "value": label_1},
                            {"key": "label_2", "mode": "replace", "value": label_2},
                            {"key": "label_3", "mode": "replace", "value": label_3},
                            {"key": "label_4", "mode": "replace", "value": label_4},
                            {"key": "label_5", "mode": "replace", "value": label_5},
                            {"key": "label_6", "mode": "replace", "value": label_6},
                            {"key": "label_7", "mode": "replace", "value": label_7},
                            {"key": "label_8", "mode": "replace", "value": label_8}
                        ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_6'
        # / Ouverture de la fenêtre sur le model 'demo_e_6'
        # / Script identique au 'button_1'
        # ---------------------------------------------------------------------

        if event == "button_6":

            demo_e_6 = self.windows.open(
                model="demo_e_6",
                wid="0",
                title="Archgui - Demo E 6")

            if demo_e_6:
                self.uniqids["demo_e_6"] = demo_e_6

            if "demo_e_6" in self.uniqids:
                if self.windows.exist(self.uniqids["demo_e_6"]):

                    lvl = self.windows.window(self.uniqids["demo_e_6"]).lvl
                    model = self.windows.window(self.uniqids["demo_e_6"]).model
                    wid = self.windows.window(self.uniqids["demo_e_6"]).wid

                    label_1 = "Fenêtre actuelle:"
                    label_2 = "- Lvl: " + lvl
                    label_3 = "- Model: " + model
                    label_4 = "- Wid: " + wid

                    self.windows.update(
                        uniqid=self.uniqids["demo_e_6"],
                        items=[
                            {"key": "label_1", "mode": "replace", "value": label_1},
                            {"key": "label_2", "mode": "replace", "value": label_2},
                            {"key": "label_3", "mode": "replace", "value": label_3},
                            {"key": "label_4", "mode": "replace", "value": label_4},
                        ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_7'
        # / Ouverture de la fenêtre sur le model 'demo_e_7'
        # / Script identique au 'button_1'
        # ---------------------------------------------------------------------

        if event == "button_7":

            demo_e_7 = self.windows.open(
                model="demo_e_7",
                wid="0",
                title="Archgui - Demo E 6")

            if demo_e_7:
                self.uniqids["demo_e_7"] = demo_e_7

            if "demo_e_7" in self.uniqids:
                if self.windows.exist(self.uniqids["demo_e_7"]):

                    lvl = self.windows.window(self.uniqids["demo_e_7"]).lvl
                    model = self.windows.window(self.uniqids["demo_e_7"]).model
                    wid = self.windows.window(self.uniqids["demo_e_7"]).wid

                    label_1 = "Fenêtre actuelle:"
                    label_2 = "- Lvl: " + lvl
                    label_3 = "- Model: " + model
                    label_4 = "- Wid: " + wid

                    self.windows.update(
                        uniqid=self.uniqids["demo_e_7"],
                        items=[
                            {"key": "label_1", "mode": "replace", "value": label_1},
                            {"key": "label_2", "mode": "replace", "value": label_2},
                            {"key": "label_3", "mode": "replace", "value": label_3},
                            {"key": "label_4", "mode": "replace", "value": label_4},
                        ])

        # ---------------------------------------------------------------------
        # / Event lors du clique sur l'item 'button_8'
        # / Ouverture de la fenêtre sur le model 'demo_e_8'
        # / Script identique au 'button_1'
        # ---------------------------------------------------------------------

        if event == "button_8":

            demo_e_8 = self.windows.open(
                model="demo_e_8",
                wid="0",
                title="Archgui - Demo E 6")

            if demo_e_8:
                self.uniqids["demo_e_8"] = demo_e_8

            if "demo_e_8" in self.uniqids:
                if self.windows.exist(self.uniqids["demo_e_8"]):

                    lvl = self.windows.window(self.uniqids["demo_e_8"]).lvl
                    model = self.windows.window(self.uniqids["demo_e_8"]).model
                    wid = self.windows.window(self.uniqids["demo_e_8"]).wid

                    label_1 = "Fenêtre actuelle:"
                    label_2 = "- Lvl: " + lvl
                    label_3 = "- Model: " + model
                    label_4 = "- Wid: " + wid

                    self.windows.update(
                        uniqid=self.uniqids["demo_e_8"],
                        items=[
                            {"key": "label_1", "mode": "replace", "value": label_1},
                            {"key": "label_2", "mode": "replace", "value": label_2},
                            {"key": "label_3", "mode": "replace", "value": label_3},
                            {"key": "label_4", "mode": "replace", "value": label_4},
                        ])

