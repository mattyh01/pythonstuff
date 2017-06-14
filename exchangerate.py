import requests, openpyxl, os, datetime, json

#Retrieve JSON data
exchangeget = requests.get('http://api.fixer.io/latest?base=USD')
ethget = requests.get('https://api.cryptowat.ch/markets/coinbase/ethusd/price')
btcget = requests.get('https://api.cryptowat.ch/markets/coinbase/btcusd/price')

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

ratio = eth / btc

# Current money spent
personal = 756

time = datetime.datetime.now().strftime('%H:%M:%S')

#os.chdir('/Users/holmes/Documents/Personal') #Not needed but useful

wb = openpyxl.load_workbook("/Users/holmes/Documents/Personal/Copy of Personal Finance Sheet.xlsx")

sheet = wb.get_sheet_by_name('BTC+ETH')

try:

	sheet['I12'] = gbp

except:

	print "Write of GBP rate failed."

try:

    sheet['G12'] = eth

except:

	print "Write of current ETH rate failed."

#sheet.title("BTC+ETH")

wb.save("/Users/holmes/Documents/Personal/Copy of Personal Finance Sheet.xlsx")

profit = 4.3125 * (eth * gbp) - personal

print ""
print "############# CRYPTOCURRENCY #############"
print str(time) + ":  GBP Ratio to Dollar:    " + str(gbp)
print str(time) + ":  Current ETH Price ($)   " + str(eth)
print str(time) + ":  Current profit/loss:    " + str(profit)
print str(time) + ":  Current BTC Price ($):  " + str(btc)
print str(time) + ":  Current conversion:     " + str(ratio)
print ""


