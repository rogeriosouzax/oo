

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__codigo_banco = "001"

    def deposita(self, valor):
        self.__saldo += valor

    def __saque_autorizado(self, valor_saque):
        valor_disponivel_saque = self.saldo + self.limite
        return valor_saque <= valor_disponivel_saque

    def saque(self, valor):
        if self.__saque_autorizado(valor):
            self.__saldo -= valor
        else:
            print("Não é possível realizar o saque no valor: {}!".format(valor))

    def extrato(self):
        print("Caro cliente {1}, o saldo de sua conta é {0} reais.".format(self.__saldo, self.__titular))

    def transferencia(self, conta_destino, valor):
        self.saque(valor)
        conta_destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"