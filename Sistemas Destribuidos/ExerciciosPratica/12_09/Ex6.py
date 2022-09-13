# tabuada = int(input("Informa a tabuada: "))
# for item in range(1, 10):
#   total = item * tabuada;
#   print("{} x {} = {}".format(tabuada, item,total))


for x in range(1, 10):
  print("TABUADA DO {}".format(x))
  for y in range(1, 10):
    total = x * y
    print(f"{x} x {y} = {total}")
  print("\n")
