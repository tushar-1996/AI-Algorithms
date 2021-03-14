#Arc Consistency

from sys import stdin
import argparse
import sys
import itertools
import sys

rows = "123456789"
cols = "ABCDEFGHI"

class Sudoku:

    def __init__(self, grid):
        game = list(grid)
        
        # generation of all the coords of the grid
        self.cells = [col + row for col in cols for row in rows]

        # generation of all the possibilities for each one of these coords
        self.possibilities = {v: list(range(1, 10)) if game[i] == '0' else [int(game[i])] for i, v in enumerate(self.cells)}
   
        # generation of the line / row / square constraints
        rule_constraints = self.generate_rules_constraints()

        # convertion of these constraints to binary constraints
        self.binary_constraints = list()
        self.binary_constraints = self.generate_binary_constraints(rule_constraints)

        # generating all constraint-related cells for each of them
        self.related_cells = dict()
        self.related_cells = self.generate_related_cells()

        #prune
        self.pruned = dict()
        self.pruned = {v: list() if grid[i] == '0' else [int(grid[i])] for i, v in enumerate(self.cells)}


    """
    generates the constraints based on the rules of the game:
    value different from any in row, column or square
    """
    def generate_rules_constraints(self):
        row_constraints = []
        column_constraints = []
        square_constraints = [[0 for i in range(9)] for j in range(9)] 

        # get rows constraints
        for row in rows:
            row_constraints.append([col + row for col in cols])

        # get columns constraints
        for col in cols:
            column_constraints.append([col + row for row in rows])
        
        # get square constraints
        for i in range(9):
            for j in range(9):
                square_constraints[(j//3)+((i//3)*3)][(j%3)+((i%3)*3)]=cols[i]+rows[j]
                     
        return row_constraints + column_constraints + square_constraints

    """
    generates the binary constraints based on the rule constraints
    """
    def generate_binary_constraints(self, rule_constraints):
        generated_binary_constraints = list()

        # for each set of constraints
        for constraint_set in rule_constraints:

            binary_constraints = list()
            
            #for tuple_of_constraint in itertools.combinations(constraint_set, 2):
            for tuple_of_constraint in itertools.permutations(constraint_set, 2):
                binary_constraints.append(tuple_of_constraint)

            # for each of these binary constraints
            for constraint in binary_constraints:
                constraint_as_list = list(constraint)
                if(constraint_as_list not in generated_binary_constraints):
                    generated_binary_constraints.append([constraint[0], constraint[1]])

        return generated_binary_constraints

    """
    generates the the constraint-related cell for each one of them
    """
    def generate_related_cells(self):
        related_cells = dict()

        #for each one of the 81 cells
        for cell in self.cells:

            related_cells[cell] = list()
            # related cells are the ones that current cell has constraints with
            for constraint in self.binary_constraints:
                if cell == constraint[0]:
                    related_cells[cell].append(constraint[1])

        return related_cells

    """
    returns a human-readable string
    """
    def __str__(self):
        output = ""
        count = 1
        for cell in self.cells:
            value = str(self.possibilities[cell])[1:-1]            
            output += "{" + value + "}"
            if count%9 == 0:
                output += "\n"
            count += 1
        output=output.replace(" ","")
        return output[:-1]
       
def AC3(csp, queue=None):

    if queue == None:
        queue = list(csp.binary_constraints)

    while queue:

        (xi, xj) = queue.pop(0)

        if remove_inconsistent_values(csp, xi, xj): 
            # if a cell has 0 possibilities, sudoku has no solution
            if len(csp.possibilities[xi]) == 0:
                return False
            
            for Xk in csp.related_cells[xi]:
                if Xk != xi:
                    queue.append((Xk, xi))
                    
    return True

"""
remove_inconsistent_values
returns true if a value is removed
"""
def remove_inconsistent_values(csp, cell_i, cell_j):

    removed = False
    # for each possible value remaining for the cell_i cell
    for value in csp.possibilities[cell_i]:

        # if cell_i=value is in conflict with cell_j=poss for each possibility
        if not any([(value!=poss) for poss in csp.possibilities[cell_j]]):
            
            # then remove cell_i=value
            csp.possibilities[cell_i].remove(value)
            removed = True

    # returns true if a value has been removed
    return removed



if __name__ == "__main__":
    inputstr=""
    lines=stdin.readlines()
    for i in range(9):
        #arr.append(list(map(int,lines[i][0:9])))
        inputstr=inputstr+lines[i][0:9]

    sudoku = Sudoku(inputstr)
    # launch AC-3 algorithm of it
    AC3_result = AC3(sudoku)
    # Sudoku has no solution

    if not AC3_result:
        print("This sudoku has no solution") 
    else:
        print(sudoku)
