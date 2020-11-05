import template
import datetime


def welcome():
    print('='*30)
    print('-: Welcome To FoodPlaza :-')
    print('{:^26}'.format(datetime.date.today().strftime('%d %B %Y')))


#main menu
def main():
    while True:
        print('='*30)
        print('Select - \n1. User Login\n2. Admin Login\n3. Register\n4. Exit')
        print('='*30)
        try:
            choice = int(input('Enter your choice : '))
            print('='*30)
            if choice == 1:
                template.login()
            if choice == 2:
                template.admin()
            elif choice == 3:
                template.register()
                template.login()
            elif choice == 4:
                print('Have a nice day !! Bye.. Bye..')
                print()
                exit()
            else:
                print('Wrong choice..')
        except ValueError:
            print('Enter proper choice..')


#Menu For Customer
def menu():
    while True:
        print('='*30)
        print('Select - \n1. Edit Profile\n2. Place Order\n3. View Cart\n4. Sign Out')
        print('='*30)
        try:
            choice = int(input('Enter your choice : '))
            print('='*30)
            if choice == 1:
                profile()
            elif choice == 2:
                template.create_order()
            elif choice == 3:
                template.show_cart()
            elif choice == 4:
                main()
            else:
                print('Wrong choice..')
                print('='*30)
        except ValueError:
            print('Enter proper choice..')


#User Profile Menu
def profile():
    while True:
        print('='*30)
        print('Select - \n1. View Profile\n2. Update Profile\n3. Delete Profile\n4. Main Menu\n5. Sign Out')
        print('='*30)
        try:
            choice = int(input('Enter your choice : '))
            print('='*30)
            if choice == 1:
                template.view_profile()
            elif choice == 2:
                template.update_profile()
            elif choice == 3:
                template.delete_profile()
            elif choice == 4:
                menu()
            elif choice == 5:
                main()
            else:
                print('Wrong choice..')
                print('='*30)
        except ValueError:
            print('Enter proper choice..')


#Menu For Admin
def admin_menu():
    while True:
        print('='*30)
        print('Select -  \n1. View Customers\n2. View Foods\n3. Add Food\n4. Update Food\n5. Delete Food\n6. View Orders\n7. Sign Out')
        print('='*30)
        try:
            choice = int(input('Enter your choice : '))
            print('='*30)
            if choice == 1:
                template.show_customers()
            elif choice == 2:
                template.show_foods()
            elif choice == 3:
                template.create_food()
            elif choice == 4:
                template.food_update()
            elif choice == 5:
                template.food_delete()
            elif choice == 6:
                template.show_orders()
            elif choice == 7:
                main()
            else:
                print('Wrong choice..')
                print('='*30)
        except ValueError:
            print('Enter proper choice..')


if __name__ == '__main__':
    welcome()
    main()
