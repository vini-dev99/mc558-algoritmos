n, m, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    x, y, c = map(int, input().split())
    graph[x].append((y, c))

indegree = [0]*n
for v in range(n):
    for u, _ in graph[v]:
        indegree[u] += 1

queue = [i for i in range(n) if indegree[i] == 0]
topo = []
idx = 0
while idx < len(queue):
    v = queue[idx]
    idx += 1
    topo.append(v)
    for u, _ in graph[v]:
        indegree[u] -= 1
        if indegree[u] == 0:
            queue.append(u)

dp = [[0, 0, 0] for _ in range(n)]
for cor in range(3):
    dp[t][cor] = 1

valid = [
    [True,  True,  True ],  # last_color = 0 → aceita 0,1,2
    [True,  True,  False],  # last_color = 1 → não aceita 2
    [True,  False, False],  # last_color = 2 → só aceita 0
]

for v in reversed(topo):
    if v == t:
        continue
    for last in range(3):
        total = 0
        for u, c in graph[v]:
            if valid[last][c]:
                total += dp[u][c]
        dp[v][last] = total

print(dp[s][0])
