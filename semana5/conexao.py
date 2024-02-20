#importando o BD
import sqlite3

#conexão com o arquivo que tem o mesmo nome criado no BD
conexao = sqlite3.connect('bancodedados')

#passando a conexão para uma nova variável
cursor = conexao.cursor()

#Criando a tabela
cursor.execute('CREATE TABLE usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(100));')
#Caso queira criar uma nova tabela, basta comentar a tabela ja criada

#indicando que serão enviadas novas informações
conexao.commit()

#finaliza para não gerar conflitos
conexao.close