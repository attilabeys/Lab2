mytuple = ("apple", "banana", "cherry") #this is tuple , using () brackets
#Tuple items are ordered, unchangeable, and allow duplicate values.
print(mytuple[0]) #prints the first item in the tuple, which is "apple"
print(len(mytuple)) # returns the length of tuple

thistuple = ("apple",) #tuple with one item, ALWAYS PUT COMMA IN THE END
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#Like a list, tuple can be every data type
tuple1 = ("apple", "banana", "cherry") #str
tuple2 = (1, 5, 7, 9, 3) #int
tuple3 = (True, False, False) #bool
#mixed tuple
tuple1 = ("abc", 34, True, 40, "male")

mytuple = ("apple", "banana", "cherry")
print(type(mytuple)) # tuple has a class called "tuple"

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #prints last item in the tuple

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) #prints the third, fourth, and fifth item

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) # from the beginning to the fourth number, Not Included

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) # from the second item to the end

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple: #conditions used in tuple
  print("Yes, 'apple' is in the fruits tuple")

  x = ("apple", "banana", "cherry")
y = list(x) #convert to a list to change items, since tuple is unchangeable
y[1] = "kiwi"
x = tuple(y) #convert to a tuple again
print(x)
'''Add values to a tuple'''
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y #add tuple to a tuple to add items
print(thistuple)
'''remove tuple'''
thistuple = ("apple", "banana", "cherry")
del thistuple #deletes whole tuple
print(thistuple) #this will raise an error because the tuple no longer exists

'''Unpacking a tuple'''

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits #unpacking a tuple
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits #asterisk means all left values will be in the new list, called "red"
print(green)
print(yellow)
print(red)
'''Loops with tuples are the same as in the lists'''

'''Join tuples'''
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2  #Multiply tuples
print(mytuple)
'''Tuple methods'''
'''count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''
