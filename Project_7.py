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
    prime_counter = 0
    cur = 0
    
    while prime_counter <= 10000:
        cur += 1
        
        if isPrime(cur):
            prime_counter += 1
        # End if
    # End while 
    
    print "The 10001st prime number is: %s" % cur
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?"""