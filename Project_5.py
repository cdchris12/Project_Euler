#!/usr/bin/python

def isEvenDiv(n, to):
    for a in range(1,to):
        if n % a != 0: 
            return False
        # End if
    # End for
    
    return True
# end div

i = 1
while True:
    if isEvenDiv(i, 20):
        break
    else:
        i += 1
    # End if/else block
    
    #if i % 1000000 == 0: print "Tested %s !!" % i
# End while


print "The smallest number that is evenly divisible by all numbers from 1 - 20 is: %s" % i

# Goal:
"""2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""