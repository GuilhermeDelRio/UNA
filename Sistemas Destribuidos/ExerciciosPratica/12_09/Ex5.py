velocidade = float(input('Velocidade do carro (KM): '))
if(velocidade > 80):
  print('Você está acima de 80 Km/h e será multado!')
  multa = (velocidade - 80) * 5
  print('Multa de R$: ' + str(multa))
else:
  print('Dentro do limite permitido')