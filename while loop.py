correct_pin='1234'
entered_pin=''

#here user have to enter the correct_pin otherwise that will ask enter your pin like that until write the correct pin
while entered_pin != correct_pin:
    entered_pin = input('enter your correct pin:')

print('access granted')