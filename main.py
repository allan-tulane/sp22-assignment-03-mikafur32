# assignment-03

# no other imports needed
from collections import defaultdict
import math


### PARENTHESES MATCHING

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])


def reduce(f, id_, a):
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        return f(reduce(f, id_, a[:len(a) // 2]),
                 reduce(f, id_, a[len(a) // 2:]))


#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """

    result = iterate(parens_update, '', mylist)
    return len(result) == 0  # if 0, then no unmatched


def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    if len(current_output) == 0:
        return next_input

    if current_output[
        -1] == '(' and next_input == ')':  # most recent in curroutput. [-1] = last element, first from back
        return current_output[:-1]

    elif not (current_output[-1] in '()'):
        return next_input

    elif (next_input in '()'):
        return current_output + next_input

    elif not (next_input[-1] in '()'):
        return current_output


def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    mappingResult = []
    for paren in mylist:  # to get map
        mappingResult.append(paren_map(paren))

    if mappingResult[0] == -1 or mappingResult[len(mappingResult) - 1] == 1 or reduce(plus, 0, mappingResult) != 0:
        return False
    return True


def plus(x, y):
    return x + y


def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
        [reduce(f, id_, a[:i + 1]) for i in range(len(a))],
        reduce(f, id_, a)
    )


def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """

    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0


def min_f(x, y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y


def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False


#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n = parens_match_dc_helper(mylist)
    return n[0] == 0 and n[1] == 0


def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """
    if len(mylist) == 0:
        return (0, 0)  # satisfy []
    elif len(mylist) == 1:
        if mylist[0] == '(':
            return (0, 1)
        elif mylist[0] == ')':
            return (1, 0)
        else:
            return (0, 0)

    right = parens_match_dc_helper(mylist[:len(mylist) // 2])
    left = parens_match_dc_helper(mylist[len(mylist) // 2:])
    # need a way of conditionally adding tuples. Regular plus doesnt work. --> tuplePlus

    left, right = reduce(tuplePlus, [0, 0], [left]), reduce(tuplePlus, [0, 0], [right])
    return tuplePlus(left, right)


def tuplePlus(left, right):
    leftlst = list(left)  # cant edit info of tuples. Cast to list, then take their values.
    rightlst = list(right)
    if (left[0] > 0 and right[1] > 0):  # (n, k), n > 0, k > 0
        theta = left[0]
        lambd = right[1]  # carrier

        leftlst[0] = abs(theta - lambd)  # don't want them to go negative
        rightlst[1] = abs(lambd - theta)
    return (leftlst[0] + rightlst[0], leftlst[1] + rightlst[1])  # add the remaining to next tuple


def test_parens_match_dc():
    # print(parens_match_dc(['(', ')']))
    # print(parens_match_dc(['(']))
    # print(parens_match_dc([')']))

    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False
