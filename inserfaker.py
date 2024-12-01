from classes import Funcionario, Hospede, PessoaDados
from bd import conectar_banco_dados, obter_cursor

mydb = conectar_banco_dados()
mycursor = obter_cursor(mydb)

conectar_banco_dados()
mycursor.execute ()

#save