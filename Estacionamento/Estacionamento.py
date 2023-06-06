import requests
import hashlib
import hmac
import time

API_KEY = 'sua_api_key'
SECRET_KEY = 'sua_secret_key'

BASE_URL = 'https://api.binance.com'

def generate_signature(query_string):
    return hmac.new(SECRET_KEY.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()

def place_order(symbol, side, quantity, price):
    endpoint = '/api/v3/order'
    url = BASE_URL + endpoint

    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'side': side,
        'type': 'LIMIT',
        'timeInForce': 'GTC',
        'quantity': quantity,
        'price': price,
        'timestamp': timestamp,
        'recvWindow': 5000,
        'signature': ''
    }

    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    params['signature'] = generate_signature(query_string)

    headers = {'X-MBX-APIKEY': API_KEY}

    response = requests.post(url, params=params, headers=headers)
    return response.json()

def get_account_balance():
    endpoint = '/api/v3/account'
    url = BASE_URL + endpoint

    timestamp = int(time.time() * 1000)
    params = {
        'timestamp': timestamp,
        'recvWindow': 5000,
        'signature': ''
    }

    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    params['signature'] = generate_signature(query_string)

    headers = {'X-MBX-APIKEY': API_KEY}

    response = requests.get(url, params=params, headers=headers)
    return response.json()

def get_order_status(symbol, order_id):
    endpoint = '/api/v3/order'
    url = BASE_URL + endpoint

    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'orderId': order_id,
        'timestamp': timestamp,
        'recvWindow': 5000,
        'signature': ''
    }

    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    params['signature'] = generate_signature(query_string)

    headers = {'X-MBX-APIKEY': API_KEY}

    response = requests.get(url, params=params, headers=headers)
    return response.json()

def cancel_order(symbol, order_id):
    endpoint = '/api/v3/order'
    url = BASE_URL + endpoint

    timestamp = int(time.time() * 1000)
    params = {
        'symbol': symbol,
        'orderId': order_id,
        'timestamp': timestamp,
        'recvWindow': 5000,
        'signature': ''
    }

    query_string = '&'.join([f"{k}={v}" for k, v in params.items()])
    params['signature'] = generate_signature(query_string)

    headers = {'X-MBX-APIKEY': API_KEY}

    response = requests.delete(url, params=params, headers=headers)
    return response.json()

# Exemplo de uso
symbol = 'BTCUSDT'  # Par de criptomoedas para negociação
side = 'BUY'       # Lado da negociação (compra)
quantity = 0.01     # Quantidade da criptomoeda a ser comprada
price = 40000      # Preço limite da ordem de compra

# Criar uma ordem de compra
response = place_order(symbol, side, quantity, price)
print(response)

# Obter o saldo da conta
balance_response = get_account_balance()
print(balance_response)

# Verificar o status da ordem
order_id = response['orderId']
status_response = get_order_status(symbol, order_id)
print(status_response)

# Cancelar a ordem
cancel_response = cancel_order(symbol, order_id)
print(cancel_response)
