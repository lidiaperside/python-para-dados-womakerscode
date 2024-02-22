#importando o BD
import sqlite3

#conexão com o arquivo que tem o mesmo nome criado no BD
conexao = sqlite3.connect('banco')

#passando a conexão para uma nova variável
cursor = conexao.cursor()

#Criando a tabela
#cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#Caso queira criar uma nova tabela ou rodar novamente o código, basta comentar a tabela ja criada


#Utilizando ALTER para alterar informações da tabela
#cursor.execute('ALTER TABLE usuarios RENAME TO usuario')
#Após atualizar, deve ser comentado

#cursor.execute('ALTER TABLE usuario ADD COLUMN telefoni INT')
#cursor.execute('ALTER TABLE usuario RENAME COLUMN telefoni TO telefone')

#Criando uma nova tabela
#cursor.execute('CREATE TABLE produtos(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')

#Deletando uma tabela
#cursor.execute('DROP TABLE produtos')

#Inserindo dados
#cursor.execute("INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (1, 'Lidia', 'Sapé', 'lidia@lidia.com', 123)")
#cursor.execute("INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (2, 'Patricia', 'Sapé', 'patricia@patricia.com', 234)")
#cursor.execute("INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (3, 'Kao', 'Sapé', 'kao@kao.com', 345)")
#cursor.execute("INSERT INTO usuario(id,nome,endereco,email,telefone) VALUES (4, 'Jose Maria', 'João Pessoa', 'jose@maria.com', 456)")

#Deletando item
#gitcursor.execute('DELETE FROM usuario where id=1')

#Alterando os dados
#cursor.execute('UPDATE usuario SET endereco ="China" WHERE NOME ="Kao"')

#Visualizar informações com SELECT
#dados = cursor.execute('SELECT * FROM usuario') #pode ser colocado o que quer
#dados = cursor.execute('SELECT nome,telefone FROM usuario WHERE id>2') 

#ORDER BY
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome') #ordenando os dados
#ORDER BY - DESC
#dados = cursor.execute('SELECT * FROM usuario ORDER BY nome DESC') #ordenando os dados de forma decrescente

#LIMIT e DISTINCT
#dados = cursor.execute('SELECT * FROM usuario LIMIT 3') #limitando ate onde pode ser visto
dados = cursor.execute('SELECT DISTINCT * FROM usuario') #retorna apenas valores que nao tem repetições, pode ser usado junto com o LIMIT

for usuario in dados:
    print(usuario)



#indicando que serão enviadas novas informações
conexao.commit()

#finaliza para não gerar conflitos
#conexao.close