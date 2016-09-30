#!/usr/bin/python

def isPal(n):
    # Tests integers to validate if they are palindromes.
    
    string = str(n)
    length = len(string)
    
    # Single digits are automatically palindromes!
    if length == 1:
        return True
    # End if
    
    # The variable "mid" will be the begining of the second half of the tested palindrome
    mid = len(string) / 2
    end = mid-1
    
    # For strings with an even number of digits, we need to test every digit in the number. For strings with an odd number of digits, we need to skip over checking just the middle number.
    if len(string) % 2 != 0: 
        mid += 1
    # End if
    
    while end >=0:
        if string[end] is string[mid]:
            end -= 1
            mid += 1
        else:
            return False
        # End if/else block
    # End while
    return True
# End def

x = 100
y = 100
pal = 0

while x <= 999:
    while y <= 999:
        temp = x * y
        if isPal(temp):
            if temp > pal:
                pal = temp
                #print "Assigned %s to pal!!" % temp
            # End if
        # End if
        y += 1
    # End while
    y = 100
    x += 1
# End while


print "The largest palindromic number made from a set of three digit numbers is: %s" % pal

# Goal:
"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers."""