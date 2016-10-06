#!/usr/bin/python

matrix = []
size = 20

def traverseMatrix(cur_pos, cnt):
    # Input will be a tuple of the current position in the list and the current number of routes
    # Output will be the adjusted number of routes
    
    y, x = cur_pos
    
    print "Checking y: %s, x: %s." % (y, x)
    
    # Down
    if y + 1 < size:
        cnt += traverseMatrix((y + 1, x), cnt)
    # End if
    
    # Right
    if x + 1 < size:
        cnt += traverseMatrix((y, x + 1), cnt)
    # End if
    
    # Down and Right
    if y + 1 < size and x + 1 < size:
        cnt += traverseMatrix((y + 1, x + 1), cnt)
    # End if
    
    return cnt
# End def

def main():
    for i in range(20):
        matrix.append([])
        
        for j in range(20):
            matrix[i].append(0)
        # End for
    # End for
    
    cnt = traverseMatrix((0, 0), 0)
    
    print cnt
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?"""