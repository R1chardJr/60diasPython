import sqlite3

conexao = sqlite3.connect('exemplo.db')

cursor = conexao.cursor()

cursor.execute('UPDATE Personagens SET poder = poder + 500 WHERE nome = "Luffy"')
print("Dados atualizados com sucesso!")

conexao.commit()
cursor.close()
conexao.close()