#!/usr/bin/env python

import csv
import requests
import json
from time import sleep
import pygeoip

#Ugly Global varialbe for easily change code
country_name = 'MY'

def read_csv(file_name):
	''' This function read the data by raws in csv, into a list '''
	with open(file_name, 'rb') as f:
		reader = csv.reader(f)
		list_output = list(reader)
	# To get rid of the first raw, if it is the title from mongo export
	if list_output[0][0] == '_id':
		list_output = list_output[1:]

	return list_output

#This is get ip by a free url API, has limits on calling times
def get_geo_from_ip(list_ip): #For online API method only
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

#This is get ip by a free url API, has limits on calling times
def get_geo_multiple_ip(list_ip): #For online API method only
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


def filter_only_ID_IP(L_json): #For online API method only
	L_id_json = []
	for i in L_json:
		if i['countryCode'] == country_name:
			L_id_json.append(i)
			print 'This data belong to ID \n', i, '\n' 
	print 'there are %s sets of data collected' %len(L_id_json)
	return L_id_json

def stop_here():
	raw_input('exiting now...') #for debug
	exit() #for debug

def find_ID_IP_by_API(l_ip_group): #This part of code is only copy from main, cannot use
	l_id = []
	i = 0
	for l_ip in l_ip_group:
		#print 'l_ip is:', l_ip
		l_dict = get_geo_multiple_ip(l_ip)

		#print 'l_dict is:', l_dict
		## l_id is a list of dicts, each dicts contains 32 key pairs
		## each pair is{IP: {return from API}}
		l_id.append(l_dict) 		
		#print 'i for l_id(i) now =',i
		#print 'length for l_id now =',len(l_id)
	#print l_id
		for p in l_id[i]:
			#print 'l_id[0][i] is: ', l_id[0][i]
			#print 'type of l_id[0][i] is:', type(l_id[0][i])
			if isID_IP_single(l_id[i][p]):
				print 'This Data from ip ##', p, '##belong to ID \n', l_id[i][p], '\n'
		i += 1
		sleep(1) #To prevent API response: OVER_QUERY_LIMIT
	return l_id	

def isID_IP_single(s_json): #For online API method only
	try:
#		if s_json['countryCode'] == 'ID':
		if s_json['countryCode'] == country_name:
			return True
		else:
			return False
	except:
		print 'now type of s_json is:', type(s_json)
		print 's_json is:', s_json
		stop_here()
		return False

def write_to_file(list_to_write,file_name):
	'''This function write a list to a csv file'''
	with open(file_name, 'w') as f:
	    for item in list_to_write:
	        print >> f, item

def main():
	print 'country_name is:', country_name
	#list_all = read_csv('10000_lines.csv')
	list_all = read_csv('/Users/linxz/Documents/IP_filter_FO4TH/FO4_MATCH_IP.csv')

	# Get IP 
	## But this step de-couple the ip with the original record, so is only for test.
	## In final application, may record the index for which line, or use list_all[i][4] directly
	list_ip = [i[4] for i in list_all]
	print 'There are %d of records from csv.' %len(list_ip)
	set_ip = set(list_ip)
	print 'There are %d of uniq IPs from csv.' %len(set_ip)
	#L_json = get_geo_from_ip(list_ip)

	#Use geoip to get country for each IP, append to the last of list_all
	gi4 = pygeoip.GeoIP('/Users/linxz/Documents/GitHub/Python_excercise/Data/CSV_IP_filter/TonyIP.dat', pygeoip.MEMORY_CACHE)
	ip_country_dict = {}	
	#Here I put selected country IP into dict only
	for ip in list_ip:
		if gi4.country_code_by_addr(ip) == country_name:
			ip_country_dict[ip]=gi4.country_code_by_addr(ip)
	print ip_country_dict
	
	#Here I collect the only the IP out
	ip_country_list = ip_country_dict.keys()
	print ip_country_list

	write_to_file(ip_country_list,'IP_out_put_record.csv')

	#Take the original record out
	result_list = []
	for record in list_all:
		if record[4] in ip_country_list:
			result_list.append(record)

	write_to_file(result_list,'Match_out_put_record.csv')

if __name__ == '__main__':
	main()


