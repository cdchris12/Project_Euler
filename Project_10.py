#!/usr/bin/python

def isPrime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # End if/else block
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        # End if
        
        i = i + 6
    # End while
    
    return True
# End def

def main():
    res = 0
    for i in range(1, 2000000):
        if isPrime(i):
            res += i
        # End if
    # End for
    
    print "The sum of all primes below 2,000,000 is: %s" % res
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""