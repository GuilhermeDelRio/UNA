sal = float(input("Informe seu salário: "))


def aumento_sal(sal):
  novoSal = sal + (sal * 25) / 100
  return novoSal


novoSal = aumento_sal(sal)
print(f"Seu salário aumentou de {sal} para {novoSal}")