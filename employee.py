class Employee:
    def __init__(self, name, gross_income, employment_type, organization_type, deductions):
        # Employee's personal details
        self.name = name  # Name of the employee
        self.gross_income = gross_income # Annual income of the employee
        # Employee's organizational details
        self.employment_type = employment_type  # Type of employment (eg: regular or contract)
        self.organization_type = organization_type  # Type of organization (eg: Government, private or corporate)
        self.deductions = deductions
        # Tax-related variables (to be calculated later)
        self.tax_rate = 0        # Tax rate applicable to the employee (initially set to 0)
        self.taxable_income = 0  # Taxable income of the employee (initially set to 0)
        self.tax_payable = 0     # Tax amount payable by the employee (initially set to 0)
    
    def calculate_tax(self):
        # Initialize the deductions variables to store the total deductions
        deductions = 0
        taxable_income = self.gross_income - self.deductions
        if self.employment_type == "Regular":
            deductions += self.gross_income * 0.11  # PF(11%) deduction

        if self.organization_type == "Government" and self.employment_type == "Contract":
            deductions += self.income * 0.03  # GIS(3%) deduction

        elif self.organization_type != "Government":
            if self.employment_type != "Contract":
                deductions = 0
                deductions += self.gross_income * 0.11 # PF(11%) deduction

        taxable_income = self.gross_income - deductions
        if taxable_income <= 300000:
            self.tax_rate = 0
        elif taxable_income <= 400000:
            self.tax_rate = 0.1
        elif taxable_income <= 650000:
            self.tax_rate = 0.15
        elif taxable_income <= 1000000:
            self.tax_rate = 0.2
        elif taxable_income <= 1500000:
            self.tax_rate = 0.25
        else:
            self.tax_rate = 0.3


        self.taxable_income = taxable_income
        self.tax_payable = taxable_income * self.tax_rate

        if self.tax_payable >= 1000000:
            self.tax_payable += self.tax_payable * 0.1 #10% surcharge

    def display__tax__details(self):
        print(f"Name: {self.name}")
        print(f"Gross_Income : Nu. {self.gross_income}")
        print(f"Employment_Type: {self.employment_type}")
        print(f"Organization_Type: {self.organization_type}")
        print(f"deductions: {self.deductions}")
        print(f"Taxable Income: Nu. {self.taxable_income}")
        print(f"Tax Rate: {self.tax_rate * 100:.2f}%")
        print(f"Tax Payable: Nu. {self.tax_payable:.2f}")


# Example usage
try:
    name = input("Enter employee's name: ")
    gross_income = float(input("Enter employee's gross_income: "))
    employment_type = input("Enter employee's employment type(Regular/Contract):").capitalize() # Capitalize input
    organization_type = input("Enter employee's organization type(Government/Private/Corporate):").capitalize() #Capitalize input
    deductions = float(input("Enter the employee's deductions: "))

    employee = Employee(name, gross_income, employment_type, organization_type, deductions)
    employee.calculate_tax()
    employee.display__tax__details()

    class Manager(Employee):
      def __init__(self, name, gross_income, employment_type, organization_type, deductions):
        self.name = name  
        self.gross_income = gross_income 
        self.employment_type = employment_type  
        self.organization_type = organization_type  
        self.deductions = deductions

    def calculate_tax(self):
        # calculate tax based on self.gross_income, self.organization_type, and self.deductions
        manager.calculate_tax()

    class Consultant(Employee):
      def __init__(self, name, gross_income, employment_type, organization_type, deductions):
        self.name = name
        self.gross_income = gross_income
        self.employment_type = employment_type
        self.organization_type = organization_type
        self.deductions = deductions

      def calculate_tax(self):
        # calculate tax based on self.gross_income, self.employment_type, self.organization_type, and self.deductions
        consultant.calculate_tax()

    class Investor(Employee):
      def __init__(self, name, gross_income, employment_type, organization_type, deductions):
        self.name = name
        self.gross_income = gross_income
        self.employment_type = employment_type
        self.organization_type = organization_type
        self.deductions = deductions

      def calculate_tax(self):
        # calculate tax based on self.gross_income, self.employment_type, self.organization_type, and self.deductions
        consultant.calculate_tax()

    class Landlord(Employee):
      def __init__(self, name, gross_income, employment_type, organization_type, deductions):
        self.name = name
        self.gross_income = gross_income
        self.employment_type = employment_type
        self.organization_type = organization_type
        self.deductions = deductions

      def calculate_tax(self):
        # calculate tax based on self.gross_income, self.employment_type, self.organization_type, and self.deductions
        consultant.calculate_tax()

 # some code that might raise a ValueError
except ValueError:
    print("An error occurred: invalid value.")


employee = Employee("Pema", 500000, "Regular", "Government", 0)
manager = Manager("Dawa", 800000, "Contract", "Private", 2000)
consultant = Consultant("Jamyang Pelzin", 700000, "Contract", "Corporate", 40000)
investor = Investor("Maya Gurung", 1000000, "Regular", "Private", 5000)
landlord = Landlord("Vishal Tamang", 900000, "Regular", "Government", 7000)

if employee is not None:
    if employee.name is not None and hasattr(employee, 'calculate_tax') and callable(employee.calculate_tax) and employee.calculate_tax() is not None:
        print(f"{employee.name}'s total tax payable: Nu. {employee.calculate_tax():.2f}")
    else:
        print("Error: Either employee name or calculate_tax method is None")
else:
    print("Error: employee object is None")








