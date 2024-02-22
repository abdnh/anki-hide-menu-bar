from aqt import gui_hooks, mw
from aqt.qt import *


def hide_menubar() -> None:
    mw.form.menubar.setFixedHeight(0)


def show_menubar() -> None:
    mw.form.menubar.setMaximumSize(QWIDGETSIZE_MAX, QWIDGETSIZE_MAX)
    mw.form.menubar.setMinimumSize(0, 0)


def toggle_menubar() -> None:
    config = mw.addonManager.getConfig(__name__)
    is_hidden = not bool(mw.form.menubar.height())
    if is_hidden:
        show_menubar()
    else:
        hide_menubar()
    config["was_hidden"] = not is_hidden
    mw.addonManager.writeConfig(__name__, config)


config = mw.addonManager.getConfig(__name__)
shortcut = QShortcut(config["shortcut"], mw)
shortcut.activated.connect(toggle_menubar)


def on_main_window_did_init():
    if config["was_hidden"]:
        hide_menubar()
    else:
        show_menubar()


gui_hooks.main_window_did_init.append(on_main_window_did_init)
