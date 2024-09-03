from InteresCuentaBancaria import CuentaBancaria
def main():
    saldo_inicial = float(input("Dame saldo actual: "))
    cuenta = CuentaBancaria(saldo_inicial)
    cuenta.calcular_interes()
    cuenta.mostrar_saldo()

if __name__ == "__main__":
    main()