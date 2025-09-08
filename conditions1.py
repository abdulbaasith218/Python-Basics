order_amount=1000
days='mon'
membership='no gold'

if (order_amount >=1000 and days in['sat','sun']) or membership=='gold':
    print('20% discount')

else:
    print('no discount')