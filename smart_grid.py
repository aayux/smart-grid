#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

import sys
import os

# Import GUI files

from smartgrid_gui import Ui_MainWindow
from login_gui import Ui_Dialog

# Environment variable QGISHOME must be set to the install directory
# before running the application

QGIS_PREFIX = os.getenv('QGISHOME')


class SmartGrid(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(SmartGrid, self).__init__(parent)
        self.setupUi(self)
        self.layers = []
        self.root_flag = False

        self.setWindowTitle('Smart Grid')
        self.actionImport_Rlayer.triggered.connect(self.on_actionImport_Rlayer_toggled)
        self.actionImport_Vlayer.triggered.connect(self.on_actionImport_Vlayer_toggled)
        self.actionPan.triggered.connect(self.click_to_pan)

        self.canvas = QgsMapCanvas()
        self.canvas.useImageToRender(False)

        # Reference to root node of layer tree

        self.root = QgsProject.instance().layerTreeRoot()

        # Convert project into a layer tree so
        # that the layers appear on the canvas

        self.bridge = QgsLayerTreeMapCanvasBridge(self.root,
                self.canvas)

        self.canvas.show()

        # Table of Contents/Legend Model

        self.model = QgsLayerTreeModel(self.root)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeReorder)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeChangeVisibility)
        self.view = QgsLayerTreeView()
        self.view.setModel(self.model)

        # Dock legend to main window

        self.LegendDock = QDockWidget('Layer Tree', self)
        self.LegendDock.setObjectName('layers')
        self.LegendDock.setAllowedAreas(Qt.LeftDockWidgetArea
                | Qt.RightDockWidgetArea)
        self.LegendDock.setWidget(self.view)
        self.LegendDock.setContentsMargins(5, 5, 5, 5)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.LegendDock)

        self.layout = QVBoxLayout(self.frame)
        self.layout.addWidget(self.canvas)

    def on_actionImport_Rlayer_toggled(self, checked=None):
        if checked is None:
            return
        fileName = QFileDialog.getOpenFileName(self, 'Open Layer', '.',
                'Image Files (*.tif)')
        fileInfo = QFileInfo(fileName)
        baseName = fileInfo.baseName()
        raster_layer = QgsRasterLayer(fileName, baseName)
        if not raster_layer.isValid():
            print 'Layer failed to load!'

        # Add layer to the registry....

        QgsMapLayerRegistry.instance().addMapLayer(raster_layer, False)
        if self.root_flag is False:
            rootnode = self.root.insertLayer(0, raster_layer)
            print 'Loaded root'
            self.root_flag = True
        else:
            self.root.insertLayer(0, raster_layer)

    def on_actionImport_Vlayer_toggled(self, checked=None):
        if checked is None:
            return
        fileName = QFileDialog.getOpenFileName(self, 'Open Layer', '.',
                'shp (*.shp);;dgn (*.dgn)')
        fileInfo = QFileInfo(fileName)
        vector_layer = QgsVectorLayer(fileName, fileInfo.fileName(),
                'ogr')
        if not vector_layer.isValid():
            print 'Layer failed to load!'

        # Add layer to the registry

        QgsMapLayerRegistry.instance().addMapLayer(vector_layer, False)
        if self.root_flag is False:
            rootnode = self.root.insertLayer(0, vector_layer)
            print 'Loaded root'
            self.root_flag = True
        else:
            self.root.insertLayer(0, vector_layer)

    def click_to_pan(self):
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.canvas.setMapTool(self.toolPan)


class LoginScreen(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_click_login)
        self.setWindowTitle('Login')

    def on_click_login(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        if self.username == '' and self.password == '':
            self.close()
            self.main_window = SmartGrid(self)
            self.main_window.showMaximized()
        else:
            QMessageBox.warning(self, 'Warning',
                                'Incorrect Username/Password')
            self.lineEdit.clear()
            self.lineEdit_2.clear()


def main(argv):

    # create Qt application

    app = QApplication(argv)

    # Initialize qgis libraries

    QgsApplication.setPrefixPath(QGIS_PREFIX, True)
    QgsApplication.initQgis()

    login_window = LoginScreen()
    login_window.move(100, 100)
    login_window.show()

    retval = app.exec_()

    QgsApplication.exitQgis()
    sys.exit(retval)


if __name__ == '__main__':
    main(sys.argv)

			
