import sys #to read from stdin

class Node:
  def __init__(self, row_ind, col_ind, parent, depth, action=''):
    self.state = [row_ind,col_ind]
    self.parent = parent
    self.children = []
    self.action = action
    self.depth = depth
    #self.depth = self.parent.depth+1
    #components: state, parent, children, action, depth, path-cost=depth

#implements breadth-first search strategy
def expand(node,labyrinth):
  nodes=[]
  r=node.state[0]
  c=node.state[1]
  #upwards expansion
  if r > 0:
    if labyrinth[r-1][c] != '#':
      child=Node(r-1,c,node,node.depth+1,action='up') # this should be down
      nodes.append(child)
  #downwards expansion
  if r < len(labyrinth)-1:
    if labyrinth[r+1][c] != '#':
      child=Node(r+1,c,node,node.depth+1,action='down') #this should be up
      nodes.append(child)
  #leftward expansion
  if c > 0:
    if labyrinth[r][c-1] != '#':
      child=Node(r,c-1,node,node.depth+1,action='left')
      nodes.append(child)
  #rightward expansion
  if c < len(labyrinth[0])-1:
    if labyrinth[r][c+1] != '#':
      child=Node(r,c+1,node,node.depth+1,'right')
      nodes.append(child)
  return nodes

#returns the number of steps needed to reach the goal
def steps_to_goal():
  lab=[]
  n=None #state variable: agent row index
  m=None #state variable: agent column index

  #represent labyrinth input and find initial position of the agent
  input=sys.stdin.readlines()
  for line in input:
    row=[]
    row_values=list(line.rstrip('\n'))
    for char in row_values:
      if char == '@':
        n=input.index(line)
        m=row_values.index(char)
      row.append(char)
    lab.append(row)

  #breadth-first graph-search: find goal and record number of steps taken
  closed=[]
  fringe=[]
  node = Node(row_ind=n,col_ind=m, parent=None, depth=0)#initial node
  fringe.append(node)#initial fringe
  while True:
    if fringe==[]:
      return None
    node = fringe.pop(0)
    if lab[node.state[0]][node.state[1]]=='.': #goal-test
      return node.depth
    if node.state not in closed:
      closed.append(node.state)
      fringe=fringe + expand(node,lab)

print(steps_to_goal())
