import time
from archgui.Model import Model
from archgui.Printer import Printer

# - LOADING EVENTS ZONE START
from archgui.events.sys.loader import Events as sys_loader_events
from archgui.events.usr.demo_c import Events as usr_demo_c_events
from archgui.events.usr.demo_e_2 import Events as usr_demo_e_2_events
from archgui.events.usr.demo_e_6 import Events as usr_demo_e_6_events
from archgui.events.usr.demo_e_3 import Events as usr_demo_e_3_events
from archgui.events.usr.demo_e_7 import Events as usr_demo_e_7_events
from archgui.events.usr.demo_b import Events as usr_demo_b_events
from archgui.events.usr.demo_e_1 import Events as usr_demo_e_1_events
from archgui.events.usr.demo_e_5 import Events as usr_demo_e_5_events
from archgui.events.usr.demo_d import Events as usr_demo_d_events
from archgui.events.usr.demo_e_8 import Events as usr_demo_e_8_events
from archgui.events.usr.demo_e import Events as usr_demo_e_events
from archgui.events.usr.demo_a import Events as usr_demo_a_events
from archgui.events.usr.demo_e_4 import Events as usr_demo_e_4_events
# - LOADING EVENTS ZONE END

# - LOADING WINDOWS ZONE START
specters = {
    "sys": {
        "loader": {'parameters': {'location_x': '50%', 'location_y': '50%', 'width': 500, 'height': 250}, 'items': [[[{'t': 'column', 'k': 'col'}, [[[{'t': 'frame', 'k': 'frm', 'v': ' Frame 1 '}, [[[{'t': 'in_lines', 'k': 'logs', 's': [80, 10]}]]]]]]]]]},
    },
    "usr": {
        "demo_c": {'parameters': {'location_x': '50%', 'location_y': '50%', 'width': 574, 'height': 100}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Frame 1 ', 'xx': True, 'xy': True}, [[[{'t': 'progress_bar', 'k': 'progress_bar_1', 'p': [[15, 15], [10, 15]], 's': [50, 20]}]]]]]]]]]},
        "demo_e_2": {'parameters': {'location_x_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'location_y': 0, 'width_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'height_until': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 2 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_e_6": {'parameters': {'location_x': 0, 'location_y_relative': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'width_until': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'height': 0}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 6 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_e_3": {'parameters': {'location_x_relative': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'location_y': 0, 'width': 0, 'height_until': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 3 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_e_7": {'parameters': {'location_x_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'location_y_relative': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'width_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'height': 0}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 7 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_b": {'parameters': {'location_x': '50%', 'location_y': '50%', 'width': 854, 'height': 260}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Frame 1 ', 'xx': True, 'xy': True}, [[[{'t': 'canvas', 'k': 'canvas_1', 'p': [[5, 5], [0, 5]], 's': [800, 200], 'xx': True, 'xy': True}]]]]]]]]]},
        "demo_e_1": {'parameters': {'location_x': 0, 'location_y': 0, 'width_until': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'height_until': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 1 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_e_5": {'parameters': {'location_x_relative': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'location_y_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'width': 0, 'height_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 5 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_d": {'parameters': {'location_x': '50%', 'location_y': '50%', 'width': 528, 'height': 136}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'tab_group', 'k': 'tab_group_1', 'xx': True, 'xy': True}, [[[{'t': 'tab', 'k': 'tab_1', 'v': ' Tab 1 '}, [[[{'t': 'column', 'k': 'column_11', 'p': [[10, 10], [10, 10]]}, [[[{'t': 'label', 'k': 'label_1', 'v': 'label_1', 's': [8, 1]}], [{'t': 'in_line', 'k': 'in_line_1', 'v': ''}], [{'t': 'button', 'k': 'button_1', 'v': 'button_1'}]]]]]]], [{'t': 'tab', 'k': 'tab_2', 'v': ' Tab 2 '}, [[[{'t': 'column', 'k': 'column_12', 'p': [[10, 10], [10, 10]]}, [[[{'t': 'label', 'k': 'label_2', 'v': 'label_2', 's': [8, 1]}], [{'t': 'in_line', 'k': 'in_line_2', 'v': ''}], [{'t': 'button', 'k': 'button_2', 'v': 'button_2'}]]]]]]], [{'t': 'tab', 'k': 'tab_3', 'v': ' Tab 3 '}, [[[{'t': 'column', 'k': 'column_13', 'p': [[10, 10], [10, 10]]}, [[[{'t': 'label', 'k': 'label_3', 'v': 'label_3', 's': [8, 1]}], [{'t': 'in_line', 'k': 'in_line_3', 'v': ''}], [{'t': 'button', 'k': 'button_3', 'v': 'button_3'}]]]]]]]]]]]]]]]},
        "demo_e_8": {'parameters': {'location_x_relative': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'location_y_relative': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'width': 0, 'height': 0}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 8 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
        "demo_e": {'parameters': {'location_x': '50%', 'location_y': '50%', 'width': 390, 'height': 348}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'button', 'k': 'button_1', 'v': 'button_1', 's': [12, 6], 'p': [[5, 5], [15, 5]]}], [{'t': 'button', 'k': 'button_2', 'v': 'button_2', 's': [12, 6], 'p': [[5, 5], [15, 5]]}], [{'t': 'button', 'k': 'button_3', 'v': 'button_3', 's': [12, 6], 'p': [[5, 5], [15, 5]]}]], [[{'t': 'button', 'k': 'button_4', 'v': 'button_4', 's': [12, 6], 'p': [[5, 124], [5, 5]]}], [{'t': 'button', 'k': 'button_5', 'v': 'button_5', 's': [12, 6]}]], [[{'t': 'button', 'k': 'button_6', 'v': 'button_6', 's': [12, 6]}], [{'t': 'button', 'k': 'button_7', 'v': 'button_7', 's': [12, 6]}], [{'t': 'button', 'k': 'button_8', 'v': 'button_8', 's': [12, 6]}]]]]]]},
        "demo_a": {'parameters': {'location_x': '50%', 'location_y': '50%', 'width': 516, 'height': 133}, 'items': [[[{'t': 'column', 'k': 'column_1', 'p': [[0, 0], [0, 5]], 'sc': False, 'scvo': False}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Frame 1 '}, [[[{'t': 'column', 'k': 'column_11', 'p': [[5, 5], [0, 10]]}, [[[{'t': 'label', 'k': 'label_1', 'v': 'label_1', 's': [14, 1]}], [{'t': 'in_line', 'k': 'in_line_1', 'v': 'in_line_1', 's': [20, 1]}], [{'t': 'button', 'k': 'button_1', 'v': 'button_1', 's': [16, 1]}]], [[{'t': 'in_line', 'k': 'in_line_2', 'v': 'in_line_2', 's': [50, 1]}]]]]]]]]]]]]},
        "demo_e_4": {'parameters': {'location_x': 0, 'location_y_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'width_until': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}, 'height_equal': {'lvl': 'usr', 'model': 'demo_e', 'wid': '0'}}, 'items': [[[{'t': 'column', 'k': 'column_1', 'xx': True, 'xy': True}, [[[{'t': 'frame', 'k': 'frame_1', 'v': ' Demo E : Fenêtre 4 ', 'ae': 'left'}, [[[{'t': 'label', 'k': 'label_1', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_2', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_3', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_4', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_5', 'v': '', 's': [0, 1], 'p': [[20, 5], [10, 0]]}]], [[{'t': 'label', 'k': 'label_6', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_7', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]], [[{'t': 'label', 'k': 'label_8', 'v': '', 's': [0, 1], 'p': [[40, 5], [0, 0]]}]]]]]]]]]},
    },
}
# - LOADING WINDOWS ZONE END

# - LOADING CONFIG ZONE START
config = {'general': {'theme': 'DarkBlue14', 'font': ['Courier', 12]}, 'column': {'k': None, 'p': [[5, 5], [0, 10]], 's': [None, None], 'av': 'top', 'ae': 'center', 'sc': False, 'scvo': False, 'xx': None, 'xy': None}, 'tab_group': {'k': None, 'p': [[5, 5], [15, 10]], 's': [None, None], 'f': ['Courier', 12], 'tl': 'topleft', 'xx': None, 'xy': None}, 'tab': {'v': None, 'k': None, 'p': [[5, 5], [10, 10]], 'd': False, 'ae': 'center', 'xx': None, 'xy': None}, 'frame': {'v': None, 'k': None, 'p': [[5, 5], [5, 5]], 's': [None, None], 'f': ['Courier', 12], 'av': 'top', 'ae': 'center', 'xx': True, 'xy': True}, 'canvas': {'v': None, 'k': None, 'p': [[5, 5], [5, 5]], 's': [None, None], 'xx': True, 'xy': True}, 'label': {'v': None, 'k': None, 'p': [[5, 0], [5, 5]], 's': [6, 1], 'd': False, 'f': ['Courier', 12], 'xx': None, 'xy': None}, 'in_line': {'v': None, 'k': None, 'p': [[5, 0], [5, 5]], 's': [20, 1], 'd': False, 'f': ['Courier', 13], 'ro': False, 'xx': None, 'xy': None}, 'in_lines': {'v': '', 'k': None, 'p': [[10, 10], [10, 10]], 's': [None, None], 'f': ['Courier', 10], 'd': True, 'ns': True, 'xx': None, 'xy': None, 'tw': True, 'th': True}, 'in_radio': {'k': None, 'g': None, 'd': False, 'p': [[5, 0], [5, 5]], 's': [30, 3], 'f': ['Courier', 10], 'df': False, 'xx': None, 'xy': None}, 'in_checkbox': {'k': None, 'd': False, 'p': [[5, 0], [5, 5]], 's': [30, 3], 'f': ['Courier', 10], 'df': False, 'xx': None, 'xy': None}, 'in_combo': {'k': None, 'v': None, 'd': False, 'p': [[5, 0], [5, 5]], 's': [30, 3], 'dv': None, 'xx': None, 'xy': None}, 'button': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9]}, 'button_file': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_files': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_save': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_folder': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_calendar': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_color': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'progress_bar': {'k': None, 'v': 100, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'xx': None, 'xy': None}, 'parameters': {'t': 'type', 'v': None, 'k': 'key', 'p': 'pad', 's': 'size', 'd': 'disabled', 'o': 'orientation', 'f': 'font', 'g': 'group', 'df': 'default', 'dv': 'default_value', 'tl': 'tab_location', 'ro': 'readonly', 'av': 'vertical_alignment', 'ae': 'element_justification', 'tg': 'target', 'sc': 'scrollable', 'scvo': 'vertical_scroll_only', 'ns': 'no_scrollbar', 'xx': 'expand_x', 'xy': 'expand_y', 'tw': 'truncate_height', 'th': 'truncate_width'}}
config_user = {'general': {'theme': 'DarkBlue14', 'font': ['Courier', 12]}, 'column': {'k': None, 'p': [[5, 5], [0, 10]], 's': [None, None], 'av': 'top', 'ae': 'center', 'sc': False, 'scvo': False, 'xx': None, 'xy': None}, 'tab_group': {'k': None, 'p': [[5, 5], [15, 10]], 's': [None, None], 'f': ['Courier', 12], 'tl': 'topleft', 'xx': None, 'xy': None}, 'tab': {'v': None, 'k': None, 'p': [[5, 5], [10, 10]], 'd': False, 'ae': 'center', 'xx': None, 'xy': None}, 'frame': {'v': None, 'k': None, 'p': [[5, 5], [5, 5]], 's': [None, None], 'f': ['Courier', 12], 'av': 'top', 'ae': 'center', 'xx': True, 'xy': True}, 'canvas': {'v': None, 'k': None, 'p': [[5, 5], [5, 5]], 's': [None, None], 'xx': True, 'xy': True}, 'label': {'v': None, 'k': None, 'p': [[5, 0], [5, 5]], 's': [6, 1], 'd': False, 'f': ['Courier', 12], 'xx': None, 'xy': None}, 'in_line': {'v': None, 'k': None, 'p': [[5, 0], [5, 5]], 's': [20, 1], 'd': False, 'f': ['Courier', 13], 'ro': False, 'xx': None, 'xy': None}, 'in_lines': {'v': '', 'k': None, 'p': [[10, 10], [10, 10]], 's': [None, None], 'f': ['Courier', 10], 'd': True, 'ns': True, 'xx': None, 'xy': None, 'tw': True, 'th': True}, 'in_radio': {'k': None, 'g': None, 'd': False, 'p': [[5, 0], [5, 5]], 's': [30, 3], 'f': ['Courier', 10], 'df': False, 'xx': None, 'xy': None}, 'in_checkbox': {'k': None, 'd': False, 'p': [[5, 0], [5, 5]], 's': [30, 3], 'f': ['Courier', 10], 'df': False, 'xx': None, 'xy': None}, 'in_combo': {'k': None, 'v': None, 'd': False, 'p': [[5, 0], [5, 5]], 's': [30, 3], 'dv': None, 'xx': None, 'xy': None}, 'button': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9]}, 'button_file': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_files': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_save': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_folder': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_calendar': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'button_color': {'k': None, 'v': None, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'tg': None}, 'progress_bar': {'k': None, 'v': 100, 'd': False, 'p': [[5, 5], [5, 5]], 's': [10, 1], 'f': ['Courier', 9], 'xx': None, 'xy': None}}
# - LOADING CONFIG ZONE END


class Loader:

    def __init__(self, windows):

        self.windows = windows
        self.fsg = windows.fsg

        # -----------------------------------------------------------------

        self.config = config

        for parameter in config:
            if parameter in list(config_user):
                for sub_parameter in config[parameter]:
                    if sub_parameter in list(config_user[parameter]):
                        if self.config[parameter][sub_parameter] != config_user[parameter][sub_parameter]:
                            self.config[parameter][sub_parameter] = config_user[parameter][sub_parameter]

        # -----------------------------------------------------------------

        self.printer = Printer()

        # - LOADING MODELS LIST ZONE START
        self.models_list = {
            "sys": [
                "loader",
            ],
            "usr": [
                "demo_c",
                "demo_e_2",
                "demo_e_6",
                "demo_e_3",
                "demo_e_7",
                "demo_b",
                "demo_e_1",
                "demo_e_5",
                "demo_d",
                "demo_e_8",
                "demo_e",
                "demo_a",
                "demo_e_4",
            ]
        }
        # - LOADING MODELS LIST ZONE END

        self.models_window = {
            "sys": {},
            "usr": {}
        }
        self.models_event = {
            "sys": {},
            "usr": {}
        }

        self.wds_archgui = {}
        self.wds_simplegui = {}

    def run(self):

        try:
            self.windows.load_config(self.config)

            self.models_window["sys"]["loader"] = Model(self.windows, "sys", "loader", specters["sys"]["loader"])
            self.models_event["sys"]["loader"] = eval("sys_loader_events")()
            self.windows.load_models(self.models_window, self.models_event)

            loader_id = self.windows.open(lvl="sys", model="loader", wid="0", title="Loader")
            time.sleep(0.1)

            for lvl in self.models_list:
                for model in self.models_list[lvl]:
                    if lvl != "sys" and model != "loader":

                        self.models_window[lvl][model] = Model(self.windows, lvl, model, specters[lvl][model])
                        self.models_event[lvl][model] = eval(lvl + "_" + model.replace("/", "_") + "_events")()

                        self.windows.update(uniqid=loader_id, items=[
                            {"key": "logs", "mode": "add", "value": "window loaded: '" + lvl + "/" + model + "'"}
                        ])

                        time.sleep(0.01)

            self.windows.load_models(self.models_window, self.models_event)
            time.sleep(0.1)
            self.windows.close(uniqid=loader_id)
        except:
            self.printer.error("__main__", "LOADER_RUN")
