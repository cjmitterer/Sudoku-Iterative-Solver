import ast

#with open("sudoku-constraints.py") as constraints_file:
#    csp = ast.literal_eval(constraints_file.read())

simplePuzzle = [[1, None, None, None],
                [None, 2, None, None],
                [None, 4, None, None],
                [None, None, None, 3]]
puzzleOne = [[7,    None, None, 4,    None, None, None, 8,    6],
             [None, 5,    1,    None, 8,    None, 4,    None, None],
             [None, 4,    None, 3,    None, 7,    None, 9,    None],
             [3,    None, 9,    None, None, 6,    1,    None, None],
             [None, None, None, None, 2,    None, None, None, None],
             [None, None, 4,    9,    None, None, 7,    None, 8],
             [None, 8,    None, 1,    None, 2,    None, 6,    None],
             [None, None, 6,    None, 5,    None, 9,    1,    None],
             [2,    1,    None, None, None, 3,    None, None, 5]]
puzzleTwo = None
puzzleThree = None
puzzleFour = None
puzzleFive = None

def print_hi(name):
    print(f'Hi, {name}')

# Maybe use a class, we'll see
class State:
    counter = 0

# 1

fourxFourDomainPuzzle = {
    'C11': [1],
    'C12': [1, 2, 3, 4],
    'C13': [1, 2, 3, 4],
    'C14': [1, 2, 3, 4],

    'C21': [1, 2, 3, 4],
    'C22': [2],
    'C23': [1, 2, 3, 4],
    'C24': [1, 2, 3, 4],

    'C31': [1, 2, 3, 4],
    'C32': [1, 2, 3, 4],
    'C33': [3],
    'C34': [1, 2, 3, 4],

    'C41': [1, 2, 3, 4],
    'C42': [1, 2, 3, 4],
    'C43': [1, 2, 3, 4],
    'C44': [4]
}


fourxFourConstraints = {
    ('C11', 'C12'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C13'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C11', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C12', 'C13'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C21'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C12', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C13', 'C14'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C13', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C14', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C14', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C14', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C14', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C21', 'C22'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C31'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C21', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C22', 'C23'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C22', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C22', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C22', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C23', 'C24'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C23', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C23', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C24', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C24', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C31', 'C32'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C31', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C32', 'C33'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C32', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C32', 'C41'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C32', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C33', 'C34'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C33', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C33', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C34', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C34', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C41', 'C42'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C41', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C41', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C42', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],
    ('C42', 'C43'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]],

    ('C43', 'C44'): [[1, 2], [1, 3], [1, 4], [2, 1], [2, 3], [2, 4], [3, 1], [3, 2], [3, 4], [4, 1], [4, 2], [4, 3]]
}

# 1 TODO
nineXNineConstraints = {
    # See constraints file
}

# 2 TODO
# May need to sort var1 and var2

# Inputs:
#   domains: this is the list



def helper(i, c1, c2, domain):
    for j in domain:
        if c1 is not None and [i, j] in c1 or c2 is not None and [i, j] in c2:
            return True
    return False

# Uses list comprehension, iterate over a list easily

def revise(constraints, domain, var1, var2):
    initial = len(domain[var1])
    c1 = constraints.get((var1, var2))
    c2 = constraints.get((var2, var1))
    domain[var1][:] = [i for i in domain[var1] if helper(i, c1, c2, domain[var2])] # Helper returns true or false, if true something doesn't
    return initial != len(domain[var1]) # If size changes something got removed



"""
def revise(CSP, var1, var2):
    values1 = [CSP[k] for k in CSP.keys() if k[0] == var1 or k[1] == var1]
    values2 = [CSP[k] for k in CSP.keys() if k[0] == var2 or k[1] == var2]
    for x in values1:
        for y in values2:
            if () and x != y:
                revised = True
                #remove x from values1
                break
"""

# 3 TODO
#BADDDD
def AC3(domain, constraints):
    arc = list(constraints)
    while arc:
        (xi, xj) = arc.pop(0)

        if(revise(constraints, domain, xi, xj)):
            if(len(domain[xi]) == 0):
                return False
        for xk in domain[xi]:######THIS IS WRONG FIND BETTER ROUTE
            if xk != xi:
                arc.append(xk, xi)

        #if c1 is not None and [i, j] in c1 or c2 is not None and [i, j] in c2
    return True



# 4 TODO
# ALSO BAD
def minimumRemainingValues(domain, constraints, assignments):
    currentMin = 10000000000
    location = None
    for x in domain:
        if(len(x) < currentMax and len(x) > 1):
            currentMax = len(x)
            location = x
    return location

# 5 TODO

def backTrackingSearch(domain, constraints, assignments):
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hellow World")
   #print(fourxFourConstraints.get(('C11', 'C12')))
    print(revise(fourxFourConstraints, fourxFourDomainPuzzle, 'C11', 'C12'))