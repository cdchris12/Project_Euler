#!/usr/bin/python
from math import pow

def main():
    power = 1000
    
    num = pow(2, power)
    
    res = 0
    for i in str((long(num))):
        res += int(i)
    # End for
    
    print "The sum of digits for the %s power of 2 is: %s" % (power, res)
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
""""""