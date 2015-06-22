# -*- coding: utf-8 -*-
# Form implementation generated from reading ui file 'defplot.ui'

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    """
	def on_actionImport_Layer_triggered(self, checked = None): 
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
       	QgsMapLayerRegistry.instance().addMapLayer(layer);
        # Set extent to the extent of our layer
       	self.canvas.setExtent(layer.extent())
       	
        # Set up the map canvas layer set
       	cl = QgsMapCanvasLayer(layer)
       	layers = [cl]
       	self.canvas.setLayerSet(layers)
    """
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(749, 554)
        self.setWindowIcon(QtGui.QIcon('icons/icon.png'))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridlayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 749, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.LeftToolBarArea, self.toolBar)
        
        self.actionImport_Layer = QtGui.QAction(MainWindow)
        #self.actionImport_Layer.triggered.connect(QtGui.qApp.quit)
        #self.actionImport_Layer.setCheckable(True)
        #self.actionImport_Layer.setChecked(True)
        #self.actionImport_Layer.triggered.connect(self.on_actionImport_Layer_triggered)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icons/import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_Layer.setIcon(icon)
        self.actionImport_Layer.setObjectName(_fromUtf8("actionImport_Layer"))
        
        self.actionPlot_Sensors = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icons/plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPlot_Sensors.setIcon(icon1)
        self.actionPlot_Sensors.setObjectName(_fromUtf8("actionPlot_Sensors"))
        
        self.toolBar.addAction(self.actionImport_Layer)
        self.toolBar.addAction(self.actionPlot_Sensors)
        self.toolBar.addSeparator()        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionImport_Layer.setText(_translate("MainWindow", "Import Layer", None))
        self.actionImport_Layer.setToolTip(_translate("MainWindow", "Import Layer", None))
        self.actionPlot_Sensors.setText(_translate("MainWindow", "Plot Sensors", None))

