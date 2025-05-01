from collections import deque

class bfs:
    def bfs(self, start_node):
        queue = deque([start_node])
        visited = set()

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                for neighbor in node.neighbors:
                    queue.append(neighbor)
        return visited