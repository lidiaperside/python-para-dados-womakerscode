#importando o BD
import sqlite3

#conexão com o arquivo que tem o mesmo nome criado no BD
conexao = sqlite3.connect('banco.db')

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
cursor.execute('DROP TABLE produtos')

#indicando que serão enviadas novas informações
conexao.commit()

#finaliza para não gerar conflitos
#conexao.close