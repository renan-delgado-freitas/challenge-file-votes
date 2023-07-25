import requests
from datetime import datetime

requisicao = resquest.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

requisicao_dic = requisicao.json()
cotacao_dolar = requisicao_dic['USDBRL']['bid']
cotacao_euro = requisicao_dic['EURBRL']['bid']
cotacao_btc = requisicao_dic['BTCBRL']['bid']

print(f"Cotacao atualizada: {datetime.now()}\nDolar: {cotacao_dolar}\nEuro: {cotacao_euro}\nBTC: {cotacao_btc}")

