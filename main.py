from timeit import default_timer as timer
from datetime import timedelta
from collections import defaultdict


# Depth First Search
def deptFirstPrint(graph: dict, node, visited):
    if node not in visited:
        visited.append(node)
        for k in graph[node]:
            deptFirstPrint(graph, k, visited)
    return visited


# Breadth First Search
def breadthFirstPrint(graph: dict, node, visited):
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        s = queue.pop(0)
        for k in graph[s]:
            if k not in visited:
                visited.append(k)
                queue.append(k)
    return visited


# Build Adjacency list

def buildAdjList(wordlist):
    startswith, endswith = defaultdict(list), defaultdict(list)
    for word in wordlist:
        startswith[word[0]].append(word)
        # endswith[word[-1]].append(word)
    graph = {word: startswith[word[-1]] for word in wordlist}
    return graph


if __name__ == '__main__':

    # Read file contents
    file = input("Enter the full file path incl Filename with extn :")
    dictl = {}  # Dict obj to store label and ids
    with open(file, "r+") as f:
        for nodeid, label in enumerate(f):
            dictl[label.rstrip('\n')] = nodeid
    f.close()

    # Get option (DFS/BFS)
    GetOption = input("Enter the search DFS/BFS:")
    GetWord = input("Enter label:")
    if GetOption == 'DFS':
        start = timer()
        if GetWord not in dictl.keys():
            print("Label not found")
        else:
            print(f"Graph traversal : {deptFirstPrint(buildAdjList(list(dictl.keys())), GetWord, [])} ")
            print(f"Node id : {dictl[GetWord]}")
        end = timer()
        print("\nTime taken for " + GetOption + " is :" + str(timedelta(seconds=end - start)) + " seconds")
    else:
        start = timer()
        if GetWord not in dictl.keys():
            print("Label not found")
        else:
            print(f"Graph traversal : {breadthFirstPrint(buildAdjList(list(dictl.keys())), GetWord, [])} ")
            print(f"Node id : {dictl[GetWord]}")
        end = timer()
        print("\nTime taken for " + GetOption + " is :" + str(timedelta(seconds=end - start)) + " seconds")
