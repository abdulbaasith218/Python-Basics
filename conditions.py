age=15
if age>=18:
    print('you can vote')
else:
    print('you can not vote')

#conditions: if/elif/else
#when we have lot of conditions
mark=34
if mark >=75:
    print('Grade A')
elif mark >=65:
    print('Grade B')
elif mark >=50:
    print('Grade C')
elif mark >=35:
    print('Grade S')
else:
    print('Grade W')

#nested if/else
#for multiple conditions
age=19
has_license='no'
if age>=18:
    if has_license=='yes':
        print('you can drive')
    else:
        print('go and take license')
else:
    print('you are not authorized')


#the condition using the and logic
mark=54
attendence=74

if mark >=55 and attendence >=70:
    print('You are allowed for exam')
else:
    print('You are not allowed for exam')


#The conditions using the or logic
if mark >= 55 or attendence >= 70:
    print('You are allowed for exam')
else:
    print('You are not allowed for exam')
