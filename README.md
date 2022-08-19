# Objetivo

Verificar se vale mais a pena comprar packs de cartas ou cartas individualmente na Steam.

O CSV atualizado é baixado em: https://steam.tools/cards/


## BS_&_CSV_compare.ipynb

Comparação com os dados do site: https://www.steamcardexchange.net

Extração do csv: https://steam.tools/cards/


## Steam_analisando_dados.ipynb

### Exemplo de tratamento de dados: Steam

Aqui existe uma lógica, na qual cada game possui um número de cartas para fechar um 'set'. Cada pacote de booster gera 3 cartas aleatórias deste set. Tanto os boosters quanto as cartas podem ser vendidas individualmente

## Dataset Information

- Game - Name of the set's game;
- \# Owned - 
- \# Unique -
- \# Cards - Number of cards in the set;
- Badge Lvl -
- Set Price - The total price of all the cards for the set;
- Price Diff -
- Card Avg - The total price of all the cards for the set;
- Booster Avg - The average price of a card from the set's booster;
- Booster % - How many percent cheaper average booster cards are for the set;
- Emote Avg - The average price of the set's emoticons;
- BG Avg - The average price of the set's backgrounds;
- Avg Qty - The average quantity of items on the market;
- Discount - The money you would make by selling all your drops for that game;
- Added - The date the set was added;
- AppId -
