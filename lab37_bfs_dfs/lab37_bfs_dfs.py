from collections import deque

# Graph representation using adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# BFS Implementation
def bfs(start_node, graph):
    visited = set()
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=' ')
            visited.add(node)
            queue.extend([n for n in graph[node] if n not in visited])

# DFS Implementation
def dfs(node, graph, visited=None):
    if visited is None:
        visited = set()
    if node not in visited:
        print(node, end=' ')
        visited.add(node)
        for neighbor in graph[node]:
            dfs(neighbor, graph, visited)

print("BFS Traversal:")
bfs('A', graph)
print("\nDFS Traversal:")
dfs('A', graph)
print()
