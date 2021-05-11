from dao.employee_dao_impl import EmployeeDAOImpl


class EmployeeService:
    employee_dao = EmployeeDAOImpl()

    @classmethod
    def employee_authentication(cls, employee):
        return cls.employee_dao.employee_authentication(employee)

    @classmethod
    def get_employee_by_id(cls, employee_id):
        return cls.employee_dao.get_employee_by_id(employee_id)

