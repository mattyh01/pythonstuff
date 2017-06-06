import requests, os, time, json


#Retrieve JSON data
ethget = requests.get('https://api.cryptowat.ch/markets/coinbase/ethusd/price')

#Assigns JSON to text, loads as a dictionary, prints key 'price' in key 'result'
ethstring = ethget.text
price = json.loads(ethstring)
eth = price['result']['price']


while True:

	f = open('ethprices.txt', 'w')
	
	print eth
	f.write(str(eth))	

	if eth < 250 :

        	print "DIPPING!"

	f.close()

	time.sleep(30)
		
