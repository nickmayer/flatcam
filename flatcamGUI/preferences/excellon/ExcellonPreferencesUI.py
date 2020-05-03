from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings

from flatcamGUI.preferences.excellon.ExcellonEditorPrefGroupUI import ExcellonEditorPrefGroupUI
from flatcamGUI.preferences.excellon.ExcellonExpPrefGroupUI import ExcellonExpPrefGroupUI
from flatcamGUI.preferences.excellon.ExcellonAdvOptPrefGroupUI import ExcellonAdvOptPrefGroupUI
from flatcamGUI.preferences.excellon.ExcellonOptPrefGroupUI import ExcellonOptPrefGroupUI
from flatcamGUI.preferences.excellon.ExcellonGenPrefGroupUI import ExcellonGenPrefGroupUI

import gettext
import FlatCAMTranslation as fcTranslate
import builtins

fcTranslate.apply_language('strings')
if '_' not in builtins.__dict__:
    _ = gettext.gettext

settings = QSettings("Open Source", "FlatCAM")
if settings.contains("machinist"):
    machinist_setting = settings.value('machinist', type=int)
else:
    machinist_setting = 0


class ExcellonPreferencesUI(QtWidgets.QWidget):

    def __init__(self, decimals, parent=None):
        QtWidgets.QWidget.__init__(self, parent=parent)
        self.layout = QtWidgets.QHBoxLayout()
        self.setLayout(self.layout)
        self.decimals = decimals

        self.excellon_gen_group = ExcellonGenPrefGroupUI(decimals=self.decimals)
        self.excellon_gen_group.setMinimumWidth(220)
        self.excellon_opt_group = ExcellonOptPrefGroupUI(decimals=self.decimals)
        self.excellon_opt_group.setMinimumWidth(290)
        self.excellon_exp_group = ExcellonExpPrefGroupUI(decimals=self.decimals)
        self.excellon_exp_group.setMinimumWidth(250)
        self.excellon_adv_opt_group = ExcellonAdvOptPrefGroupUI(decimals=self.decimals)
        self.excellon_adv_opt_group.setMinimumWidth(250)
        self.excellon_editor_group = ExcellonEditorPrefGroupUI(decimals=self.decimals)
        self.excellon_editor_group.setMinimumWidth(260)

        self.vlay = QtWidgets.QVBoxLayout()
        self.vlay.addWidget(self.excellon_opt_group)
        self.vlay.addWidget(self.excellon_exp_group)

        self.layout.addWidget(self.excellon_gen_group)
        self.layout.addLayout(self.vlay)
        self.layout.addWidget(self.excellon_adv_opt_group)
        self.layout.addWidget(self.excellon_editor_group)

        self.layout.addStretch()
