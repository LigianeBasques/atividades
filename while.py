
lista = []
entrada = ''
parar_agora = False

#
while parar_agora != True:
    entrada = input('Digite o nome de uma fruta:')
    if entrada == 'parar':
        parar_agora = True
    lista.append(entrada)
    print(lista)



