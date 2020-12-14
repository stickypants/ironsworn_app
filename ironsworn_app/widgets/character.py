import sys
import json
import os
from Qt import QtWidgets, QtGui, QtCore


class CharacterWidget(QtWidgets.QWidget):

    def __init__(self):
        super(CharacterWidget, self).__init__()

        # layout

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        header_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(header_layout)

        name_label = QtWidgets.QLabel("Name")
        self.name_ql = QtWidgets.QLineEdit("")

        health_label = QtWidgets.QLabel("Health")
        self.health_cb = QtWidgets.QComboBox()
        self.health_cb.addItems(["5", "4", "3", "2", "1", "0"])
        self.health_cb.setFixedSize(75, 40)

        spirit_label = QtWidgets.QLabel("Spirit")
        self.spirit_cb = QtWidgets.QComboBox()
        self.spirit_cb.addItems(["5", "4", "3", "2", "1", "0"])
        self.spirit_cb.setFixedSize(75, 40)

        supply_label = QtWidgets.QLabel("Supply")
        self.supply_cb = QtWidgets.QComboBox()
        self.supply_cb.addItems(["5", "4", "3", "2", "1", "0"])
        self.supply_cb.setFixedSize(75, 40)

        momentum_label = QtWidgets.QLabel("Momentum")
        self.momentum_cb = QtWidgets.QComboBox()
        self.momentum_cb.addItems(["10", "9", "8", "7", "6", "5", "4", "3", "2", "1", "0",
                              "-1", "-2", "-3", "-4", "-5", "-6"])
        self.momentum_cb.setFixedSize(75, 40)

        header_layout.addWidget(name_label)
        header_layout.addWidget(self.name_ql)
        header_layout.addWidget(health_label)
        header_layout.addWidget(self.health_cb)
        header_layout.addWidget(spirit_label)
        header_layout.addWidget(self.spirit_cb)
        header_layout.addWidget(supply_label)
        header_layout.addWidget(self.supply_cb)
        header_layout.addWidget(momentum_label)
        header_layout.addWidget(self.momentum_cb)

        stats_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(stats_layout)

        edge_label = QtWidgets.QLabel("Edge")
        self.edge_ql = QtWidgets.QLineEdit()
        self.edge_ql.setFixedSize(75, 40)

        heart_label = QtWidgets.QLabel("Heart")
        self.heart_ql = QtWidgets.QLineEdit()
        self.heart_ql.setFixedSize(75, 40)

        iron_label = QtWidgets.QLabel("Iron")
        self.iron_ql = QtWidgets.QLineEdit()
        self.iron_ql.setFixedSize(75, 40)

        shadow_label = QtWidgets.QLabel("Shadow")
        self.shadow_ql = QtWidgets.QLineEdit()
        self.shadow_ql.setFixedSize(75, 40)

        wits_label = QtWidgets.QLabel("Wits")
        self.wits_ql = QtWidgets.QLineEdit()
        self.wits_ql.setFixedSize(75, 40)

        xp_label = QtWidgets.QLabel("XP")
        self.xp_ql = QtWidgets.QLineEdit()
        self.xp_ql.setFixedSize(75, 40)

        xp_spent_label = QtWidgets.QLabel("XP Spent")
        self.xp_spent_ql = QtWidgets.QLineEdit()
        self.xp_spent_ql.setFixedSize(75, 40)

        stats_layout.addWidget(edge_label)
        stats_layout.addWidget(self.edge_ql)
        stats_layout.addWidget(heart_label)
        stats_layout.addWidget(self.heart_ql)
        stats_layout.addWidget(iron_label)
        stats_layout.addWidget(self.iron_ql)
        stats_layout.addWidget(shadow_label)
        stats_layout.addWidget(self.shadow_ql)
        stats_layout.addWidget(wits_label)
        stats_layout.addWidget(self.wits_ql)
        stats_layout.addWidget(xp_label)
        stats_layout.addWidget(self.xp_ql)
        stats_layout.addWidget(xp_spent_label)
        stats_layout.addWidget(self.xp_spent_ql)

        state_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(state_layout)

        wounded_label = QtWidgets.QLabel("Wounded")
        self.wounded = QtWidgets.QCheckBox()
        shaken_label = QtWidgets.QLabel("Shaken")
        self.shaken= QtWidgets.QCheckBox()
        unprepared_label = QtWidgets.QLabel("Unprepared")
        self.unprepared = QtWidgets.QCheckBox()
        encumbered_label = QtWidgets.QLabel("Encumbered")
        self.encumbered = QtWidgets.QCheckBox()

        corrupted_label = QtWidgets.QLabel("Corrupted")
        self.corrupted = QtWidgets.QCheckBox()
        cursed_label = QtWidgets.QLabel("Cursed")
        self.cursed = QtWidgets.QCheckBox()
        maimed_label = QtWidgets.QLabel("Maimed")
        self.maimed = QtWidgets.QCheckBox()
        tormented_label = QtWidgets.QLabel("Tormented")
        self.tormented = QtWidgets.QCheckBox()

        state_layout.addWidget(wounded_label)
        state_layout.addWidget(self.wounded)
        state_layout.addWidget(shaken_label)
        state_layout.addWidget(self.shaken)
        state_layout.addWidget(unprepared_label)
        state_layout.addWidget(self.unprepared)
        state_layout.addWidget(encumbered_label)
        state_layout.addWidget(self.encumbered)

        state_layout.addWidget(corrupted_label)
        state_layout.addWidget(self.corrupted)
        state_layout.addWidget(cursed_label)
        state_layout.addWidget(self.cursed)
        state_layout.addWidget(maimed_label)
        state_layout.addWidget(self.maimed)
        state_layout.addWidget(tormented_label)
        state_layout.addWidget(self.tormented)

        self.restored_saved_data()

    def restored_saved_data(self):

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/character.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        self.name_ql.setText(data["name"])

        self.edge_ql.setText(data["edge"])
        self.heart_ql.setText(data["heart"])
        self.iron_ql.setText(data["iron"])
        self.shadow_ql.setText(data["shadow"])
        self.wits_ql.setText(data["wits"])

        self.xp_ql.setText(data["xp"])
        self.xp_spent_ql.setText(data["xp_spent"])

        self.health_cb.setCurrentIndex(data["health"])
        self.spirit_cb.setCurrentIndex(data["spirit"])
        self.supply_cb.setCurrentIndex(data["supply"])
        self.momentum_cb.setCurrentIndex(data["momentum"])

        self.wounded.setChecked(data["wounded"])
        self.shaken.setChecked(data["shaken"])
        self.unprepared.setChecked(data["unprepared"])
        self.encumbered.setChecked(data["encumbered"])

        self.corrupted.setChecked(data["corrupted"])
        self.cursed.setChecked(data["cursed"])
        self.maimed.setChecked(data["maimed"])
        self.tormented.setChecked(data["tormented"])

    def save_data(self):

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/character.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        data["name"] = self.name_ql.text()

        data["edge"] = self.edge_ql.text()
        data["heart"] = self.heart_ql.text()
        data["iron"] = self.iron_ql.text()
        data["shadow"] = self.shadow_ql.text()
        data["wits"] = self.wits_ql.text()

        data["health"] = self.health_cb.currentIndex()
        data["spirit"] = self.spirit_cb.currentIndex()
        data["supply"] = self.supply_cb.currentIndex()
        data["momentum"] = self.momentum_cb.currentIndex()

        data["xp"] = self.xp_ql.text()
        data["xp_spent"] = self.xp_spent_ql.text()

        data["wounded"] = self.wounded.isChecked()
        data["shaken"] = self.shaken.isChecked()
        data["unprepared"] = self.unprepared.isChecked()
        data["encumbered"] = self.encumbered.isChecked()

        data["corrupted"] = self.corrupted.isChecked()
        data["cursed"] = self.cursed.isChecked()
        data["maimed"] = self.maimed.isChecked()
        data["tormented"] = self.tormented.isChecked()

        os.remove(filename)

        with open(filename, 'w') as write_file:
            json.dump(data, write_file, indent=4)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    button = CharacterWidget()
    button.show()
    app.exec_()