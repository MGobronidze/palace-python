class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_info(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def show_info(self):
        return f"{super().show_info()}, Department: {self.department}"

class Engineer(Employee):
    def __init__(self, name, salary, field):
        super().__init__(name, salary)
        self.field = field

    def show_info(self):
        return f"{super().show_info()}, Field: {self.field}"

class TechLead(Manager, Engineer):
    def __init__(self, name, salary, department, field, project):
        Employee.__init__(self, name, salary)  # თავიდან Employee-ის კონსტრუქტორს ვიძახებთ
        self.department = department
        self.field = field
        self.project = project

    def show_info(self):
        return f"{super().show_info()}, Project: {self.project}, Field: {self.field}"

tech_lead = TechLead("Anna", 90000, "IT", "Software Engineering", "AI System")
print(tech_lead.show_info())
