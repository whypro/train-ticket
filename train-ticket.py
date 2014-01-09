# -*- coding: utf-8 -*-
# Python 2.7
# PyQt 4
from __future__ import unicode_literals, print_function
import json
import re
from urllib import urlencode
from urllib2 import urlopen
import sys


def get_data(url):
    u = urlopen(url)
    data = u.read()
    try:
        content = data.decode('utf-8')
    except UnicodeDecodeError:
        content = data.decode('gbk', 'ignore')
    return content


class Query(object):
    station_names_uri = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js'
    query_train_url = 'https://kyfw.12306.cn/otn/lcxxcx/query?'

    def __init__(self, from_station_name, to_station_name, train_date, is_student=False):
        self.from_station_name = from_station_name
        self.to_station_name = to_station_name
        self.train_date = train_date
        self.is_student = is_student

    def query_trains(self):
        station_names_content = get_data(self.station_names_uri)
        from_station_telecode = re.findall('%s\|([^|]+)' % self.from_station_name, station_names_content)[0]
        to_station_telecode = re.findall('%s\|([^|]+)' % self.to_station_name, station_names_content)[0]

        query_train_data = [
            ('purpose_codes', '0X00' if self.is_student else 'ADULT'),
            ('queryDate', self.train_date),
            ('from_station', from_station_telecode),
            ('to_station', to_station_telecode),
        ]   # 此处用 list 而不是 dict，是因为 list 是有序的

        full_url = self.query_train_url + urlencode(query_train_data)
        # print(full_url)
        result_content = get_data(full_url)
        return json.loads(result_content)['data']


class Ticket(object):
    query_price_url = 'https://kyfw.12306.cn/otn/leftTicket/queryTicketPrice?'

    def __init__(self, train_no, from_station_no, to_station_no, seat_types, train_date):
        self.train_no = train_no
        self.from_station_no = from_station_no
        self.to_station_no = to_station_no
        self.seat_types = seat_types
        self.train_date = train_date

    def query_price(self):
        query_price_data = [
            ('train_no', self.train_no),
            ('from_station_no', self.from_station_no),
            ('to_station_no', self.to_station_no),
            ('seat_types', self.seat_types),
            ('train_date', self.train_date),
        ]
        full_url = self.query_price_url + urlencode(query_price_data)
        # print full_url
        result_content = get_data(full_url)
        return json.loads(result_content)['data']

if __name__ == '__main__':

    # from_station_name = '西安'    # IN
    # to_station_name = '杭州'      # IN
    # train_date = '2014-01-12'       # IN

    # 1. 输入出发站名
    from_station_name = raw_input('请输入出发站名（如：西安）：').decode(sys.stdin.encoding)
    # 2. 输入到达站名
    to_station_name = raw_input('请输入到达名（如：杭州）：').decode(sys.stdin.encoding)
    # 3. 输入日期
    train_date = raw_input('请输入日期（如：2014-01-31）：').decode(sys.stdin.encoding)

    query = Query(from_station_name, to_station_name, train_date)
    trains = query.query_trains()

    print('{0:<8}{1:<8}{2:<8}{3:<8}{4:<8}{5:<8}{6:<8}'.format(
        '车次', '出发时间', '历时', '软卧', '硬卧', '硬座', '无座'
    ))
    for t in trains['datas']:
        print('{0:<8}{1:<8}{2:<8}{3:<8}{4:<8}{5:<8}{6:<8}'.format(
            t['station_train_code'], t['start_time'], t['lishi'],
            t['rw_num'], t['yw_num'], t['yz_num'], t['wz_num']
        ))

    # 4. 选择车次
    station_train_code = raw_input('请选择车次（如：Z88）：').decode(sys.stdin.encoding)

    train_no = None
    from_station_no = None
    to_station_no = None
    seat_types = None
    for t in trains['datas']:
        if station_train_code in t['station_train_code']:
            train_no = t['train_no']
            from_station_no = t['from_station_no']
            to_station_no = t['to_station_no']
            seat_types = t['seat_types']

    if train_no:
        ticket = Ticket(train_no, from_station_no, to_station_no, seat_types, train_date)
        price = ticket.query_price()
        print('{0:<8}{1:<8}{2:<8}{3:<8}'.format('软卧', '硬卧', '硬座', '无座'))
        print('{0:<8}{1:<8}{2:<8}{3:<8}'.format(price.get('A4', '--'), price.get('A3', '--'), price.get('A1', '--'), price.get('WZ', '--')))
    else:
        print('未找到该车次')









