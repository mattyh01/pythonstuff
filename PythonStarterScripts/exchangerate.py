import requests, openpyxl, os, datetime, json, sys

#Retrieve JSON data
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

ratio = eth / btc
personal = 2302.58

#print("No checking at this time. Exiting...")
#sys.exit() # NO CHECKING

# Current money spent

bchowned = 0.363858
btcowned = 0.1017
ethowned = 5.14
omgowned = 19

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
    sheet['E12'] = total
    sheet['E13'] = totalgbp
    sheet['E14'] = profit

except:

	print "Write of current Crypto rates failed."

#sheet.title("BTC+ETH")



wb.save("/Users/holmes/Documents/Personal/Crypto.xlsx")


if len(sys.argv) > 1 and sys.argv[1] == "ratio":

    print ""
    print "############# CRYPTOCURRENCY #############"
    print str(time) + ":  GBP Ratio to Dollar:    " + str(gbp)
    print str(time) + ":  Current ETH Price ($)   " + str(eth)
    print str(time) + ":  Current profit/loss:    " + str(profit)
    print str(time) + ":  Current BTC Price ($):  " + str(btc)
    print str(time) + ":  Current conversion:     " + str(ratio)
    print "Ethereum currently held: " + str(hodl)
    print "Current personal outlay: " + str(personal)
    print "Current cash value: " + str(pca)
    print ""

else:

	print str(time) + ":  Current profit/loss:    " + str(profit)
