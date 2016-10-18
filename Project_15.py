#!/usr/bin/python

from time import sleep

memory = {
    (0,1): 1,
    (1,0): 1
}

matrix = []
size = 20

def traverseMatrix(cur_pos):
    # Input will be a tuple of the current position in the list and the current number of routes
    # Output will be the adjusted number of routes
    
    y, x = cur_pos
    
    #print "Checking y: %s, x: %s." % (y, x)
    #print "Count is: %s" % cnt
    
    if cur_pos in memory:
        return memory[cur_pos]
    # End if
    
    paths = 0
    if 0 in cur_pos:
        paths += 1
    else:
        paths = traverseMatrix((y, x - 1)) + traverseMatrix((y - 1, x))
    # End if/else block
    
    memory[cur_pos] = paths
    return paths
# End def

def main():
    for i in range(20):
        matrix.append([])
        
        for j in range(20):
            matrix[i].append(0)
        # End for
    # End for
    
    cnt = traverseMatrix((size, size))
    
    print cnt
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?"""