def color_grafica():
    # pregunto usuario color grafica
    pregunta = input("que color quieres usar: r,b,c,g,y?")
    
    # creo lista de colores
    colores = ["r","b","c","g","y"]
    
    # uso if / else para evitar fallos
    if pregunta not in colores:
        print("Los colores son r,b,c,g,y")
        color_grafica()
    
    else:
        # creo una simple grafica de prueba
        X= np.random.randn(50)
        Y= np.random.randn(50)

        plt.scatter(X,Y,c=pregunta)
        plt.title("Grafica de puntos")
        plt.show()

