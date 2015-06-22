#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

import pdb
import sys
import os

# Import our GUI
from defplot_gui import Ui_MainWindow

# pdb.set_trace()

# Environment variable QGISHOME must be set to the install directory
# before running the application
qgis_prefix = os.getenv('QGISHOME')

class DefPlot(QMainWindow, Ui_MainWindow):

    def on_actionImport_Layer_triggered (self, checked = None):
		if checked is None:
			return
		fileName = QFileDialog.getOpenFileName(self, "Open TIF File", ".", "Image Files (*.tif)")
		fileInfo = QFileInfo(fileName)
		baseName = fileInfo.baseName()
		layer = QgsRasterLayer(fileName, baseName)
		
		if not layer.isValid():
			print "Layer failed to load!"
		
		# Change the color of the layer to gray
        #symbols = layer.renderer().symbols()
        #ymbol = symbols[0]
        #ymbol.setFillColor(QColor.fromRgb(192,192,192))
        
        # Add layer to the registry
		QgsMapLayerRegistry.instance().addMapLayer(layer)
        # Set extent to the extent of our layer
		self.canvas.setExtent(layer.extent())
        
        # Set up the map canvas layer set
		cl = QgsMapCanvasLayer(layer)
		layers = [cl]
		self.canvas.setLayerSet(layers)
    
    def __init__(self, parent = None):
        super(DefPlot, self).__init__(parent)

        # Required by Qt4 to initialize the UI

        self.setupUi(self)
        self.setWindowTitle('DefPlot')
        #pdb.set_trace()
        self.actionImport_Layer.toggled.connect(self.on_actionImport_Layer_triggered)		
		
        self.canvas = QgsMapCanvas()
        self.canvas.useImageToRender(False)
        self.canvas.show()

        self.layout = QVBoxLayout(self.frame)
        self.layout.addWidget(self.canvas)
		
def main(argv):

  # create Qt application
    app = QApplication(argv)

  # Initialize qgis libraries
    QgsApplication.setPrefixPath(qgis_prefix, True)
    QgsApplication.initQgis()

  # create main window
    main_window = DefPlot()

  # move app window to left corner
    main_window.move(100, 100)
    main_window.show()

  # run!
    retval = app.exec_()

  # exit
    QgsApplication.exitQgis()
    sys.exit(retval)


if __name__ == '__main__':
    main(sys.argv)
			
