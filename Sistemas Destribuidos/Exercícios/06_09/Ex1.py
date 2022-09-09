import requests

r = requests.get('https://api.hgbrasil.com/finance?format=json-cors&key=a32243ce')

if (r.status_code == 200):
  print()
  print('JSON : ', r.json())
  print()
else:
  print('Nao houve sucesso na requisicao.')
