import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def color_grafica():
    # pregunto usuario color grafica
    pregunta = input("que color quieres usar: r, b, o, g: ")


    # creo una simple grafica de prueba
    x = np.random.randn(50)
    y = np.random.randn(50)

    plt.scatter(x, y, color=pregunta)

    # creo una regression lineal en base al scatter plot
    s, i = np.polyfit(x, y, 1) # s = slope, i = intercept
    plt.plot(x, s*x + i)

    plt.title("Grafica de puntos")
    plt.show()

# pregunto de nuevo
pregunta_fin = input("Quieres ver la grafica Y/N: ")
try:
    if pregunta_fin == "Y":
        color_grafica()
    elif pregunta_fin == "N":
        print("Gracias por usar el programma")
except:
        print("An exception occurred")



# nuevo cambio"