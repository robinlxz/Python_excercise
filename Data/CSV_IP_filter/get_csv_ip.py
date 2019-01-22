#!/usr/bin/env python

import csv
import requests
import json

def read_csv(file_name):
	''' This function read the data by raws in csv, into a list '''
	with open(file_name, 'rb') as f:
		reader = csv.reader(f)
		list_output = list(reader)
	# To get rid of the first raw, if it is the title from mongo export
	if list_output[0][0] == '_id':
		list_output = list_output[1:]

	return list_output


def get_geo_from_ip(list_ip):
	''' Use the API to get geo info for each IP, store them into list
	Input: a list of IP
	Return: a list contains all dict element return by API for each IP'''
	L = []
	prefix = 'http://api.db-ip.com/v2/free/'
	for ip in list_ip:
	#	ip = '184.22.218.93'
		url = prefix + str(ip)
		print url
		r = requests.get(url).text
		try:
			r_dict = json.loads(r)
		except:
			print 'Fail to convert r to r_dict, r is %s' %r
		L.append(r_dict)
	return L

def get_geo_multiple_ip(list_ip):
	'''To call API only once, with all the IP in the list argument'''
	prefix = 'http://api.db-ip.com/v2/free/'
	string_ip = ','.join(list_ip)
	#print string_ip
	url = prefix + string_ip
	#print 'url is', url
	r = requests.get(url).text
	#print 'respond is', r
	try:
		r_dict = json.loads(r)
	except:
		print 'Fail to convert r to r_dict, r is %s' %r
	#print r_dict
	return r_dict


def filter_only_ID_IP(L_json):
	L_id_json = []
	for i in L_json:
		if i['countryCode'] == 'ID':
			L_id_json.append(i)
			print 'This data belong to ID \n', i, '\n' 
	print 'there are %s sets of data collected' %len(L_id_json)
	return L_id_json

def isID_IP_single(s_json):
	try:
		if s_json['countryCode'] == 'ID':
			return True
		else:
			return False
	except:
		print 'now type of s_json is:', type(s_json)
		print 's_json is:', s_json
		return False

def main():
	list_all = read_csv('100_lines.csv')
	#print list_all

	# Get IP 
	## But this step de-couple the ip with the original record, so is only for test.
	## In final application, may record the index for which line, or use list_all[i][4] directly
	list_ip = [i[4] for i in list_all]
	print 'There are %d of IPs from csv.' %len(list_ip)
	#L_json = get_geo_from_ip(list_ip)

	#Due to multiple ip is restricted to 32 in the API for each call, separate the list
	n = 32
	l_ip_group = [list_ip[i:i + n] for i in xrange(0, len(list_ip), n)]
	#print L_json
	#print 'l_ip_group is', l_ip_group
	print 'There are %d groups of IP, other then last one, each contains %d IPs.' %(len(l_ip_group), n)
	l_id = []
	i = 0
	for l_ip in l_ip_group:
		#print 'l_ip is:', l_ip
		l_dict = get_geo_multiple_ip(l_ip) #this failed
		#print 'l_dict is:', l_dict
		## l_id is a list of dicts, each dicts contains 32 key pairs
		## each pair is{IP: {return from API}}
		l_id.append(l_dict) 
		#print 'l_id is:', l_id
		
		#print 'i for l_id(i) now =',i
		#print 'length for l_id now =',len(l_id)
	#print l_id
		for p in l_id[i]:
			#print 'l_id[0][i] is: ', l_id[0][i]
			#print 'type of l_id[0][i] is:', type(l_id[0][i])
			if isID_IP_single(l_id[i][p]):
				print 'This Data from ip ##', p, '##belong to ID \n', l_id[i][p], '\n'
		i += 1

if __name__ == '__main__':
	main()


