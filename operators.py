'''Arithmetic operators'''
print(5 + 5) #addition
print(5 - 5) #substraction
print(5 * 5) #multiplication
print(5 / 5) #division
print(5 % 5) #modulus (остаток)
print(5 ** 5) #exponentiation
print(5 // 5) #floor division (без остатка)
'''Assignment opperators'''
x = 5 # assign value to variable
x += 5 # x = x + 5
x -= 5 # x = x - 5
x *= 5 # x = x * 5
x /= 5 # x = x / 5
x %= 5 # x = x % 5
x //= 5 # x = x // 5
x **= 5 # x = x ** 5
x &= 5 # x = x & 5
print(x := 5) # x = 3 print(x)
'''Comparison operators'''
y = 4
x == y #Equal
x != y #Not equal
x > y #Greater than
x < y #Less than
x >= y #Greater than or equal
x <= y #Less than or equal
'''Logical operators'''
x < 5 and x < 10 #returns true if both conditions are true
x < 5 or x < 10 #returns true if at least one condition is true
not(x < 5 and x < 10) #Reverse result, returns false if the result is true
'''Identity operators'''
x is y #checks if both variables are the same object
x is not y #checks if both variables are not the same object
'''Membership operators'''
x in y #checks if a value is present in a sequencec
x not in y #checks if a value is not present in a sequencec
'''Bitwise operators'''
x & y #AND sets each bits to 1 if both bits are 1
x | y #OR sets eah bit to 1 if one bit is one
x ^ y #XOR sets each bit to 1 if onle one of two bits is 1
~x #NOT inverts all the bits
x << 2 #zero fill left Shift left by pushing zeros in
x >> 2 #shift right by pushing copies of leftmost bit in from the left
'''Operator Precedence'''
print(3 + 4 * 2) #3 + (4 * 2) 
print(3 + 4**2) #3 + 16
