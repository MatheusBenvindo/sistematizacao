import mysql.connector

def conectar_banco_dados():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="HOTEL_TESTE"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None

def obter_cursor(mydb):
    if mydb is not None and mydb.is_connected():
        return mydb.cursor()
    else:
        print("Não foi possível obter o cursor. A conexão com o banco de dados não foi estabelecida.")
        return None

# Conectar ao banco de dados
mydb = conectar_banco_dados()
mycursor = obter_cursor(mydb)

if mycursor:
    try:
        mycursor.execute("""
        CREATE TABLE Pessoa (
            idPessoa INT PRIMARY KEY AUTO_INCREMENT,
            tipo_pessoa INT NOT NULL,
            nome_pessoa VARCHAR(255) NOT NULL,
            email_pessoa VARCHAR(255) NOT NULL
        );""")
        
        mycursor.execute("""
        CREATE TABLE Funcionario (
            idFuncionario INT PRIMARY KEY AUTO_INCREMENT,
            nome_funcionario VARCHAR(255) NOT NULL,
            idPessoa INT,
            FOREIGN KEY (idPessoa) REFERENCES Pessoa(idPessoa)
        );""")
        
        mycursor.execute("""
        CREATE TABLE Hospede (
            idHospede INT PRIMARY KEY AUTO_INCREMENT,
            nome_hospede VARCHAR(255) NOT NULL,
            email_hospede VARCHAR(255) NOT NULL,
            idPessoa INT,
            FOREIGN KEY (idPessoa) REFERENCES Pessoa(idPessoa)
        );""")
        
        mycursor.execute("""
        CREATE TABLE Quarto (
            idQuarto INT PRIMARY KEY AUTO_INCREMENT,
            numero INT NOT NULL,
            tipo VARCHAR(255) NOT NULL,
            disponivel BOOLEAN NOT NULL
        );""")
        
        mycursor.execute("""
        CREATE TABLE Reserva (
            idReserva INT PRIMARY KEY AUTO_INCREMENT,
            hospede_id INT, 
            quarto_id INT,
            FOREIGN KEY (hospede_id) REFERENCES Hospede(idHospede),
            FOREIGN KEY (quarto_id) REFERENCES Quarto(idQuarto)
        );""")
    
        mycursor.execute("""
        CREATE TABLE Hospede_Reserva (
            hospede_id INT,
            reserva_id INT,
            PRIMARY KEY (hospede_id, reserva_id),
            FOREIGN KEY (hospede_id) REFERENCES Hospede(idHospede),
            FOREIGN KEY (reserva_id) REFERENCES Reserva(idReserva)
        );""")
        
        print("Tabelas criadas com sucesso.")

    except mysql.connector.Error as err:
        print(f"Erro ao criar tabelas: {err}")

    finally:
        mycursor.close()
        mydb.close()
else:
    print("A conexão com o banco de dados falhou.")