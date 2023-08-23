if __name__ == "__main__":
    print("iniciando")
    print("...")
    respuesta = open("respuesta.txt", "w")

    x1 = float(input("Valor X1"))
    if x1 % 1 == 0:
        x1 = int(x1)
    Z1 = float(input("valor Z1"))
    if Z1 % 1 == 0:
        Z1 = int(Z1)
    x2 = float(input("valor x2"))
    if x2 % 1 == 0:
        x2 = int(x2)
    Z2 = float(input("valor Z2"))
    if Z2 % 1 == 0:
        Z2 = int(Z2)
    pasos = float(input("Ingrese proifundidad de desvaste"))
    if pasos % 1 == 0:
        pasos = int(pasos)

    resta = x1 - x2
    if resta % pasos != 0:
        print("Los pasoss no son un divisor del diametro a calar")
    else:
        vuelta = 1
        while True:
            XActual = x1 - (pasos * vuelta)
            print("Vuelta a X =", XActual)
            respuesta.write("G01 X{0}\n".format(XActual))
            respuesta.write("G01 Z{0}\n".format(Z2))
            respuesta.write("G00 x{0} Z{1}\n".format(XActual+1, Z1))
            vuelta += 1
            if XActual == x2:
                print("Fin de programa")
                break

    respuesta.close()
