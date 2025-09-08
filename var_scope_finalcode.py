delivery_partner='swiggy' #G

def hotel():
    item="pizza"  #E

    def order_now():
        quantity=2  #L
        print(f"ordering {quantity} {item} using {delivery_partner}")
    order_now()

hotel()
#print(quantity)
#print(item)
print(delivery_partner)
print(__file__)


