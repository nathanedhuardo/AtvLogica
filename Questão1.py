# Conjunto seria um coleção de elementos únicos, ou seja, não teria duplicatas, então são usados para armazenar uma coleção de itens de forma que cada item dele só apareça uma vez.

conjunto = {1, 2, 3, 4, 5}

conjunto.add(6)

listacomDuplicadas = [1, 1, 2, 2, 3, 3, 4, 4]
conjuntosemDuplicadas = set(listacomDuplicadas)

print(conjunto)
print(conjuntosemDuplicadas)