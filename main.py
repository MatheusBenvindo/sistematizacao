from classes import Pessoa, Funcionario, Hospede, Hotel, Quarto, Reserva
from bd import obter_cursor, BD


















def main():
    # Criar instâncias das classes
    hotel = Hotel()
    funcionario = Funcionario(1, "Alice", "alice@example.com")
    hospede = Hospede(2, "Bob", "bob@example.com")
    quarto1 = Quarto(101, "Single")
    quarto2 = Quarto(102, "Double")

    # Adicionar quartos ao hotel
    funcionario.add_quarto(hotel, quarto1)
    funcionario.add_quarto(hotel, quarto2)

    # Registrar hóspede
    funcionario.registrar_hospede(hotel, hospede)

    # Fazer uma reserva
    reserva1 = Reserva(hospede, quarto1)
    hospede.fazer_reserva(reserva1)
    quarto1.reservar()

    # Consultar reservas do hóspede
    reservas = hospede.consultar_reservas()
    print(f"Hospede {hospede.get_nome()} tem {len(reservas)} reservas.")

    # Cancelar uma reserva
    hospede.cancelar_reserva(reserva1)
    quarto1.liberar()
    funcionario.cancelar_reserva(hotel, reserva1)

    # Consultar reservas do hóspede novamente
    reservas = hospede.consultar_reservas()
    print(f"Hospede {hospede.get_nome()} tem {len(reservas)} reservas.")

if __name__ == "__main__":
    main()
    Pessoa.get_nome()
    Pessoa.get_email()

    def BD (bd):

        global mydb = _mysql_connector.connect(
        host = "localhost",
        user = "root",
        password = ""

        mycursor = mydb.cursor()
    )

    mycursor.execute

#save