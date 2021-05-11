from abc import ABC, abstractmethod

class EmployeeDAO(ABC):

    @abstractmethod
    def employee_authentication(self, employee):
        # authorization.html will request employee object for employee.name && employee.title
        pass




    @abstractmethod
    def get_employee_by_id(self, employee_id):
        # authorization.html will request employee object for employee.name && employee.title
        pass



















    # @abstractmethod
    # def employee_available_amount_override(self, employee):
    #     # the Benefits coop can changes this value higher than $1000.00
    #     pass

