class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_employee(self):
        remainder = X % 3
        if remainder == 0:
            print("Nume:", self.name)
        elif remainder == 1:
            print("Salariu:", self.salary)
        elif remainder == 2:
            print("Departament:", self.department)

    def __del__(self):
        Employee.empCount -= 1

    def modify_task(self, task_name, status="New"):
        self.tasks[task_name] = status

    def display_task(self, status):
        print(f"Tasks with status {status}:")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)


class Manager(Employee):
    mgr_count = 0

    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = f"D14"
        Manager.mgr_count += 1

    def display_employee(self):
        remainder = X % 3
        if remainder == 0:
            print("Nume", self.name)
        elif remainder == 1:
            print("Salariu:", self.salary)
        elif remainder == 2:
            print("Departament:", self.department)


# Citirea valorilor X și Y de la tastatură
X = int(input("Introdu X: "))
Y = int(input("Introdu Y: "))
#Cazul meu : X = 5 ; Y = 15;
# X % 5 = 2 => afiseaza numai departmentul
# Y / 3 = 5 => afiseaza obiectele create de 5 ori 
managers = []
for i in range(Y // 3):
    managers.append(Manager(f"Manager{i}", 10000 + i * 1000, i + 1))

# Afisarea doar a departamentului pentru  X % 3 == 2
for manager in managers:
    if X % 3 == 2:
        manager.display_employee()

# Crearea unui obiect din clasa Employee
employee = Employee("Marin Valentin", 5000)

#X % 3 corespunde condițiilor atunci afiseaza:
if X % 3 == 0:
    employee.display_employee()
elif X % 3 == 1:
    print("Salariu:", employee.salary)


print(f"Nr. Angajati: {employee.empCount}")
print(f"Nr. Manageri: {Manager.mgr_count}")
