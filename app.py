from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO

app = Flask(__name__)
app.secret_key = "rato123"  # Chave secreta para sessões e flash messages

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_alunos():
    dao = AlunoDAO()
    lista = dao.listar()
    return render_template('aluno/lista_aluno.html', lista=lista)

@app.route('/aluno/form')
def form_aluno():
    return render_template('aluno/form.html', aluno=None)

@app.route('/aluno/salvar/', methods=['POST'])  # Inserção
def salvar_aluno(id=None):
    nome = request.form['nome']
    idade = request.form['idade']
    cidade = request.form['cidade']
    dao = AlunoDAO()
    result = dao.salvar(id, nome, idade, cidade) 


    if result["status"] == "ok":
        flash("Aluno salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")


    return redirect('/aluno')


@app.route('/professor')
def listar_professor():
    dao = ProfessorDAO()
    lista = dao.listar()
    return render_template('professor/lista_professor.html', lista=lista)


@app.route('/professor/form_professor')
def form_professor():
    return render_template('professor/form_professor.html', professor=None)


@app.route('/professor/salvar/', methods=['POST'])
def salvar_professor():
    nome = request.form['nome']
    disciplina = request.form['disciplina']

    dao = ProfessorDAO()
    result = dao.salvar(None, nome, disciplina)

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')



@app.route('/saudacao1/<nome>')
def saudacao1(nome):
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/saudacao2/')
def saudacao2():
    nome = request.args.get('nome')
    return render_template('saudacao/saudacao.html', valor_recebido=nome)


@app.route('/login', methods=['POST'])
def login():
    usuario = request.form['usuario']
    senha = request.form['senha']
    email = request.form['email']
    dados = f"Usuário: {usuario}, Senha: {senha}, E-mail: {email}"
    return render_template('saudacao/saudacao.html', valor_recebido=dados)



@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista_turma.html', lista=lista)



@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista_curso.html', lista=lista)


@app.route('/curso/form_curso')
def form_curso():
    return render_template('curso/form_curso.html', curso=None)


@app.route('/curso/salvar/', methods=['POST'])
def salvar_curso():
    nome = request.form['nome']
    duracao = request.form['duracao']

    dao = CursoDAO()
    result = dao.salvar(None, nome, duracao)

    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')


@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

if __name__ == '__main__':
    app.run(debug=True)