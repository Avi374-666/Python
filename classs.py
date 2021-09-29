class Employee:
    def __init__(self, id, name, sal, dept, age):
        self.id = id
        self.name = name
        self.sal = sal
        self.dept = dept
        self.age = age

    def details(self):
        print("Employee Name:", self.id)
        print("Employee Age:", self.name)
        print("Employee Name:", self.sal)
        print("Employee Age:", self.dept)
        print("Employee Age:", self.age)


emp = Employee(1111, "Avi", 2000, "DP", 20)
emp.details()


class Timesheet:
    def __init__(self, date, no_of_hrs, activity, desc, stats):
        self.date = date
        self.no_of_hrs = no_of_hrs
        self.activity = activity
        self.desc = desc
        self.stats = stats

    def Details(self):
        print("Timesheet Date:", self.date)
        print("Timesheet HRS:", self.no_of_hrs)
        print("Timesheet Activity:", self.activity)
        print("Timesheet Description:", self.desc)
        print("Timesheet Stats:", self.stats)


time = Timesheet("29/09/21", 8, "Python", "Training", "Ongoing")
time.Details()
