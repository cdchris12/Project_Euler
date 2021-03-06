#!/usr/bin/python

f1 = 1
f2 = 2
sum = 0

while f2 <= 4000000:
    if f2 % 2 == 0: sum += f2
    temp = f1
    f1 = f2
    f2 = f1 + temp
# End while

print "The sum of even valued terms in the Fibonacci sequence whose values do not exceed 4 Million is: %s" % sum

# Goal:
"""Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms."""