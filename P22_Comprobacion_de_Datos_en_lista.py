colores = ('azul','amarillo','blanco','negro') #Se crea la tupla

color = input("Introduce un color: ") #Se le pide al usuario un color

if color in colores: #Se verifica si el color se encuentra en la tupla
    print("El color " + color + " esta en la tupla") #Se imprime si el dato esta dentro de la tupla
else:
    print("Color no admitido")