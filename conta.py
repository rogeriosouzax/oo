

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def deposita(self, valor):
        self.__saldo += valor

    def saque(self, valor):
        self.__saldo -= valor

    def extrato(self):
        print("Caro cliente {1}, o saldo de sua conta é {0} reais.".format(self.__saldo, self.__titular))

    def transferencia(self, conta_destino, valor):
        self.saque(valor)
        conta_destino.deposita(valor)