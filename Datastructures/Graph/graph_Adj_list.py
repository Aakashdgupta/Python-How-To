'''
GRAPH IMPLEMENTATION USING ADJENCY LIST
A GRAPH IS ADATA STRUCTURE IN WHICH VARIOUS NODES
ARE CONNECTED USING EDGES BETWEEN THEM
  A--------B
  |        |
  |        |
  |        |
  C--------D

  HERE A B C D ARE NODES
  A GRAPH CAN NE BOTH DIRECTED OR UNDIRECTED
  IN A DIRECTED GRAAPH TWO NODES HAVE SINGLE DIRECTIONAL
  EDGE
  A-------->B

  A GRAPH CAN BE REPRESENTED IN MANY WAYS HERE
  WE ARE USING ADJENCY LIST METHOD
  IN ADJENCY LIST
  EVERY UNIQUE NODE CONTAINS LIST OF ITS EDGES
  A {B,C}
  B {A,D}
  C {A,D}
  D {B,C}
'''

def removeDuplicates(L):
    l =[]
    for i in L:
        if i in l:
            continue
        else:
            l.append(i)
    
    
    return l


# li = [1,4,3,7,1,4]
# print(li)
# print("remove dup")
# li =removeDuplicates(li)
# print(li)

class graph:
    def __init__(self, nodes, isDirected=False):

        # initializing adjency list {}
        # ex
        # {
        # "A":["B","C"],
        # }
        self.adj_list = {}

        # bool that makes graph directional
        # or un directional default undirectional
        self.isDirected = isDirected

        self.nodes = nodes
        # creating empty list for each node in
        # received nodes
        # ex {
        # "A":[],
        # "B":[]
        # }
        for node in self.nodes:
            self.adj_list[node] = []

    # method to add nodes one by one
    def addNode(self, node):
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            self.adj_list[node] = []

    def printGraph(self):
        for node in self.nodes:
            print(f"{node} ---> {self.adj_list[node]}")

    # method to add edges to graph
    def addEdge(self, u, v):
        # checking if nodes exist in graph
        # or its a new node
        u_exist = u in self.adj_list
        v_exist = v in self.adj_list

        # print(f"{u} exists", u_exist)
        # print(f"{v} exists", v_exist)

        # if u already exixts
        # just add v to its edge list
        if u_exist:
            self.adj_list[u].append(v)
            self.adj_list[u] = removeDuplicates(self.adj_list[u])
        # else first add new node u
        # then add v as its edge
        #
        else:
            self.addNode(u)
            self.adj_list[u].append(v)
        # if node v exist in graph
        # and its not adirectional graph
        # add u as its edge
        if v_exist:
            if self.isDirected == False:
                self.adj_list[v].append(u)
                self.adj_list[v] = removeDuplicates(self.adj_list[v])
        # else first add v as a node
        # and if its not a directional graph
        # add u as its edge
        #
        else:

            self.addNode(v)
            if self.isDirected == False:
                self.adj_list[v].append(u)





if __name__ == "__main__":
    nodes = ["A", "B", "C"]
    g = graph(nodes)
    g.addNode("D")
    # print(g.add_node("A"))
    # print(g.add_node("B"))
    # print(g.add_node("A"))

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
