#!/usr/bin/python
import re

grid = "08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08\n\
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00\n\
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65\n\
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91\n\
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80\n\
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50\n\
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70\n\
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21\n\
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72\n\
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95\n\
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92\n\
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57\n\
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58\n\
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40\n\
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66\n\
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69\n\
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36\n\
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16\n\
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54\n\
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48"

step = 4

def readMatrix(matrix):
    # Input is a space seperated list of values, with rows denoted by newlines.
    # Output is a two dimensional list of lists
    
    lst = []
    cnt = 0
    regex = re.compile(r"(\d\d)")
    
    for line in matrix.splitlines():
        lst.append([])
        
        for item in re.finditer(regex, line):
            lst[cnt].append(int(item.group(0)))
        # End for
        
        cnt += 1
    # End for
    
    return lst
# End def

def rowSearch(matrix, step):
    # input is a list of lists, each of which contains numbers which are <= 99
    # output is the highest product from among the searched numbers.
    res = 0
    
    for row in matrix:
        head = 0
        tail = head + step
        end = len(row)
    
        while tail <= end:
            tmp = 1
        
            # Any number times zero is always zero, so we should skip the calculations if this set contains a zero.
            if 0 not in row[head:tail]:
            
                for i in range(0, step):
                    tmp *= row[head + i]
                # End for
            
                if tmp > res:
                    res = tmp
                # End if
            # End if
        
            head += 1
            tail += 1
        # End while
    # End for
    
    return res
# End def

def colSearch(matrix, step):
    # input is a parsed matrix (list of lists)
    # output is the highest product from among the searched numbers
    res = 0
    row_end = len(matrix[0]) # This tells us how long each row is
    col_end = len(matrix) # This tells us how deep each column is
    
    for i in range(0, row_end):
        head = 0
        tail = head + step
        
        while tail <= col_end:
            tmp = 1
    
            for j in range(0, step):
                tmp *= matrix[head + j][i]
            # End for
    
            if tmp > res:
                res = tmp
            # End if
    
            head += 1
            tail += 1
        # End while
    # End for
    
    return res
# End def

def diagSearch(matrix, step):
    res = 0
    
    # search diagonally (top left to bottom right), starting from col[0][col_len - step] and going up to, but not including, col[0][0]
    # search diagonally (top left to bottom right), starting from row[0][0] and going to row[0][row_len - step]
    
    start_row
    
# End def

def main():
    max_num = 0
    matrix = readMatrix(grid)
    
    temp = rowSearch(matrix, step)
    if temp > max_num:
        max_num = temp
    # End if
    
    temp = colSearch(matrix, step)
    if temp > max_num:
        max_num = temp
    # End if
    
    temp = diagSearch(matrix, step)
    if temp > max_num:
        max_num = temp
    # End if
    
    #TODO
    # Search diagonally from bottom left to top right
    # Search diagonally from top left to bottom right
    
    print "The greatest product of any four adjacent numbers in this grid is: %s" % max_num
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""In the 20x20 grid below, four numbers along a diagonal line have been marked in red.

08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 * 63 * 78 * 14 = 1788696.

What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20x20 grid?"""