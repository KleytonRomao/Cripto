import requests
import json
import os 

os.system('clear')

url_quotes = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?'
url_news = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/news?'
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'sua chave api aqui'
}

def Moedas(symbol):
    params = {
        'symbol': symbol.upper(),
        'convert' :'BR'
    }

    response = requests.get(url_quotes, headers=headers, params=params)
    data = response.json()
    return data

def noticias(symbol):
    params = {
        'symbol': symbol.upper(),
        'sort': 'published_at',
        'start_date': '2021-01-01',
        'end_date': '2023-03-06'
    }

    response = requests.get(url_news, headers=headers, params=params)
    data = response.json()
    return data

def print_moedas(symbol):
    data = Moedas(symbol)
    if 'data' in data and symbol in data['data']:
        print(f'{data["data"][symbol]["name"]} ({data["data"][symbol]["symbol"]}): R$ {data["data"][symbol]["quote"]["BR"]["price"]:.2f}')
    else:
        print(f'A criptomoeda {symbol} não foi encontrada.')

def print_noticias(symbol):
    data = noticias(symbol)
    if 'data' in data and len(data['data']) > 0:
        for news in data['data']:
            print(f'{news["published_at"]} - {news["title"]}\n{news["url"]}\n\n')
    else:
        print(f'Não há notícias para a criptomoeda {symbol}.')

print('''  #####   ######    ####   ######   ######    #####
#######  ### ###  ######  ### ###   ######  ### ###
### # #  ###  ##    ###   ###  ##    ###    ### ###
##       ### ###    ###   ### ###    ###    ##   ##
##       ######    ###    ######     ###    ##   ##
### # #  ### ###   ###    ###        ###    ### ###
#######   ### ### #####    ###       ###    #######
 #####    ### ###  #####   ###      #####    #####
 
 ''')

while True:
    print('Acompanhar cotação[1]. Acompanhar notícias[2]. Adicionar Moeda[3]. Sair[0]')
    opcao = input()

    if opcao == '1':
        symbol = input('Digite o símbolo da criptomoeda que deseja acompanhar: ')
        print_moedas(symbol)
    elif opcao == '2':
        symbol = input('Digite o símbolo da criptomoeda que deseja acompanhar as notícias: ')
        print_noticias(symbol)
    elif opcao == '3':
        symbol = input('Digite o símbolo da criptomoeda que deseja adicionar: ')
        print_moedas(symbol)
    elif opcao == '0':
        break
    else:
        print('Opção inválida. Tente novamente.')
