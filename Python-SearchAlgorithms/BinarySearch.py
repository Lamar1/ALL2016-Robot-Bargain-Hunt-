"""
Binary search algorithm (Depth-First and Breadth-First)
"""

__author__ = "Ryan"

#Depth first search
def DFS(graph, start):
    path = []
    queue = [start]
    while queue:
        v = queue.pop(0)
        if v not in path:
            path = path + [v]
            queue = graph[v] + queue
    return path

#Breadth first search
def BFS(graph, start):
    path = []
    queue = [start]
    while queue:
        v = queue.pop(0)
        if v not in path:
            path = path + [v]
            queue = queue + graph[v]
    return path

graph = {'A':['B','C'], 'B':['E'], 'C':['E','D'], 'D':['E'], 'E':['F'], 'F':[]}
print ('DFS path: ', DFS(graph, 'A'))
print ('BFS path: ', BFS(graph, 'A'))
