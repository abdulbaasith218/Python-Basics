#tupples like a list
#but it is immutable(you can not do the modifications)
#in the list we will use []
#in the tupple we will use ()
#tuple is fater than the list(because we use this to only reading)

trip_summary=('ubergo','chennai','airport',450.00,'completed')
print(trip_summary)

print(trip_summary[1])

#loop
#for item in trip_summary:
#    print(item)


#length
#print(len(trip_summary))

#count
print(trip_summary.count('completed'))
print(trip_summary.index('airport'))

#testing the immutable
#trip_summary[1]='tamil naadu'