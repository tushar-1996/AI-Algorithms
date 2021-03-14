#absolutely not cleaned up yet

''' tests:
first testcase:
5 7
5
3
16
2
0
0 1 3
0 2 1
0 3 6
1 3 2
1 4 7
2 3 15
3 4 2

'''

#returns a list of expanded nodes (one by line)

from sys import stdin

class Node:
    def __init__(self, name, path, f, cost):
        self.name = name
        self.path = path #printable, probably unnecessary now
        self.f = f
        self.cost = cost


def get_f(node):
    return node.f

def expand(node, h_list, edges):
    nodes=[]
    successors=[edge for edge in edges if edge[0]==node.name] #all edges originating from this node
    while successors!=[]: #add all successors in any order (priority queue is implemented in a_star()), compute fs
        nodes.append(Node(name=successors[0][1],
                          path=node.path+"\n%d"%successors[0][1], #probably unnecessary
                          f=node.cost+successors[0][2]+h_list[successors[0][1]],
                          cost=node.cost+successors[0][2]))
        successors.pop(0)
    return nodes
    
def a_star():
    #get input from stdin
    h=[] #to hold heuristic values in node order
    edges=[]
    graph=stdin.readlines()
    nm=list(map(int,graph[0].split())) #save n,m so they can be used as index
    for i in range(1, nm[0]+1):
        h.append(int(graph[i].rstrip('\n')))
    for i in range(nm[0]+1, nm[0]+nm[1]+1):
        edges.append(list(map(int,graph[i].split())))

    closed = []
    fringe = []
    node = Node(name=0, path="0", f=h[0], cost=0)
    fringe.append(node)
    while True:
        if fringe == []:
            return None
        node = fringe.pop(0)
        if node.name == nm[0]-1:
            closed.append(node.name)
            resString=""
            for exp_node in closed:
                resString+="%d\n"%exp_node
            return resString
        if node.name not in closed:
            closed.append(node.name)
            fringe=expand(node, h, edges)+fringe
            fringe.sort(key = get_f) #priority queue

print(a_star(), end="")
