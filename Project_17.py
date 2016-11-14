#!/usr/bin/python
import math

def getThousands(i):
    orig = i
    
    i -= (i % 1000)
    # Remove everything but the thousands place
    
    i /= 1000
    # Divide to get the raw number of thousands
    
    if (orig % 1000) == 0:
        return getOnes(i) + " thousand"
    else:
        return getOnes(i) + " thousand "
    # End if/else block
# End def

def getHundreds(i):
    orig = i
    
    i -= (i % 100)
    # Remove everything but the hundreds place
    
    i /= 100
    # Divide to get the raw number of hundreds
    
    if (orig % 100) == 0:
        return getOnes(i) + " hundred"
    else:
        return getOnes(i) + " hundred and "
        # Adding the "and" here is very important
    # End if/else block
# End def

def getTens(i):
    table = {
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "fourty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninty"
    }
    
    if i in table:
        return (table[i], False)
    else:
        i -= (i % 10)
        # Remove everything but the tens place
    
        return (table[i] + "-", True)
        # Adding the "-" here is very important
    # End if/else block
# End def

def getOnes(i):
    table = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }
    
    return table[i]
# End def

def main():
    _max = 1000
    _min = 1
    
    length = 0
    
    for i in xrange(_min, _max + 1):
        res = ""
        cont = True
        
        if i >= 1000:
            res += getThousands(i)
            i %= 1000
        # End if
        
        if i >= 100:
            res += getHundreds(i)
            i %= 100
        # End if
        
        if i >= 10:
            tmp, cont = getTens(i)
            res += tmp
            i %= 10
        # End if
        
        if i != 0 and cont:
            res += getOnes(i)
        # End if
        
        res = res.replace(" ", "").replace("-", "")
        length += len(res)
    # End for
    
    print "The total number of letters used to write out the spellings of the numbers from %s to %s (inclusive) is: %s!" % (_min, _max, length)
# End def

if __name__ == "__main__":
    main()
# End if

# Goal:
"""If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage."""