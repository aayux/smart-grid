# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sensor_gui.ui'
#
# Created: Fri Jul  3 15:35:55 2015
#      by: PyQt4 UI code generator 4.11.3
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

class Ui_sDialog(object):
    def setupUi(self, sDialog):
        sDialog.setObjectName(_fromUtf8("sDialog"))
        sDialog.resize(358, 279)
        sDialog.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.sinfolabel = QtGui.QLabel(sDialog)
        self.sinfolabel.setGeometry(QtCore.QRect(10, 60, 131, 20))
        self.sinfolabel.setObjectName(_fromUtf8("sinfolabel"))
        self.snotelabel = QtGui.QLabel(sDialog)
        self.snotelabel.setGeometry(QtCore.QRect(10, 240, 351, 20))
        self.snotelabel.setObjectName(_fromUtf8("snotelabel"))
        self.widget = QtGui.QWidget(sDialog)
        self.widget.setGeometry(QtCore.QRect(220, 80, 129, 92))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.saddbtn = QtGui.QPushButton(self.widget)
        self.saddbtn.setObjectName(_fromUtf8("saddbtn"))
        self.verticalLayout.addWidget(self.saddbtn)
        self.sdltbtn = QtGui.QPushButton(self.widget)
        self.sdltbtn.setObjectName(_fromUtf8("sdltbtn"))
        self.verticalLayout.addWidget(self.sdltbtn)
        self.smodbtn = QtGui.QPushButton(self.widget)
        self.smodbtn.setObjectName(_fromUtf8("smodbtn"))
        self.verticalLayout.addWidget(self.smodbtn)
        self.widget1 = QtGui.QWidget(sDialog)
        self.widget1.setGeometry(QtCore.QRect(10, 20, 341, 29))
        self.widget1.setObjectName(_fromUtf8("widget1"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget1)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.snamelabel = QtGui.QLabel(self.widget1)
        self.snamelabel.setObjectName(_fromUtf8("snamelabel"))
        self.horizontalLayout.addWidget(self.snamelabel)
        self.comboBox = QtGui.QComboBox(self.widget1)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.horizontalLayout.addWidget(self.comboBox)
        self.widget2 = QtGui.QWidget(sDialog)
        self.widget2.setGeometry(QtCore.QRect(10, 80, 191, 141))
        self.widget2.setObjectName(_fromUtf8("widget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget2)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.sinfo = QtGui.QPlainTextEdit(self.widget2)
        self.sinfo.setReadOnly(True)
        self.sinfo.setObjectName(_fromUtf8("sinfo"))
        self.verticalLayout_2.addWidget(self.sinfo)
        self.sdeploy = QtGui.QPushButton(self.widget2)
        self.sdeploy.setObjectName(_fromUtf8("sdeploy"))
        self.verticalLayout_2.addWidget(self.sdeploy)

        self.retranslateUi(sDialog)
        QtCore.QMetaObject.connectSlotsByName(sDialog)

    def retranslateUi(self, sDialog):
        sDialog.setWindowTitle(_translate("sDialog", "Deploy Sensor", None))
        self.sinfolabel.setText(_translate("sDialog", "Sensor Information", None))
        self.snotelabel.setText(_translate("sDialog", "NOTE: Click on the canvas to deploy selected sensor", None))
        self.saddbtn.setText(_translate("sDialog", "Add New Sensor", None))
        self.sdltbtn.setText(_translate("sDialog", "Delete Sensor", None))
        self.smodbtn.setText(_translate("sDialog", "Modify Sensor", None))
        self.snamelabel.setText(_translate("sDialog", "Sensors Available", None))
        self.sdeploy.setText(_translate("sDialog", "Deploy", None))

