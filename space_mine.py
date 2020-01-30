#imports CHECK
import requests
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()

def crypto_price():
    #get user input type in ticker symbol ex(BTC) CHECK
    #only allow lowercase inputs. CHECK
    #allow multiple searches until user quits. CHECK

    while True:
        request = input("Enter coin symbol: ").lower()
        if request == "quit":
            break
        else:
            #cg.get_coin_ticker_by_id(request.lower)
            library = cg.get_coins_list()
            print(library)
            for coin in library:
                if coin == request:
                    #look deeper into documentation on how to call price
                    price = cg.get_token_price
                    print(price)
            pass


crypto_price()

    #search engine = https://api.coingecko.com/api/v3/coins/list    IN PROGRESS

    #search example for later use https://api.coingecko.com/api/v3/coins/list   IN PROGRESS

    #print price IN PROGRESS