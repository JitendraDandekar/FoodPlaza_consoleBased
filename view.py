
from database import CustomerDB, FoodDB, OrderDB

import template
import main


#For user
def login_customer(obj):
    customerdb = CustomerDB()
    customer_details = customerdb.loginChecker(obj.getCustomerEmail(), obj.getCustomerPassword())

    if customer_details:
        return customer_details
    else:
        return False


#For user
def register_customer(obj):
    print('='*30)
    confirm = input('Confirm registration?(Y/N) : ').lower()
    
    if confirm == 'y':
        customerdb = CustomerDB()
        customer = customerdb.add_customer(obj.getCustomerName(), obj.getCustomerEmail(), 
                            obj.getCustomerPassword(), obj.getCustomerAddress(), obj.getCustomerContact())

        if customer:
            print('='*30)
            print('Profile created !')
            print('='*30)
        else:
            template.register()
    
    elif confirm == 'n':
        main.main()
    
    else:
        print('='*30)
        print('Enter proper choice..')
        register_customer(obj)


#For user
def update_customer(obj):
    customerdb = CustomerDB()
    status = customerdb.update_customer(obj.getCustomerName(),obj.getCustomerAddress(),
                                obj.getCustomerContact(), obj.getCustomerEmail())

    if status:
        print('='*30)
        print('Profile updated !')
        print('='*30)
    else:
        print('='*30)
        print('Please fill proper information !')
        print('='*30)
        template.update_profile()


#For user
def delete_customer(obj):
    customerdb = CustomerDB()
    status = customerdb.delete_customer(obj.getCustomerEmail())
    if status:
        print('Profile deleted !')
    

#For admin
def customer_details():
    customerdb = CustomerDB()
    data = customerdb.show_all_customers()
    return data


#For admin
def food_details():
    fooddb = FoodDB()
    data = fooddb.show_all_foods()
    return data


#For admin
def add_food(obj):
    fooddb = FoodDB()
    food = fooddb.add_food(obj.getFoodName(), obj.getFoodQuantity(), obj.getFoodPrice())
    return food


#For admin
def update_food(obj):
    fooddb = FoodDB()
    food = fooddb.update_food(obj.getFoodName(), obj.getFoodQuantity(), obj.getFoodPrice(), obj.getFoodId())
    return food


#for admin
def delete_food(obj):
    fooddb = FoodDB()
    food = fooddb.delete_food(obj.getFoodId())
    return food


#for admin
def order_details():
    orderdb = OrderDB()
    order = orderdb.show_all_orders()
    return order


#for user
def add_order(objs):
    totalBill = 0
    for obj in objs:
        fooddb = FoodDB()
        price = fooddb.order_food(obj.getFoodId())
        fooodPrice = price[2]*obj.getQuantity()

        orderdb = OrderDB()
        order = orderdb.add_order(obj.getCustomerId(), obj.getFoodId(), obj.getQuantity(), fooodPrice)
        if order:
            totalBill += fooodPrice
            fooodPrice = 0
        else:
            break
    else:
        return order, totalBill


#for user
def view_cart(obj):
    orderdb = OrderDB()
    orders = orderdb.view_order(obj.getCustomerId())
    return orders


if __name__ == "__main__":
    login_customer(obj)
    register_customer(obj)
    update_customer(obj)
    delete_customer(obj)
    customer_details()
    food_details()
    add_food(obj)
    update_food(obj)
    delete_food(obj)
    order_details()
    add_order(objs)
    view_cart(obj)