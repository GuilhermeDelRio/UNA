def ajustaNumero(numero):
  if(len(str(numero)) < 8):
    return '3' + str(numero)
  return numero

numero = int(input("Digite seu número de telefone: "))
while len(str(numero)) < 7:
  numero = int(input("Digite seu número de telefone: "))

resultado = ajustaNumero(numero)
print(f"O número do telefone é {resultado}")
