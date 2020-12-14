import sys
from Qt import QtWidgets, QtGui, QtCore

from widgets.progress import ProgressWidget
from generators.loot import Loot
from generators.combat import Combat

class CombatDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super(CombatDialog, self).__init__(parent)

        self.setWindowTitle("Ironsworn App | Combat")

        # layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        progress_track_widget = ProgressWidget()
        main_layout.addWidget(progress_track_widget)

        self.log_widget = QtWidgets.QTextEdit()
        self.log_widget.setReadOnly(True)
        main_layout.addWidget(self.log_widget)

        btn_layout = QtWidgets.QHBoxLayout()

        generators_group_box = QtWidgets.QGroupBox("Generators")
        generators_group_box.setLayout(btn_layout)

        combat_btn = QtWidgets.QPushButton("Combat Move")
        btn_layout.addWidget(combat_btn)
        combat_btn.clicked.connect(self.generate_combat)

        pay_the_price_btn = QtWidgets.QPushButton("Pay The Price")
        btn_layout.addWidget(pay_the_price_btn)
        pay_the_price_btn.clicked.connect(self.generate_pay_the_price)

        loot_btn = QtWidgets.QPushButton("Loot")
        btn_layout.addWidget(loot_btn)
        loot_btn.clicked.connect(self.generate_loot)

        main_layout.addWidget(generators_group_box)

    def generate_combat(self):
        combat_generator = Combat()
        output = combat_generator.generate_combat()
        self.log_widget.append(output)

    def generate_pay_the_price(self):
        combat_generator = Combat()
        output = combat_generator.generate_pay_the_price()
        self.log_widget.append(output)

    def generate_loot(self):
        loot_generator = Loot()
        output = loot_generator.generate_loot()
        self.log_widget.append(output)











