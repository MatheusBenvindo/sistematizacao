from classes import Funcionario, Hospede, PessoaDados
from bd import conectar_banco_dados, obter_cursor

# Coleta de dados do usuário
nome_pessoa = input("Digite o nome da pessoa: ")
email_pessoa = input("Digite o email da pessoa: ")

tipo_pessoa = int(input("[1] FUNCIONARIO\n[2] HOSPEDE\n\nOPÇÃO: "))
if tipo_pessoa == 1:
    pessoa = Funcionario(1, nome_pessoa, email_pessoa)
    tipo_pessoa_str = 1
elif tipo_pessoa == 2:
    pessoa = Hospede(2, nome_pessoa, email_pessoa)
    tipo_pessoa_str = 2
else:
    print("OPÇÃO INVÁLIDA, DIGITE 1 OU 2")
    quit()  # Sai do programa se a opção for inválida

print(f"Tipo de pessoa: {tipo_pessoa_str}")
print(f"Nome: {pessoa.get_nome()}")
print(f"Email: {pessoa.get_email()}")

# Conectando ao banco de dados
mydb = conectar_banco_dados()
mycursor = obter_cursor(mydb)

if mycursor:
     # Inserindo os dados da pessoa na tabela PESSOA
        sql_pessoa = "INSERT INTO Pessoa (tipo_pessoa, nome_pessoa, email_pessoa) VALUES (%s, %s, %s)"
        val_pessoa = (tipo_pessoa, nome_pessoa, email_pessoa)
        mycursor.execute(sql_pessoa, val_pessoa)
        mydb.commit()

        # Obtendo o último idPessoa inserido
        id_pessoa = mycursor.lastrowid

        # Inserindo na tabela específica
        if tipo_pessoa == 1:
            sql_funcionario = "INSERT INTO Funcionario (idPessoa, nome_funcionario) VALUES (%s, %s)"
            val_funcionario = (id_pessoa, nome_pessoa)
            mycursor.execute(sql_funcionario, val_funcionario)
        elif tipo_pessoa == 2:
            sql_hospede = "INSERT INTO Hospede (idPessoa, nome_hospede, email_hospede) VALUES (%s, %s, %s)"
            val_hospede = (id_pessoa, nome_pessoa, email_pessoa)
            mycursor.execute(sql_hospede, val_hospede)

        mydb.commit()
        print("Dados inseridos com sucesso.")
else:
    print("Erro ao conectar ao banco de dados.")


#save