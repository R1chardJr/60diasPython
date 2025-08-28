import sqlite3

conexao = sqlite3.connect('exemplo.db')

cursor = conexao.cursor()

print("Conexão bem sucedida!")

cursor.execute('''CREATE TABLE IF NOT EXISTS Personagens (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                poder INTEGER NOT NULL,
                universo TEXT NOT NULL
                )
               ''')
print("Tabela criada com sucesso!")

cursor.execute('''INSERT INTO Personagens (nome, poder, universo)
               VALUES ('Naruto', 8000, 'Naruto'),
                      ('Luffy', 8000, 'One Piece'),
                      ('Goku', 7000, 'Dragon Ball')
               ''')
print("Dados inseridos com sucesso!")

conexao.commit()
conexao.close()