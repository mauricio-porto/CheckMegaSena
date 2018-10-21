# CheckMegaSena
Um "robô" para verificar suas apostas na MegaSena

## Criar arquivo de apostas

A forma mais simples é usar a linha de comando para gerar um único registro JSON com as apostas.
Um exemplo vale mais que mil palavras:

` echo '{"sorteios":[2088,2089,2090,2091],"apostas":[[1,2,3,4,5,6,7],[11,22,33,44,55,59]]}' > apostas.json `

O que significa que você apostou em dois conjuntos de dezenas ([1,2,3,4,5,6,7] e [11,22,33,44,55,59]) para os sorteios 2088, 2089, 2090 e 2091



