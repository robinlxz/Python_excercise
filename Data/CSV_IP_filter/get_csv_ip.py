#!/usr/bin/env python

import csv
import requests
import json

def read_csv(file_name):
	''' This function read the data by raws in csv, into a list '''
	with open(file_name, 'rb') as f:
		reader = csv.reader(f)
		list_output = list(reader)
	# To get rid fo the first raw, if it is the title from mongo export
	if list_output[0][0] == '_id':
		list_output = list_output[1:]

	return list_output


def get_geo_frmo_ip(list_ip):
	''' Use the API to get geo info for each IP, store them into list
	Input: a list of IP
	Return: a list contains all dict element return by API for each IP'''
	L = []
	for ip in list_ip:
	#	ip = '184.22.218.93'
		prefix = 'http://api.db-ip.com/v2/free/'
		url = prefix + str(ip)
		print url
		r = requests.get(url).text
		try:
			r_dict = json.loads(r)
		except:
			print 'Fail to convert r to r_dict, r is %s' %r
		L.append(r_dict)
	return L



def main():
	list_all = read_csv('1000_lines.csv')
	#print list_all

	# Get IP 
	## But this step de-couple the ip with the original record, so is only for test.
	## In final application, may record the index for which line, or use list_all[i][4] directly
	list_ip = [i[4] for i in list_all]
	L_json = get_geo_frmo_ip(list_ip)
	print L_json

	# filter_only_ID_IP
	L_id_json = []
	for i in L_json:
		if i['countryCode'] == 'ID':
			L_id_json.append(i)
	print 'there are %s sets of data collected' %len(L_id_json)


if __name__ == '__main__':
	main()


