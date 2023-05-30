from aqt import mw
from aqt.qt import *


def toggle_menubar() -> None:
    if mw.form.menubar.isVisible():
        mw.form.menubar.hide()
    else:
        mw.form.menubar.show()


config = mw.addonManager.getConfig(__name__)
shortcut = QShortcut(config["shortcut"], mw)
shortcut.activated.connect(toggle_menubar)
