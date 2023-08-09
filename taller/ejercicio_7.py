class CuentaBancaria:
    def __init__(self, numero_cuenta, propietarios, balance):
        self.numero_cuenta = numero_cuenta
        self.propietarios = propietarios
        self.balance = balance

if __name__ == "__main__":
    numero_cuenta = "958903402"
    propietarios = ["sandra", "laura", "liliana"]
    balance = 1000

cuenta = CuentaBancaria(numero_cuenta, propietarios, balance)

print("Número de cuenta: ", cuenta.numero_cuenta)
print("Propietarios: ", cuenta.propietarios)
print("Balance: ", cuenta.balance)