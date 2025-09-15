class order:
    def __init__(self,customer_name,items,total_amount,discount):
        self.customer_name=customer_name   #public
        self.items=items                   #public
        self.__total_amount=total_amount   #private
        self.__discount=discount           #private


    def __calculate_final(self):
        return self.__total_amount - self.__discount

    def _get_admin_view(self):
        return {
            'customer':self.customer_name,
            'items':self.items,
            'total_amount':self.__total_amount,
            'discount': self.__discount,
            'final_bill':self.__calculate_final(),
        }

    def get_customer_view(self):
        return{
            'customer':self.customer_name,
            'items':self.items,
            'final_bill':self.__calculate_final(),
        }


class adimnportal:
    def show_order(self,order):
        return order._get_admin_view()  #allowed but protected

class customerapp:
    def show_order(self,order):
        return order.get_customer_view()  #safe public method


order = order('gowtham',['pizza','pepsi'],600,150)

admin = adimnportal()
customer = customerapp()

print('admin view:')
print(admin.show_order(order))

print('\n customer view:')
print(customer.show_order(order))