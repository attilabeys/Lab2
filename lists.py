list = ["pen", "pencil", "book"] #store multiple items in a single variable
print(list) 
'''List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

'''
list2 = ["beer", "beer", "vodka", "whiskey", "vodka"] #list allows dublicates
print(list2)
print(len(list2)) #How many values in the list

list1 = ["apple", "banana", "cherry"] #string
list2 = [1, 5, 7, 9, 3] #int
list3 = [True, False, False] #boolean

'''mixed list'''
mixedList = ["text", 5, True, "oneMore"]
print(mixedList)
print(type(myList)) #list has type "list" 

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist) # another way to create list

print(list2[0]) #print the first item in the list
print(list2[-1]) #print the first item in the list from the end
print(list2[4:6]) #return the fourth, fifth, and sixth elements from the list

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: #checks if apple is in the list
  print("Yes, 'apple' is in the fruits list") 

thislist[2] = "beer" #change the item in the list
print(thislist) 

thislist.insert(2, "Jim Beam") #insert new value as the third item
thislist.append("Milk") #append an item to the end of the list
print(thislist)

thatlist = ["strawberry", "blueberry", "grape"]
thislist.extend(thatlist) #extend the list with the items from thatlist

thislist.remove("apple") #removes item from the list
'''if there are some items with the same name, remove() will remove the first occurency'''

thislist.pop(1) #removes the specified index
print(thislist)
thislist.pop() #removes last item
print(thislist)
del thislist(0) #also removes the specified index
del thislist # deletes all list

list1.clear() #clear all list content
print(list1) #prints: []

'''Loop through a list'''
for x in thatlist:
  print(x)
  for i in range(len(thatlist)):
    print(thatlist[i])
i = 0
while i < len(thatlist):
  print(thatlist[i])
  i = i + 1
[print(x) for x in thatlist]
'''List Comprehension'''
#List Comprehension is a compact way to create lists
for x in thatlist: #common method
  if "w" in x:
    list2.append(x)

    list2 = [x for x in thatlist if "w" in x]

newlist = [x for x in range(10)] #range() function to create an iterable
newlist = [x for x in range(10) if x < 5] #Accept only numbers lower than 5
newlist = [x.upper() for x in thatlist] #values to upper case
newlist = [x if x != "banana" else "orange" for x in thatlist] #Return "orange" instead of "banana"
'''Sort list'''
thislist.sort() #sorts the list in-place alphanumerically
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True) #sort descending, case sensitive, firstly there are capital letters
print(thislist) 
#Customized sort
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc) #Sort the list based on how close the number is to 50
print(thislist)

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse() #REverse the order
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy() #Copy method
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist) #Copy using a list() function
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:] #Copy using a slice operator
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2 #Join 2 lists
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x) #joining lists using append() function
print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2) #add items to the end of list1
print(list1)

#List methods
'''append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list'''