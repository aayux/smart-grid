#!/usr/bin/python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QObject, pyqtSlot

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

import sys, string
import os
import pdb

# Import GUI files

from smartgrid_gui import Ui_MainWindow
from login_gui import Ui_Dialog
from connect_gui import Ui_pgDialog

# Environment variable QGISHOME must be set to the install directory
# before running the application

QGIS_PREFIX = os.getenv('QGISHOME')
uri = QgsDataSourceURI()

class pgconnect(QDialog,Ui_pgDialog):
    global uri
    def __init__(self, parent=None):
        super(pgconnect, self).__init__(parent)
        self.setuppgUi(self)
        self.pgpushButton.clicked.connect(self.onclick_pglogin)
        self.hname ='localhost'
        self.port ='5432'
        self.dbname = None
        self.uname = None
        self.pwd = None
        self.move(QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())
     
    def onclick_pglogin(self):
        print 'pass1'
        self.dbname=self.pglineEdit_3.text()
    	self.uname=self.pglineEdit_4.text()
    	self.pwd=self.pglineEdit_5.text()
    	print "lol"
    	uri.setConnection(self.hname, self.port, str(self.dbname), str(self.uname), str(self.pwd))
    	print "1"
    	uri.setDataSource("public", "range", "the_geom",'', "id")
    	print "2"
    	self.close()
    	print 'pass2'
            
class MapCoords(object):
  def __init__(self, mainwindow):
    self.mainwindow = mainwindow
    # This one is to capture the mouse move for coordinate display
    
    QObject.connect(mainwindow.canvas, SIGNAL('xyCoordinates(const QgsPoint&)'), self.updateCoordsDisplay)
    self.latlon = QLabel("0.0 , 0.0")
    self.latlon.setFixedWidth(300)
    self.latlon.setAlignment(Qt.AlignHCenter)
    self.latlon.setFrameStyle(QFrame.StyledPanel)
    self.mainwindow.statusbar.addPermanentWidget(self.latlon)

  # Signal handeler for updating coord display
  def updateCoordsDisplay(self, point):

  	capture_string = QString(str(point.x()) + " , " + str(point.y()))
  	self.latlon.setText(capture_string)

class SmartGrid(QMainWindow, Ui_MainWindow):
    global uri
    def __init__(self, parent = None):
        super(SmartGrid, self).__init__(parent)
        self.setupUi(self)
        self.root_flag = False
        
        
        self.setWindowTitle('Smart Grid')
        self.actionImport_Rlayer.triggered.connect(self.onactionImport_Rlayer_toggled)
        self.actionImport_Vlayer.triggered.connect(self.onactionImport_Vlayer_toggled)
        self.actionImport_PGlayer.triggered.connect(self.onactionImport_PGlayer_toggled)
        self.actionPan.triggered.connect(self.click_to_pan)

        self.canvas = QgsMapCanvas()
        self.canvas.useImageToRender(False)
		
		# New Map Coords display in status bar
        
        self.map_coords = MapCoords(self)

        # Reference to root node of layer tree

        self.root = QgsProject.instance().layerTreeRoot()

        # Convert project into a layer tree so
        # that the layers appear on the canvas

        self.bridge = QgsLayerTreeMapCanvasBridge(self.root, self.canvas)

        self.canvas.show()

        # Table of Contents/Legend Model

        self.model = QgsLayerTreeModel(self.root)
        self.model.setFlag(QgsLayerTreeModel.AllowNodeReorder)
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
    
    def onactionImport_Rlayer_toggled(self, checked = None):
        if checked is None:
            return
        fileName = QFileDialog.getOpenFileName(self, 'Open Layer', '.',
                'Image Files (*.tif)')
        fileInfo = QFileInfo(fileName)
        baseName = fileInfo.baseName()
        raster_layer = QgsRasterLayer(fileName, baseName)
        if not raster_layer.isValid():
            print 'Layer failed to load!'
            return

        # Add layer to the registry....
        self.temp_layer=raster_layer
        QgsMapLayerRegistry.instance().addMapLayer(raster_layer, False)
        if self.root_flag is False:
            rootnode = self.root.insertLayer(0, raster_layer)
            print 'Loaded root'
            self.root_flag = True
        else:
            self.root.insertLayer(0, raster_layer)
        
    def onactionImport_Vlayer_toggled(self, checked=None):
        if checked is None:
            return
        fileName = QFileDialog.getOpenFileName(self, 'Open Layer', '.',
                'shp (*.shp);;dgn (*.dgn)')
        fileInfo = QFileInfo(fileName)
        vector_layer = QgsVectorLayer(fileName, fileInfo.fileName(),
                'ogr')
        if not vector_layer.isValid():
            print 'Layer failed to load!'
            return

        # Add layer to the registry
        palyr= QgsPalLayerSettings()
        self.canvas.mapRenderer().setLabelingEngine(QgsPalLabeling())
        palyr.readFromLayer(vector_layer)
        palyr.enabled = True 
        palyr.fieldName = 'Text'
        #palyr.fontSizeInMapUnits = True
        #palyr.textColor = Qt.red
        palyr.placement= QgsPalLayerSettings.OverPoint
        palyr.setDataDefinedProperty(QgsPalLayerSettings.Size,True,True,'8','')
        palyr.writeToLayer(vector_layer)
        QgsMapLayerRegistry.instance().addMapLayer(vector_layer, False)
        
        if self.root_flag is False:
            rootnode = self.root.insertLayer(0, vector_layer)
            print 'Loaded root'
            self.root_flag = True
        else:
            self.root.insertLayer(0, vector_layer)
    
    def onactionImport_PGlayer_toggled(self):
        print "abcd"
        self.dlg = pgconnect(self)
        self.dlg.show()
        print "back"
        self.dlg.exec_()
        print "done"
        vlayer = QgsVectorLayer(uri.uri(), "people", "postgres")
    	print "3"
    	if not vlayer.isValid():
            print 'Layer failed to load!'
            return
        QgsMapLayerRegistry.instance().addMapLayer(vlayer, False)
        if self.root_flag is False:
            rootnode = self.root.insertLayer(0, vlayer)
            print 'Loaded root'
            self.root_flag = True
        else:
            self.root.insertLayer(0, vlayer)
	
    def click_to_pan(self):
        self.toolPan = QgsMapToolPan(self.canvas)
        self.toolPan.setAction(self.actionPan)
        self.canvas.setMapTool(self.toolPan)


    
class LoginScreen(QDialog, Ui_Dialog):

    def __init__(self, parent=None):
        super(LoginScreen, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.onclick_login)
        self.setWindowTitle('Login')

    def onclick_login(self):
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

			
			
