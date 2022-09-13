num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

if num1 == num2 and num2 == num3:
  print('Equilátero')
elif (num1 == num2 and num2 != num3) or (num2 == num3 and num3 != num1) or (num3 == num1 and num1 != num2):
  print("Isóceles")
else:
  print('Escaleno')