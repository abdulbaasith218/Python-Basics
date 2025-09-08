#this is not like a list and tuple(these are ordered)
#the set this is  unordered(this dont maintain the order)
#this is mutable
#here we will use the {}

a={1,2,3}

#you can define the set the set from the list
b=set([1,2,3])
#or
b=set(a)

uber_cities=['chennai','bangalore','chennai','delli','bangalore']
unique_cities=set(uber_cities) #now this will remove the duplicates
print(unique_cities)

uber_cities1={'chennai','mumbai','bangalore'}
uber_cities2={'bangalore','delli','hyd'}
print(uber_cities1.union(uber_cities2))
print(uber_cities1.intersection(uber_cities2))
print(uber_cities2.difference(uber_cities1))

uber_cities1.add('abx') #wherever it can be add
print(uber_cities1)

uber_cities1.remove('mumbai')
print(uber_cities1)


#to search something available
#here using the index position we can not find the element

my_set={1,2,3}
print(my_set)
my_set.remove(1)
my_set.add(26)
print(my_set)

#to remove the particular number. but we dont know available or not , to remove safe we will use the discard
my_set.discard(8)
print(my_set)