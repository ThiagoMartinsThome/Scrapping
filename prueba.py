import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import funcines as fc


#pregunta de inicio
pregunta_fin = input("quieres ver la grafica Y/N")
try:
    if pregunta_fin == "Y":
        fc.color_grafica()
    elif pregunta_fin == "N":
        print ("gracias por usar el programma")
except:
        print("An exception occurred")

