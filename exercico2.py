# Cria uma lista vazia
my_list = []

# Adiciona os elementos 10, 20, 30, 40
my_list.extend([10, 20, 30, 40])

# Insere o valor 15 na segunda posição (índice 1)
my_list.insert(1, 15)

# Estende a lista com outra lista [50, 60, 70]
my_list.extend([50, 60, 70])

# Remove o último elemento da lista
my_list.pop()

# Classifica a lista em ordem crescente
my_list.sort()

# Encontra o índice do valor 30
index_of_30 = my_list.index(30)

# Imprime o índice do valor 30
print(f"O índice do valor 30 é: {index_of_30}")


