nomes = []
for item in range(4):
  nome = input(f"Informe o {item + 1}º nome: ")
  nomes.append(nome)

print('\n')

for item in nomes:
  print(f"O nome {item.upper()} possui {len(item)} letras.")
