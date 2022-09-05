colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja'] #Se declara la lista con los arrays

n1 = colores.pop(1) #Se elimina el valor en el lugar 1 de la lista y se almacena en n1
n2 = colores.pop(7) #Se elimina el valor en el lugar 8 de la lista y se almacena en n2

print(colores) #Se imprime la lista para verificar los cambios

colores2 = n1 + " y " + n2 + " fueron eliminados de la lista" #Se cre una nueva lista con los datos eliminados anteriormente
print(colores2) #Se imprime la lista con los valores eliminados de la otra