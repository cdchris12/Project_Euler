#!/usr/bin/python

def FindTriplet():
    a = 1
    b = 2
    c = 3
    
    while a <= 334:
        while b <= 499:
            while c <= 997:
                if a + b + c == 1000:
                    if ((a * a) + (b * b) == (c * c)):
                        return ((a, b, c))
                    # End if
                # End if
                
                c += 1
            # End while
            
            c = 1
            b += 1
        # End while
        
        c = 1
        b = 1
        a += 1
    # End while
    
    return ((1,2,3))
# End def

def main():
    a, b, c = FindTriplet()
    
    print "The pythagorean triplet for which a + b + c equals 1000 is:\
    \na:\t%s\
    \nb:\t%s\
    \nc:\t%s" % (a, b, c)
    
    print "The product of these numbers is: %s" % (a * b * c)
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""