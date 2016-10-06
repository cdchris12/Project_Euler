#!/usr/bin/python
from time import sleep

target = 1000000

def getChain(n):
    tot = 1
    
    while True:
        if n == 1:
            break
        elif n % 2 == 0:
            n =  (n / 2)
        else:
            n = ((3 * n) + 1)
        # End if/else block

        tot += 1
        #sleep(.01)
    # End while
    
    return tot
# End def

def main():
    _len = 0
    max_num = 1
    
    for i in range(1, target):
        res = getChain(i)
        
        if res > _len:
            _len = res
            max_num = i
        # End if
        
        if i % 1000 == 0:
            print "Checked number %s" % i
        # End if
    # End for
    
    print "The starting number below %s that produces the longest chain using the provided rules is: %s, with a total chain length of %s." % (target, max_num, _len)
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""The following iterative sequence is defined for the set of positive integers:

n > n/2 (n is even)
n > 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 > 40 > 20 > 10 > 5 > 16 > 8 > 4 > 2 > 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million."""