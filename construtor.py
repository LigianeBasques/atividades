#usando o construtor list()

#fruta = list(('maça','uva','buriti','abacaba')) # o construtor lis() cria uma lista
#print(fruta)

# adicionando um elemento ou uma lista em lista

#fruta = ['maça','uva','buriti','abacaba']
#fruta.append('laranja') # esse metodo adiciona um item no final da lista.

#print(fruta)

#a = ['maça','banana','abacate']
#b = ['Ford', 'BMW', 'Volvo']
#a.append(b)
#print(a)

# metodo para remover elementos da lista

#fruta = ['maça','banana','abacate']
#fruta.clear()
#print(fruta)

#O método retorna uma cópia da lista especificada.copy()

#frutas = ['apple', 'banana', 'cherry', 'orange']
#x = frutas.copy()
#print(frutas)

#O método retorna o número de elementos com o valor especificado.count()
#Devolva o número de vezes que o valor 9 aparece int na lista
#pontos = [1, 4, 2, 9, 7, 8, 9, 3, 1]
#x = pontos.count(9)
#print(x)

#fruits = ['apple', 'banana', 'cherry', 'banana', 'banana']
#x = fruits.count('banana')
#print(x)

##Método extend () da lista Python
# O método adiciona os elementos de lista especificados (ou qualquer iterável) ao final da lista atual.extend ()
# Exemplo: adione os elementos da lista car em frutas.

#frutas = ['apple', 'banana', 'uva', 'orange']
#carros = ['Ford', 'BMW', 'Volvo']

#frutas.extend(carros) # adicionou os elementos
#print(frutas)

##Método Python List index () O método retorna a posição na primeira ocorrência do valor especificado.index()
#qual é a posição do valor "orange":
#frutas = ['apple', 'banana', 'uva', 'orange']
#x = frutas.index('uva')
#print(x)

#Itens de acesso
#Os itens da lista são indexados e você pode acessá-los referindo-se ao número do índice:
#Imprima o segundo item da lista:

#frutas = ['apple', 'banana', 'uva', 'orange']
#print(frutas[1])

# Indexação Negativa
#Indexação negativa significa começar a partir do fim
#-1 refere-se ao último item, refere-se ao segundo último item etc.-2
#Imprima o último item da lista:
#frutas = ['apple', 'banana', 'uva', 'orange']
#print(frutas[-2])

#Faixa de Índices
#Você pode especificar uma série de índices especificando por onde iniciar e por onde terminar o intervalo.
#Ao especificar um intervalo, o valor de retorno será uma nova lista com os itens especificados.
#frutas = ['apple', 'banana', 'uva', 'orange', 'abacate','mamão', 'morango']
#print(frutas[2:5])
#A pesquisa começará no índice 2 (incluído) e terminará no índice 5 (não incluído).

#Ao deixar de fora o valor inicial, o intervalo começará no primeiro item:
#Este exemplo retorna os itens do início para, mas NÃO incluindo, "abacate":
frutas = ['apple', 'banana', 'uva', 'orange', 'abacate','mamão', 'morango']
#print(frutas[:4])

#Ao deixar de fora o valor final, o intervalo irá até o final da lista:
#Este exemplo retorna os itens de "uva" até o final
#print(frutas[2:])

#Faixa de Índices Negativos
#Especifique índices negativos se quiser iniciar a pesquisa a partir do final da lista:
#Este exemplo retorna os itens de "orage" (-4) para, mas NÃO incluindo "morango" (-1)
#print(frutas[-4:-1])
#Verifique se o item existe
#Para determinar se um item especificado está presente em uma lista use a palavra-chave:in
#Verifique se "uva" está presente na lista:

frutas = ['apple', 'banana', 'uva', 'orange', 'abacate','mamão', 'morango']

if 'uva' in frutas:
    print('uva')
