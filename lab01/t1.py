# Implementando o algoritmo de Havel-Hakimi
def check_if_is_graphic_sequence(d):
    while d:
        d.sort(reverse=True)
        if d[0] == 0:
            return True  # Todos os graus são zero, sequência gráfica válida
        first = d.pop(0)
        if first > len(d):  # Não pode haver esse número de conexões
            return False
        for i in range(first):
            d[i] -= 1
            if d[i] < 0:  # Se algum grau ficou negativo, sequência inválida
                return False
    return True

# Construindo a lista de adjacências 
def create_adjacency_list(n, d):
    graph = [[] for _ in range(n)]
    nodes = list(range(n))  # Lista de vértices indexados de 0 a n-1
    degrees = d[:]  # Fazemos uma cópia para evitar modificar a lista original

    while sum(degrees) > 0:  # Enquanto houver graus a processar
        # Ordena os nós pelo grau restante (decrescente)
        nodes.sort(key=lambda i: -degrees[i])
        
        first = nodes[0]  # Seleciona o vértice de maior grau
        first_degree = degrees[first]

        # Conectar aos primeiros 'first_degree' nós disponíveis
        for i in range(1, first_degree + 1):  # Pula o próprio nó (i = 0)
            neighbor = nodes[i]
            graph[first].append(neighbor + 1)
            graph[neighbor].append(first + 1)
            degrees[neighbor] -= 1

        degrees[first] = 0  # Zera o grau do vértice processado

    return graph


# Entrada e saída
n = int(input())
d = list(map(int, input().split()))

if check_if_is_graphic_sequence(d.copy()):
    graph = create_adjacency_list(n, d)
    for line in graph:
            print(*sorted(line))  # Ordena para garantir saída correta
else:
    print("Não é sequência gráfica!")
