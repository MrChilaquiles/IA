# Subir una colina en busca de una función objetiva unidimensional

de numpy importación asarray

de numpy.al azar importación randn

de numpy.al azar importación rand

de numpy.al azar importación semilla

# Función objetiva

def objetivo(x):

volver x[[0]**2.0

# Algoritmo de búsqueda local de escalada de colinas

def escalada(objetivo, bounds, n_iteraciones, tamaño_paso):

# Generar un punto inicial

solución = bounds[[:, 0] + rand(len(bounds)) * (bounds[[:, 1] – bounds[[:, 0])

# Evaluar el punto inicial

solution_eval = objetivo(solución)

# Corre la subida de la colina

para i en rango(n_iteraciones):

# dar un paso

candidato = solución + randn(len(bounds)) * paso_tamaño

# Evaluar el punto de candidato

candidata_eval = objetivo(candidato)

# comprobar si debemos mantener el nuevo punto

si candidata_eval <= solution_eval:

# Almacena el nuevo punto

solución, solution_eval = candidato, candidato_eval

# Reportar el progreso…

imprimir(‘>%d f(%s) = %.5f’ % (i, solución, solution_eval))

volver [[solución, solution_eval]

# Sembrar el generador de números pseudoaleatorios

semilla(5)

# Definir el rango de entrada

bounds = asarray([[[[–5.0, 5.0]])

# Definir las iteraciones totales

n_iteraciones = 1000

# Definir el tamaño máximo del paso

tamaño_paso = 0.1

# realizar la búsqueda de la escalada de la colina

mejor, puntuación = escalada(objetivo, bounds, n_iteraciones, tamaño_paso)

imprimir(«¡Hecho!)

imprimir(«f(%s) = %f % (mejor, puntuación))
