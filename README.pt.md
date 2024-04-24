# Crypto Tracker

Um simples programa Python para acompanhar cotações e notícias de criptomoedas.

## Requisitos

- Python 3.x
- Bibliotecas: `requests`, `json`

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu_usuario/nome_do_repositorio.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd nome_do_repositorio
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Execute o programa:

   ```bash
   python crypto_tracker.py
   ```

## Funcionalidades

- **Acompanhar cotação**: Digite o símbolo da criptomoeda para ver sua cotação em reais.
- **Acompanhar notícias**: Digite o símbolo da criptomoeda para ver as últimas notícias relacionadas.
- **Adicionar Moeda**: Adicione uma nova criptomoeda para acompanhar sua cotação.

## Aviso

Este programa faz uso da API do CoinMarketCap. Certifique-se de ter uma chave de API válida e substitua-a no código-fonte antes de executar o programa.

```python
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'sua chave api aqui'
}
```

## Contribuição

Sinta-se à vontade para contribuir com novos recursos, correções de bugs ou melhorias. Abra um PR e teremos o prazer de revisar.