from aqt import mw
from aqt.qt import *


def toggle_menubar() -> None:
    config = mw.addonManager.getConfig(__name__)
    mw.form.menubar.setVisible(not mw.form.menubar.isVisible())
    config["was_hidden"] = not mw.form.menubar.isVisible()
    mw.addonManager.writeConfig(__name__, config)


config = mw.addonManager.getConfig(__name__)
shortcut = QShortcut(config["shortcut"], mw)
shortcut.activated.connect(toggle_menubar)
mw.form.menubar.setVisible(not config["was_hidden"])
