def restoDivisao(dividendo, divisor):
  x = 0
  resto = 0
  while x <= dividendo:
    if(dividendo > divisor):
      
      resto = dividendo / divisor
      dividendo - 3
    x += 1
  return resto

resultado2 = restoDivisao(27, 3)
print(f"O resto da divisão entre 27 e 3 é {resultado2}")

def resto(num1, num2):
  return num1 % num2

def sub(num1, num2):
  return num1 - num2

def soma(num1, num2):
  return num1 + num2

def mult(num1, num2):
  return num1 * num2

def div(num1, num2):
  return num1 / num2

resultado = mult(10, 5)
print(resultado)