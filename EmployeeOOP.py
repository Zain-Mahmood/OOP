class Employees:
    def __init__(self, f_name, l_name, b_year, b_month, b_day, position, uni):
        self.f_name = f_name
        self.l_name = l_name
        self.b_year = b_year
        self.b_month = b_month
        self.b_day = b_day
        self.postion = position
        self.uni = uni
        
    def print_name(self):
        print(self.first_name)
        
# employee_list = []
# for index in range(4):
#     employee_first_name = input("Please enter the employee name")
#     employee = Employees(employee_first_name)
    
#     print(employee)
#     employee.print_name()
#     employee_list.append(employee)
#     print("****************")



# s1 = Employees("Zain","Mahmood", 1997, 8, 17, "Devops", True)
# print(s1.uni)
# print(s1)






# Employees(f_name, l_name, b_year, b_month, b_day, position, uni)
print("\n")
print("What would you like to do?")
print("\n")
print("1. Add employees")
print("2. Remove employees")
print("3. Get total number of employees")
print("4. retrieve data on employee")
print("5. modify existing employee information")
print("6. Exit")


while True:
    choice = int(input("Enter number choice From operations list above"))
    if choice in (1,2,3,4,5,6):
        if choice == 1:
            z = input("number of new employees you would like to add ")
            for i in range(int(z)):
                employee_info = []

                employee_id = input("Please enter your employee ID")
                a = 
                b = read_lastname()
                c = birth_year()
                d = birth_month()
                e = birth_day()
                f = position()
                g = uni()
                print(employee_info)
                employee_dict[employee_id] = employee_info 
                print(employee_dict)











