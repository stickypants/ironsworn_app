import sys
from Qt import QtWidgets, QtGui, QtCore


class NPCDialog(QtWidgets.QDialog):

    def __init__(self, parent):
        super(NPCDialog, self).__init__(parent)

        self.setWindowTitle("Ironsworn App | NPC")

        # layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        self.npc_name_ql = QtWidgets.QLineEdit()
        self.npc_name_ql.setReadOnly(True)
        main_layout.addWidget(self.npc_name_ql)

        self.npc_stance_ql = QtWidgets.QLineEdit()
        self.npc_stance_ql.setReadOnly(True)
        main_layout.addWidget(self.npc_stance_ql)

        self.npc_description_widget = QtWidgets.QTextEdit()
        self.npc_description_widget.setReadOnly(True)
        main_layout.addWidget(self.npc_description_widget)

    def init_ui(self, npc):

        self.npc_name_ql.setText(npc.npc_name)
        self.npc_stance_ql.setText(npc.npc_stance)

        npc_description = "NPC Role : {} \nNPC Goal : {} \n" \
                          "NPC Descriptors : {} - {} - {}\n".format(npc.npc_role, npc.npc_goal, npc.npc_desc_001,
                                                                    npc.npc_desc_002, npc.npc_desc_003)

        self.npc_description_widget.append(npc_description)

    def init_ui_from_json(self, npc):

        self.npc_name_ql.setText(npc["name"])
        self.npc_stance_ql.setText(npc["stance"])

        npc_description = "NPC Role : {} \nNPC Goal : {} \n" \
                          "NPC Descriptors : {} - {} - {}\n".format(npc["role"], npc["goal"], npc["descriptor_001"],
                                                                    npc["descriptor_002"], npc["descriptor_003"])

        self.npc_description_widget.append(npc_description)

    def save(self, npc):
        import os
        import json

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/npc.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        temp = data["npc"]

        new_data = {
                "name": npc.npc_name,
                "stance": npc.npc_stance,
                "role": npc.npc_role,
                "goal": npc.npc_goal,
                "descriptor_001": npc.npc_desc_001,
                "descriptor_002": npc.npc_desc_002,
                "descriptor_003": npc.npc_desc_003,
                "bounded": "False"
        }

        temp.append(new_data)

        with open(filename, 'w') as write_file:
            json.dump(data, write_file, indent=4)


