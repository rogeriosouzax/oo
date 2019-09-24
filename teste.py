from conta import Conta
from cliente import Cliente
from datas import Data


def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta


def deposita(conta, valor):
    conta["saldo"] += valor


def saque(conta, valor):
    conta["saldo"] -= valor


def extrato(conta):
    print("O saldo de sua conta é {} reais.".format(conta["saldo"]))


conta = Conta(123, "Rogerio", 1000000.0, 7000.0)
conta2 = Conta(155, "Google", 10000000000.0, 5000000.0)

conta2.transferencia(conta, 32000.0)

conta.extrato()
conta2.extrato()

