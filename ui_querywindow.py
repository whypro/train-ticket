# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'querywindow.ui'
#
# Created: Thu Jan 09 20:49:40 2014
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

class Ui_QueryWindow(object):
    def setupUi(self, QueryWindow):
        QueryWindow.setObjectName(_fromUtf8("QueryWindow"))
        QueryWindow.resize(800, 513)
        self.centralwidget = QtGui.QWidget(QueryWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.fromStationLayout = QtGui.QHBoxLayout()
        self.fromStationLayout.setObjectName(_fromUtf8("fromStationLayout"))
        self.fromStationNameLabel = QtGui.QLabel(self.centralwidget)
        self.fromStationNameLabel.setObjectName(_fromUtf8("fromStationNameLabel"))
        self.fromStationLayout.addWidget(self.fromStationNameLabel)
        self.fromStationNameEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fromStationNameEdit.sizePolicy().hasHeightForWidth())
        self.fromStationNameEdit.setSizePolicy(sizePolicy)
        self.fromStationNameEdit.setObjectName(_fromUtf8("fromStationNameEdit"))
        self.fromStationLayout.addWidget(self.fromStationNameEdit)
        self.horizontalLayout.addLayout(self.fromStationLayout)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.toStationLayout = QtGui.QHBoxLayout()
        self.toStationLayout.setObjectName(_fromUtf8("toStationLayout"))
        self.toStationNameLabel = QtGui.QLabel(self.centralwidget)
        self.toStationNameLabel.setObjectName(_fromUtf8("toStationNameLabel"))
        self.toStationLayout.addWidget(self.toStationNameLabel)
        self.toStationNameEdit = QtGui.QLineEdit(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toStationNameEdit.sizePolicy().hasHeightForWidth())
        self.toStationNameEdit.setSizePolicy(sizePolicy)
        self.toStationNameEdit.setObjectName(_fromUtf8("toStationNameEdit"))
        self.toStationLayout.addWidget(self.toStationNameEdit)
        self.horizontalLayout.addLayout(self.toStationLayout)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.trainDateLayout = QtGui.QHBoxLayout()
        self.trainDateLayout.setObjectName(_fromUtf8("trainDateLayout"))
        self.trainDateLabel = QtGui.QLabel(self.centralwidget)
        self.trainDateLabel.setObjectName(_fromUtf8("trainDateLabel"))
        self.trainDateLayout.addWidget(self.trainDateLabel)
        self.trainDateEdit = QtGui.QDateEdit(self.centralwidget)
        self.trainDateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2014, 1, 1), QtCore.QTime(0, 0, 0)))
        self.trainDateEdit.setCalendarPopup(True)
        self.trainDateEdit.setObjectName(_fromUtf8("trainDateEdit"))
        self.trainDateLayout.addWidget(self.trainDateEdit)
        self.horizontalLayout.addLayout(self.trainDateLayout)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.studentCheckbox = QtGui.QCheckBox(self.centralwidget)
        self.studentCheckbox.setObjectName(_fromUtf8("studentCheckbox"))
        self.horizontalLayout.addWidget(self.studentCheckbox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setHighlightSections(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setHighlightSections(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.buttonLayout = QtGui.QHBoxLayout()
        self.buttonLayout.setObjectName(_fromUtf8("buttonLayout"))
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.buttonLayout.addItem(spacerItem4)
        self.queryButton = QtGui.QPushButton(self.centralwidget)
        self.queryButton.setObjectName(_fromUtf8("queryButton"))
        self.buttonLayout.addWidget(self.queryButton)
        self.closeButton = QtGui.QPushButton(self.centralwidget)
        self.closeButton.setObjectName(_fromUtf8("closeButton"))
        self.buttonLayout.addWidget(self.closeButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        QueryWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(QueryWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        QueryWindow.setMenuBar(self.menubar)

        self.retranslateUi(QueryWindow)
        QtCore.QObject.connect(self.closeButton, QtCore.SIGNAL(_fromUtf8("clicked()")), QueryWindow.close)
        QtCore.QMetaObject.connectSlotsByName(QueryWindow)

    def retranslateUi(self, QueryWindow):
        QueryWindow.setWindowTitle(_translate("QueryWindow", "列车查询", None))
        self.fromStationNameLabel.setText(_translate("QueryWindow", "出发站", None))
        self.toStationNameLabel.setText(_translate("QueryWindow", "到达站", None))
        self.trainDateLabel.setText(_translate("QueryWindow", "日期", None))
        self.trainDateEdit.setDisplayFormat(_translate("QueryWindow", "yyyy-MM-dd", None))
        self.studentCheckbox.setText(_translate("QueryWindow", "学生票", None))
        self.queryButton.setText(_translate("QueryWindow", "查询", None))
        self.closeButton.setText(_translate("QueryWindow", "关闭", None))

