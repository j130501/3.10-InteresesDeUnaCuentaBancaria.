class CuentaBancaria:
    def __init__(self, saldo):
        self.saldo = saldo

    def calcular_interes(self):
        if self.saldo < 10000.00:
            self.saldo *= 1.03
        else:
            self.saldo *= 1.04

    def mostrar_saldo(self):
        print("Saldo final es %5.2f" % self.saldo)