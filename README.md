# CheckMegaSena
Um "robô" para verificar suas apostas na MegaSena

## Funcionamento

Para que este robô faça seu trabalho, ele precisa saber sobre suas apostas e isso é feito através de um pequeno arquivo no formato JSON contendo os números dos sorteios que você está concorrendo e os conjuntos de dezenas que apostou. Veja como criar o arquivo e um exemplo logo abaixo.

O script Python primeiro faz download do arquivo ZIP com os resultados da MegaSena a partir do site da CEF, descompactando-o em seguida.

Logo após ele percorre cada linha do arquivo (*d_megasc.htm*) verificando o número do sorteio (1a coluna) e pulando os sorteios que não estamos concorrendo.

Quando encontra um sorteio para o qual estamos concorrendo, passa a verificar o conjunto de dezenas sorteadas contra os conjuntos de dezenas apostadas, contando número de acertos.
Se o número de acertos nesse sorteio for 4 ou mais, parabéns, você é um feliz ganhador da MegaSena e irá receber um email notificando.

## Uso

Como os sorteios da MegaSena costuma ocorrer 2 vezes por semana, no final da quarta-feira e no final do sábado, o melhor é definir uma rotina de execução do script Python nas manhãs do dia seguinte, dando tempo para a CEF avaliar e divulgar o arquivo ZIP de resultados.
Para fazer isso, eu criei um simples script em shell que apenas invoca o Python (veja *CheckMegaSena.sh*) e o invoco através do *crontab* nas manhãs de quinta-feira e domingos.
Veja as entradas no meu crontab:

```
00 09 * * 4 /home/mapo/Desktop/TechStuff/CheckMegaSena.sh
00 09 * * 0 /home/mapo/Desktop/TechStuff/CheckMegaSena.sh
```
### Ajustes

Para que você receba os emails notificando que ganhou um prêmio ou que as suas apostas jão não mais concorrem, você precisa ajustar os endereços de email dentro do script Python.
Substitua aonde está escrito *fulano@gmail* e *<fulano ou beltrano>@gmail.com* com os endereços de eamil válidos para você.

### Criar arquivo de apostas

A forma mais simples é usar a linha de comando para gerar um único registro JSON com as apostas.
Um exemplo vale mais que mil palavras:

` echo '{"sorteios":[2088,2089,2090,2091],"apostas":[[1,2,3,4,5,6,7],[11,22,33,44,55,59]]}' > apostas.json `

O que significa que você apostou em dois conjuntos de dezenas ([1,2,3,4,5,6,7] e [11,22,33,44,55,59]) para os sorteios 2088, 2089, 2090 e 2091

# BOA SORTE!

