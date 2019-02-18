#!/usr/bin/env python

import csv
import requests
import json
from time import sleep
import pygeoip

# Ugly Global varialbe for easily change code
COUNTRY_NAME = 'ID'


def read_csv(file_name):
    ''' This function read the data by raws in csv, into a list '''
    with open(file_name, 'rb') as f:
        reader = csv.reader(f)
        list_output = list(reader)
    # To get rid of the first raw, if it is the title from mongo export
    if list_output[0][0] == '_id':
        list_output = list_output[1:]

    return list_output

def stop_here():
    raw_input('exiting now...')  # for debug
    exit()  # for debug

def write_to_file(list_to_write, file_name):
    '''This function write a list to a csv file'''
    with open(file_name, 'w') as f:
        for item in list_to_write:
            print >> f, item


def main():
    print 'country_name is:', COUNTRY_NAME
    #list_all = read_csv('new_10_lines.csv')
    #list_all = read_csv('/Users/linxz/Documents/IP_filter_FO4TH/FO4_MATCH_IP.csv')
    list_all = read_csv('/Users/linxz/Downloads/FO4_MATCH_IP_log_20190213.csv')

    gi4 = pygeoip.GeoIP('/Users/linxz/Documents/GitHub/Python_excercise/Data/CSV_IP_filter/TonyIP.dat', pygeoip.MEMORY_CACHE)

    res = []
    for i in range(len(list_all)):
        ip_country = gi4.country_code_by_addr(list_all[i][4])
        if ip_country != 'TH':
            print 'progress:', (float(i)/len(list_all))
            res.append(list_all[i] + [ip_country])
    print 'the result csv file have %s lines' %len(res)

    write_to_file(res, 'output_append_with_IP.csv')

if __name__ == '__main__':
    main()
