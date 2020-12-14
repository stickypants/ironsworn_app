import sys
from Qt import QtWidgets, QtGui, QtCore

from widgets.progress import ProgressWidget
from widgets.npc import NPCDialog
from widgets.combat import CombatDialog
from widgets.settlement import SettlementDialog

from generators.weather import Weather
from generators.waypoint import Waypoint
from generators.event import Event
from generators.npc import NPC
from generators.settlement import Settlement


class JourneyDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super(JourneyDialog, self).__init__(parent)

        self.setWindowTitle("Ironsworn App | Journey")

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

        weather_btn = QtWidgets.QPushButton("Weather")
        btn_layout.addWidget(weather_btn)
        weather_btn.clicked.connect(self.generate_weather)

        waypoint_btn = QtWidgets.QPushButton("Waypoint")
        btn_layout.addWidget(waypoint_btn)
        waypoint_btn.clicked.connect(self.generate_waypoint)

        event_btn = QtWidgets.QPushButton("Event")
        btn_layout.addWidget(event_btn)
        event_btn.clicked.connect(self.generate_event)

        main_layout.addWidget(generators_group_box)

    def generate_weather(self):
        weather_generator = Weather()
        output = weather_generator.generate_weather()
        self.log_widget.append(output)

    def generate_waypoint(self):
        waypoint_generator = Waypoint()
        output = waypoint_generator.generate_waypoint()
        self.log_widget.append(output)

    def generate_event(self):
        event_generator = Event()
        output = event_generator.generate_event()
        self.log_widget.append(output)








