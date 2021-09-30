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
frutas = ['apple', 'banana', 'uva', 'orange']
x = frutas.index('uva')
print(x)
