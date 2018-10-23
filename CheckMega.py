import json
from bs4 import BeautifulSoup
import requests
import zipfile

url = 'http://www1.caixa.gov.br/loterias/_arquivos/loterias/D_mgsasc.zip'
z = requests.get(url)
open('D_mgsasc.zip', 'wb').write(z.content)

zipfile.ZipFile('D_mgsasc.zip').extractall()


def send_email(subject, body):
    import smtplib

    gmail_user = 'fulano@gmail.com'
    gmail_pwd = 'fulanoPwd'

    FROM = 'fulano@gmail.com'
    TO = '<fulano ou beltrano>@gmail.com'
    SUBJECT = subject
    TEXT = body

    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, TO, SUBJECT, TEXT)

    try:
       server = smtplib.SMTP('smtp.gmail.com', 587)
       server.ehlo()
       server.starttls()
       server.login(gmail_user, gmail_pwd)
       server.sendmail(FROM, TO, message)
       server.close()
    except:
       print('Algo deu errado no envio de email...')

with open('apostas.json', 'r') as arq_apostas:
    read_apostas = arq_apostas.read();

apostas_json = json.loads(read_apostas)

with open('d_megasc.htm', 'r', encoding="utf8", errors='ignore') as arq:
    read_htm = arq.read();

apostas = apostas_json["apostas"]
sorteios = apostas_json["sorteios"]
nr_acertos = []
for n in range(len(apostas)):
    nr_acertos.append(0)
nr_apostas = len(apostas)
encerrou = False

rawh = BeautifulSoup(read_htm, 'html.parser')

rows = rawh.find_all('tr')
for row in rows[:]:
    first_td = row.find('td')
    if(first_td is not None):
      if(first_td.text.isnumeric()):
          nr_sorteio = int(first_td.text)
          if(nr_sorteio >= sorteios[len(sorteios)-1]):
              encerrou = True
          tamu_dentro = False
          for sorteio in sorteios[:]:
              if(nr_sorteio == sorteio):
                  tamu_dentro = True
                  break
          if(tamu_dentro):
            data_sorteio = first_td.next_sibling.next_sibling
            for n in range(len(sorteios)):
                nr_acertos[n] = 0
            dezena = data_sorteio
            for d in range(6):
                dezena = dezena.next_sibling.next_sibling
                dezena_int = int(dezena.text)
                for aposta in range(nr_apostas):
                    for d in range(len(apostas[aposta])):
                        if(dezena_int == apostas[aposta][d]):
                            nr_acertos[aposta-1] += 1
            for aposta in range(nr_apostas):
                if(nr_acertos[aposta-1] == 4):
                    send_email('QUADRA !', 'ACERTOU NO SORTEO ' + str(nr_sorteio))
                elif(nr_acertos[aposta-1] == 5):
                    send_email('QUINA !!', 'ACERTOU NO SORTEIO ' + str(nr_sorteio))
                elif(nr_acertos[aposta-1] == 6):
                    send_email('SENA !!!', 'ACERTOU NO SORTEIO ' + str(nr_sorteio))

if(encerrou):
    send_email('MEGASENA','Fazer novas apostas')

