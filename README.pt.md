README

Este é um script Python que permite acompanhar o preço e notícias de criptomoedas. Ele usa a API CoinMarketCap para obter os dados.
Requisitos

    Python 3.x
    módulo requests

Instalação

    Clone o repositório ou baixe o script
    Instale o módulo requests usando pip install requests

Como Usar

    Adicione sua chave API CoinMarketCap na variável headers

    Execute o script usando python nome_do_script.py

    Escolha uma das opções disponíveis no menu:
        Acompanhar cotação: mostra o preço atual de uma criptomoeda especificada pelo seu símbolo (ex: BTC para Bitcoin).
        Acompanhar notícias: mostra as notícias mais recentes de uma criptomoeda especificada pelo seu símbolo.
        Adicionar moeda: adiciona uma nova criptomoeda à lista de moedas a serem monitoradas.
        Sair: encerra o programa.

Observações

    A lista de moedas monitoradas é armazenada apenas na memória enquanto o programa está em execução, ou seja, ela será reiniciada toda vez que o programa for encerrado.
    O intervalo de datas das notícias é definido nas variáveis start_date e end_date dentro da função noticias.
    O valor da moeda é apresentado em reais (BRL), mas pode ser modificado alterando a variável convert dentro da função Moedas.
