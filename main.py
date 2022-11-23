print("Introduzla la cantidad total de la compra")
cantidad: float = input()

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