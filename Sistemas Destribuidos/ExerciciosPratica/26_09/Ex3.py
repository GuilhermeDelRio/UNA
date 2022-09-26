valorEmReal = float(input("Informe o valor em real: "))

def real_para_dolar(valorEmReal):
  return valorEmReal / 5.39

valor_convertido = real_para_dolar(valorEmReal)
print(f"R$ {valorEmReal} vale {valor_convertido} em dólares")
