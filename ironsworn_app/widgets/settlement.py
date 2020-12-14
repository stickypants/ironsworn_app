import sys
from Qt import QtWidgets, QtGui, QtCore

from generators.weather import Weather
from generators.event import Event
from generators.npc import NPC
from generators.settlement import Settlement

from widgets.npc import NPCDialog
from widgets.combat import CombatDialog


class SettlementDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super(SettlementDialog, self).__init__(parent)

        self.setWindowTitle("Ironsworn App | Settlement")

        # layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        self.stl_name_ql = QtWidgets.QLineEdit()
        self.stl_name_ql.setReadOnly(True)
        main_layout.addWidget(self.stl_name_ql)

        self.stl_leader_ql = QtWidgets.QLineEdit()
        self.stl_leader_ql.setReadOnly(True)
        main_layout.addWidget(self.stl_leader_ql)

        self.stl_description_widget = QtWidgets.QTextEdit()
        self.stl_description_widget.setReadOnly(True)
        main_layout.addWidget(self.stl_description_widget)

        self.log_widget = QtWidgets.QTextEdit()
        self.log_widget.setReadOnly(True)
        main_layout.addWidget(self.log_widget)

        btn_layout = QtWidgets.QHBoxLayout()

        generators_group_box = QtWidgets.QGroupBox("Generators")
        generators_group_box.setLayout(btn_layout)

        weather_btn = QtWidgets.QPushButton("Weather")
        btn_layout.addWidget(weather_btn)
        weather_btn.clicked.connect(self.generate_weather)

        event_btn = QtWidgets.QPushButton("Event")
        btn_layout.addWidget(event_btn)
        event_btn.clicked.connect(self.generate_urban_event)

        building_btn = QtWidgets.QPushButton("Building")
        btn_layout.addWidget(building_btn)
        building_btn.clicked.connect(self.generate_building)

        main_layout.addWidget(generators_group_box)

    def init_ui(self, settlement, npc):

        self.stl_name_ql.setText(settlement.stl_name)
        self.stl_leader_ql.setText(npc.npc_name)

        settlement_description = "Settlement Governement : {} \nSettlement Known For : {} \nSettlement Trait : {}\nSettlement Trouble : {}".format(
            settlement.stl_governement, settlement.stl_known_for, settlement.stl_trait, settlement.stl_trouble)
        self.stl_description_widget.append(settlement_description)

    def init_ui_from_json(self, settlement):

        self.stl_name_ql.setText(settlement["name"])
        self.stl_leader_ql.setText(settlement["leader_name"])

        settlement_description = "Settlement Governement : {} \nSettlement Known For : {} \nSettlement Trait : {}\nSettlement Trouble : {}".format(
            settlement["governement_type"], settlement["settlement_known_for"], settlement["settlement_trait"], settlement["settlement_trouble"])
        self.stl_description_widget.append(settlement_description)

    def save(self, settlement, npc):
        import os
        import json

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/settlement.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        temp = data["settlement"]

        new_data = {
                "name": settlement.stl_name,
                "leader_name": npc.npc_name,
                "governement_type": settlement.stl_governement,
                "settlement_known_for": settlement.stl_known_for,
                "settlement_trait": settlement.stl_trait,
                "settlement_trouble": settlement.stl_trouble,
        }

        temp.append(new_data)

        with open(filename, 'w') as write_file:
            json.dump(data, write_file, indent=4)

    def generate_urban_event(self):
        event_generator = Event()
        output = event_generator.generate_urban_event()
        self.log_widget.append(output)

    def generate_weather(self):
        weather_generator = Weather()
        output = weather_generator.generate_weather()
        self.log_widget.append(output)

    def generate_building(self):
        event_generator = Settlement()
        output = event_generator.generate_building()
        self.log_widget.append(output)
