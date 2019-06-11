# ==============================PROBLEM==============================
# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

#     I can be placed before V (5) and X (10) to make 4 and 9. 
#     X can be placed before L (50) and C (100) to make 40 and 90. 
#     C can be placed before D (500) and M (1000) to make 400 and 900.

# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.


# ==============================RESTATEMENT==============================
# For any given a roman numeral from 1 to 3999 return the equivalent integer.


# ==============================CLARIFICATION==============================
# Is the input 
# Are the inputs guaranteed to be valid Roman Numerals?
#     Would I need to account for invalid inputs?
# Does casing matter?


# ==============================ASSUMTIONS==============================


# ==============================SOLUTIONS==============================

VALUES = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}


def rom_to_int(rom=''):
    if len(rom) == 0:
        return 0
    
    i = len(rom) - 1
    val = 0

    while i >= 0:
        try:
            if VALUES[rom[i+1]] > VALUES[rom[i]]:
                val -= VALUES[rom[i]]
            else:
                val += VALUES[rom[i]]
            i -= 1
        except IndexError:
            val += VALUES[rom[i]]
            i -= 1
        
    return val
