import time
import requests
from termcolor import colored
#import os


var_tempo = time.sleep(3)


while var_tempo != 1:

  BTC = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT').json()
  ETH = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT').json()
  LINK = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=LINKUSDT').json()
  DOT = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=DOTUSDT').json()


  print(colored(BTC,'red'))
  print(colored(ETH, 'green'))
  print(colored(LINK, 'grey'))
  print(colored(DOT, 'white'))


  var_tempo = var_tempo
  time.sleep(0.5)
#  os.system('cls')