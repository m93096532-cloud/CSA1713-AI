def bidirectional_search(graph, start, goal):
    if start == goal:
        return [start]

    forward = {start: None}
    backward = {goal: None}

    q1 = [start]
    q2 = [goal]

    while q1 and q2:
        node = q1.pop(0)

        for neighbor in graph[node]:
            if neighbor not in forward:
                forward[neighbor] = node
                q1.append(neighbor)

            if neighbor in backward:
                meet = neighbor
                path1 = []
                path2 = []

                while meet is not None:
                    path1.append(meet)
                    meet = forward[meet]

                meet = neighbor
                while meet is not None:
                    path2.append(meet)
                    meet = backward[meet]

                return path1[::-1] + path2[1:]

        node = q2.pop(0)

        for neighbor in graph[node]:
            if neighbor not in backward:
                backward[neighbor] = node
                q2.append(neighbor)

            if neighbor in forward:
                meet = neighbor
                path1 = []
                path2 = []

                while meet is not None:
                    path1.append(meet)
                    meet = forward[meet]

                meet = neighbor
                while meet is not None:
                    path2.append(meet)
                    meet = backward[meet]

                return path1[::-1] + path2[1:]

    return None


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['C', 'F'],
    'F': ['D', 'E']
}

start = 'A'
goal = 'F'

path = bidirectional_search(graph, start, goal)

print("Path:", path)
