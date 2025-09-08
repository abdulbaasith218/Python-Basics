

playlist=['Shape of you','Naa ready','Beliver','Abc']  #spotify
favourite_foods=['Pizza','Burgar','Dosa','Briyani']    #zomato
recent_locations=['Home','Airport','Work','Mall']      #uber


#in the list we can create the multiple data types in the list
#a=[1,6.3,'gowtham']


print('Spotify playlist:',playlist)
print('Zomato foods:',favourite_foods)
print('Uber locations:',recent_locations)

#list methods:that is a data structure
#list is a muetable: we can update and errace

playlist.append('oo antava')
print('after append:',playlist)

#append: always add in the last

#insert:in the list anywhere we can add the item

playlist.insert(1,'kanmani anbodu')
print('after insert:',playlist)

#remove
playlist.remove('Naa ready')
print('after remove:',playlist)

#pop: pop like a remove but remove the item from the last position of the list
playlist.pop()
print('after pop:',playlist)

#reverse
playlist.reverse()
print('after reverse:',playlist)

#count: to find the index position
print('count:',playlist.count('Beliver'))

#list slicing: like a cutting
#to take the particular position  item from the list we will use the slicing
print('top 2 songs',playlist[:2])
print('last 2 locations:',recent_locations[-2:])
print('last 2 locations:',recent_locations[1:3])

#list iteration
for food in favourite_foods:
    print('all food',food)

for song in playlist:
    print(song ,'by gowtham')

#check the item if it exist
if 'Dosa' in favourite_foods:
    print('yes')

    #or
if 'Dosa' in ['Pizza','Burgar','Dosa','Briyani']:
    print('yes')


#to update the list(Burgar)
favourite_foods[1]='Shawarma'
print(favourite_foods)

#mixed items(multiple data type) in the  list
mixed=['gowtham',64,5.2]
for a in mixed:
    print(a)

#to find the index position
recent_locations=['Home','Airport','Work','Mall']
for i,location in enumerate(recent_locations):
#enumerate returns two things first every location and particular location index position
    print(f'location {i}: {location}')