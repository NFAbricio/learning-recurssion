def soma(lista):
    if not lista:
        return 0
    else:
        num1 = lista[0]
        resto_da_lista = lista[1::]
        return num1 + soma(resto_da_lista)
      



# um teste a seguir
# b = soma([1, 4, 6, 7, 8])
# print (b)


