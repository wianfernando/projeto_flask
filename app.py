from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_alunos():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, idade, cidade FROM aluno')
    lista = cursor.fetchall()
    return render_template('aluno/lista_aluno.html', lista=lista)

@app.route('/professor')
def listar_professor():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT id, nome, disciplina from professor')
    lista = cursor.fetchall()
    return render_template('professor/lista_professor.html', lista=lista)


@app.route('/turma')
def listar_turma():
    DB_PATH = "banco_escola.db"
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT turma.id, turma.semestre, nome_curso, professor.nome from turma\n' 
                   'JOIN curso on curso.id=turma.curso_id\n' 
                   'JOIN professor on professor.id=turma.professor_id')
    lista = cursor.fetchall()
    return render_template('turma/lista_turma.html', lista=lista)




@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

if __name__ == '__main__':
    app.run(debug=True)