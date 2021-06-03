class Employee:
    employees = []

    def __init__(self, name, surname, email, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = int(salary)

        Employee.employees.append(self)

    def get_annual_salary(self):
        print("{} {} annual salary is {}".format(self.name, self.surname, self.salary * 12))

    def show_employee_information(self):
        print("Pracownik: {} {}".format(self.name, self.surname))
        print("Adres email: {}".format(self.email))
        print("Wynagrodzenie miesięczne: {}".format(self.salary))


anna = Employee("Anna", "Bittermann", "ania@wp.pl", 2500)
edward = Employee("Edward", "Warzywniak", "edek@onet.pl", 3500)
marcin = Employee("Marcin", "Andraszkiewicz", "marcin@gmail.com", 4200)

employees_number = len(Employee.employees)

anna.show_employee_information()
marcin.show_employee_information()
edward.get_annual_salary()


print(Employee.employees)
print("Liczba pracowników wynosi {}.".format(str(employees_number)))
