import requests

url = 'https://viacep.com.br/ws/'
estado = 'MG/'
cidade = 'Belo Horizonte/'
rua = 'Rua dos Aimores'
formato = '/json/'

r = requests.get(url + estado + cidade + rua + formato)

if (r.status_code == 200):
  print()
  print('JSON : ', r.content.decode())
  print()
else:
  print('Nao houve sucesso na requisicao.')