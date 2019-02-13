#!/usr/bin/env python

import csv
#import requests
import json


def read_csv(file_name):
    ''' This function read the data by raws in csv, into a list '''
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        list_output = list(reader)

    return list_output

# def main():
#     list_all = read_csv('100_lines.csv')
#     print len(list_all)
#     print list_all[0][7]
#     #for i in range(10):
#     #    print list_all[i][1]
#     print " 'timestamp': 1546790438" in list_all[0]

def getListFromSourceCSV():
    list_071_0107 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/100071_01_07.csv')
    list_071_0108 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/100071_01_08.csv')
    list_072_0107 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/100072_01_07.csv')
    list_072_0108 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/100072_01_08.csv')
    list_836_0107 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/32836_01_07.csv')
    list_836_0108 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/32836_01_08.csv')
    list_837_0107 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/32837_01_07.csv')
    list_837_0108 = read_csv('/Users/linxz/Documents/20190125_server_notification_log/32837_01_08.csv')
#    print len(list_071_0107)
#    print len(list_071_0108)
    fo4mth = []
    fo4mvn = []
    fo4th = []
    fo4vn = []
    for x in list_071_0107:
        if 'timestamp' in x[7]:
            fo4mth.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4mth.append(x[6][14:])
        try:
            int(fo4mth[-1])
        except:
            print 'fo4mth[-1] as %s doesn\'t fit' %fo4mth[-1]

    for x in list_071_0108:
        if 'timestamp' in x[7]:
            fo4mth.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4mth.append(x[6][14:])
        try:
            int(fo4mth[-1])
        except:
            print 'fo4mth[-1] as %s doesn\'t fit' %fo4mth[-1]

    for x in list_072_0107:
        if 'timestamp' in x[7]:
            fo4mvn.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4mvn.append(x[6][14:])
        try:
            int(fo4mvn[-1])
        except:
            print 'fo4mvn[-1] as %s doesn\'t fit' %fo4mvn[-1]

    for x in list_072_0108:
        if 'timestamp' in x[7]:
            fo4mvn.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4mvn.append(x[6][14:])
        try:
            int(fo4mvn[-1])
        except:
            print 'fo4mvn[-1] as %s doesn\'t fit' %fo4mvn[-1]

#below is to read fo4 data record
    for x in list_836_0107:
        if 'timestamp' in x[7]:
            fo4th.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4th.append(x[6][14:])
        try:
            int(fo4th[-1])
        except:
            print 'fo4th[-1] as %s doesn\'t fit' %fo4th[-1]

    for x in list_836_0108:
        if 'timestamp' in x[7]:
            fo4th.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4th.append(x[6][14:])
        try:
            int(fo4th[-1])
        except:
            print 'fo4th[-1] as %s doesn\'t fit' %fo4th[-1]

    for x in list_837_0107:
        if 'timestamp' in x[7]:
            fo4vn.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4vn.append(x[6][14:])
        try:
            int(fo4vn[-1])
        except:
            print 'fo4vn[-1] as %s doesn\'t fit' %fo4vn[-1]

    for x in list_837_0108:
        if 'timestamp' in x[7]:
            fo4vn.append(x[7][14:])
        elif 'timestamp' in x[6]:
            fo4vn.append(x[6][14:])
        try:
            int(fo4vn[-1])
        except:
            print 'fo4vn[-1] as %s doesn\'t fit' %fo4vn[-1]

    #print len(fo4mth)
    #print len(fo4mvn)
    #print len(fo4th)
    #print len(fo4vn)
    return [fo4mth,fo4th,fo4mvn,fo4vn]

def main():
    list_th_record = read_csv('/Users/linxz/Documents/20190125_server_notification_log/gop_log_th.csv')
    list_vn_record = read_csv('/Users/linxz/Documents/20190125_server_notification_log/gop_log_vn.csv')
    #print len(list_th_record)
    #print len(list_vn_record)
    [fo4mth, fo4th, fo4mvn, fo4vn] = getListFromSourceCSV()
    #print len(fo4mth)
    print list_th_record[1][5]
    print len(list_th_record[1])
    for x in list_th_record:
        if x[5] in fo4mth:
            x.append('fo4mth')
        if x[5] in fo4th:
            x.append('fo4th')
        if len(x) == 8:
            print 'x is not found in the record, timestamp is %s, it is the %s line' %(x[5], list_th_record.index(x))
    print len(list_th_record[1])

if __name__ == '__main__':
    main()