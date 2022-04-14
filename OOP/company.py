class Company:
    def __init__(self, department_name, company_name = "Health-X"):
        self.company_name = company_name
        self.department_name = department_name

class Department(Company):
    def __init__(self):
        super().__init__(self)
    # def number_of_employees(self):
    #     ...

surgery = Department()
surgery.department_name = "Surgery"
surgery.number_of_employees = 50
print(surgery.company_name + " " + "\nDepartment Name:",surgery.department_name + "\n" +"Number of Employees:", surgery.number_of_employees)