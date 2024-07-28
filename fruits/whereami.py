import inspect

def whereami(msg="", verbose=True):
    data = inspect.stack()
    myself = data[1]

    dmsg = f"[{myself[1]}:{myself[2]}]:{myself[3]} ->{msg}"

    if verbose:
        print(dmsg)
        
    return(dmsg)

def whocalledme():
    data = inspect.stack()
    parent = data[2]

    return(f"[{parent[1]}:{parent[2]}]:{parent[3]} ->")

def calledtree(tree_depth=3, verbose=False):
    data = inspect.stack()
    tree = ""
    
    stack_len = len(data)
    
    if (verbose):
        print(f"stack_len :{stack_len}")
        
    for (i, sf) in enumerate(data):
        if (i == 0):
            continue
        if (i > tree_depth):
            break
        tree = tree + f"#{tree_depth-i}[{data[i][1]}:{data[i][2]}]:{data[i][3]} <-- \n"

    return tree

def whoami():
    return inspect.stack()[1][3]

def whosdaddy():
    return inspect.stack()[2][3]
