# Depth First Search

from timeit import default_timer as timer
from datetime import timedelta

"""
def deptFirstPrint(graph: dict, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current, end=" ")
        for neighbour in graph[current]:
            stack.append(neighbour)

"""


def deptFirstPrint(graph: dict, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            deptFirstPrint(graph, k, visited)
    return visited


# Breadth First Search

def breadthFirstPrint(graph: dict, node, visited):
    if node not in visited:
        visited.append(node)
    while len(visited) > 0:
        current = graph[node]
        graph = graph[1:]
        for k in graph[current]:
            if k not in visited:
                visited.append(k)
    return visited


if __name__ == '__main__':

    z = input("Enter the search DFS/BFS:")

    # list1 = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}

    list1 = {
        'A': ['B', 'S'],
        'B': ['A'],
        'C': ['D', 'E', 'F', 'S'],
        'D': ['C'],
        'E': ['C', 'H'],
        'F': ['C', 'G'],
        'G': ['F', 'S'],
        'H': ['E', 'G'],
        'S': ['A', 'C', 'G']
    }

    if z == 'DFS':
        start = timer()
        print(deptFirstPrint(list1, 'F', []))
        end = timer()
        print("\nTime taken for " + z + " is :" + str(timedelta(seconds=end - start)) + " seconds")
    else:
        start = timer()
        print(breadthFirstPrint(list1, 'F', []))
        end = timer()
        print("\nTime taken for " + z + " is :" + str(timedelta(seconds=end - start)) + " seconds")
