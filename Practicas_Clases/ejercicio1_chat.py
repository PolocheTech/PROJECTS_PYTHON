class Cliente():

    def __init__(self, nombre, valor_compra):
        self.nombre = nombre
        self.valor_compra = valor_compra
    
    def calcular_descuento(self):
        descuento_total = 0
        if self.valor_compra >= 200000:
            return self.valor_compra * 0.20
        elif self.valor_compra < 200000:
            return self.valor_compra * 0.05
        else:
            print("Valor ingresado incorrecto")

    def calcular_total_pagar(self):
        descuento = self.calcular_descuento()
        return self.valor_compra - descuento

def crear_clientes():
    nombre_nuevo_usuario = str(input("Ingresa tu nombre\n>>> "))
    valor_compras = validar_valor_compra()
    cliente_nuevo = Cliente(nombre_nuevo_usuario, valor_compras)
    return cliente_nuevo

def validar_valor_compra():
    while True:
        try:
            valor = float(input("Ingresa el valor de las compras\n>>> "))
            if valor < 0:
                print("Error: el valor no puede ser negativo.")
            else:
                return valor
        except ValueError:
            print("Error: debes ingresar un número válido.")

def main():
    cliente = crear_clientes()

    descuento = cliente.calcular_descuento()
    total = cliente.calcular_total_pagar()

    print(f"Descuento aplicado: {descuento}")
    print(f"Total a pagar: {total}")

main()