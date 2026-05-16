import json
import requests
from typing import Final

BASE_URL: Final[str] = 'http://api.exchangeratesapi.io/v1/latest'
API_KEY: Final[str] = '19e3f332479f11df8aa7405b09adbd97'

def get_rates(mock: bool = False) -> dict:
    if mock:
        with open('python_intermediate_projects/currency_converter/rates.json', 'r') as f:
            return json.load(f)
    
    payload: dict = {
        'access_key': API_KEY
    }
    request = requests.get(BASE_URL, params=payload)
    data: dict = request.json()

    return data

def get_currency(currency: str, rates: dict) -> float:
    currency = currency.upper()
    if currency in rates.keys():
        return rates.get(currency)
    else:
        raise ValueError(f'Currency {currency} not found in rates.')

def convert_currency(amount: float, base: str, vs: str, rates: dict) -> float:
    base_rate: float = get_currency(base, rates)
    vs_rate: float = get_currency(vs, rates)

    conversion: float = round((vs_rate / base_rate) * amount, 2)
    print(f'{amount:,.2f} ({base}) is equal to {conversion:,.2f} ({vs}).')
    return conversion

def main():
    data: dict = get_rates(mock=True)
    rates: dict = data.get('rates')

    convert_currency(100, 'USD', 'LKR', rates=rates)

if __name__ == '__main__':
    main()