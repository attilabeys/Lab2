thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#Dictionaries are used to store data values in key:value pairs.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
#When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020 #dublicates are not allowed
}
print(len(thisdict))
#ANy data type
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

print(type(thisdict)) #dict type 'dict'

'''Access items'''

x = thisdict.get("model") #Get the value of the "model" key

x = thisdict.keys() #method will return a list of all the keys in the dictionary.

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change

x = thisdict.values() #Get a list of the values

x = thisdict.items() #Get a list of the key:value pairs

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  '''Change Values'''
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

'''Addinf Values'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})

'''Remove Items'''

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model") #method removes the item with the specified key name
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"] # keyword removes the item with the specified key name
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear() #method empties the dictionary
print(thisdict)

'''Loop Dictionary'''

for x in thisdict:
  print(x)

for x in thisdict.values(): #method to return values of a dictionary:
     print(x)
for x in thisdict.keys(): #method to return the keys of a dictionary
   print(x)
for x, y in thisdict.items(): #Loop through both keys and values
  print(x, y)

  '''Copy a dictionary'''
  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy() #Make a copy of a dictionary
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict) #Make a copy of a dictionary
print(mydict)


'''Nested dictionary'''

myfamily = { #dictionary that contains three dictionaries
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"]) #Print the name of child 2

for x, obj in myfamily.items(): #Loop through the keys and values of all nested dictionaries
  print(x)

  for y in obj:
    print(y + ':', obj[y])


    '''Dictionary methods'''

    '''clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary'''