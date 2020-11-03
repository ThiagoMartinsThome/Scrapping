import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def color_grafica():
    # pregunto usuario color grafica
    pregunta = input("que color quieres usar: r,b,o,g?")


    # creo una simple grafica de prueba
    X= np.random.randn(50)
    Y= np.random.randn(50)

    plt.scatter(X,Y,color=pregunta)
    plt.title("Grafica de puntos")
    plt.show()

#pregunto de nuevo
pregunta_fin = input("quieres ver la grafica Y/N")
try:
    if pregunta_fin == "Y":
        color_grafica()
    elif pregunta_fin == "N":
        print ("gracias por usar el programma")
except:
        print("An exception occurred")

# Hola Lalo#####

