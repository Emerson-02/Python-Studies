'''
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
'''

def romanToInt(s):
    roman = []
    roman[:0] = s
    #print(len(roman))
    dec = 0
    for i in range(len(roman)):
        #print(i)
        if i > 0:
            if roman[i] == 'V' and roman[i-1] == 'I':
                dec = dec + 3
            elif roman[i] == 'X' and roman[i-1] == 'I':
                dec = dec + 8
            elif roman[i] == 'L' and roman[i-1] == 'X':
                dec = dec + 30
            elif roman[i] == 'C' and roman[i-1] == 'X':
                dec = dec + 80
            elif roman[i] == 'D' and roman[i-1] == 'C':
                dec = dec + 300
            elif roman[i] == 'M' and roman[i-1] == 'C':
                dec = dec + 800
            elif roman[i] == 'I':
                dec = dec + 1
            elif roman[i] == "V":
                dec = dec + 5
            elif roman[i] == "X":
                dec = dec + 10
            elif roman[i] == "L":
                dec = dec + 50
            elif roman[i] == "C":
                dec = dec + 100
            elif roman[i] == "D":
                dec = dec + 500
            elif roman[i] == "M":
                dec = dec + 1000
        else:
            if roman[i] == 'I':
                dec = dec + 1
            elif roman[i] == "V":
                dec = dec + 5
            elif roman[i] == "X":
                dec = dec + 10
            elif roman[i] == "L":
                dec = dec + 50
            elif roman[i] == "C":
                dec = dec + 100
            elif roman[i] == "D":
                dec = dec + 500
            elif roman[i] == "M":
                dec = dec + 1000
        
    return dec



romanToInt('XVII') #17
romanToInt('XCIX') #99
romanToInt('CMVI') #906
romanToInt('MMXXII') #2022
romanToInt('CMMLXXIX') #1979
print(romanToInt('MCDLXXVI'))

