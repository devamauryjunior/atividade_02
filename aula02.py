import sqlite3

conn = sqlite3.connect('user.db')

curso = conn.cursor()

curso.execute('''
    CREATE TABLE IF NOT 
    EXISTS Usuarios(
        id INTERGE PRIMARY
        KEY,
        nome TEXT,
        idade INTERGE
    )
''')


curso.execute('INSERT INTO Usuarios (nome,idade) VALUES (?, ?)', ('jhon',12))
curso.execute('INSERT INTO Usuarios (nome,idade) VALUES (?, ?)', ('Matheus',20))


conn.commit()

curso.execute('SELECT * FROM Usuarios')
for row in curso.fetchall(): print(row)

conn.close()