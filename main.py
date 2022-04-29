# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def deptFirstPrint(graph: dict, source):
    stack = [source]
    while len(stack) > 0:
        current = stack.pop()
        print(current)
        for neighbour in graph[current]:
            stack.append(neighbour)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list1 = {'a': ['b', 'c'], 'b': ['d'], 'c': ['e'], 'd': ['f'], 'e': [], 'f': []}
    deptFirstPrint(list1, 'a')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
