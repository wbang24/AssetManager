import csv
import os
from PySide2 import QtGui, QtWidgets, QtCore


import Assets as utils

class AssetUI(QtWidgets.QWidget):
    """UI for the Asset Manager."""

    def __init__(self):
        """Initialize the AssetUI."""
        super().__init__()
        self.setWindowTitle("Asset Manager")
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)
        
        # get our data from the db/csv
        self.assets = utils.AssetManager()
        self.all_data = self.assets.all_data

        # make our list of assets by name.
        self.asset_list_widget = QtWidgets.QListWidget()
        self.populate_asset_list()
        # if you click that item, then run update_asset_info
        self.asset_list_widget.itemClicked.connect(self.update_asset_info)
        self.layout.addWidget(self.asset_list_widget)

        self.asset_info_label = QtWidgets.QLabel()
        self.layout.addWidget(self.asset_info_label)
        
        # work in progress...
        self.load_button = QtWidgets.QPushButton("Load File")
        self.load_button.clicked.connect(self.load_file)
        self.layout.addWidget(self.load_button)

    def populate_asset_list(self):
        """Populate the asset list widget with asset names."""
        for asset_name, asset_info in self.all_data.items():
            item = QtWidgets.QListWidgetItem(asset_name)
            item.setData(QtCore.Qt.UserRole, asset_info)
            item.setSizeHint(QtCore.QSize(150, 60))
            self.asset_list_widget.addItem(item)

    def update_asset_info(self):
        """Update the asset information label with the selected asset's details."""
        selected_item = self.asset_list_widget.currentItem()
        # for transparency I didn't know what UserRole was for QT and used chatgpt to help me understand how this part works
        # AI is scary but cool.
        asset_info = selected_item.data(QtCore.Qt.UserRole)
        asset_text = "Asset Name: {}\n".format(asset_info['asset_name'])
        asset_text += "Asset Type: {}\n".format(asset_info['asset_type'])
        asset_text += "Texture Resolution: {}\n".format(asset_info['txt_res'])
        asset_text += "Vertex Count: {}\n".format(asset_info['vrt_count'])
        asset_text += "Modeling File: {}\n".format(asset_info['model_file'])
        asset_text += "Texture File: {}\n".format(asset_info['texture_file'])
        asset_text += "Rigging File: {}\n".format(asset_info['rigging_file'])
        self.asset_info_label.setText(asset_text)

    def load_file(self):
        """Open a file dialog and perform file loading logic when a file is selected."""
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Load File")
        if file_path:
            utils.Asset.load_maya_file(file_path)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    asset_ui = AssetUI()
    asset_ui.show()
    sys.exit(app.exec_())
