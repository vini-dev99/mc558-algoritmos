class ED:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0

    def find(self, x):
        # se x ainda não tem conjunto, cria agora
        if x not in self.parent:
            self.make(x)
        # path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # garante que ambos existam
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        # union by rank
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[ry] < self.rank[rx]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        return True


def kruskal(edges, max):
    # Ordene as arestas em ordem nao-decrescente de peso
    edges.sort(key=lambda e: e[2])

    total_cost = 0
    edges_used  = 0
    dsu = ED()

    for u, v, w in edges:
        if edges_used == max:
            break
        # se u e v estão em componentes diferentes, unimos
        if dsu.union(u, v):
            total_cost += w 
            edges_used += 1

    return total_cost


n, m, k = map(int, input().split())
edges = []

for _ in range(m):
    a, b, w = map(int, input().split())
    edges.append((a, b, w))

cost = kruskal(edges, n - k)
print(cost)



    