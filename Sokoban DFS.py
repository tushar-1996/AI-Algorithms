#changes made from BFS:
#fringe expansion -> LIFO

import sys #to read from stdin

class Node:
  def __init__(self, poslist, parent, depth, action=''):
    self.state = poslist
    self.parent = parent
    self.children = []
    self.action = action
    self.depth = depth
    #self.depth = self.parent.depth+1
    #components: state, parent, children, action, depth, path-cost=depth

#implements breadth-first search strategy
def expand(node,labyrinth):
  nodes=[]
  r=node.state[0][0]
  c=node.state[0][1]
  #upwards expansion
  if r>0:
    if labyrinth[r-1][c] != '#': #wall?
      if [r-1,c] in node.state: #box?
        if r-2>0 and labyrinth[r-2][c] != '#' and not [r-2,c] in node.state: #room to push?
          newpos=[[r-1,c]]
          for pos in node.state[1:len(node.state)]:
            if pos == [r-1,c]:
              newpos.append([r-2,c])
            else:
              newpos.append(pos)
          child=Node(newpos,node,node.depth+1,action=node.action+'U')
          nodes.append(child)
      else: #empty field
        newpos=[[r-1,c]]+node.state[1:len(node.state)]
        child=Node(newpos,node,node.depth+1,action=node.action+'U')
        nodes.append(child)
  #downwards expansion
  if r<len(labyrinth)-1:      
    if labyrinth[r+1][c] != '#': #wall?
      if [r+1,c] in node.state: #box?
        if r<len(labyrinth)-2 and labyrinth[r+2][c] != '#' and not [r+2,c] in node.state: #room to push?
          newpos=[[r+1,c]]
          for pos in node.state[1:len(node.state)]:
            if pos == [r+1,c]:
              newpos.append([r+2,c])
            else:
              newpos.append(pos)
          child=Node(newpos,node,node.depth+1,action=node.action+'D')
          nodes.append(child)
      else: #empty field
        newpos=[[r+1,c]]+node.state[1:len(node.state)]
        child=Node(newpos,node,node.depth+1,action=node.action+'D')
        nodes.append(child)      
  #leftward expansion
  if c>0:
    if labyrinth[r][c-1] != '#': #wall?
      if [r,c-1] in node.state: #box?
        if c-2>0 and labyrinth[r][c-2] != '#' and not [r,c-2] in node.state: #room to push?
          newpos=[[r,c-1]]
          for pos in node.state[1:len(node.state)]:
            if pos == [r,c-1]:
              newpos.append([r,c-2])
            else:
              newpos.append(pos)
          child=Node(newpos,node,node.depth+1,action=node.action+'L')
          nodes.append(child)
      else: #empty field
        newpos=[[r,c-1]]+node.state[1:len(node.state)]
        child=Node(newpos,node,node.depth+1,action=node.action+'L')
        nodes.append(child)
  #rightward expansion
  if c<len(labyrinth[0])-1:
    if labyrinth[r][c+1] != '#': #wall?
      if [r,c+1] in node.state: #box?
        if c<len(labyrinth[0])-2 and labyrinth[r][c+2] != '#' and not [r,c+2] in node.state: #room to push?
          newpos=[[r,c+1]]
          for pos in node.state[1:len(node.state)]:
            if pos == [r,c+1]:
              newpos.append([r,c+2])
            else:
              newpos.append(pos)
          child=Node(newpos,node,node.depth+1,action=node.action+'R')
          nodes.append(child)
      else: #empty field
        newpos=[[r,c+1]]+node.state[1:len(node.state)]
        child=Node(newpos,node,node.depth+1,action=node.action+'R')
        nodes.append(child)
  return nodes

#returns the number of steps needed to reach the goal
def steps_to_goal():
  lab=[]
  xylist = [None] #list to hold row and column indices of agent and boxes [[agent_row, agent_col], [box1_row, box1_col], ... boxn_col]]

  #represent labyrinth input and find initial position of the agent
  input=sys.stdin.readlines()
  for line in input:
    row=[]
    row_values=list(line.rstrip('\n'))
    for col in range(len(row_values)):
      if row_values[col] == '@':
        xylist[0]=[input.index(line), col]
      if row_values[col] == '$':
        xylist.append([input.index(line),col])
      row.append(row_values[col])
    lab.append(row)
  if len(xylist)==1: #no boxes
    return None

  #breadth-first graph-search: find goal
  closed=[]
  fringe=[]
  node = Node(poslist = xylist, parent=None, depth=0)#initial node
  fringe.append(node)#initial fringe
  while True:
    if fringe==[]: 
      return None
    node = fringe.pop(0)
    goal = [] #goal-test
    for boxpos in node.state[1:len(node.state)]:
      if lab[boxpos[0]][boxpos[1]]=='.':
        goal.append(True)
      else:
        goal.append(False)
    if all(goal): 
      return node.action #end goal-test
    if node.state not in closed:
      closed.append(node.state)
      fringe=expand(node,lab)+fringe

print(steps_to_goal())
