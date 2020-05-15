class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first.lower(),self.last.lower())
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')

class Developer(Employee):
    pass

emp1=Employee('Siraj', 'Deen', 50000)
print (emp1.fullname)
print (emp1.email)
emp1.fullname = "Suresh Deen"

print (emp1.fullname)
print (emp1.email)

print (issubclass(Employee, Developer))