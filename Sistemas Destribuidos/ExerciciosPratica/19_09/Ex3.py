# cada cigarro - 10min
# 24h

cigarrosDia = int(input("Quantos cigarros por dia: "))
anosDeFumante = int(input("Quantos anos fumou: "))

def anos_perdidos(cigarrosDia, anosDeFumante):
  dia = (cigarrosDia * 10) / 60
  ano = ((365 * dia) / 24) * anosDeFumante
  return ano

resultado = anos_perdidos(cigarrosDia, anosDeFumante)
print(f"Você perdeu {round(resultado)} dias de vida.")


def anos_perdidos2(cigarrosDia, anosDeFumante):
  dia = (cigarrosDia * 10) / 60
  ano = ((365 * dia) / 24) * anosDeFumante
  print(f"Você perdeu {round(ano)} dias de vida.")

anos_perdidos2(cigarrosDia, anosDeFumante)
