import sys
from Qt import QtWidgets, QtGui, QtCore
from pyside_material import apply_stylesheet

from widgets.character import CharacterWidget
from widgets.progress import ProgressTrackWidget
from widgets.journey import JourneyDialog
from widgets.world_explorer import WorldExplorerWidget
from widgets.npc import NPCDialog
from widgets.combat import CombatDialog
from widgets.delves import DelvesDialog
from widgets.settlement import SettlementDialog
from generators.npc import NPC
from generators.settlement import Settlement


class IronSworn(QtWidgets.QWidget):

    def __init__(self):
        super(IronSworn, self).__init__()

        self.setWindowTitle("Ironsworn App")

        # layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        # widgets
        self.character_widget = CharacterWidget()
        main_layout.addWidget(self.character_widget)

        self.quest_progress_widget = ProgressTrackWidget()
        main_layout.addWidget(self.quest_progress_widget)

        self.world_explorer = WorldExplorerWidget()
        main_layout.addWidget(self.world_explorer)

        btn_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(btn_layout)

        journey_btn = QtWidgets.QPushButton("Undertake A Journey")
        btn_layout.addWidget(journey_btn)
        journey_btn.clicked.connect(self.add_journey_track)

        npc_btn = QtWidgets.QPushButton("NPC")
        btn_layout.addWidget(npc_btn)
        npc_btn.clicked.connect(self.generate_npc)

        settlement_btn = QtWidgets.QPushButton("Settlement")
        btn_layout.addWidget(settlement_btn)
        settlement_btn.clicked.connect(self.generate_settlement)

        combat_btn = QtWidgets.QPushButton("Combat")
        btn_layout.addWidget(combat_btn)
        combat_btn.clicked.connect(self.generate_combat)

        delves_btn = QtWidgets.QPushButton("Delves")
        btn_layout.addWidget(delves_btn)
        delves_btn.clicked.connect(self.generate_delves)

        oracle_btn = QtWidgets.QPushButton("Ask Oracle")
        btn_layout.addWidget(oracle_btn)
        oracle_btn.clicked.connect(self.ask_oracle)

        save_btn = QtWidgets.QPushButton("Save Session")
        btn_layout.addWidget(save_btn)
        save_btn.clicked.connect(self.save_session)

        self.oracle_status_ql = QtWidgets.QLineEdit("")
        self.oracle_status_ql.setReadOnly(True)
        main_layout.addWidget(self.oracle_status_ql)

    def save_session(self):

        self.character_widget.save_data()
        self.quest_progress_widget.save()

    def add_journey_track(self):

        d = JourneyDialog(parent=self)
        d.setModal(False)
        d.show()

    def generate_npc(self):
        npc_generator = NPC()

        d = NPCDialog(parent=self)
        d.init_ui(npc_generator)
        d.save(npc_generator)
        d.setModal(False)
        d.show()

        self.world_explorer._refresh_npc_list()

    def generate_settlement(self):
        settlement_generator = Settlement()
        npc_generator = NPC()

        d = SettlementDialog(parent=self)
        d.init_ui(settlement_generator, npc_generator)
        d.save(settlement_generator, npc_generator)
        d.setModal(False)
        d.show()

        d = NPCDialog(parent=self)
        d.init_ui(npc_generator)
        d.save(npc_generator)
        d.setModal(False)
        d.show()

        self.world_explorer._refresh_npc_list()
        self.world_explorer._refresh_settlement_list()

    def generate_combat(self):
        d = CombatDialog(parent=self)
        d.setModal(False)
        d.show()

    def generate_delves(self):
        d = DelvesDialog(parent=self)
        d.setModal(False)
        d.show()

    def ask_oracle(self):

        import random

        dice = random.randint(0, 100)

        almost_certain = "No"
        likely = "No"
        half = "No"
        unlikely = "No"
        small_chance = "No"

        if dice > 11:
            almost_certain = "Yes"
        if dice > 26:
            likely = "Yes"
        if dice > 51:
            half = "Yes"
        if dice > 76:
            unlikely = "Yes"
        if dice > 91:
            small_chance = "Yes"

        output = "Oracle say : Almost Certain : {}, Likely : {}, 50/50 : {}, Unlikely : {}, Small Chance : {}.".format(
            almost_certain, likely, half, unlikely, small_chance)

        self.oracle_status_ql.setText(output)


if __name__ == "__main__":
    # create the application and the main window
    app = QtWidgets.QApplication(sys.argv)
    window = IronSworn()

    # setup stylesheet
    apply_stylesheet(app, theme='dark_blue.xml')

    # run
    window.show()
    app.exec_()