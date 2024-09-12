print(9 > 1) #true
print(9 == 10) #false
a = 100
b = 30
if(a > b):
    print("a is greater than b") #true
else:
    print("b is greater than a")
    '''
    it is always true when there is some content
    '''
    print(bool("I am a student")) #true
    print(bool(667)) #true

    a = 100
    b = 'ghost'
    print(bool(a)) #true
    print(bool(b)) #true
    '''
    the following commands will return FALSE'''
    bool(False)
    bool(None)
    bool(0)
    bool("")
    bool(())
    bool([])
    bool({})
    #Also there is a function that will return false
    class lab2() :
        def __len__(self):
            return 0
        
    task = lab2()
    print(bool(task))
    '''
    You can create a function that returns a Boolean function
    '''
    def task2() :
        return True

    print(task2())

'''we can use boolean with solving tasks'''
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


  #isinstance is the boolean function that return type of variable
  x = 'text'
  print(isinstance(x, str))