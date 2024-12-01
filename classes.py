class PessoaDados:
    def __init__(self, tipo_pessoa, nome, email):
        self.__nome = nome
        self.__email = email
        self.__tipo_pessoa = tipo_pessoa

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

class Funcionario(PessoaDados):
    def add_quarto(self, hotel, quarto):
        hotel.add_quarto(quarto)

    def remover_quarto(self, hotel, quarto):
        hotel.remover_quarto(quarto)

    def registrar_hospede(self, hotel, hospede):
        hotel.registrar_hospede(hospede)

    def cancelar_reserva(self, hotel, reserva):
        hotel.cancelar_reserva(reserva)

class Hospede(PessoaDados):
    def __init__(self, id, nome, email):
        super().__init__(id, nome, email)
        self.__reservas = []

    def fazer_reserva(self, reserva):
        self.__reservas.append(reserva)

    def cancelar_reserva(self, reserva):
        self.__reservas.remove(reserva)

    def consultar_reservas(self):
        return self.__reservas

class Hotel:
    def __init__(self):
        self.__quartos = []
        self.__hospedes = []
        self.__reservas = []

    def add_quarto(self, quarto):
        self.__quartos.append(quarto)

    def remover_quarto(self, quarto):
        self.__quartos.remove(quarto)

    def registrar_hospede(self, hospede):
        self.__hospedes.append(hospede)

    def cancelar_reserva(self, reserva):
        self.__reservas.remove(reserva)

class Quarto:
    def __init__(self, numero, tipo, disponivel=True):
        self.__numero = numero
        self.__tipo = tipo
        self.__disponivel = disponivel

    def reservar(self):
        self.__disponivel = False

    def liberar(self):
        self.__disponivel = True

    def esta_disponivel(self):
        return self.__disponivel

class Reserva:
    def __init__(self, hospede, quarto):
        self.__hospede = hospede
        self.__quarto = quarto

#save