import sys
from .Printer import Printer

printer = Printer()
windows = None


def init(config, specters, models_event):

    import matplotlib

    matplotlib.use('TkAgg')

    import matplotlib.pyplot as plt
    import FreeSimpleGUI as fsg

    from sys import platform

    from .Windows import Windows
    from .Model import Model
    from .Workarea import Workarea

    global windows

    workarea = Workarea(platform, fsg)
    windows = Windows(platform, plt, fsg, workarea)

    windows.load_config(config)

    models_window = {}

    for model in models_event:
        models_window[model] = Model(windows, model, specters[model])

    windows.load_models(models_window, models_event)


def define_modules(modules):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_DEFINE_MODULES", tb=False)
        sys.exit()
    else:
        if windows.define_modules(modules):
            return True
        else:
            printer.error("define_modules()", "INIT_DEFINE_MODULES_RETURN", tb=False)
            return False


def define_main(uniqid: str):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_DEFINE_MAIN", tb=False)
        sys.exit()
    else:
        if windows.define_main(uniqid=uniqid):
            return True
        else:
            printer.error("define_main()", "INIT_DEFINE_MAIN_RETURN", tb=False)
            return False


def open(model: str, wid: str, title=None, uniqid=None, location=None, size=None):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_OPEN", tb=False)
        sys.exit()
    else:
        uniqid = windows.open(
            model=model,
            wid=wid,
            title=title,
            uniqid=uniqid,
            location=location,
            size=size)

        if uniqid:
            return uniqid
        else:
            printer.error("open()", "INIT_OPEN_RETURN", tb=False)
            return False


def update(uniqid: str, items: list):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_UPDATE", tb=False)
        sys.exit()
    else:
        if windows.update(
                uniqid=uniqid,
                items=items):
            return True
        else:
            printer.error("update()", "INIT_UPDATE_RETURN", tb=False)
            return False


def close(uniqid: str):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_CLOSE", tb=False)
        sys.exit()
    else:
        if windows.close(uniqid=uniqid):
            return True
        else:
            printer.error("close()", "INIT_CLOSE_RETURN", tb=False)
            return False


def create_graph(uniqid: str, container=None, gid=None, matrix=None):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_CREATE_GRAPH", tb=False)
        sys.exit()
    else:
        uniqid = windows.create_graph(
            uniqid=uniqid,
            container=container,
            gid=gid,
            matrix=matrix)

        if uniqid:
            return uniqid
        else:
            printer.error("create_graph()", "INIT_CREATE_GRAPH_RETURN", tb=False)
            return False


def update_graph(uniqid: str, gid: str, matrix=None):

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_UPDATE_GRAPH", tb=False)
        sys.exit()
    else:
        if windows.update_graph(
                uniqid=uniqid,
                gid=gid,
                matrix=matrix):
            return True
        else:
            printer.error("update_graph()", "INIT_UPDATE_GRAPH_RETURN", tb=False)
            return False


def run():

    global printer
    global windows

    if windows is None:
        printer.error("__init__", "INIT_RUN", tb=False)
        sys.exit()
    else:
        windows.events_run()
