def main():
    n, m = map(int, input().split())
    graph = [{} for _ in range(n)]  # graph[u][color] = list of (v, edge_id)
    edge_list = []

    for eid in range(m):
        u, v, c = map(int, input().split())
        edge_list.append((u, v, c))

        if c not in graph[u]:
            graph[u][c] = []
        if c not in graph[v]:
            graph[v][c] = []
        graph[u][c].append((v, eid))
        graph[v][c].append((u, eid))

    # Verificar se cada vértice tem grau par alternável (mesmo número de arestas por cor)
    for u in range(n):
        red = len(graph[u].get(0, []))
        blue = len(graph[u].get(1, []))
        if red != blue:
            print("Não possui trilha Euleriana alternante")
            return

    used = [False] * m
    path = []
    stack = []

    # Começar de um vértice com grau > 0
    for start in range(n):
        if graph[start]:
            stack.append((start, None))  # (vértice atual, última cor usada)
            break

    while stack:
        u, last_color = stack[-1]
        found = False
        for color in [0, 1]:
            if color == last_color:
                continue
            if color in graph[u]:
                while graph[u][color]:
                    v, eid = graph[u][color].pop()
                    if not used[eid]:
                        used[eid] = True
                        # Remover o outro lado da aresta
                        for i in range(len(graph[v][color])):
                            if graph[v][color][i][0] == u and graph[v][color][i][1] == eid:
                                graph[v][color].pop(i)
                                break
                        stack.append((v, color))
                        found = True
                        break
            if found:
                break
        if not found:
            path.append(u)
            stack.pop()

    if all(used) and path[0] == path[-1]:
        print(" ".join(map(str, reversed(path))))
    else:
        print("Não possui trilha Euleriana alternante")

main()
