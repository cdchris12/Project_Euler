#!/usr/bin/python

def SumSquare(start, end):
    end += 1
    sq_sum = 0
    
    for i in range(start, end):
        sq_sum += (i * i)
        #print "i: %s\t\t sum: %s" % (i, sq_sum)
    # End for
    
    return sq_sum
# End def

def SquareSum(start, end):
    end += 1
    to_sq = 0
    
    for i in range(start, end):
        to_sq += i
    # End for
    
    return to_sq * to_sq
# end def

sumSq = SumSquare(1, 100)
sqSum = SquareSum(1, 100)
diff = sqSum - sumSq


print "The difference between the squares of the first 100 natural numbers and the sum of the squares of the first 100 natural numbers is: %s" % diff

# Goal:
"""The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""