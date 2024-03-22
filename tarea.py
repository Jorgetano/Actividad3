# ///////////////////LISTAS////////////////

lista = list(range(1, 11))

print("Lista original:", lista)

lista_ascendente = sorted(lista)
print("Lista ordenada ascendente:", lista_ascendente)

lista_descendente = sorted(lista, reverse=True)
print("Lista ordenada descendente:", lista_descendente)

minimo = min(lista)
print("Número más pequeño:", minimo)

maximo = max(lista)
print("Número más grande:", maximo)

contador_5 = lista.count(5)
print("Número de veces que aparece el 5:", contador_5)

lista.remove(5)
print("Lista sin el número 5:", lista)

lista.append(11)
print("Lista con el número 11 agregado:", lista)

# ///////////////////TUPLAS////////////////

tupla = ("Hola", "mundo", "Python")

print("Tupla original:", tupla)

tupla_ordenada = tuple(sorted(tupla))
print("Tupla ordenada alfabéticamente:", tupla_ordenada)

primera_palabra = tupla[0]
print("Primera palabra en la tupla:", primera_palabra)

ultima_palabra = tupla[-1]
print("Última palabra en la tupla:", ultima_palabra)

numero_palabras = len(tupla)
print("Número de palabras en la tupla:", numero_palabras)

tupla_sin_mundo = tuple(word for word in tupla if word != "mundo")
print("Tupla sin la palabra 'mundo':", tupla_sin_mundo)

tupla_con_hola = tupla + ("Hola",)
print("Tupla con la palabra 'Hola' agregada:", tupla_con_hola)

# ///////////////////CONJUNTOS////////////////

conjunto_numeros = set(range(1, 11))

print("Conjunto de números del 1 al 10:", conjunto_numeros)

conjunto_numeros.add(11)

conjunto_numeros.remove(5)

num_elementos = len(conjunto_numeros)
print("Número de elementos en el conjunto:", num_elementos)

print("¿El número 5 está en el conjunto?", 5 in conjunto_numeros)

print("¿El número 11 está en el conjunto?", 11 in conjunto_numeros)

conjunto_palabras = {"Hola", "mundo", "Python"}

print("Conjunto de palabras:", conjunto_palabras)

print("¿La palabra 'Hola' está en el conjunto?", "Hola" in conjunto_palabras)

print("¿La palabra 'mundo' está en el conjunto?", "mundo" in conjunto_palabras)

# ///////////////////DICCIONARIOS////////////////

dias_semana = {
    "Lunes": 1,
    "Martes": 2,
    "Miércoles": 3,
    "Jueves": 4,
    "Viernes": 5,
    "Sábado": 6,
    "Domingo": 7
}

print("Diccionario de días de la semana:", dias_semana)

numero_lunes = dias_semana["Lunes"]
print("Número del día de la semana 'Lunes':", numero_lunes)
