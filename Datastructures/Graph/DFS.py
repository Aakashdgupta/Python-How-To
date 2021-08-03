

'''
DFS OF DEPTH FIRST SEARCH ALGORITHM TAKES A GRAPH AND VISITS EACH AND 
EVERY NODE IN A GRAPH  IT TAKES ASTARTING NODE , A COLOR DICTIONARY
FIRST IT SETS COLOR FOR STARTIN NODE TO GREY WHICH MEANS IT IS BEING VISITED
AND VISITS ITS ALL NEIGHOUR ONE BY ONE ONLY IF THEIR COLOR VALUE IS WHITE 
WHICH MEANS THEY ARE NOT VISITED YET AND SETS THEIR COLOR VALUE IN THE WAY
BY REPEATING IT RECURSIVELY IT VISITS EACH AND EVERY CONNECTED NODE 

'''

import graph_Adj_list as gr




class DFS:
    def __init__(self):
        pass

    def dfs(self, node, colorDict, visitedList, graph):
        colorDict[node] = "grey"
        visitedList.append(node)
        for i in graph.nodes:
            if colorDict[i] == 'white':
                self.dfs(i, colorDict, visitedList, graph)
        colorDict[node] = "black"
    
    def applyDFS(self, startNode, graph):
        visitedList = []
        colorDict = {}
        for i in graph.nodes:
            colorDict[i] = "white"

        self.dfs(startNode, colorDict, visitedList, graph)
        # printing color

        print(f" Color array \n white = not visited \n grey = Partially visited \n Black = fully visited")
        print()
        for k, v in colorDict.items():
            print(k, v)

            # printing traversal ootput
        print("Traversal Output")
        print(visitedList)


nodes = ["A", "B", "C"]
g = gr.graph(nodes)
g.addNode("D")
g.addEdge("A", "E")
g.addEdge("A", "B")
g.addEdge("A", "C")
g.addEdge("B", "E")
g.addEdge("D", "E")
g.addEdge("C", "A")
g.addEdge("C", "D")
g.addEdge("E", "B")
g.addEdge("E", "C")
g.addEdge("E", "D")

g.printGraph()

d = DFS()
d.applyDFS("A", g)
