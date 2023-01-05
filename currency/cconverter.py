# write your code here!
import requests


def convert_currency(value, rate):
    return round(value * rate, 2)


def get_exchange_rate(code):
    url = f"http://www.floatrates.com/daily/{code}.json"
    r = requests.get(url).json()
    currencies_cache = {}

    if code != 'usd':
        currencies_cache['usd'] = float(r['usd']['rate'])
    if code != 'eur':
        currencies_cache['eur'] = float(r['eur']['rate'])

    while True:
        request_code = input().lower()
        if request_code == '':
            break
        amount = int(input())
        print("Checking the cache...")
        request_rate = float(r[request_code]['rate'])
        if request_code in currencies_cache.keys():
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            currencies_cache[request_code] = request_rate
        print(f"You received {convert_currency(amount, request_rate)} {request_code.upper()}")


user_input = input().lower()
get_exchange_rate(user_input)
