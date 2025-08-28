import sqlite3

conexao = sqlite3.connect('exemplo.db')

cursor = conexao.cursor()

cursor.execute('SELECT * FROM Personagens')
personagens = cursor.fetchall()

print("Personagens na base de dados:")
for personagem in personagens:
    print(personagem)
    
cursor.close()
conexao.close()