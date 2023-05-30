from aqt import mw
from aqt.qt import *


def toggle_menubar() -> None:
    config = mw.addonManager.getConfig(__name__)
    if mw.form.menubar.isVisible():
        mw.form.menubar.hide()
    else:
        mw.form.menubar.show()
    config["was_hidden"] = mw.form.menubar.isHidden()
    mw.addonManager.writeConfig(__name__, config)


config = mw.addonManager.getConfig(__name__)
shortcut = QShortcut(config["shortcut"], mw)
shortcut.activated.connect(toggle_menubar)
mw.form.menubar.setVisible(not config["was_hidden"])
