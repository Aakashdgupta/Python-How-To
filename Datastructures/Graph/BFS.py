import graph_Adj_list as gr

from queue import Queue


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


visited = {}
level = {}
parent = {}
bfs_traversal_output = []
queue = Queue()

for node in g.adj_list.keys():
    visited[node] = False
    parent[node] = None
    level[node] = -1

print(visited)
print(level)
print(parent)
print(bfs_traversal_output)

# bfs algp

# source node
src = "A"

# set source as visited
visited[src] = True

# define level of source node to 0
level[src] = 0

# set parent of src to none

parent[src] = None


# add source node to queue
queue.put(src)

while not queue.empty():
    # pop first element
    u = queue.get()
    # set popped node as visited output
    bfs_traversal_output.append(u)
    # explore its neighour
    for v in g.adj_list[u]:
        # chech if v is not visited
        if not visited[v]:
            # if not set it as visited
            visited[v] = True
            # set its parent as u
            parent[v] = u
            # set its level as its parents level + 1
            level[v] = level[u]+1
            # put v in queue
            queue.put(v)


print(visited)
print(level)
print(parent)
print(bfs_traversal_output)
