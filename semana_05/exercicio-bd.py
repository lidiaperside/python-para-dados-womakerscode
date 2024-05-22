import sqlite3
conexao = sqlite3.connect('banco-exercicio2')
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
#registros = cursor.execute('SELECT * FROM alunos') 

#for alunos in registros:
#    print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
#idade = cursor.execute ('SELECT nome,idade FROM alunos WHERE idade>20')

#for alunos in idade:
#    print(alunos)

#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
#curso = cursor.execute("SELECT nome FROM alunos WHERE curso = 'Engenharia Civil' ORDER BY nome")

#for alunos in curso:
#    print(alunos)

#d) Contar o número total de alunos na tabela
#total = cursor.execute('SELECT COUNT (*) FROM alunos')

#for alunos in total:
#    print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
#cursor.execute('UPDATE alunos SET idade = 20 WHERE nome = "Sophia"')

#b) Remova um aluno pelo seu ID.
#cursor.execute('DELETE FROM alunos WHERE id =6')

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.
#cursor.execute('CREATE TABLE clientes (id INT PRIMARY KEY, nome VARCHAR(100), idade INT, saldo FLOAT)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (1, "Ingrid", 48, 1000.0)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (2, "Marcelo", 46, 785.70)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (3, "Cleber", 29, 35.0)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (4, "Antonio", 68, 2000.05)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (5, "Joey", 15, 10.0)')
#cursor.execute('INSERT INTO clientes(id, nome, idade, saldo) VALUES (6, "Theo", 18, 1010.0)')

#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
#idade = cursor.execute ('SELECT nome,idade FROM clientes WHERE idade>30')

#for clientes in idade:
#    print(clientes)

#b) Calcule o saldo médio dos clientes.
#saldo = cursor.execute('SELECT saldo FROM clientes').fetchall()

#total_saldo = 0
#for clientes in saldo:
#    total_saldo += clientes[0]  # Adiciona o saldo do cliente atual ao total

#saldo_medio = total_saldo / len(saldo)  # Calcula o saldo médio

#print("Saldo médio dos clientes:", saldo_medio)


#c) Encontre o cliente com o saldo máximo.
#saldo = cursor.execute('SELECT nome,saldo FROM clientes').fetchall()

#saldo_maximo = 0
#cliente_maximo = None


#for nome, saldo_cliente in saldo:
#    if saldo_cliente > saldo_maximo:
#        saldo_maximo = saldo_cliente
#        cliente_maximo = nome

#print('Cliente com o saldo máximo:', cliente_maximo)
#print('Saldo máximo:', saldo_maximo)

#d) Conte quantos clientes têm saldo acima de 1000.
#qtd_clientes = cursor.execute("SELECT COUNT(*) FROM clientes WHERE saldo > 1000")
#qtd_clientes_acima_1000 = 0 

#for clientes in qtd_clientes:
#    qtd_clientes_acima_1000 += 1
#    print('Quantidade de clientes com saldo acima de 1000: ', clientes)


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
#cursor.execute('UPDATE clientes SET saldo = 3000.0 WHERE nome = "Ingrid"')
    
#b) Remova um cliente pelo seu ID.
#cursor.execute('DELETE FROM clientes WHERE id = 5')

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.
#cursor.execute('CREATE TABLE compras (id INT PRIMARY KEY, cliente_id INT, produto VARCHAR(100), valor INT, FOREIGN KEY (cliente_id) REFERENCES clientes(id))')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (1, 1, "Carne", 50)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (2, 3, "Shampoo", 10)')
#cursor.execute('INSERT INTO compras(id, cliente_id, produto, valor) VALUES (3, 6, "Video Game", 500)')
    
dados = cursor.execute('SELECT clientes.nome, compras.produto, compras.valor FROM clientes JOIN compras ON clientes.id = compras.cliente_id;')

for compras in dados:
    print ('Informações: ', compras)
    
conexao.commit()
conexao.close()