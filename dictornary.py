#dictonary will not allow the duplicate
trip= {
    "trip id":"UB12345",
    "pickup":"chennai",
    "dropoff":"airport",
    "fare":430.25,
    "driver":"ravi",
    "status":"completed"
}

#here using the key we can access the value
#that will call as a lookup
print(trip['pickup']) #lookup

print(trip.get('pickup'))
print(trip.get('airport')) #here now this cheak the airport in the key, that is not available , so it will not show the error
#instead show like a NONE
#using this we can run the code without the error

print(trip.keys()) #this will take and show the all keys from the dictornary
print(trip.values())#like a keys(), it shows the values


for key,value in trip.items(): #item() , this will return the two, that are key and value
    print(key,':',value)

#lets do the update
trip.update({'car_model':'suzuki'})
print(trip)
#update mean like a upsert
#upsert mean if the particular element available then update, not available add or insert that

trip.pop('status') #pop mean it will remove the element from the last
print(trip)


#to cheak the duplicates
abc={
    'as':'fj123',
    'je':'qded',
    'kj':['hk','jf','gf','rd'], #you can keep the multiple values
    'dsd':123,
    'as':'ab'
}
print(abc) #here this did not allow the duplicate, but it shows the latest update in the duplicate key


#here, this hydration also shows the all multiple values in the single key
for key,value in abc.items():
    print(key,':',value)

#to access the jf single value from the kj key, this is a process below
print(abc['kj'][1])

#to show the list from the dictornary
for location in abc['kj']:
    print(location)








