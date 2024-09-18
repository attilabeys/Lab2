#introduction to If condition
w1 = 56
w2 = 45
if(w1 > w2):
    print('w2 is lighter than w1')
#Elif condition
w1 = 45
w2 = 54
if w1 > w2:
     print('w2 is lighter than w1')
elif w2 > w1: #try this condition if previous doesnt work
     print('w1 is lighter than w2')
else:
     print('Both are equal')
if w1 > w2: print('w2 is lighter than w1') #short hand
#nested if
if w1 > w2:
     if w1 == 45:
         if w2 == 54:
              print('nested if')

#pass
if(w1 > w2):
     pass