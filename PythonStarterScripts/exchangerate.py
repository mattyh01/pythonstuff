import requests, openpyxl, os, datetime, json, sys

from exchange_info import *

print "Please ensure exchange_info.py is filled with your personal details first."

time = datetime.datetime.now().strftime('%H:%M:%S')

try:
	exchangeget = requests.get('http://api.fixer.io/latest?base=USD')
	ethget = requests.get('https://api.cryptowat.ch/markets/coinbase/ethusd/price')
	btcget = requests.get('https://api.cryptowat.ch/markets/coinbase/btcusd/price')
	bchget = requests.get('https://api.cryptowat.ch/markets/bitfinex/bchusd/price')
	omgget = requests.get('https://api.cryptowat.ch/markets/bitfinex/omgusd/price')

except:
	print "Issue retrieving currency data - potentially down to too many requests"

	#Assigns JSON to text, loads as a dictionary, prints key 'price' in key 'result'

class workStuff:
	def __init__(self):
 		self.bchowned = bchowned
		self.btcowned = btcowned
		self.ethowned = ethowned
		self.omgowned = omgowned
		self.personal = personal

	def workProcessing(self):
		self.ethstring = ethget.text
		self.price = json.loads(self.ethstring)
		self.eth = self.price['result']['price']

		#Same as above, but key in 'GBP' in key 'rates'
		self.string = exchangeget.text
		self.currencylist = json.loads(self.string)
		self.gbp = self.currencylist['rates']['GBP']

		#BTC Json
		self.btcstring = btcget.text
		self.btcprice = json.loads(self.btcstring)
		self.btc = self.btcprice['result']['price']

                self.ratio = self.eth / self.btc

		self.bchstring = bchget.text
		self.price = json.loads(self.bchstring)
		self.bch = self.price['result']['price']

		self.omgstring = omgget.text
		self.price = json.loads(self.omgstring)
		self.omg = self.price['result']['price']

		# Current money spent
		self.bchtotal = self.bch * self.bchowned
		self.btctotal = self.btc * self.btcowned
		self.ethtotal = self.eth * self.ethowned
		self.omgtotal = self.omg * self.omgowned

		self.total = self.btctotal + self.bchtotal + self.ethtotal + self.omgtotal
		self.totalgbp = self.total * self.gbp
		self.profit = self.totalgbp - self.personal

	def changeValues(self):
		self.ethowned = float(raw_input("How much ETH do you own? "))
		self.btcowned = float(raw_input("How much BTC do you own? "))
		self.bchowned = float(raw_input("How much BCH do you own? "))
		self.omgowned = float(raw_input("How much OMG do you own? "))
		w.workProcessing()
		oneLiner()

w = workStuff()
w.workProcessing()

def oneLiner():
	print str(time) + ":  Current profit/loss:    " + str(w.profit)

#Write to DB Function
def writetoDB():
	print "Writing to Database..."
#os.chdir('/Users/holmes/Documents/Personal') #Not needed but useful

def excelWrite():

	wb = openpyxl.load_workbook("/Users/holmes/Documents/Personal/Crypto.xlsx")
	sheet = wb.get_sheet_by_name('Info')

	try:
		sheet['E4'] = w.gbp
		print "Writing GBP conversion rate..."
	except:
		print "Write of GBP rate failed."

	try:
	    sheet['D8'] = w.bch
	    sheet['D9'] = w.eth
	    sheet['D10'] = w.btc
	    sheet['D11'] = w.omg
	    #sheet['E12'] = total
	    #sheet['E13'] = totalgbp
	    print "Writing Cryptocurrency values..."
	except:
	    print "Write of current Crypto rates failed."

	try:
		wb.save("/Users/holmes/Documents/Personal/Crypto.xlsx")
		print "Writes to Excel spreadsheet Crypto.xlsx successful."
	except:
		print "Writes failed - exiting..."
		quit()


if len(sys.argv) > 1 and sys.argv[1] == "-l":

    print ""
    print "############# CRYPTOCURRENCY #############"
    print "Current personal outlay: " + str(personal)
    print ""
    print str(time) + ":  GBP Ratio to Dollar:    " + str(w.gbp)
    print str(time) + ":  Current ETH Price ($)   " + str(w.eth)
    print str(time) + ":  Current BTC Price ($):  " + str(w.btc)
    print str(time) + ":  Current Ratio Price:    " + str(w.ratio)
    print str(time) + ":  Current BCH Price ($):  " + str(w.bch)
    print str(time) + ":  Current OMG Price ($):  " + str(w.omg)
    print str(time) + ":  Current profit/loss:    " + str(w.profit)
    print ""

elif len(sys.argv) > 1 and sys.argv[1] == '-c':
	w.changeValues()

elif len(sys.argv) > 1 and sys.argv[1] == '-d':
	writetoDB()

elif len(sys.argv) > 1 and sys.argv[1] == '-e':
	excelWrite()

elif len(sys.argv) > 1 and sys.argv[1] == '-1':
	oneLiner()

elif len(sys.argv) < 2 :
	print ""
	print "---------------------------------------------"
	print "Pick one of the following arguments"
	print "-l - Displays information on all Crypto prices"
	print "-1 - Shows just the profit/loss margin"
	print "-c - Change amount of crypto you own"
	print "-d - Write to database (Multiple argument option, sysopts/case?)"
	print "-e - Write to database (Multiple argument option, sysopts/case?)"
	print "---------------------------------------------"

else:
	print "Incorrect argument specified, exiting"
