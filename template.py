from model import Customer, Food, Order

import view
import getpass
import main


#Admin Login
def admin():
    print('\1 Login as Admin') 
    email = input('Enter Username : ')
    password = getpass.getpass('Enter Password : ')
    if email == 'admin' and password == 'admin@123':
        main.admin_menu()
    else:
        main.main()


#User Login
def login():
    print('\1 Log In')
    t = 0
    while t < 3: 
        email = input('Enter Email : ')
        password = getpass.getpass('Enter Password : ')
        
        if email == '' and password == '':
            print('='*30)
            print('Enter proper Username & Password')
            t += 1
        else:
            customer = Customer()
            customer.setCustomerEmail(email)
            customer.setCustomerPassword(password)
            
            print('='*30)
            global user
            user = view.login_customer(customer)
            if user:
                print('Welcome {} !'.format(user[0]))
                print('='*30)
                main.menu()
            else:
                print('Invalid Credential !')
                print('='*30)
                t += 1
    main.main()


#User Registration
def register():
    print('Enter Details')
    print('='*30)
    name = input('Name : ')
    address = input('Address : ')
    contact = input('Contact : ')
    email = input('Email : ')

    if name == '' or address == '' or contact == '' or email == '':
        print('='*30)
        print('All fields are mendatory !')
        register()
    else:
        customer = Customer()
        customer.setCustomerName(name)
        customer.setCustomerAddress(address)
        customer.setCustomerContact(contact)
        customer.setCustomerEmail(email)
    
    while True:
        password = getpass.getpass('Password : ')
        password1 = getpass.getpass('Confirm Password : ')
        if password == '' and password1 == '':
            print('='*30)
            print('Password should not be null !')
            print('='*30)
        elif password == password1:
            customer.setCustomerPassword(password)        
            view.register_customer(customer)
            break
        else:
            print('='*30)
            print('Password Mismatched !\nPlease re-enter password !')
            print('='*30)


#user profile
def view_profile():
    print('Name :', user[0])
    print('Email :', user[1])
    print('Address :', user[2])
    print('Contact :', user[3])
    print('='*30)


#for user
def update_profile():
    print('Enter Details\nPress enter to set default')
    print('='*30)
    print('Current Name :', user[0])
    name = input('Enter Name : ')
    print('Current Address :', user[2])
    address = input('Enter Address : ')
    print('Current Contact :', user[3])
    contact = input('Enter Contact : ')

    if name == '' and address == '' and contact == '':
        print('='*30)
        print('Updation Failed !')
        print('='*30)
        main.profile()
    else:
        if name == '':
            name = user[0]
        if address == '':
            address = user[2]
        if contact == '':
            contact = user[3]
        
        while True:
            print('='*30)
            confirm = input('Confirm updation?(Y/N) : ').lower()
            print('='*30)
            if confirm == 'y':
                customer = Customer()
                customer.setCustomerName(name)
                customer.setCustomerAddress(address)
                customer.setCustomerContact(contact)
                customer.setCustomerEmail(user[1])

                view.update_customer(customer)
                login()
            elif confirm == 'n':
                main.profile()
            else:
                print('='*30)
                print('Enter proper choice !')


#for user
def delete_profile():
    while True:
        confirm = input('Want to delete account?(Y/N) : ').lower()
        print('='*30)
        if confirm == 'y':
            customer = Customer()
            customer.setCustomerEmail(user[1])
            view.delete_customer(customer)
            main.main()
        elif confirm == 'n':
            main.profile()
        else:
            print('='*30)
            print('Enter proper choice !')


#for admin
def show_customers():
    customers = view.customer_details()
    if customers:
        print('-'*126)
        print('|{:^20}|{:^20}|{:^30}|{:^30}|{:^20}|'.format('id', 'name', 'email', 'address', 'contact'))
        print('-'*126)
        for row in customers:
            print('|{:^20}|{:^20}|{:^30}|{:^30}|{:^20}|'.format(row[0], row[1], row[2], row[3], row[4]))
        print('-'*126)
    else:
        print('Records not founds !')


#for admin
def show_foods():
    foods = view.food_details()
    if foods:
        print('-'*85)
        print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format('id', 'name', 'quantity', 'price'))
        print('-'*85)
        for row in foods:
            print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format(row[0], row[1], row[2], row[3]))
        print('-'*85)
    else:
        print('Records not founds !')


#to add food items for admin
def create_food():
    print('Enter Details')
    print('='*30)
    foodName = input('Food Name : ')
    quantity = input('Food Quantity : ')
    price = float(input('Price : '))

    if foodName == '' or quantity == '' or price == '':
        print('='*30)
        print('All fields are mendatory !')
        create_food()
    else:
        food = Food()
        food.setFoodName(foodName)
        food.setFoodQuantity(quantity)
        food.setFoodPrice(price)
        status = view.add_food(food)
        if status:
            print('='*30)
            print('Food added !')
        else:
            print('='*30)
            print('Process Failed !')


#for admin
def food_update():
    print('Enter Details')
    print('='*30)

    foodId = int(input('Enter Food Id : '))
    name = input('Enter Name : ')
    quantity = input('Enter Quantity : ')
    price = float(input('Enter Price : '))

    if foodId == '' or name == '' or quantity == '' or price == '':
        print('='*30)
        print('All fields are mendatory !')
        print('='*30)
        food_update()
    else:
        while True:
            print('='*30)
            confirm = input('Confirm updation?(Y/N) : ').lower()
            print('='*30)
            if confirm == 'y':
                food = Food()
                food.setFoodId(foodId)
                food.setFoodName(name)
                food.setFoodQuantity(quantity)
                food.setFoodPrice(price)

                status = view.update_food(food)
                if status:
                    print('='*30)
                    print('Food Updated !')
                    main.admin_menu()
                else:
                    print('='*30)
                    print('Process Failed !')
                    food_update()
            elif confirm == 'n':
                main.admin_menu()
            else:
                print('='*30)
                print('Enter proper choice !')


#for admin
def food_delete():
    foodId = int(input('Enter Food Id : '))
    print('='*30)
    while True:
        confirm = input('Want to delete food?(Y/N) : ').lower()
        print('='*30)
        if confirm == 'y':
            food = Food()
            food.setFoodId(foodId)
            status = view.delete_food(food)
            if status:
                print('='*30)
                print('Food Deleted !')
                main.admin_menu()
            else:
                print('='*30)
                print('Process Failed !')
                food_delete()
        elif confirm == 'n':
            main.admin_menu()
        else:
            print('='*30)
            print('Enter proper choice !')


#for admin
def show_orders():
    orders = view.order_details()
    if orders:
        for order in orders:
            print('customer_id :', order[0])
            print('customer_name :', order[1])
            print('customer_email :', order[2])
            print('customer_address :', order[3])
            print('customer_contact :', order[4])

            fname = order[5].split(',')
            fprice = order[6].split(',')
            fquantity = order[7].split(',')
            oquantity = order[8].split(',')
            fbill = order[9].split(',')
            print('-'*106)
            print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'
            .format('food_name', 'food_price', 'food_quantity', 'order_quantity', 'food_bill'))
            print('-'*106)
            for (food_name, food_price, food_quantity, quantity, bill) in zip(fname, fprice, fquantity, oquantity, fbill):
                print('|{:^20}|{:^20}|{:^20}|{:^20}|{:^20}|'
                .format(food_name, food_price, food_quantity, quantity, bill))
            print('-'*106)
            print('total_bill :', order[10])
            print('order_date :', str(order[11]))
            print('='*30)
    else:
        print('Records not founds !')


#for user to place order
def create_order():
    show_foods()
    print('Add Your Order')
    print('='*30)
    orders = []
    while True:
        try:
            foodId = int(input('Food Id : '))
            foodQuantity = int(input('Food Quantity : '))
            if foodId == '' or foodQuantity == '':
                print('='*30)
                print('All fields are mendatory !')
            else:
                order = Order()
                order.setCustomerId(user[4])
                order.setFoodId(foodId)
                order.setQuantity(foodQuantity)
                orders.append(order)
                
                print('='*30)
                add = input('Add more order?(Y/N) : ').lower()
                print('='*30)
                if add == 'y':
                    pass
                elif add == 'n':
                    status = view.add_order(orders)
                    if status[0]:
                        print('='*30)
                        print('Ordered Successfully !')
                        print('-'*30)
                        print('Total Bill :', status[1])
                        main.menu()
                    else:
                        print('='*30)
                        print('Order Failed !')
                else:
                    print('='*30)
                    print('Entered wrong choice..') 
                    print('='*30)

        except ValueError:
            print('='*30)
            print('Enter valid data')
            print('='*30)


#for user
def show_cart():
    customer = Customer()
    customer.setCustomerId(user[4])
    carts = view.view_cart(customer)
    if carts:
        print('Ordered Details')
        for cart in carts:
            print('-'*85)
            print('|{:^83}|'.format('Date : '+str(cart[0])))
            print('-'*85)
            print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format('Food Name', 'Food Quantity', 'Ordered Quantity', 'Food Price'))
            print('-'*85)
            foodName = cart[1].split(',')
            foodQuantity = cart[2].split(',')
            orderQuantity = cart[3].split(',')
            price = cart[4].split(',')
            for (n, q, o, p) in zip(foodName, foodQuantity, orderQuantity, price):
                print('|{:^20}|{:^20}|{:^20}|{:^20}|'.format(n, q, o, p))
                print('-'*85)
            print('|{:^20}|{:^20} {:^20}|{:^20}|'.format('Total Bill','' , '', cart[5]))
            print('-'*85)
            print()
    else:
        print('Records not founds !')


if __name__ == "__main__":
    admin()
    login()
    register()
    view_profile()
    update_profile()
    delete_profile()
    show_customers()
    show_foods()
    create_food()
    food_update()
    food_delete()
    show_orders()
    create_order()
    show_cart()