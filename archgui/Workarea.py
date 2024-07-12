class Workarea:

    def __init__(self, platform, fsg):

        self.platform = platform
        self.fsg = fsg

    # ---------------------------------------------------------------------
    # / Retourne la géométrie interne de la workarea
    # ---------------------------------------------------------------------

    def geometry(self):

        window = self.fsg.Window(
            '',
            [[]],
            alpha_channel=0,
            finalize=True,
            auto_close=True
        )

        window.TKroot.update_idletasks()
        window.set_size((100, 100))
        window.TKroot.update_idletasks()

        offset_y = int(window.TKroot.geometry().rsplit('+', 1)[-1])
        titlebar_height = window.TKroot.winfo_rooty() - offset_y

        workarea_geometry = {}

        # -----------------------------------------------------------------
        # Utilisation de screeninfo pour Linux
        # -----------------------------------------------------------------

        if self.platform == "linux" or self.platform == "linux2":

            from screeninfo import get_monitors

            primary_monitor = {}
            for monitor in get_monitors():
                if monitor.is_primary:
                    primary_monitor["x"] = int(monitor.x)
                    primary_monitor["y"] = int(monitor.y)
                    primary_monitor["width"] = int(monitor.width)
                    primary_monitor["height"] = int(monitor.height)

            x_min = primary_monitor["x"]
            x_max = x_min + primary_monitor["width"]
            y_min = primary_monitor["y"]
            y_max = y_min + primary_monitor["height"]

            calib_siz = {"width": 0, "height": 0}
            calib_pos = [
                ["tl", {"x": x_min, "y": y_min}],
                ["br", {"x": x_max - calib_siz["width"], "y": y_max - calib_siz["height"]}],
            ]

            calib_res = {}
            for pos in calib_pos:
                window = self.fsg.Window(
                    '',
                    [[]],
                    alpha_channel=1,
                    size=(calib_siz["width"], calib_siz["height"]),
                    location=(int(pos[1]["x"]), int(pos[1]["y"])),
                    finalize=True,
                    auto_close=True
                )

                calib_res[pos[0]] = {"x": window.TKroot.winfo_x(), "y": window.TKroot.winfo_y()}
                window.close()

            workarea_geometry = {
                "x_min": calib_res["tl"]["x"],
                "y_min": calib_res["tl"]["y"] - titlebar_height,
                "x_max": calib_res["br"]["x"] + calib_siz["width"] + 1,
                "y_max": calib_res["br"]["y"] + calib_siz["height"] + 1,
                "width": (calib_res["br"]["x"] + calib_siz["width"] + 1) - calib_res["tl"]["x"],
                "height": (calib_res["br"]["y"] + calib_siz["height"] + 1) - (calib_res["tl"]["y"] - titlebar_height),
                "titlebar_height": titlebar_height
            }

        # -----------------------------------------------------------------
        # Utilisation de win32api pour Windows
        # -----------------------------------------------------------------

        elif self.platform == "win32":

            from win32api import GetMonitorInfo, MonitorFromPoint

            monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
            work_area = monitor_info.get("Work")

            workarea_raw = {
                "x": int(work_area[0]),
                "y": int(work_area[1]),
                "width": int(work_area[2]),
                "height": int(work_area[3])
            }

            workarea_geometry = {
                "x_min": workarea_raw["x"],
                "y_min": workarea_raw["y"] + titlebar_height,
                "x_max": workarea_raw["width"],
                "y_max": workarea_raw["height"],
                "width": workarea_raw["width"],
                "height": workarea_raw["height"],
                "titlebar_height": titlebar_height
            }

        return workarea_geometry
