# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connect_gui.ui'
#
# Created: Thu Jul  2 23:22:53 2015
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

class Ui_pgDialog(object):
    def setupUi(self, pgDialog):
        pgDialog.setObjectName(_fromUtf8("pgDialog"))
        pgDialog.resize(307, 293)
        self.layoutWidget = QtGui.QWidget(pgDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 10, 288, 232))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pglabel_6 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pglabel_6.setFont(font)
        self.pglabel_6.setObjectName(_fromUtf8("pglabel_6"))
        self.verticalLayout_3.addWidget(self.pglabel_6)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.pglabel = QtGui.QLabel(self.layoutWidget)
        self.pglabel.setObjectName(_fromUtf8("pglabel"))
        self.verticalLayout_2.addWidget(self.pglabel)
        self.pglabel_2 = QtGui.QLabel(self.layoutWidget)
        self.pglabel_2.setObjectName(_fromUtf8("pglabel_2"))
        self.verticalLayout_2.addWidget(self.pglabel_2)
        self.pglabel_3 = QtGui.QLabel(self.layoutWidget)
        self.pglabel_3.setObjectName(_fromUtf8("pglabel_3"))
        self.verticalLayout_2.addWidget(self.pglabel_3)
        self.pglabel_4 = QtGui.QLabel(self.layoutWidget)
        self.pglabel_4.setObjectName(_fromUtf8("pglabel_4"))
        self.verticalLayout_2.addWidget(self.pglabel_4)
        self.pglabel_5 = QtGui.QLabel(self.layoutWidget)
        self.pglabel_5.setObjectName(_fromUtf8("pglabel_5"))
        self.verticalLayout_2.addWidget(self.pglabel_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pglineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.pglineEdit.setObjectName(_fromUtf8("pglineEdit"))
        self.horizontalLayout.addWidget(self.pglineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.pglineEdit_2 = QtGui.QLineEdit(self.layoutWidget)
        self.pglineEdit_2.setObjectName(_fromUtf8("pglineEdit_2"))
        self.horizontalLayout_2.addWidget(self.pglineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.pglineEdit_3 = QtGui.QLineEdit(self.layoutWidget)
        self.pglineEdit_3.setObjectName(_fromUtf8("pglineEdit_3"))
        self.horizontalLayout_3.addWidget(self.pglineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pglineEdit_4 = QtGui.QLineEdit(self.layoutWidget)
        self.pglineEdit_4.setObjectName(_fromUtf8("pglineEdit_4"))
        self.horizontalLayout_4.addWidget(self.pglineEdit_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.pglineEdit_5 = QtGui.QLineEdit(self.layoutWidget)
        self.pglineEdit_5.setEchoMode(QtGui.QLineEdit.Password)
        self.pglineEdit_5.setObjectName(_fromUtf8("pglineEdit_5"))
        self.horizontalLayout_5.addWidget(self.pglineEdit_5)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.pgpushButton = QtGui.QPushButton(pgDialog)
        self.pgpushButton.setGeometry(QtCore.QRect(200, 250, 91, 31))
        self.pgpushButton.setObjectName(_fromUtf8("pgpushButton"))

        self.retranslateUi(pgDialog)
        QtCore.QMetaObject.connectSlotsByName(pgDialog)

    def retranslateUi(self, pgDialog):
        pgDialog.setWindowTitle(_translate("pgDialog", "Dialog", None))
        self.pglabel_6.setText(_translate("pgDialog", "            Connection information", None))
        self.pglabel.setText(_translate("pgDialog", "Host", None))
        self.pglabel_2.setText(_translate("pgDialog", "Port          ", None))
        self.pglabel_3.setText(_translate("pgDialog", "Database ", None))
        self.pglabel_4.setText(_translate("pgDialog", "Username", None))
        self.pglabel_5.setText(_translate("pgDialog", "Password ", None))
        self.pglineEdit.setText(_translate("pgDialog", "localhost", None))
        self.pglineEdit_2.setText(_translate("pgDialog", "5432", None))
        self.pgpushButton.setText(_translate("pgDialog", "Connect", None))

