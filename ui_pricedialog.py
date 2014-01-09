# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pricedialog.ui'
#
# Created: Thu Jan 09 23:48:10 2014
#      by: PyQt4 UI code generator 4.10.3
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

class Ui_PriceDialog(object):
    def setupUi(self, PriceDialog):
        PriceDialog.setObjectName(_fromUtf8("PriceDialog"))
        PriceDialog.setWindowModality(QtCore.Qt.NonModal)
        PriceDialog.resize(282, 351)
        PriceDialog.setModal(False)
        self.verticalLayout = QtGui.QVBoxLayout(PriceDialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tableWidget = QtGui.QTableWidget(PriceDialog)
        self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.okButton = QtGui.QPushButton(PriceDialog)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(PriceDialog)
        QtCore.QObject.connect(self.okButton, QtCore.SIGNAL(_fromUtf8("clicked()")), PriceDialog.close)
        QtCore.QMetaObject.connectSlotsByName(PriceDialog)

    def retranslateUi(self, PriceDialog):
        PriceDialog.setWindowTitle(_translate("PriceDialog", "Dialog", None))
        self.okButton.setText(_translate("PriceDialog", "确定", None))

