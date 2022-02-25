def display_menu():
    print("---------------------------------------")
    print("| 1- Create Employee                  |")
    print("| 2- Create Item                      |")
    print("| 3- Make Purchase                    |")
    print("| 4- All Employee Summary             |")
    print("| 5- Exit                             |")
    print("---------------------------------------\n")
    menu_item = input("choose from the menu")
    return menu_item


def employee_info(employees, employees_discount):
    employee_info = ["Employee ID", "Employee Name", "Employee Type", "Years Worked",
                     "Total Purchased", "Total Discounts", "Employee Discount Number"]
    employee_data = []
    index = 0
    while index < 7:
        info = employee_info[index]
        if index != 4 and index != 5:
            data = input("Enter the " + info + ': ')
            if index == 0:
                if data.isnumeric() and data not in employees:
                    employee_data.append(int(data))
                    employees.append(int(data))
                    index += 1
                else:
                    print("Employee ID not valid")
                    continue
            elif index == 1:
                if not data:
                    print("wrong name")
                    continue
                else:
                    employee_data.append(data)
                    index += 1
            elif index == 2:
                if data in ["hourly", "manager"]:
                    employee_data.append(data)
                    index += 1
                else:
                    print("wrong Employee Type")
                    continue
            elif index == 3:
                if data.isnumeric():
                    employee_data.append(int(data))
                    index += 1
                else:
                    print("invalid years worked")
                    continue
            elif index == 6:
                if data.isnumeric() and data not in employees_discount:
                    employee_data.append(int(data))
                    employees_discount.append(int(data))
                    index += 1
                else:
                    print("invalid employee discount")
                    continue
            else:
                continue
        else:
            employee_data.append(0)
            index += 1

    print(employee_data)
    return employee_data, employees, employees_discount


def item_info(item_list):
    item_info = ["Item Number", "Item Name", "Item Cost"]
    item_exists = False
    item_data = []
    index = 0
    while index < 3:
        info = item_info[index]
        data = input("Enter the " + info + ": ")
        if index == 0:
            if data.isnumeric():
                for j in item_list:
                    if str(j[0]) == data:
                        item_exists = True
                        continue
                if not item_exists:
                    print("item number right")
                    item_data.append(int(data))
                    index += 1
            else:
                print("invalid item number")
                continue
        elif index == 2:
            if data.isnumeric():
                item_data.append(int(data))
                index += 1
            else:
                print("invalid item cost")
                continue
        else:
            item_data.append(data)
            index += 1
    print(item_data)
    return item_data


def calculate_cost(employee_list, item_list, discount_num, item_num):
    for employee in employee_list:
        if employee[6] == int(discount_num):
            if employee[5] < 200:
                years_worked = int(employee[3])
                if employee[2].lower() == "manager":
                    new_discount = min(10, (2 * years_worked)) + 10
                else:
                    new_discount = min(10, (2 * years_worked)) + 2
                for item in item_list:
                    if item[0] == int(item_num):
                        discount = (item[2] * new_discount) / 100
                        if employee[5] + discount < 200 :
                            employee[5] += discount
                            employee[4] += item[2] - discount
                        else:
                            discount_left = 200 - employee[5]
                            employee[5] += discount_left
                            employee[4] += item[2] - discount_left
            else:
                print("you have reached the limit discount of 200$")
    return employee_list


def make_purchase(employee_list, employees_discount, item_list):
    item_exists = False
    discount_exists = False
    print(employees_discount)
    if not item_list or not employee_list:
        print("not enough data to purchase an item")
    else:
        while not item_exists and not discount_exists:
            discount_num = input("Enter your Employee discount number")
            if int(discount_num) not in employees_discount:
                print("Invalid Discount number")
            else:
                discount_exists = True
                while not item_exists:
                    item_num = input("Enter the Item number")
                    for j in item_list:
                        if j[0] == int(item_num):
                            item_exists = True
                            confirmation = input("Confirm purchase of "+j[1]+"?")
                            if confirmation.lower() == "yes" or confirmation.lower() == "y":
                                employee_list = calculate_cost(employee_list, item_list, discount_num, item_num)
                    if not item_exists:
                        print("Invalid item number")
    return employee_list
