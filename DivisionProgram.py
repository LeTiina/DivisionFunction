
def divide_list(lista:list):
    negatiiviset = []
    positiiviset = []
    for i in lista:
        if i < 0:
            negatiiviset.append(i)
        if i >= 0:
            positiiviset.append(i)
    return negatiiviset,positiiviset



lista = [1, -1, 2, -3, 5, -1, 1, 1, 9]
lista1, lista2 = divide_list(lista)
print(lista1)
print(lista2)