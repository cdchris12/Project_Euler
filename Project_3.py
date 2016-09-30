#!/usr/bin/python

original = 600851475143
i = 2
n = original

while i * i < n:
    while n % i == 0:
        n = n / i
    # End while
    i += 1
# End while

print "The largest prime factor of %s is: %s" % (original, n)

#Goal:
"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""