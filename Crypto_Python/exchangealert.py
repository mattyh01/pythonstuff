import requests, os, time, json, smtplib

from secrets import email_pass

email="mattyh03@gmail.com"

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.login(email, email_pass)

#Retrieve JSON data
ethget = requests.get('https://api.cryptowat.ch/markets/coinbase/ethusd/price')
btcget = requests.get('https://api.cryptowat.ch/markets/coinbase/btcusd/price')
#Assigns JSON to text, loads as a dictionary, prints key 'price' in key 'result'
ethstring = ethget.text
price = json.loads(ethstring)
eth = price['result']['price']

btcstring = btcget.text
btcprice = json.loads(btcstring)
btc = btcprice['result']['price']

# Define e-mail here

FROM = email
TO = 'mholmes01@btinternet.com'
SUBJECT = ""
MESSAGE = ""

#with open('names.txt', 'r') as open_file:

while True:
	with open('ethprices.txt', 'a') as f:
		f.write(str(eth) + "\n")
	with open('btcprices.txt', 'a') as ff:
		ff.write(str(btc) + "\n")

	# Prints value inside variable eth

	if eth > 400 :

		SUBJECT = "ETH above 400!"
		MESSAGE = "ETH above 400 - Moon! Moon!"
		server.sendmail(FROM, TO, SUBJECT, MESSAGE)


	elif eth < 250 :

		SUBJECT = "ETH below 250!"
		MESSAGE = "ETH below 250 - D'oh!"
		server.sendmail(FROM, TO, SUBJECT, MESSAGE)


	elif btc > 6500 :

		SUBJECT = "ETH above 6500!"
		MESSAGE = "BTC above 6500 - Moon! Moon!"
		server.sendmail(FROM, TO, SUBJECT, MESSAGE)

	elif btc < 4000 :

		SUBJECT = "ETH below 4000!"
		MESSAGE = "BTC below 4000 - D'oh!"
		server.sendmail(FROM, TO, SUBJECT, MESSAGE)

	f.close()
	ff.close()

	time.sleep(10) # 3 for debug, 120 for live running
