import sqlite3

conn= sqlite3.connect('banco')
cursor =conn.cursor()
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS usuarios(
    i INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    idade INTEGER
    )'''
)

cursor.execute('''
INSERT INTO usuarios(i, nome, idade) VALUES(?,?,?)
''', (1, "leonardo", 29))


conn.commit()

cursor.execute(''' SELECT * FROM usuarios''')
registro = cursor.fetchall()
for regis in registro:
    print(regis)