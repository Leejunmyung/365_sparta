import sys

n, m, v = map(int, sys.stdin.readline().split())

graph = {i : list() for i in range(1,n+1)}
dfs_visited = []
bfs_visited = []

for j in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

for h in range(1,n+1):
    graph[h].sort()

def dfs(graph, v):
    dfs_visited.append(v)
    for gra_node in graph[v]:
        if gra_node not in dfs_visited:
            dfs(graph, gra_node)
    return dfs_visited


def bfs(graph, v):
    queue = [v]
    while queue:
        cur_node = queue.pop(0)
        bfs_visited.append(cur_node)
        for gra_node in graph[cur_node]:
            if gra_node not in bfs_visited and gra_node not in queue:
                queue.append(gra_node)
    return bfs_visited

dfs(graph,v)
bfs(graph,v)

for z in dfs_visited:
    print(z,end=' ')

print(sep='\n')

for t in bfs_visited:
    print(t,end=' ')

