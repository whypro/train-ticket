# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
import datetime
from PyQt4 import QtGui, QtCore
from ui_querywindow import Ui_QueryWindow
from ui_pricedialog import Ui_PriceDialog
from train import Query, Ticket


class PriceDialog(QtGui.QDialog, Ui_PriceDialog):
    def __init__(self, parent, price):
        super(PriceDialog, self).__init__(parent)
        self.setupUi(self)

        # 设置表头
        tableHeaders = (
            '商务座', '特等座', '一等座', '二等座', '高级软卧', '软卧',
            '硬卧', '软座', '硬座', '无座',
        )
        self.tableWidget.setRowCount(len(tableHeaders))
        self.tableWidget.setVerticalHeaderLabels(tableHeaders)
        self.tableWidget.setColumnCount(1)
        tableItemData = [
            price.get('A9', '--'),
            price.get('P', '--'),
            price.get('M', '--'),
            price.get('O', '--'),
            price.get('A6', '--'),
            price.get('A4', '--'),
            price.get('A3', '--'),
            '--',
            price.get('A1', '--'),
            price.get('WZ', '--'),
        ]

        for row in range(len(tableItemData)):
            tableItem = QtGui.QTableWidgetItem(tableItemData[row])
            tableItem.setTextAlignment(QtCore.Qt.AlignCenter)
            #tableItem.setFlags(QtCore.Qt.ItemIsEnabled)
            self.tableWidget.setItem(row, 0, tableItem)


class QueryWindow(QtGui.QMainWindow, Ui_QueryWindow):
    def __init__(self):
        super(QueryWindow, self).__init__()
        self.setupUi(self)
        self.trainDateEdit.setDate(datetime.datetime.now())
        self.queryButton.clicked.connect(self.query)
        self.aboutAction.triggered.connect(self.showAbout)

        self.trains = None
        self.train_date = None

    def query(self):
        self.statusBar.showMessage('查询中，请稍候……')
        query = Query(
            self.fromStationNameEdit.text(), self.toStationNameEdit.text(),
            self.trainDateEdit.text(), self.studentCheckbox.isChecked()
        )
        self.trains = query.query_trains()['datas']
        self.train_date = self.trainDateEdit.text()

        # 设置表头
        tableHeaders = (
            '车次', '出发站', '到达站', '出发时间', '到达时间', '历时',
            '商务座', '特等座', '一等座', '二等座', '高级软卧', '软卧',
            '硬卧', '软座', '硬座', '无座', '备注',
        )
        self.tableWidget.setColumnCount(len(tableHeaders))
        self.tableWidget.setHorizontalHeaderLabels(tableHeaders)

        self.tableWidget.setRowCount(len(self.trains))
        for (row, train) in enumerate(self.trains):
            tableItemData = [
                train.get('station_train_code'),
                train.get('from_station_name'),
                train.get('to_station_name'),
                train.get('start_time'),
                train.get('arrive_time'),
                train.get('lishi'),
                train.get('swz_num'),
                train.get('tz_num'),
                train.get('zy_num'),
                train.get('ze_num'),
                train.get('gr_num'),
                train.get('rw_num'),
                train.get('yw_num'),
                train.get('rz_num'),
                train.get('yz_num'),
                train.get('wz_num'),
                train.get('note'),
                # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(records[row].startTime)),
                # time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(records[row].lastTime)),
            ]

            for col in range(len(tableItemData)):
                tableItem = QtGui.QTableWidgetItem(tableItemData[col])
                tableItem.setTextAlignment(QtCore.Qt.AlignCenter)
                #tableItem.setFlags(QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(row, col, tableItem)

        self.statusBar.showMessage('查询完毕！')
        # 重设列宽
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.resizeRowsToContents()
        self.tableWidget.itemDoubleClicked.connect(self.showPrice)

    def showAbout(self):
        aboutMessage = \
            '<p><strong>列车查询</strong>&nbsp;{0}&nbsp;\
            <font color="red"><em>{1}</em></font></p>\
            <p>版权所有&nbsp;&copy;&nbsp;2014&nbsp;WHYPRO</p>'.format(
            '0.1.1', 'Alpha'
        )
        QtGui.QMessageBox.about(self, u'关于', aboutMessage)

    def showPrice(self, item):
        train = self.trains[item.row()]
        ticket = Ticket(
            train['train_no'], train['from_station_no'],
            train['to_station_no'], train['seat_types'],
            self.train_date,
        )
        price = ticket.query_price()

        priceDialog = PriceDialog(self, price)
        priceDialog.setWindowTitle(train['station_train_code'])
        priceDialog.setModal(True)
        priceDialog.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = QueryWindow()
    window.show()
    app.exec_()
