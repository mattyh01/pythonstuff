import requests, openpyxl, os, datetime, json, sys

from exchange_info import *

print "Please ensure exchange_info.py is filled with your personal details first."

try:
	exchangeget = requests.get('http://api.fixer.io/latest?base=USD')
	ethget = requests.get('https://api.cryptowat.ch/markets/coinbase/ethusd/price')
	btcget = requests.get('https://api.cryptowat.ch/markets/coinbase/btcusd/price')
	bchget = requests.get('https://api.cryptowat.ch/markets/bitfinex/bchusd/price')
	omgget = requests.get('https://api.cryptowat.ch/markets/bitfinex/omgusd/price')

except:
	print "Issue retrieving currency data - potentially down to too many requests"

	#Assigns JSON to text, loads as a dictionary, prints key 'price' in key 'result'
ethstring = ethget.text
price = json.loads(ethstring)
eth = price['result']['price']

	#Same as above, but key in 'GBP' in key 'rates'
string = exchangeget.text
currencylist = json.loads(string)
gbp = currencylist['rates']['GBP']

	#BTC Json
btcstring = btcget.text
btcprice = json.loads(btcstring)
btc = btcprice['result']['price']

bchstring = bchget.text
price = json.loads(bchstring)
bch = price['result']['price']

omgstring = omgget.text
price = json.loads(omgstring)
omg = price['result']['price']

# Current money spent

bchtotal = bch * bchowned
btctotal = btc * btcowned
ethtotal = eth * ethowned
omgtotal = omg * omgowned

time = datetime.datetime.now().strftime('%H:%M:%S')

total = btctotal + bchtotal + ethtotal + omgtotal
totalgbp = total * gbp
profit = totalgbp - personal

#os.chdir('/Users/holmes/Documents/Personal') #Not needed but useful

wb = openpyxl.load_workbook("/Users/holmes/Documents/Personal/Crypto.xlsx")


sheet = wb.get_sheet_by_name('Info')


try:

	sheet['E4'] = gbp

except:

	print "Write of GBP rate failed."

try:
    sheet['D8'] = bch
    sheet['D9'] = eth
    sheet['D10'] = btc
    sheet['D11'] = omg
    #sheet['E12'] = total
    #sheet['E13'] = totalgbp

except:

	print "Write of current Crypto rates failed."

#sheet.title("BTC+ETH")



wb.save("/Users/holmes/Documents/Personal/Crypto.xlsx")


if len(sys.argv) > 1 and sys.argv[1] == "-l":

    print ""
    print "############# CRYPTOCURRENCY #############"
    print "Current personal outlay: " + str(personal)
    print ""
    print str(time) + ":  GBP Ratio to Dollar:    " + str(gbp)
    print str(time) + ":  Current ETH Price ($)   " + str(eth)
    print str(time) + ":  Current BTC Price ($):  " + str(btc)
    print str(time) + ":  Current BCH Price ($):  " + str(bch)
    print str(time) + ":  Current OMG Price ($):  " + str(omg)
    print str(time) + ":  Current profit/loss:    " + str(profit)
    print ""

elif len(sys.argv) > 1 and sys.argv[1] == '-c':
	print "Change the amount of Cryptocurrency you own."
	eth = raw_input("How much Eth do you now have?")

elif len(sys.argv) > 1 and sys.argv[1] == '-1':
	print str(time) + ":  Current profit/loss:    " + str(profit)

elif len(sys.argv) < 2 :
	print ""
	print "---------------------------------------------"
	print "Pick one of the following arguments"
	print "-l - Displays information on all Crypto prices"
	print "-1 - Shows just the profit/loss margin"
	print "-c - Change amount of crypto you own"
	print "-d - Write to database (Multiple argument option, sysopts/case?)"
	print "---------------------------------------------"

else:
	print "Incorrect argument specified, exiting"
