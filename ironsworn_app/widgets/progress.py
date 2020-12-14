import sys
import os
import json

from Qt import QtWidgets, QtGui, QtCore


class ProgressTrackWidget(QtWidgets.QWidget):

    def __init__(self):
        super(ProgressTrackWidget, self).__init__()

        # layout
        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        self.progress_track_list = QtWidgets.QListWidget()
        self.progress_track_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

        main_layout.addWidget(self.progress_track_list)

        btn_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(btn_layout)

        add_btn = QtWidgets.QPushButton("Add Progress Track")
        btn_layout.addWidget(add_btn)
        delete_btn = QtWidgets.QPushButton("Delete Progress Track")
        btn_layout.addWidget(delete_btn)

        add_btn.clicked.connect(self.add_progress_track)
        delete_btn.clicked.connect(self.delete_progress_track)

        self.restore_save_data()

    def add_progress_track(self):

        item = QtWidgets.QListWidgetItem(self.progress_track_list)
        item_widget = ProgressWidget()
        item.setSizeHint(item_widget.sizeHint())

        self.progress_track_list.addItem(item)
        self.progress_track_list.setItemWidget(item, item_widget)

    def delete_progress_track(self):

        items = self.progress_track_list.selectedItems()

        for item in items:
            self.progress_track_list.takeItem(self.progress_track_list.row(item))

    def save(self):

        import os
        import json

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/quests.json')

        quest_data = {"quests": []}

        for i in range(0, self.progress_track_list.count()):
            item = self.progress_track_list.item(i)
            widget = self.progress_track_list.itemWidget(item)

            quest_name = widget.title.text()
            quest_ranking = widget.ranking_cb.currentIndex()
            quest_progress = []

            progress_cb_list = [widget.combo_box_layout.itemAt(i).widget() for i in range(
                widget.combo_box_layout.count())]

            for progress_cb in progress_cb_list:
                quest_progress.append(progress_cb.currentIndex())

            new_data = {
                    "name": quest_name,
                    "ranking": quest_ranking,
                    "progress": quest_progress,
                }

            quest_data["quests"].append(new_data)

        os.remove(filename)

        with open(filename, 'w') as write_file:
            json.dump(quest_data, write_file, indent=4)

    def restore_save_data(self):

        dirname = os.path.dirname(__file__)
        filename = os.path.join(dirname, 'saves/quests.json')

        with open(filename, "r") as read_file:
            data = json.load(read_file)

        for quest in data["quests"]:

            item = QtWidgets.QListWidgetItem(self.progress_track_list)

            item_widget = ProgressWidget()
            item_widget.title.setText(quest["name"])

            item_widget.ranking_cb.setCurrentIndex(quest["ranking"])

            progress_cb_list = [item_widget.combo_box_layout.itemAt(i).widget() for i in range(
                item_widget.combo_box_layout.count())]

            for i, progress_cb in enumerate(progress_cb_list):
                index = quest["progress"][i]
                progress_cb.setCurrentIndex(index)

            item.setSizeHint(item_widget.sizeHint())

            self.progress_track_list.addItem(item)
            self.progress_track_list.setItemWidget(item, item_widget)


class ProgressWidget(QtWidgets.QWidget):

    def __init__(self):
        super(ProgressWidget, self).__init__()

        # layout

        main_layout = QtWidgets.QVBoxLayout()
        self.setLayout(main_layout)

        header_layout = QtWidgets.QHBoxLayout()

        self.combo_box_layout = QtWidgets.QHBoxLayout()
        main_layout.addLayout(header_layout)
        main_layout.addLayout(self.combo_box_layout)

        # widgets

        self.title = QtWidgets.QLineEdit("Progress Track Name")
        self.title.setFixedHeight(35)

        self.ranking_cb = QtWidgets.QComboBox()
        self.ranking_cb.addItems(["Troublesome", "Dangerous",
                            "Formidable", "Extreme", "Epic"])
        self.ranking_cb.setFixedHeight(35)

        header_layout.addWidget(self.title)
        header_layout.addWidget(self.ranking_cb)

        for i in range(0, 10):
            progress_cb = QtWidgets.QComboBox()
            for j in range(0, 5):
                dirname = os.path.dirname(__file__)
                icon_path = os.path.join(dirname, 'img/progress_00{}.png'.format(j))
                pixmap = QtGui.QPixmap(icon_path)
                icon = QtGui.QIcon(pixmap)
                progress_cb.addItem(icon, "")
            progress_cb.setFixedSize(75, 50)
            self.combo_box_layout.addWidget(progress_cb)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    button = ProgressWidget()
    button.show()
    app.exec_()