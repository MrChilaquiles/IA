def colores(*args):
	print('El color', args[1], 'es mi favorito.', 'El color', args[0], 'tampoco está mal.')

colores("tinto","azul")

def sum(*args): #Se define con args para no especificar la cantidad
	t = 0 #Se crea la variable para que lleve el conteo
	for x in args: 
		t = t + x #Se suma lo obtenido con lo anterior
	print("La suma es: ",t)

sum(10,11,12,13,14)