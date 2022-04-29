# Depth First Search
from collections import deque


def deptFirstPrint(graph: dict, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current, end=" ")
        for neighbour in graph[current]:
            stack.append(neighbour)


def breadthFirstPrint(graph: dict, source):
    queue = [source]
    while len(queue) > 0:
        current = queue[0]
        print(current, end=" ")
        queue = queue[1:]
        for neighbour in graph[current]:
            queue.append(neighbour)


if __name__ == '__main__':

    z = input("Enter the search DFS/BFS:")

    list1 = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}
    if z == 'DFS':
        deptFirstPrint(list1, 'a')
    else:
        pass
        breadthFirstPrint(list1, 'a')
