#!/usr/bin/env python

import csv
#import requests
import json

FILEPATH='/Users/linxz/Documents/20190125_server_notification_log/'

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
    list_071_0107 = read_csv(FILEPATH+'100071_01_07.csv')

 #   print list_071_0107[1][5][9:]
 #   exit()


    list_071_0108 = read_csv(FILEPATH+'100071_01_08.csv')
    list_072_0107 = read_csv(FILEPATH+'100072_01_07.csv')
    list_072_0108 = read_csv(FILEPATH+'100072_01_08.csv')
    list_836_0107 = read_csv(FILEPATH+'32836_01_07.csv')
    list_836_0108 = read_csv(FILEPATH+'32836_01_08.csv')
    list_837_0107 = read_csv(FILEPATH+'32837_01_07.csv')
    list_837_0108 = read_csv(FILEPATH+'32837_01_08.csv')
    #print len(list_071_0107)
    #print len(list_071_0108)
    fo4mth = []
    fo4mvn = []
    fo4th = []
    fo4vn = []
    def getTimestampFromList(res, input_list):
        for x in input_list:
            if 'timestamp' in x[7]:
                if 'uid' in x[6]:
                    res.append(('uid:'+x[6][9:],'ts:'+x[7][14:]))
            elif 'timestamp' in x[6]: #Because some data have misplacement
                if 'uid' in x[5]:
                    res.append(('uid:'+x[5][9:],'ts:'+x[6][14:]))
            try:
                len(res[-1]) == 2
            except:
                print 'res[-1] as %s doesn\'t fit' % res[-1]
                return False
        return True

    if getTimestampFromList(fo4mth, list_071_0107) and getTimestampFromList(fo4mth, list_071_0108):
        print 'fo4mth timestamp collected, in total %s lines' %len(fo4mth)
    if getTimestampFromList(fo4mvn, list_072_0107) and getTimestampFromList(fo4mvn, list_072_0108):
        print 'fo4mvn timestamp collected, in total %s lines' %len(fo4mvn)
    if getTimestampFromList(fo4th, list_836_0107) and getTimestampFromList(fo4th, list_836_0108):
        print 'fo4th timestamp collected, in total %s lines' %len(fo4th)
    if getTimestampFromList(fo4vn, list_837_0107) and getTimestampFromList(fo4vn, list_837_0108):
        print 'fo4vn timestamp collected, in total %s lines' %len(fo4vn)

    # print len(fo4mth)
    # print len(fo4mvn)
    # print len(fo4th)
    # print len(fo4vn)
    return [fo4mth, fo4th, fo4mvn, fo4vn]

def matchToAppend(list_record, match_list, append_str):
    for x in list_record:
        #print ('uid:'+x[0],'ts:'+x[5])
        #print match_list[1]
        if ('uid:'+x[0],'ts:'+x[5]) in match_list:
            x.append(append_str)
        #else:
        #    print 'x is not found in the' + append_str + 'record, timestamp is %s, it is the %s line' %(x[5], list_record.index(x))
    print len(list_record)
    return list_record



def main():
    list_th_record = read_csv(FILEPATH+'gop_log_th.csv')
    list_vn_record = read_csv(FILEPATH+'gop_log_vn.csv')

    [fo4mth, fo4th, fo4mvn, fo4vn] = getListFromSourceCSV()

    list_th_record = matchToAppend(list_th_record, fo4mth, 'fo4mth')
    list_th_record = matchToAppend(list_th_record, fo4th, 'fo4th')
    list_vn_record = matchToAppend(list_vn_record, fo4mvn, 'fo4mvn')
    list_vn_record = matchToAppend(list_vn_record, fo4vn, 'fo4vn')
    # for x in list_th_record:
    #     print ('uid:'+x[0],'ts:'+x[5])
    #     if ('uid:'+x[0],'ts:'+x[5]) in fo4mth:
    #         x.append('fo4mth')
    #     if ('uid:'+x[0],'ts:'+x[5]) in fo4th:
    #         x.append('fo4th')
    #     if len(x) == 8:
    #         print 'x is not found in the TH record, timestamp is %s, it is the %s line' %(x[5], list_th_record.index(x))
    # print len(list_th_record)

    # for x in list_vn_record:
    #     if x[5] in fo4mvn:
    #         x.append('fo4mvn')
    #     if x[5] in fo4vn:
    #         x.append('fo4vn')
    #     if len(x) == 8:
    #         print 'x is not found in the VN record, timestamp is %s, it is the %s line' %(x[5], list_vn_record.index(x))
    # print len(list_vn_record)

    '''Output result to csv'''
    with open(FILEPATH+'th_output.csv','wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        for item in list_th_record:
            try:
                wr.writerow(item)
            except:
                print "Fail to write to file"
                break

    with open(FILEPATH+'vn_output.csv','wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        for item in list_vn_record:
            try:
                wr.writerow(item)
            except:
                print "Fail to write to file"
                break

if __name__ == '__main__':
    main()