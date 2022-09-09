import sqlite3
from datetime import date

conn = sqlite3.connect('cotacoes.db')
cursor = conn.cursor()

p_moeda = 'US$'
p_valor = '5,25'
p_data = str(date.today())

cursor.execute("""INSERT INTO cotacoes (moeda, valor, data) VALUES (?,?,?)""", (p_moeda, p_valor, p_data))

conn.commit()

print('Dados inseridos com sucesso.')

conn.close()