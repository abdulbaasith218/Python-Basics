amount=800
tax=amount*0.19
total=amount+tax
print(total)

if total>1000:
        discount=total*0.10
        total-=discount
        print(total)
else:
       print("No discount")
