from flask import Flask, render_template, request, redirect, flash
from dao.aluno_dao import AlunoDAO
from dao.professor_dao import ProfessorDAO
from dao.turma_dao import TurmaDAO
from dao.curso_dao import CursoDAO
from dao.matricula_dao import MatriculaDAO

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
@app.route('/aluno/salvar/<int:id>', methods=['POST']) # Atualização
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

@app.route('/aluno/editar/<int:id>')
def editar_aluno(id):
    dao = AlunoDAO()
    aluno = dao.buscar_por_id(id)
    return render_template('aluno/form.html', aluno=aluno)

@app.route('/aluno/remover/<int:id>')
def remover_aluno(id):
    dao = AlunoDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Aluno removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
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
@app.route('/professor/salvar/<int:id>', methods=['POST'])
def salvar_professor(id=None):
    nome = request.form['nome']
    disciplina = request.form['disciplina']

    dao = ProfessorDAO()
    result = dao.salvar(id, nome, disciplina)

    if result["status"] == "ok":
        flash("Professor salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/professor')


@app.route('/professor/editar/<int:id>')
def editar_professor(id):
    dao = ProfessorDAO()
    professor = dao.buscar_por_id(id)
    return render_template('professor/form_professor.html', professor=professor)


@app.route('/professor/remover/<int:id>')
def remover_professor(id):
    dao = ProfessorDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Professor removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    
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

@app.route('/desafio/')
def desafio():
    nome = request.args.get('nome')
    return render_template('desafio/desafio.html', valor_recebido=nome)


@app.route('/formulario', methods=['POST'])
def formulario():
    nome = request.form['nome']
    data_nascimento = request.form['data_nascimento']
    cpf = request.form['cpf']
    nome_da_mae = request.form['nome_da_mae']
    nome_do_pai = request.form['nome_do_pai']
    dados = f"Nome: {nome}, Data de Nascimento: {data_nascimento}, CPF: {cpf}, Nome da Mãe: {nome_da_mae}, Nome do Pai: {nome_do_pai}"
    return render_template('desafio/desafio.html', valor_recebido=dados)


@app.route('/turma')
def listar_turma():
    dao = TurmaDAO()
    lista = dao.listar()
    return render_template('turma/lista_turma.html', lista=lista)

@app.route('/turma/form')
def form_turma():
    dao = TurmaDAO()
    cursos = CursoDAO().listar()
    professores = ProfessorDAO().listar()
    return render_template('turma/form.html', turma=None, cursos=cursos, professores=professores)

@app.route('/turma/salvar/', methods=['POST'])
@app.route('/turma/salvar/<int:id>', methods=['POST'])
def salvar_turma(id=None):
    semestre = request.form['semestre']
    curso_id = request.form['curso_id']
    professor_id = request.form['professor_id']
    dao = TurmaDAO()
    result = dao.salvar(id, semestre, curso_id, professor_id)
    if result["status"] == "ok":
        flash("Cadastro salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")
    return redirect('/turma')

@app.route('/turma/editar/<int:id>')
def editar_turma(id):
    dao = TurmaDAO()
    turma = dao.buscar_por_id(id)
    cursos = CursoDAO().listar()
    professores = ProfessorDAO().listar()
    return render_template('turma/form.html', turma=turma, cursos=cursos, professores=professores)

@app.route('/turma/remover/<int:id>')
def remover_turma(id):
    dao = TurmaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Turma removida com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/turma')


@app.route('/curso')
def listar_curso():
    dao = CursoDAO()
    lista = dao.listar()
    return render_template('curso/lista_curso.html', lista=lista)


@app.route('/curso/form_curso')
def form_curso():
    return render_template('curso/form_curso.html', curso=None)


@app.route('/curso/salvar/', methods=['POST'])
@app.route('/curso/salvar/<int:id>', methods=['POST'])
def salvar_curso(id=None):
    nome = request.form['nome']
    duracao = request.form['duracao']
    dao = CursoDAO()
    result = dao.salvar(id, nome, duracao)
    
    if result["status"] == "ok":
        flash("Curso salvo com sucesso!", "success")
    else:
        flash(result["mensagem"], "danger")

    return redirect('/curso')


@app.route('/curso/editar/<int:id>')
def editar_curso(id):
    dao = CursoDAO()
    curso = dao.buscar_por_id(id)
    return render_template('curso/form_curso.html', curso=curso)


@app.route('/curso/remover/<int:id>')
def remover_curso(id):
    dao = CursoDAO()
    resultado = dao.remover(id)

    if resultado["status"] == "ok":
        flash("Curso removido com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")

    return redirect('/curso')


@app.route('/matricula')
def listar_matriculas():
    dao = MatriculaDAO()
    lista = dao.listar()
    return render_template('matricula/lista_matricula.html',lista=lista)


@app.route('/matricula/form')
def form_matricula():
    dao = MatriculaDAO()
    alunos = dao.listar_alunos()
    turmas = dao.listar_turmas()
    return render_template('matricula/form.html',matricula=None,alunos=alunos,turmas=turmas)

@app.route('/matricula/salvar/', methods=['POST'])
@app.route('/matricula/salvar/<int:id>', methods=['POST'])
def salvar_matricula(id=None):
    aluno_id = request.form['aluno_id']
    turma_id = request.form['turma_id']
    dao = MatriculaDAO()
    resultado = dao.salvar(id, aluno_id, turma_id)
    if resultado["status"] == "ok":
        flash("Matrícula salva com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/matricula')

@app.route('/matricula/editar/<int:id>')
def editar_matricula(id):
    dao = MatriculaDAO()
    matricula = dao.buscar_por_id(id)
    alunos = dao.listar_alunos()
    turmas = dao.listar_turmas()
    if matricula is None:
        flash("Matrícula não encontrada!", "danger")
        return redirect('/matricula')
    return render_template('matricula/form.html',matricula=matricula,alunos=alunos,turmas=turmas)

@app.route('/matricula/remover/<int:id>')
def remover_matricula(id):
    dao = MatriculaDAO()
    resultado = dao.remover(id)
    if resultado["status"] == "ok":
        flash("Matrícula removida com sucesso!", "success")
    else:
        flash(resultado["mensagem"], "danger")
    return redirect('/matricula')


@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

if __name__ == '__main__':
    app.run(debug=True)