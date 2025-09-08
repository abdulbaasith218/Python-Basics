#now we are going to do first we will write the function on one file
#then we will call that function from the another function

'''
def add(a,b):
    return a+b

'''

#now you go to the hello.py file
# in the args we can out the lot of arguments
#if you increase the no of arguments it automatically will give the answer

def add(*args):   #args: accept any arguments
    total = 0
    for num in args:
        total+=num
        #0+=1
        #1+=2
        #2+=8
        #then finally total will be = 11

        #any no of arguments you can put

    return total



#print(add(1,2,8))