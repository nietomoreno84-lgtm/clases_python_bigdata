# *
# **
# ***
# ****
# *****
# ******
# *******




altura = 6

for i in range(altura):
    espacios = " " * (altura - i - 1)
    if i % 2 == 0:
        relleno = "o"  # bolas
    else:
        relleno = "*"
    linea = (relleno * (2 * i + 1))
    print(espacios + linea)

# Tronco
print(" " * (altura - 1) + "|")

altura = 8

for i in range(altura):
    espacios = " " * (altura - i - 1)
    
    linea = ""
    for j in range(2 * i + 1):
        if (i + j) % 3 == 0:
            linea += "\033[91m●\033[0m"  # rojo (bola)
        elif (i + j) % 3 == 1:
            linea += "\033[93m●\033[0m"  # amarillo
        else:
            linea += "\033[92m*\033[0m"  # verde (hojas)
    
    print(espacios + linea)

# Tronco
print(" " * (altura - 1) + "\033[33m|\033[0m")

import time
import os
import random

altura = 8

def dibujar_arbol():
    os.system("cls" if os.name == "nt" else "clear")
    
    # Estrella
    print(" " * (altura - 1) + "\033[93m★\033[0m")
    
    # Árbol
    for i in range(altura):
        espacios = " " * (altura - i - 1)
        linea = ""
        
        for j in range(2 * i + 1):
            r = random.randint(0, 2)
            if r == 0:
                linea += "\033[91m●\033[0m"  # rojo
            elif r == 1:
                linea += "\033[94m●\033[0m"  # azul
            else:
                linea += "\033[92m*\033[0m"  # verde
        
        print(espacios + linea)
    
    # Tronco
    print(" " * (altura - 1) + "\033[33m|\033[0m")
    
    # Regalos
    print(" " * (altura - 3) + "\033[95m[ ]\033[0m \033[96m[ ]\033[0m")

# Animación
while True:
    dibujar_arbol()
    time.sleep(0.5)


    
