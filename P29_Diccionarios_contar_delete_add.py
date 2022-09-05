teclado1 = {
	'Categoría': 'Teclados',
	'Modelo': 'HyperX Alloy FPS Pro',
	'Precio': '89,99'
}

teclado2 = {
	'Categoría': 'Teclados',
	'Modelo': 'Corsair K55 RGB',
	'Precio': '59,99'
}

del teclado1 #Se elimina teclado1

del teclado2["Categoría"] #Se elimina la subcategoria 'Categoria'
del teclado2["Precio"] #Se elimina la subcategoria 'Precio'
print(teclado2) #Se imprime el restante de teclado2