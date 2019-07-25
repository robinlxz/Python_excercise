"""
This is test version to get (Parts Only) warranty start and end date by service tag

How to use:
1. put service tag in CSV file named Service_tags_to_check.csv,
2. put the file in same folder with this script.
3. in cmd, run 'python check_warranty_v1.py'
4. Wait for it's running (it took around 1 second for each service tag)
5. Check the Warranty_check_result.csv

Created on Fri 13th Oct 2017 @for FO3 GTO
"""

import csv
import requests

####Below is from get_warranty.py
def get_warranty_info(raw_data):
    entilement = raw_data['AssetSummaryResponse']['AssetEntitlementData']
    pow_list = []
    for i in range(0, len(entilement)):
        warranty_info = {}
        warranty_type = entilement[i]['ServiceLevelCode']
        #print warranty_type
        if warranty_type == 'POW':
            warranty_info[warranty_type] = {
                'StartDate':
                    entilement[i]['StartDate'],
                'EndDate':
                    entilement[i]['EndDate'],
                'ServiceLevelDescription':
                    entilement[i]['ServiceLevelDescription']}
            pow_list.append(warranty_info)
    # print warranty_info
    return pow_list

#service_tag = '7vqgh62'

DELL_BASE_URL = "https://api.dell.com/support/assetinfo/v4/"
API_KEY = "1565dd020aa6422800000000f63c7321"



###########Above is from get_warranty.py


#Write the title for each column
with open('Warranty_check_result.csv', 'wb') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Service_tag','Start_date','End_date'])
#
with open('Service_tags_to_check.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        service_tag =', '.join(row)
        url = DELL_BASE_URL + 'getassetsummary/' + service_tag
        payload = {'apikey': API_KEY}

        print service_tag

        if not service_tag == 'VM':
            r = requests.get(url, params=payload)
            raw_data = r.json()
            warranty_info = get_warranty_info(raw_data)
            start_date =  warranty_info[0]['POW']['StartDate']
            start_date = str(start_date[:10])
            #print start_date
            end_date = warranty_info[0]['POW']['EndDate']
            end_date = str(end_date[:10])
        else:
            start_date = 'VM'
            end_date = 'VM'
        #print end_date

        with open('Warranty_check_result.csv', 'ab') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([service_tag,start_date,end_date])

print "POW Warranty date collected in Warranty_check_result.csv"