import requests

base_url = "https://api.coingecko.com/api/v3/"
coin_list = requests.get(base_url+"coins/list")
coin_list = coin_list.json()

print('CRYPTO PRICE CHECKER')
# Main loop
while True:
    user_in = input('Enter coin id or q to quit >> ')
    if user_in == 'q':
        print('Exiting...')
        break
    # Look for coin in list
    my_coin = [c for c in coin_list if c['symbol'] == user_in]
    if len(my_coin) == 0:
        print('Error: Coin not found')
    else:
        my_coin = my_coin[0]
        my_id = my_coin['id']
        my_coin_result = requests.get(base_url+"simple/price?ids="+my_coin['id']+"&vs_currencies=usd")
        my_coin_result = my_coin_result.json()
        value = my_coin_result[my_id]['usd']
        print(my_id, '('+my_coin['symbol']+'): $', value)
