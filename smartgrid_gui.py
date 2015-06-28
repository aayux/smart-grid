# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smartgrid_gui.ui'
#
# Created: Sun Jun 28 10:09:49 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

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
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(931, 555)
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionImport_Vlayer = QtGui.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/v_import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_Vlayer.setIcon(icon)
        self.actionImport_Vlayer.setObjectName(_fromUtf8("actionImport_Vlayer"))
        self.actionImport_Rlayer = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/r_import.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImport_Rlayer.setIcon(icon1)
        self.actionImport_Rlayer.setObjectName(_fromUtf8("actionImport_Rlayer"))
        self.actionPlot_Sensors = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/plot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPlot_Sensors.setIcon(icon2)
        self.actionPlot_Sensors.setObjectName(_fromUtf8("actionPlot_Sensors"))
        self.actionPan = QtGui.QAction(MainWindow)
        self.actionPan.setCheckable(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/pan.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPan.setIcon(icon3)
        self.actionPan.setObjectName(_fromUtf8("actionPan"))
        self.toolBar.addAction(self.actionImport_Vlayer)
        self.toolBar.addAction(self.actionImport_Rlayer)
        self.toolBar.addAction(self.actionPan)
        self.toolBar.addAction(self.actionPlot_Sensors)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionImport_Vlayer.setText(_translate("MainWindow", "Import Vector Layer", None))
        self.actionImport_Vlayer.setToolTip(_translate("MainWindow", "Import Vector Layer", None))
        self.actionImport_Rlayer.setText(_translate("MainWindow", "Import Raster Layer", None))
        self.actionImport_Rlayer.setToolTip(_translate("MainWindow", "Import Raster Layer", None))
        self.actionPlot_Sensors.setText(_translate("MainWindow", "Plot Sensors", None))
        self.actionPlot_Sensors.setToolTip(_translate("MainWindow", "Plot Sensors", None))
        self.actionPan.setText(_translate("MainWindow", "Pan", None))
        self.actionPan.setToolTip(_translate("MainWindow", "Click to pan", None))

