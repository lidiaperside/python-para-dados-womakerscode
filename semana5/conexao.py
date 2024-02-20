#importando o BD
import sqlite3

#conexão com o arquivo que tem o mesmo nome criado no BD
conexao = sqlite3.connect('bancodedados')

#passando a conexão para uma nova variável
cursor = conexao.cursor()

cursor.execute('')

#indicando que serão enviadas novas informações
conexao.commit()

#finaliza para não gerar conflitos
conexao.close