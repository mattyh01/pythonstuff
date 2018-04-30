import json, os, datetime, sys, requests, time

while True:

    exchangeget = requests.get('http://api.fixer.io/latest?base=USD')
    ethget = requests.get('https://api.cryptowat.ch/markets/coinbase/ethusd/price')
    euroget = requests.get('https://api.cryptowat.ch/markets/coinbase/etheur/price')
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

    euroget = euroget.text
    europrice = json.loads(euroget)
    euro = europrice['result']['price']

    t = datetime.datetime.now().strftime('%H:%M:%S')
    print t + ":  Eth: " + str(eth) + ",  BTC: " + str(btc) + ",  EURETH: " + str(euro)
    time.sleep(3)
