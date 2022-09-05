x = 0
while x < 30: #Se ejecutara el bucle simpre y cuando 'x' < 30
    x += 1 #Se incrementa en 1
    if x == 4 or x == 6 or x == 10: #Sea x = 4, 6 o 10 entrara en la siguiente condicion
        print("Se salto el valor " + str(x)) #Se saltara el valor de x 
        continue #Se regresa al inicio del ciclo
    if x == 15:
        print("Se rompio la ejecucion del bucle cuando x valia " + str(x)) 
        break #Se termina la ejecucion del ciclo
    print("El valor del bucle es: " + str(x))