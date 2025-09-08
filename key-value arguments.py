#k-args
#to give the key value parameters
#ex: for k-args
# name(key):gowtham (value)
# age(key)=30 (value)

def create_profile(**kwargs):
    print('use profile')
    for key,value in kwargs.items():
        print(f'{key}:{value}')

create_profile(name='John',age=20,job='Engineer')
