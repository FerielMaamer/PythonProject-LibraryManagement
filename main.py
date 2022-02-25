import functions

# variables
employee_list=[]
employees = []
employees_discount=[]
item_list=[]
menu_item=0
exit_app = False
#menu
while menu_item != 5 and not exit_app:
    menu_item = int(functions.display_menu())
    if menu_item == 1:
        other_user = True
        while other_user:
            employee_data, employees, employees_discount = functions.employee_info(employees, employees_discount)
            employee_list.append(employee_data)
            new_user = input("anther employee?")
            if new_user.lower() == "no":
                other_user = False
                display_menu = input("Go to menu?")
                if display_menu.lower() == "yes":
                    continue
                else:
                    exit_app = True
                    break
    elif menu_item == 2:
        other_item = True
        while other_item:
            item_data= functions.item_info(item_list)
            item_list.append(item_data)
            new_item = input("another item?")
            if new_item.lower() == "no":
                other_item = False
                display_menu = input("Go to menu?")
                if display_menu.lower() == "yes":
                    continue
                else:
                    exit_app = True
                    break
    elif menu_item == 3:
        other_purchase = True
        while other_purchase:
            print("Item Number  |Item Name    |Item Cost  \n")
            for item in item_list:
                print(str(item[0])+"      |"+str(item[1])+"      |"+str(item[2])+"    \n")
            employee_list = functions.make_purchase(employee_list, employees_discount, item_list)
            new_purchase = input("another purchase?")
            if new_purchase.lower() == "no":
                other_purchase = False
                display_menu = input("Go to menu?")
                if display_menu.lower() == "yes":
                    continue
                else:
                    exit_app = True
                    break
    elif menu_item == 4:
        print("Employee ID, Employee Name, Employee Type, Years Worked, Total Purchased,"
              " Total Discounts, Employee Discount Number\n")
        for employee in employee_list:
            string = ' ,'.join(map(str, employee))
            print(string)
        display_menu = input("Go to menu?")
        if display_menu.lower() == "yes":
            continue
        else:
            exit_app = True
            break
