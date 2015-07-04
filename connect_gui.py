# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pgconnect_gui.ui'
#
# Created: Thu Jul  2 14:03:08 2015
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

class Ui_pgDialog(object):
    def setuppgUi(self, pgDialog):
        pgDialog.setObjectName(_fromUtf8("pgDialog"))
        pgDialog.resize(277, 395)
        self.pgpushButton = QtGui.QPushButton(pgDialog)
        self.pgpushButton.setGeometry(QtCore.QRect(90, 360, 85, 26))
        self.pgpushButton.setObjectName(_fromUtf8("pgpushButton"))
        self.widget = QtGui.QWidget(pgDialog)
        self.widget.setGeometry(QtCore.QRect(30, 10, 214, 342))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pglabel_6 = QtGui.QLabel(self.widget)
        self.pglabel_6.setObjectName(_fromUtf8("pglabel_6"))
        self.verticalLayout_3.addWidget(self.pglabel_6)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pglabel = QtGui.QLabel(self.widget)
        self.pglabel.setObjectName(_fromUtf8("pglabel"))
        self.verticalLayout_2.addWidget(self.pglabel)
        self.pglabel_2 = QtGui.QLabel(self.widget)
        self.pglabel_2.setObjectName(_fromUtf8("pglabel_2"))
        self.verticalLayout_2.addWidget(self.pglabel_2)
        self.pglabel_3 = QtGui.QLabel(self.widget)
        self.pglabel_3.setObjectName(_fromUtf8("pglabel_3"))
        self.verticalLayout_2.addWidget(self.pglabel_3)
        self.pglabel_4 = QtGui.QLabel(self.widget)
        self.pglabel_4.setObjectName(_fromUtf8("pglabel_4"))
        self.verticalLayout_2.addWidget(self.pglabel_4)
        self.pglabel_5 = QtGui.QLabel(self.widget)
        self.pglabel_5.setObjectName(_fromUtf8("pglabel_5"))
        self.verticalLayout_2.addWidget(self.pglabel_5)
        self.pglabel_7 = QtGui.QLabel(self.widget)
        self.pglabel_7.setObjectName(_fromUtf8("pglabel_7"))
        self.verticalLayout_2.addWidget(self.pglabel_7)
        self.pglabel_8 = QtGui.QLabel(self.widget)
        self.pglabel_8.setObjectName(_fromUtf8("pglabel_8"))
        self.verticalLayout_2.addWidget(self.pglabel_8)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pglineEdit = QtGui.QLineEdit(self.widget)
        self.pglineEdit.setObjectName(_fromUtf8("pglineEdit"))
        self.verticalLayout.addWidget(self.pglineEdit)
        self.pglineEdit_2 = QtGui.QLineEdit(self.widget)
        self.pglineEdit_2.setObjectName(_fromUtf8("pglineEdit_2"))
        self.verticalLayout.addWidget(self.pglineEdit_2)
        self.pglineEdit_3 = QtGui.QLineEdit(self.widget)
        self.pglineEdit_3.setObjectName(_fromUtf8("pglineEdit_3"))
        self.verticalLayout.addWidget(self.pglineEdit_3)
        self.pglineEdit_4 = QtGui.QLineEdit(self.widget)
        self.pglineEdit_4.setObjectName(_fromUtf8("pglineEdit_4"))
        self.verticalLayout.addWidget(self.pglineEdit_4)
        self.pglineEdit_5 = QtGui.QLineEdit(self.widget)
        self.pglineEdit_5.setEchoMode(QtGui.QLineEdit.Password)
        self.pglineEdit_5.setObjectName(_fromUtf8("pglineEdit_5"))
        self.verticalLayout.addWidget(self.pglineEdit_5)
        self.pglineEdit_6 = QtGui.QLineEdit(self.widget)
        self.pglineEdit_6.setObjectName(_fromUtf8("pglineEdit_6"))
        self.verticalLayout.addWidget(self.pglineEdit_6)
        self.pglineEdit_7 = QtGui.QLineEdit(self.widget)
        self.pglineEdit_7.setObjectName(_fromUtf8("pglineEdit_7"))
        self.verticalLayout.addWidget(self.pglineEdit_7)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.checkBox = QtGui.QCheckBox(self.widget)
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.verticalLayout_4.addWidget(self.checkBox)
        self.checkBox_2 = QtGui.QCheckBox(self.widget)
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.verticalLayout_4.addWidget(self.checkBox_2)
        self.checkBox_3 = QtGui.QCheckBox(self.widget)
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.verticalLayout_4.addWidget(self.checkBox_3)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(pgDialog)
        QtCore.QMetaObject.connectSlotsByName(pgDialog)

    def retranslateUi(self, pgDialog):
        pgDialog.setWindowTitle(_translate("pgDialog", "Dialog", None))
        self.pgpushButton.setText(_translate("pgDialog", "Connect", None))
        self.pglabel_6.setText(_translate("pgDialog", "      Enter POSTGIS DB Details", None))
        self.pglabel.setText(_translate("pgDialog", "Host", None))
        self.pglabel_2.setText(_translate("pgDialog", "Port          ", None))
        self.pglabel_3.setText(_translate("pgDialog", "Database ", None))
        self.pglabel_4.setText(_translate("pgDialog", "Username", None))
        self.pglabel_5.setText(_translate("pgDialog", "Password ", None))
        self.pglabel_7.setText(_translate("pgDialog", "Table", None))
        self.pglabel_8.setText(_translate("pgDialog", "Key", None))
        self.pglineEdit.setText(_translate("pgDialog", "localhost", None))
        self.pglineEdit_2.setText(_translate("pgDialog", "5432", None))
        self.checkBox.setText(_translate("pgDialog", "Remember Username", None))
        self.checkBox_2.setText(_translate("pgDialog", "Remember Password", None))
        self.checkBox_3.setText(_translate("pgDialog", "Remember DB", None))

