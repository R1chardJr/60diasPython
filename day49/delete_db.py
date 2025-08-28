import sqlite3

conexao = sqlite3.connect('exemplo.db')

cursor = conexao.cursor()

cursor.execute('DELETE FROM Personagens WHERE poder < 7500')
conexao.commit()
print("Dados deletados com sucesso!")

cursor.close()
conexao.close()