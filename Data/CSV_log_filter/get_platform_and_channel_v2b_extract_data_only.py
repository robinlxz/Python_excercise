#!/usr/bin/env python
import csv
from datetime import datetime

'''
#xminds
1. import all 10071/72,32837/87 csv
2. take out 10071[i][7] values into a list
3. convert to CSV and import Compare_GOP_CSLOG_20190107_20190108 to a list.
list_original
4.
if " 'timestamp': "+str(list_original[i][6]) in 10071
list_original[i].append(fo4m)
if the pair is in 32837
list_original[i].append(fo4)
else:
	print 'error, %s not exist' %list_original[i][6]
5. export list_original
_______________________
1. make a list consist of tuple (uid, timestamp)
2. from csv, check if it is in the tuple
'''

FILEPAVN='/Users/linxz/Documents/20190416_server_notification_log/'
FILE1 = '100072_04_18.csv'
FILE2 = '100072_04_19.csv'
FILE3 = '100072_01_07.csv'
FILE4 = '100072_01_08.csv'

def read_csv(file_name):
    ''' This function read the data by raws in csv, output into a list '''
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        list_output = list(reader)
    return list_output

def getListFromSourceCSV():
    list_071_0107 = read_csv(FILEPAVN + FILE1)
    list_071_0108 = read_csv(FILEPAVN + FILE2)
    #list_072_0107 = read_csv(FILEPAVN + FILE3)
    #list_072_0108 = read_csv(FILEPAVN + FILE4)
    list_836_0107 = read_csv(FILEPAVN+'32837_04_18.csv')
    list_836_0108 = read_csv(FILEPAVN+'32837_04_19.csv')
    #list_837_0107 = read_csv(FILEPAVN+'32837_01_07.csv')
    #list_837_0108 = read_csv(FILEPAVN+'32837_01_08.csv')
    fo4mth = {}
    fo4mvn = {}
    fo4th = {}
    fo4vn = {}
    def getTimestampFromList(res, input_list):
        print input_list[0][14][18:]
        # print input_list[1][16]
        exit()
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

    def getTimestampFromList(res_dict, input_list, label):
        print input_list[0][14][18:]
        print input_list[1][13][18:]
 #       exit()
        assert type(label) == str

        #platformDict = {'0':'testios', '1':'testaos', '2':'testother', '3':'test3', '4':'test4'}

        for x in input_list:
            if 'timestamp' in x[7] and 'uid' in x[6]:
                #print ('uid:'+x[6][9:],'ts:'+x[7][14:])
                #print input_list.index(x)
                res_dict[('uid:'+x[6][9:],'ts:'+x[7][14:])] = (label, 'ch:'+x[14][18:])
            elif 'timestamp' in x[6] and 'uid' in x[5]: #Because some data have misplacement
                #print ('uid:' + x[5][9:], 'ts:' + x[6][14:])
                #print input_list.index(x)
                res_dict[(('uid:'+x[5][9:],'ts:'+x[6][14:]))] = (label,'ch:'+x[13][18:])
            else:
                print 'this line of data as doesn\'t fit. \n%s\n' %x
                return False
        print 'now res_dict as the length', len(res_dict)
        return True

    if getTimestampFromList(fo4mth, list_071_0107, 'fo4mth') and getTimestampFromList(fo4mth, list_071_0108, 'fo4mth'):
        print 'fo4mth timestamp collected, in total %s lines' %len(fo4mth)
    #if getTimestampFromList(fo4mvn, list_072_0107, 'fo4mvn') and getTimestampFromList(fo4mvn, list_072_0108, 'fo4mvn'):
    #    print 'fo4mvn timestamp collected, in total %s lines' %len(fo4mvn)
    if getTimestampFromList(fo4th, list_836_0107, 'fo4th') and getTimestampFromList(fo4th, list_836_0108, 'fo4th'):
        print 'fo4th timestamp collected, in total %s lines' %len(fo4th)
    #if getTimestampFromList(fo4vn, list_837_0107, 'fo4vn') and getTimestampFromList(fo4vn, list_837_0108, 'fo4vn'):
    #    print 'fo4vn timestamp collected, in total %s lines' %len(fo4vn)
    return [fo4mth, fo4th, fo4mvn, fo4vn]


def matchToAppend(list_record, match_list, append_str):
    #This is to matchList
    for x in list_record:
        #print ('uid:'+x[0],'ts:'+x[5])
        #print match_list[1]
        if ('uid:'+x[0],'ts:'+x[5]) in match_list:
            x.append(append_str)
        else:
            print 'x is not found in the' + append_str + 'record, timestamp is %s, it is the %s line' %(x[5], list_record.index(x))
    print len(list_record)
    return list_record

def matchDictToAppend(list_record, match_dict, append_str):
    '''For each item in list_record, append its value in the match_dict'''
    assert type(list_record) == list
    assert type(match_dict) == dict
    for x in list_record:
        if ('uid:'+x[0],'ts:'+x[5]) in match_dict.keys():
            x.append(match_dict[('uid:'+x[0],'ts:'+x[5])][0])
            print match_dict[('uid:' + x[0], 'ts:' + x[5])][1][3:]
            x.append(match_dict[('uid:' + x[0], 'ts:' + x[5])][1][3:])
        # else:
        #     print 'x is not found in the' + append_str + 'record, timestamp is %s, it is the %s line' %(x[5], list_record.index(x))
    print len(list_record)
    return list_record

def main():
    list_100072_04_18 = read_csv(FILEPAVN + '100072_04_18.csv')
    list_100072_04_19 = read_csv(FILEPAVN + '100072_04_19.csv')
    list_100072_04_20 = read_csv(FILEPAVN + '100072_04_20.csv')
    list_100072_04_21 = read_csv(FILEPAVN + '100072_04_21.csv')
    list_32837_04_18 = read_csv(FILEPAVN + '32837_04_18.csv')
    list_32837_04_19 = read_csv(FILEPAVN + '32837_04_19.csv')
    list_32837_04_20 = read_csv(FILEPAVN + '32837_04_20.csv')
    list_32837_04_21 = read_csv(FILEPAVN + '32837_04_21.csv')

    output_100072_04_18 = []
    output_100072_04_18.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_100072_04_18:
        if 'timestamp' in row[14]:
            a = 0
            output_100072_04_18.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])
        elif 'timestamp' in row[13]:
            a = -1
            output_100072_04_18.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])

    output_100072_04_19 = []
    output_100072_04_19.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_100072_04_19:
        if 'timestamp' in row[14]:
            a = 0
            output_100072_04_19.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])
        elif 'timestamp' in row[13]:
            a = -1
            output_100072_04_19.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])

    output_100072_04_20 = []
    output_100072_04_20.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_100072_04_20:
        if 'timestamp' in row[14]:
            a = 0
            output_100072_04_20.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])
        elif 'timestamp' in row[13]:
            a = -1
            output_100072_04_20.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])

    output_100072_04_21 = []
    output_100072_04_21.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_100072_04_21:
        if 'timestamp' in row[14]:
            a = 0
            output_100072_04_21.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])
        elif 'timestamp' in row[13]:
            a = -1
            output_100072_04_21.append([row[8+a][9:], '100072', row[15+a], row[24+a], row[11+a], datetime.utcfromtimestamp(int(row[14+a][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4M VN'])

    print len(output_100072_04_18), len(output_100072_04_19), len(output_100072_04_20), len(output_100072_04_21)

    output_32837_04_18 = []
    output_32837_04_18.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_32837_04_18:
        if 'timestamp' in row[13]:
            output_32837_04_18.append([row[7][9:], '32837', row[14], row[23], row[10], datetime.utcfromtimestamp(int(row[13][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4 VN'])
        else:
            print "The method need to be adjusted!"
            print row[13]

    output_32837_04_19 = []
    output_32837_04_19.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_32837_04_19:
        if 'timestamp' in row[13]:
            output_32837_04_19.append([row[7][9:], '32837', row[14], row[23], row[10], datetime.utcfromtimestamp(int(row[13][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4 VN'])
        else:
            print "The method need to be adjusted!"
            print row[13]

    output_32837_04_20 = []
    output_32837_04_20.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_32837_04_20:
        if 'timestamp' in row[13]:
            output_32837_04_20.append([row[7][9:], '32837', row[14], row[23], row[10], datetime.utcfromtimestamp(int(row[13][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4 VN'])
        else:
            print "The method need to be adjusted!"
            print row[13]

    output_32837_04_21 = []
    output_32837_04_21.append(
        ['garena_uid', 'aid', 'currency', 'currency_amount', 'point_amount', 'datetime (GMT+0)', 'platform'])
    for row in list_32837_04_21:
        if 'timestamp' in row[13]:
            output_32837_04_21.append([row[7][9:], '32837', row[14], row[23], row[10], datetime.utcfromtimestamp(int(row[13][-10:])).strftime('%Y-%m-%d %H:%M:%S'), 'platform: FO4 VN'])
        else:
            print "The method need to be adjusted!"
            print row[13]

    print len(output_100072_04_18), len(output_100072_04_19), len(output_100072_04_20), len(output_100072_04_21), len(output_32837_04_18), len(output_32837_04_19), len(output_32837_04_20), len(output_32837_04_21)

    with open(FILEPAVN+'100072_04_18_output.csv','wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        for item in output_100072_04_18:
            try:
                wr.writerow(item)
            except:
                print "Fail to write to file"
                break
        for item in output_100072_04_19:
            wr.writerow(item)
        for item in output_100072_04_20:
            wr.writerow(item)
        for item in output_100072_04_21:
            wr.writerow(item)
        for item in output_32837_04_18:
            wr.writerow(item)
        for item in output_32837_04_19:
            wr.writerow(item)
        for item in output_32837_04_20:
            wr.writerow(item)
        for item in output_32837_04_21:
            wr.writerow(item)

if __name__ == '__main__':
    main()