from abc import ABC, abstractmethod


class Department:
    def __init__(self, name, code):
        self.name = name
        self.code = code


class Employee(ABC):
    def __init__(self, code, name, salary):
        self.code = code
        self.name = name
        self.salary = salary
        self.working_hours = 8

    def get_hours(self):
        return self.working_hours

    @abstractmethod
    def calc_bonus(self):
        pass


class Manager(Employee):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('managers', 1)

    def calc_bonus(self):
        return self.salary * 0.15

    def get_department(self):
        return self._departament.name

    def set_department(self):
        return self._departament.name


class Seller(Manager):
    def __init__(self, code, name, salary):
        super().__init__(code, name, salary)
        self._departament = Department('sellers', 2)
        self._sales = 0

    def calc_bonus(self):
        return self._sales * 0.15

    def get_sales(self):
        return self._sales

    def put_sales(self, value):
        self._sales += value

    def get_department(self):
        return self._departament.name

    def set_department(self):
        return self._departament.name
