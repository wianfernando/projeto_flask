from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard/index.html')


@app.route('/sobre')
def sobre():
    return render_template('dashboard/sobre.html')


@app.route('/aluno')
def listar_alunos():
    lista = [
        (1, 'Wian Fernando de Oliveira', 22, 'Teresina'),
        (2, 'João da Silva', 20, 'Teresina'),
        (3, 'Maria Souza', 21, 'Teresina'),
        (4, 'Pedro Santos', 23, 'Teresina'),
        (5, 'Ana Oliveira', 19, 'Teresina'),
        (6, 'Lucas Lima', 22, 'Teresina'),
        (7, 'Carla Rodrigues', 20, 'Teresina'),
        (8, 'Rafael Costa', 21, 'Teresina'),
        (9, 'Juliana Martins', 23, 'Teresina'),
        (10, 'Bruno Almeida', 19, 'Teresina'),
        (11, 'Gabriel Ferreira', 24, 'Teresina'),
        (12, 'Larissa Carvalho', 20, 'Teresina'),
        (13, 'Matheus Pereira', 22, 'Teresina'),
        (14, 'Beatriz Lima', 21, 'Teresina'),
        (15, 'Felipe Rodrigues', 25, 'Teresina'),
        (16, 'Camila Santos', 19, 'Teresina'),
        (17, 'Gustavo Martins', 23, 'Teresina'),
        (18, 'Amanda Costa', 22, 'Teresina'),
        (19, 'Thiago Oliveira', 20, 'Teresina'),
        (20, 'Isabela Almeida', 24, 'Teresina'),
        (21, 'Diego Carvalho', 21, 'Teresina'),
        (22, 'Mariana Ferreira', 23, 'Teresina'),
        (23, 'Vinícius Sousa', 20, 'Teresina'),
        (24, 'Letícia Alves', 22, 'Teresina'),
        (25, 'André Martins', 26, 'Teresina'),
        (26, 'Júlia Rodrigues', 19, 'Teresina'),
        (27, 'Leonardo Costa', 24, 'Teresina'),
        (28, 'Vitória Lima', 21, 'Teresina'),
        (29, 'Eduardo Santos', 23, 'Teresina'),
        (30, 'Fernanda Oliveira', 20, 'Teresina'),
        (31, 'Henrique Almeida', 22, 'Teresina'),
        (32, 'Sofia Carvalho', 19, 'Teresina'),
        (33, 'Caio Ferreira', 25, 'Teresina'),
        (34, 'Manuela Santos', 21, 'Teresina'),
        (35, 'Rodrigo Lima', 23, 'Teresina'),
        (36, 'Clara Martins', 20, 'Teresina'),
        (37, 'Samuel Rodrigues', 24, 'Teresina'),
        (38, 'Nicole Costa', 22, 'Teresina'),
        (39, 'Guilherme Alves', 21, 'Teresina'),
        (40, 'Alice Pereira', 19, 'Teresina'),
        (41, 'João Victor Carvalho', 23, 'Teresina'),
        (42, 'Laura Ferreira', 22, 'Teresina'),
        (43, 'Murilo Santos', 20, 'Teresina'),
        (44, 'Helena Oliveira', 24, 'Teresina'),
        (45, 'Enzo Martins', 19, 'Teresina'),
        (46, 'Luana Almeida', 21, 'Teresina'),
        (47, 'Arthur Costa', 23, 'Teresina'),
        (48, 'Melissa Rodrigues', 20, 'Teresina'),
        (49, 'Nicolas Lima', 22, 'Teresina'),
        (50, 'Yasmin Santos', 25, 'Teresina'),
        (51, 'Igor Ferreira', 21, 'Teresina'),
        (52, 'Bianca Alves', 19, 'Teresina'),
        (53, 'Daniel Martins', 24, 'Teresina'),
        (54, 'Rebeca Costa', 22, 'Teresina'),
        (55, 'Marcelo Oliveira', 26, 'Teresina'),
        (56, 'Isadora Lima', 20, 'Teresina'),
        (57, 'Renato Rodrigues', 23, 'Teresina'),
        (58, 'Elisa Almeida', 21, 'Teresina'),
        (59, 'Vitor Santos', 24, 'Teresina'),
        (60, 'Gabriela Carvalho', 22, 'Teresina')
    ]
    return render_template('aluno/lista_aluno.html', lista=lista)


@app.route('/professor')
def listar_professores():
    lista = [
    (1, 'Carlos Eduardo Silva', 35, 'Teresina'),
    (2, 'Mariana Oliveira Santos', 42, 'Parnaíba'),
    (3, 'Rafael Almeida Costa', 38, 'Picos'),
    (4, 'Juliana Ferreira Lima', 31, 'Floriano'),
    (5, 'Pedro Henrique Souza', 45, 'Campo Maior'),
    (6, 'Ana Clara Rodrigues', 36, 'Piripiri'),
    (7, 'Lucas Gabriel Martins', 29, 'Teresina'),
    (8, 'Camila Vitória Alves', 40, 'Parnaíba'),
    (9, 'Fernando Costa Pereira', 47, 'Picos'),
    (10, 'Beatriz Martins Oliveira', 33, 'Floriano'),
    (11, 'Gustavo Henrique Carvalho', 39, 'Teresina'),
    (12, 'Larissa Mendes Silva', 28, 'Piripiri'),
    (13, 'André Luiz Santos', 44, 'Campo Maior'),
    (14, 'Patrícia Almeida Rodrigues', 37, 'Parnaíba'),
    (15, 'Marcelo Ferreira Costa', 51, 'Teresina'),
    ]
    return render_template('professor/lista_professor.html', lista=lista)



@app.route('/contato')
def contato():
    return render_template('dashboard/contato.html')

if __name__ == '__main__':
    app.run(debug=True)