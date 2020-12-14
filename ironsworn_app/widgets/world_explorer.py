import sys
import json
import os

from Qt import QtWidgets, QtGui, QtCore

from widgets.npc import NPCDialog
from widgets.settlement import SettlementDialog

class WorldExplorerWidget(QtWidgets.QWidget):

    def __init__(self):
        super(WorldExplorerWidget, self).__init__()

        # layout

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        self.explorer_tab_widget = QtWidgets.QTabWidget()

        self.npc_tab = QtWidgets.QListWidget()
        self.explorer_tab_widget.addTab(self.npc_tab, "NPC")

        self.settlement_tab = QtWidgets.QListWidget()
        self.explorer_tab_widget.addTab(self.settlement_tab, "Settlement")

        main_layout.addWidget(self.explorer_tab_widget)

        self.npc_tab.itemClicked.connect(self._display_npc)
        self.settlement_tab.itemClicked.connect(self._display_settlement)

        self._refresh_npc_list()
        self._refresh_settlement_list()

    def _refresh_npc_list(self):

        self.npc_tab.clear()

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/npc.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        for npc in data["npc"]:
            self.npc_tab.addItem("{}| {} - {}".format(npc["name"], npc["stance"], npc["role"]))

    def _refresh_settlement_list(self):

        self.settlement_tab.clear()

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/settlement.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        for settlement in data["settlement"]:
            self.settlement_tab.addItem("{}| {} - {}".format(settlement["name"],
                                                             settlement["leader_name"],
                                                             settlement["governement_type"]))

    def _display_npc(self, item):

        npc_name = item.text().split("|")[0]

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/npc.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        for npc in data["npc"]:
            if npc["name"] == npc_name:
                d = NPCDialog(parent=self)
                d.init_ui_from_json(npc)
                d.setModal(False)
                d.show()

    def _display_settlement(self, item):

        settlement_name = item.text().split("|")[0]

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/settlement.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        for settlement in data["settlement"]:
            if settlement["name"] == settlement_name:
                d = SettlementDialog(parent=self)
                d.init_ui_from_json(settlement)
                d.setModal(False)
                d.show()






