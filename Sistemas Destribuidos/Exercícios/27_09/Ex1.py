import requests

r = requests.get('http://52.90.225.180:5000/soma/1/1')

if (r.status_code == 200):
  print()
  print('JSON : ', r.json())
  print()
else:
  print('Nao houve sucesso na requisicao.')
