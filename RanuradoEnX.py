import tkinter

def generar_gcode():
    etiquetaFinal["text"] = "iniciando"
    respuesta = open("respuesta.txt", "w")

    x1 = int(valX1.get())
    Z1 = int(valZ1.get())
    x2 = int(valX2.get())
    Z2 = int(valZ2.get())
    pasos = int(valPasada.get())

    resta = x1 - x2
    if resta % pasos != 0:
        etiquetaFinal["bg"] = "yellow"
        etiquetaFinal["text"] = "Los pasoss no son un divisor del diametro a calar"
    else:
        vuelta = 1
        while True:
            XActual = x1 - (pasos * vuelta)
            etiquetaFinal["text"] = "Vuelta a X =", XActual
            respuesta.write("G01 X{0}\n".format(XActual))
            respuesta.write("G01 Z{0}\n".format(Z2))
            respuesta.write("G00 x{0} Z{1}\n".format(XActual+1, Z1))
            vuelta += 1
            if XActual == x2:
                etiquetaFinal["bg"] = "green"
                etiquetaFinal["text"] = "Terminado: respuestas.txt"
                break

    respuesta.close()

ventana = tkinter.Tk()
ventana.geometry("550x400")
ventana.configure(bg = "gray")

titulo = tkinter.Label(ventana, text = "Generador de ranurados en eje X", font = "Arial 16", bg = "gray")
textX1 = tkinter.Label(ventana, text = "X-Inicio", bg = "gray", font = "Arial 16")
textZ1 = tkinter.Label(ventana, text = "Z-Inicio", bg = "gray", font = "Arial 16")
textX2 = tkinter.Label(ventana, text = "X-Final", bg = "gray", font = "Arial 16")
textZ2 = tkinter.Label(ventana, text = "Z-final", bg = "gray", font = "Arial 16")
textoPaso = tkinter.Label(ventana, text = "mm por pasada", bg = "gray", font = "Arial 16")
etiquetaFinal = tkinter.Label(ventana, bg = "gray")

valX1 = tkinter.Entry(ventana, font = "Arial 20", bg = "white")
valZ1 = tkinter.Entry(ventana, font = "Arial 20", bg = "white")
valX2 = tkinter.Entry(ventana, font = "Arial 20", bg = "white")
valZ2 = tkinter.Entry(ventana, font = "Arial 20", bg = "white")
valPasada = tkinter.Entry(ventana, font = "Arial 20", bg = "white")

botonCalcular = tkinter.Button(ventana, text= "Generar G-code", command = generar_gcode)


titulo.grid(row = 0, column=1)
titulo.config(width="30", height="2")

textX1.grid(row = 1, column= 0)
textX1.config(width="8", height="2")
valX1.grid(row = 1, column = 1)

textZ1.grid(row = 2, column=0)
textZ1.config(width="8", height="2")
valZ1.grid(row=2, column=1)

textX2.grid(row = 3, column= 0)
textX2.config(width="8", height="2")
valX2.grid(row = 3, column = 1)

textZ2.grid(row = 4, column=0)
textZ2.config(width="8", height="2")
valZ2.grid(row=4, column=1)

textoPaso.grid(row=5, column=0)
textoPaso.config(width="13", height="2")
valPasada.grid(row=5, column=1)

botonCalcular.grid(row=6, column=1)
etiquetaFinal.grid(row=7,column=1)
etiquetaFinal.config(height="4")



ventana.mainloop()