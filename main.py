import random

print("Introduzca la cantidad total de la compra")
cantidad: float = float(input())
descuento: float = 0

if cantidad < 100:
    print("No se le aplica promoción.")
else:
    print("Se le aplica promoción:\n")
    print("                 COLOR                   DESCUENTO\n")
    print("              BOLA BLANCA                NO TIENE")
    print("              BOLA ROJA                10 POR CIENTO")
    print("              BOLA AZUL                20 POR CIENTO")
    print("              BOLA VERDE               25 POR CIENTO")
    print("              BOLA AMARILLA            50 POR CIENTO")

    bola: int = random.randint(1, 5)

    match bola:
        case 1:
            print("Le ha tocado la bola blanca")
            descuento = 0
        case 2:
            print("Le ha tocado la bola roja")
            descuento = 0.1
        case 3:
            print("Le ha tocado la bola azul")
            descuento = 0.2
        case 4:
            print("Le ha tocado la bola verde")
            descuento = 0.25
        case 5:
            print("Le ha tocado la bola amarilla")
            descuento = 0.5
        case _:
            descuento = 0

print(f"El valor final a pagar es de {(cantidad - (cantidad * descuento))}€")