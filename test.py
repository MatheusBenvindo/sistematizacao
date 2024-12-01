import mysql.connector
from classes import Funcionario, Hospede, Quarto, Hotel, Reserva, PessoaDados
from bd import BD, obter_cursor


#SISTEMA DE CADASTRO
def main():
    nome_pessoa = input("Digite o nome da pessoa: ")
    email_pessoa = input("Digite o email da pessoa: ")

    tipo_pessoa = int(input("[1] FUNCIONARIO\n[2] HOSPEDE"))
    if tipo_pessoa == '1':
        pessoa = Funcionario(1, nome_pessoa, email_pessoa)  # Use um ID fictício ou ajuste conforme necessário
        tipo_pessoa = "FUNCIONARIO"
    elif tipo_pessoa == '2':
        pessoa = Hospede(2, nome_pessoa, email_pessoa)  # Use um ID fictício ou ajuste conforme necessário
        tipo_pessoa = "HOSPEDE"
    else: 
        print("OPÇÃO INVÁLIDA, DIGITE 1 OU 2")
        return

    print(f"Tipo de pessoa: {tipo_pessoa}")
    print(f"Nome: {pessoa.get_nome()}")
    print(f"Email: {pessoa.get_email()}")
    quarto_numero = int(input("Digite o número do quarto: "))
    quarto_tipo = input("Digite o tipo do quarto: ")
    
    print(f"Tipo de pessoa: {tipo_pessoa}")
    print(f"Nome: {pessoa.get_nome()}")
    print(f"Email: {pessoa.get_email()}")

#INSERÇÃO DO CADASTRADO NO BANCO DE DADOS DO USUÁRIO ------
    obter_cursor.execute (f"""INSERT INTO PESSOA VALUES 
    {tipo_pessoa}, 
    {nome_pessoa}, 
    {email_pessoa}""")

    quarto = Quarto(quarto_numero, quarto_tipo)

    #INSERÇÃO NO BANCO DE DADOS ------
    # Adicionar quarto ao hotel
    obter_cursor.execute (f"""INSERT VALUES {tipo_pessoa}
""")
    funcionario.add_quarto(hotel, quarto)

    # Registrar hóspede
    funcionario.registrar_hospede(hotel, hospede)

    # Inserir hóspede no banco de dados
    cursor.execute("INSERT INTO Hospede (id, nomehospede, email_hospede) VALUES (%s, %s, %s)", (hospede.get_id(), hospede.get_nome(), hospede.get_email()))
    conexao.commit()

    # Fazer uma reserva
    reserva = Reserva(hospede, quarto)
    hospede.fazer_reserva(reserva)

    # Inserir reserva no banco de dados
    cursor.execute("INSERT INTO Reserva (id, hospede_id, quarto_id) VALUES (%s, %s, %s)", (reserva.get_id(), hospede.get_id(), quarto.get_id()))
    conexao.commit()

    # Fechar a conexão com o banco de dados
    conexao.close()
    print("Dados inseridos com sucesso no banco de dados.")

if __name__ == "__main__":
    main()

#save