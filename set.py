myset = {"apple", "banana", "cherry"} #using {brackets}
'''Set items are unordered, unchangeable, and do not allow duplicate values.'''
thisset = {"apple", "banana", "cherry"}
print(len(thisset)) #length of data set
#sets can be any data type
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#mixed set
set1 = {"abc", 34, True, 40, "male"}
#type of set
myset = {"apple", "banana", "cherry"}
print(type(myset))
'''Access Set Items'''
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset) #checks if banana is in data set

thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset) #checks if banana is not in data set

'''Add set items'''
thisset = {"apple", "banana", "cherry"}
thisset.add("orange") #add(function) to add items in the set
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical) #add elements from tropical to thisset
print(thisset)

'''Remove items from a data set'''
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana") #remove() function
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana") #discard() method
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop() #removes a random item from the set
print(x)
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.clear() #clears the set
print(thisset)

thisset = {"apple", "banana", "cherry"}
del thisset #deletes all set
print(thisset)

'''Loop Items'''
thisset = {"apple", "banana", "cherry"}
for x in thisset: #usinf for cycle
  print(x)

  '''Join sets'''
  set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2) #Join set1 and set2 to a new set
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2 #the same as the union
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4) #Join multiple sets using union() method
print(myset)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2) #inserts items from set2 into set1
print(set1)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2) #new set with items from both sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2 # & used to join two sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2) # will return only items from set1 that are weren't present in the set2
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2 #the same as the difference
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2) #Keep the items that are not present in both sets
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2) #method to keep the items that are not present in both sets:
print(set1)

'''Set methods'''
'''add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others
'''

