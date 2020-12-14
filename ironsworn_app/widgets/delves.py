import sys
from Qt import QtWidgets, QtGui, QtCore

from widgets.progress import ProgressWidget
from generators.loot import Loot
from generators.delves import Delves

class DelvesDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super(DelvesDialog, self).__init__(parent)

        self.setWindowTitle("Ironsworn App | Delves")

        # layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        progress_track_widget = ProgressWidget()
        main_layout.addWidget(progress_track_widget)

        domain_layout = QtWidgets.QHBoxLayout()
        domains_group_box = QtWidgets.QGroupBox("Theme/Domain")
        domains_group_box.setLayout(domain_layout)

        themes = ["Ancient"]
        self.theme_cb = QtWidgets.QComboBox()

        for theme in themes:
            self.theme_cb.addItem(theme)

        domain_layout.addWidget(self.theme_cb)

        domains = ["Ruins"]
        self.domain_cb = QtWidgets.QComboBox()

        for domain in domains:
            self.domain_cb.addItem(domain)

        domain_layout.addWidget(self.domain_cb)

        main_layout.addWidget(domains_group_box)

        self.log_widget = QtWidgets.QTextEdit()
        self.log_widget.setReadOnly(True)
        main_layout.addWidget(self.log_widget)

        btn_layout = QtWidgets.QHBoxLayout()
        generators_group_box = QtWidgets.QGroupBox("Generators")
        generators_group_box.setLayout(btn_layout)

        feature_btn = QtWidgets.QPushButton("Features")
        btn_layout.addWidget(feature_btn)
        feature_btn.clicked.connect(self.generate_feature)

        danger_btn = QtWidgets.QPushButton("Dangers")
        btn_layout.addWidget(danger_btn)
        danger_btn.clicked.connect(self.generate_dangers)

        opportunity_btn = QtWidgets.QPushButton("Opportunity")
        btn_layout.addWidget(opportunity_btn)
        opportunity_btn.clicked.connect(self.generate_opportunity)

        trap_btn = QtWidgets.QPushButton("Trap")
        btn_layout.addWidget(trap_btn)
        opportunity_btn.clicked.connect(self.generate_trap)

        loot_btn = QtWidgets.QPushButton("Loot")
        btn_layout.addWidget(loot_btn)
        loot_btn.clicked.connect(self.generate_loot)

        main_layout.addWidget(generators_group_box)

    def generate_feature(self):

        theme = self.theme_cb.currentText()
        domain = self.domain_cb.currentText()

        delves_generator = Delves()
        output = delves_generator.generate_features(theme.lower(), domain.lower())
        self.log_widget.append(output)

    def generate_dangers(self):

        theme = self.theme_cb.currentText()
        domain = self.domain_cb.currentText()

        delves_generator = Delves()
        output = delves_generator.generate_dangers(theme.lower(), domain.lower())
        self.log_widget.append(output)

    def generate_opportunity(self):

        delves_generator = Delves()
        output = delves_generator.generate_opportunity()
        self.log_widget.append(output)

    def generate_trap(self):

        delves_generator = Delves()
        output = delves_generator.generate_trap()
        self.log_widget.append(output)

    def generate_loot(self):
        loot_generator = Loot()
        output = loot_generator.generate_loot()
        self.log_widget.append(output)











