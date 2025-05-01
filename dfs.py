class dfs:
    def dfs(self, start_node):
        my_stack = [start_node]
        visited = set()

        while my_stack:
            node = my_stack.pop()
            if node not in visited:
                visited.add(node)
                for neighbor in reversed(node.neighbors):
                    my_stack.append(neighbor)

        return visited