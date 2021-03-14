from sys import stdin

def possibleMoves(numbers):
    actions = []
    a = max(numbers)
    b = min(numbers)
    q = a//b
    actions.append([b, a-q*b])
    if q>1:
        actions.append([a-(q-1)*b, b])
    #for i in range (q-1, q + 1 ):
    #    actions.append([a - i*b, b])
    return actions

def minimax_decision(numbers):
    actions = possibleMoves(numbers)
    return max(actions, key = lambda a: min_value(a, 1))

def max_value(numbers, playerNum):
    if 0 in numbers:
        return playerNum
    v = -2
    for a in possibleMoves(numbers):
        v = max(v, min_value(a, -playerNum))
    return v

def min_value(numbers, playerNum):
    if 0 in numbers:
        return playerNum
    v = 2
    for a in possibleMoves(numbers):
        v = min(v, max_value(a, -playerNum))
    return v


numbers=list(map(int,stdin.readlines()[0].split()))
currentPlayer = 1

while not 0 in numbers:
    numbers = minimax_decision(numbers)
    currentPlayer *= -1


if (currentPlayer == -1):
    print ("Stan wins")
else:
    print ("Ollie wins")
