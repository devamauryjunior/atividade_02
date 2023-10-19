from flask import Flask, render_template
import sqlite3

conn = sqlite3.connect('user.db')

curso = conn.cursor()

curso.execute('SELECT * FROM Usuarios')
usarios1=""
for row in curso.fetchall(): usarios1 = row

app = Flask(__name__)

@app.route("/usuarios")
def lista_usuarios():
    global usuario1
    return render_tamplate("usuraios.html", usuario=usuario1)

app.run(debug=True)