import sqlite3

conexao = sqlite3.connect('exercicio.sqlite3')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(530))')


#2. Insira pelo menos 5 registros de alunos na tabela que você criou no exercício anterior.
cursor.execute("INSERT INTO alunos(id, nome, idade, curso) VALUES (1, 'Lidia', 28, 'Ciencias da Computacao')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES(2, 'Joselito', 30, 'Ciencias da Computacao')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (3, 'Patricia', 47, 'Direito')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (4, 'Jose Maria', 55, 'Engenharia Civil')")
cursor.execute("INSERT INTO alunos (id, nome, idade, curso) VALUES (5, 'Donald', 76, 'Medicina')")


#3. Consultas Básicas - #Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
registros = cursor.execute("SELECT * FROM alunos")
for alunos in registros:
    print (alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
idade = cursor.execute("SELECT nome, idade FROM alunos WHERE idade>20")
for alunos in idade: 
    print (idade)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
curso = cursor.execute("SELECT nome FROM alunos WHERE curso ='Engenharia Civil' ORDER BY nome")
for alubnos in curso:
    print (curso)

#d) Contar o número total de alunos na tabela
totalAlunos = cursor.execute("SELECT COUNT (*) FROM alunos")
for alunos in totalAlunos:
    print (totalAlunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
cursor.execute("UPDATE alunos SET idade = 30 WHERE nome = 'Joselito'")

#b) Remova um aluno pelo seu ID.

cursor.execute('DELETE FROM alunos WHERE id = 5')


#5. Criar uma Tabela e Inserir Dados - Crie uma tabela chamada "clientes" com os campos: id (chave primária), nome (texto), idade (inteiro) e saldo (float). 
cursor.execute("CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)")

#Insira alguns registros de clientes na tabela.
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, 'Tassio', 44, 750.0)")
cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (7, 'Ivan', 39, 1080.0)")
cursor.execute("INSERT INTO clientes (id, nome, idade, saldo) VALUES (8, 'Railana', 28, 500.0)")
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (9, 'Eronildo', 22, 300.0)")
cursor.execute("INSERT INTO clientes(id, nome, idade, saldo) VALUES (10, 'Dhyego', 25, 1000.5)")


#6. Consultas e Funções Agregadas - Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
idade = cursor.execute("SELECT nome, idade FROM clientes WHERE idade>30")

for clientes in idade:
    print (clientes)

#b) Calcule o saldo médio dos clientes.

saldo = cursor.execute("SELECT saldo FROM clientes").fetchall()

saldoMedio = 0
for clientes in saldo:
    saldoMedio += clientes[0]

saldo = saldoMedio/len(saldo)
print ("O saldo médio é: ", saldo)

#c) Encontre o cliente com o saldo máximo.
saldo = cursor.execute("SELECT nome, saldo FROM clientes").fetchall()

saldoMaximo = 0 
clienteMaximo = None
saldoCliente = 0 

for nome, saldoCliente in saldo:
    if saldoCliente > saldoMaximo:
        saldoMaximo = saldoCliente
        clienteMaximo = nome

print ("O cliente com o maior saldo no valor de R$ ", saldoMaximo, " é ", clienteMaximo)


#d) Conte quantos clientes têm saldo acima de 1000.
qntClientes = cursor.execute("SELECT COUNT (*) FROM clientes WHERE saldo>1000")
qntClientesAcima1000 = 0

for clientes in qntClientes:
    qntClientesAcima1000 +=1
    print ("A quantidade de clientes com saldo maior que 1000 é: ", qntClientesAcima1000)


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
cursor.execute("UPDATE clientes SET saldo = 5000.0 WHERE nome = 'Ivan'")

#b) Remova um cliente pelo seu ID.
cursor.execute ('DELETE FROM clientes WHERE id = 5')


#8. Junção de Tabelas - Crie uma segunda tabela chamada "compras" com os campos: id (chave primária), cliente_id (chave estrangeira referenciando o id da tabela "clientes"), 
#produto (texto) e valor (real). Insira algumas compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o valor de cada compra.
cursor.execute("CREATE TABLE compras (id INT PRIMARY KEY, clienteId INT, produto VARCHAR(100), valor INT, FOREIGN KEY (clienteId) REFERENCES clientes (id))")
cursor.execute("INSERT INTO compras (id, clienteId, produto, valor) VALUES (1,6, 'Carne', 50)")
cursor.execute("INSERT INTO compras (id, clienteId, produto, valor) VALUES (2,8, 'Shampoo', 5)")
cursor.execute("INSERT INTO compras (id, clienteId, produto, valor) VALUES (3,9, 'Celular', 600.0)")

dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.clienteId')

for compras in dados:
    print ("Informações: ", compras)

conexao.commit()
conexao.close()


