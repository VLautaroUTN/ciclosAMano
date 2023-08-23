import tkinter

def generar_gcode():
    print("iniciando")
    print("...")
    respuesta = open("respuesta.txt", "w")

    x1 = 56#int(input("Valor X1"))
    Z1 = 0#int(input("valor Z1"))
    x2 = 10#int(input("valor x2"))
    Z2 = -8#int(input("valor Z2"))
    pasos = 2#int(input("Ingrese proifundidad de desvaste"))

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

ventana = tkinter.Tk()
ventana.geometry("400x300")

etiqueta = tkinter.Label(ventana, text = "Generador de ranurados en eje X", bg = "white", font = "Arial 16")
etiqueta.pack(side = tkinter.TOP)

valX1 = tkinter.Entry(ventana, font = "Arial 20", bg = "gray")
valX1.pack()
valZ1 = tkinter.Entry(ventana, font = "Arial 20", bg = "gray")
valZ1.pack()
valX2 = tkinter.Entry(ventana, font = "Arial 20", bg = "gray")
valX2.pack()
valZ2 = tkinter.Entry(ventana, font = "Arial 20", bg = "gray")
valZ2.pack()


botonCalcular = tkinter.Button(ventana, text= "Generar G-code", command = generar_gcode)
botonCalcular.pack(side = tkinter.BOTTOM)

ventana.mainloop()