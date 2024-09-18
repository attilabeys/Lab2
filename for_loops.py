myTuple = ('python', 'c++', 'Java', 'HTML')
for i in myTuple:
    print(i)

for x in 'python':
    print(x)

#Break statement
for i in myTuple:
    if i == 'Java':
        break #or continue
    print(i)

#in range function
for i in range(5): #for i in range(2, 5);
     print(i)

for i in range(3, 50, 5): #increasing by 5 instead of 1
    print(i)
else:
    print("loop ended") 
for i in range(3, 50, 5):
    print(i)
    if i == 48:
        break
else:
    print("loop ended") 

#Nested loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)