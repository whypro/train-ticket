# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PyQt4 import QtGui, QtCore
import sys
import datetime
from ui_querywindow import Ui_QueryWindow
from train import Query


class QueryWindow(QtGui.QMainWindow, Ui_QueryWindow):
    def __init__(self):
        super(QueryWindow, self).__init__()
        self.setupUi(self)
        self.trainDateEdit.setDate(datetime.datetime.now())
        self.queryButton.clicked.connect(self.query)

    def query(self):
        query = Query(
            self.fromStationNameEdit.text(), self.toStationNameEdit.text(),
            self.trainDateEdit.text(), self.studentCheckbox.isChecked()
        )
        trains = query.query_trains()['datas']

        # 设置表头
        tableHeaders = (
            '车次', '出发站', '到达站', '出发时间', '到达时间', '历时',
            '商务座', '特等座', '一等座', '二等座', '高级软卧', '软卧',
            '硬卧', '软座', '硬座', '无座', '备注',
        )
        self.tableWidget.setColumnCount(len(tableHeaders))
        self.tableWidget.setHorizontalHeaderLabels(tableHeaders)

        self.tableWidget.setRowCount(len(trains))
        for (row, train) in enumerate(trains):
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

        # 重设列宽
        # self.tableWidget.resizeColumnsToContents()
        # self.tableWidget.resizeRowsToContents()

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    window = QueryWindow()
    window.show()
    app.exec_()
