from sys import stdin


class Node:
    def __init__(self, playerNum, nums):
        self.playerNum = playerNum #{-1,1}
        self.nums = nums #list containing 2 numbers
        self.children = [] # list of nodes
        self.createChildren()
        self.value = -2*playerNum

    def setValue(self, v):
        self.value = v

    def createChildren(self):
        a = max(self.nums)
        b = min(self.nums)
        if b != 0:
            q = a//b
            for i in range (1, q + 1 ):
                self.children.append(Node(-self.playerNum,[a - i*b, b]))

    def isTerminalState(self):
        return 0 in self.nums


def alpha_beta_search(node):
    #actions = possibleMoves(numbers)
    if node.playerNum == 1:
        v = max_value(node, -2, 2)
    else: ##?
        v = min_value(node, -2, 2)
    for s in node.children:
        if s.value == v:
            return s

def max_value(node, alpha, beta):
    if node.isTerminalState():
        node.setValue(-node.playerNum) #?-
        return node.value
    v = -2
    for s in node.children:
        s.setValue(max(v, min_value(s, alpha, beta)))
        v = s.value
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def min_value(node, alpha, beta):
    if node.isTerminalState():
        node.setValue(-node.playerNum)
        return node.value
    v = 2
    for s in node.children:
        s.setValue(min(v, max_value(s, alpha, beta)))
        v = s.value
        if v <= alpha:
            return v
        beta = min(beta, v)
    return v


numbers=list(map(int,stdin.readlines()[0].split()))
currentState = Node(1, numbers)
while not currentState.isTerminalState():
    currentState = alpha_beta_search(currentState)

if (currentState.playerNum == -1):
    print ("Stan wins")
else:
    print ("Ollie wins")
