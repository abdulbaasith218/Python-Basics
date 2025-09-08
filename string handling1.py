song='shApe OF yOu'
artist='goWtHam sB'

formated=f"{song.title()}-{artist.title()}"
print(formated)
#for the replacement
location='jaffna'
fixed_location=location.replace('jaffna',  'colombo')
print(fixed_location)


#for the division of the sentences
message='your uber booking id is:UB1234.please keep it safe'
booking_id=message.split(':')[1]
print(booking_id)

#strip is used to remove the space
booking_id=message.split(':')[1].split('.')[0].strip()
print(booking_id)
#delimiters uss to devide the colom(sentence) that will be charectors(like ,;/....)


#to cheak the paticular word from the particular msg
promo_msg='use zomato100 to get 100 off on your first order'
if 'zomato100' in promo_msg:
  print('offer applied')

#find the position of a particular word
feedback='the driver was polite and the ride was smooth'
print('position is:',feedback.find('polite'))


#to get the first letter of first word and second word
name='gowtham subramani'
initials=([word[0].upper() for word in name.split()])
print(initials)

#to remove the list we use ("".join)
#when we write the for loop in the single line  first we will write the logic then the loop
name='gowtham subramani'
initials="".join([word[0].upper() for word in name.split()])
print(initials)

#strip() use to remove the extra space
dirty_input=' airport '
print(dirty_input)

clean=dirty_input.strip()
print(clean)

#to count the no of words
word='the trip was amazing and the car was clean'
word_count=len(word.split())  #split using the space
print('word count is:', word_count)

word='the trip was amazing and the car was clean'
word_count=len(word.split('and'))  #split using the and
print('word count is:', word_count)