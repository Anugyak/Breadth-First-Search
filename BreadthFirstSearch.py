
#Input Graph
graph = {
    "S": ["A", "B", "C"], "A": ["S", "D", "E"], "B": ["S", "D", "F"],
    "C": ["S", "E", "F"], "D": ["A", "B"], "E": ["A", "G", "H"],
    "F": ["B", "C", "G", "H"], "G": ["E", "F"], "H": ["E", "F"] }
#Initializing a Empty List
visited = []

def bfs(graph, n, index):
    """ This Function Takes Graph,Node and Index as Input And Outputs Travesing Order Using BFS"""
    #Making Visited List As Global
    global visited
    #Finding all neighbor of node and add to visited if it is not in visited
    if n not in visited:
        visited.append(n)
    nodes = graph[n]
    for i in nodes:
     #If node in graph is not in visited, then make node at position of index of visited as starting node
        if i not in visited:
            visited.append(i)
    #Increase Index By 1
    index = index + 1
    try:
        #Recursive Call to Function
        bfs(graph, visited[index - 1], index)
    except:
        return

#Calling The Function
bfs(graph,"S",0)
print("Using bfs: ")
print(visited)






