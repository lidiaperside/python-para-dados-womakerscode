import sqlite3
conexao = sqlite3.connect('banco-exercicio')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#(inteiro), nome (texto), idade (inteiro) e curso (texto).
#cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (1, 'Lidia', 28, 'Computação')")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (2, 'Patricia', 47, 'Direito')")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (3, 'José Maria', 55, 'Engenharia Civil')")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (4, 'Kao', 76, 'Medicina')")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (5, 'Augusto', 42, 'Engenharia Civil')")
#cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (6, 'Sophia', 08, 'Ensino Infantil')")

#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
registros = cursor.execute('SELECT * FROM alunos') 

for alunos in registros:
    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
idade = cursor.execute ('SELECT nome,idade FROM alunos WHERE idade>20')

for alunos in idade:
    print(alunos)
#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
curso = cursor.execute("SELECT nome FROM alunos WHERE curso = 'Engenharia Civil' ORDER BY nome")

for alunos in curso:
    print(alunos)

#d) Contar o número total de alunos na tabela
total = cursor.execute('SELECT COUNT (*) FROM alunos')

for alunos in total:
    print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#b) Remova um aluno pelo seu ID.

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#b) Calcule o saldo médio dos clientes.
#c) Encontre o cliente com o saldo máximo.
#d) Conte quantos clientes têm saldo acima de 1000.

#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#b) Remova um cliente pelo seu ID.

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.

conexao.commit()
conexao.close()