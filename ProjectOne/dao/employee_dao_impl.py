from dao.employee_dao import EmployeeDAO
from exceptions.resource_not_found import ResourceNotFound
from model.employee import Employee
from util.db_connection import connection


class EmployeeDAOImpl(EmployeeDAO):

    def employee_authentication(self, employee):
        sql = "SELECT * FROM employee where employee_name = %s AND title = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (employee.name, employee.title))
        record = cursor.fetchone()
        cursor.close()

        if record:
            return Employee(record[0], record[1], record[2], record[3], float(record[4]), record[5])
        else:
            raise ResourceNotFound(f"Employee record could not be verified with input data.")




    def get_employee_by_id(self, employee_id):
        sql = "SELECT * FROM employee where id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        record = cursor.fetchone()
        cursor.close()

        if record:
            return Employee(record[0], record[1], record[2], record[3], float(record[4]), record[5])
        else:
            raise ResourceNotFound(f"Employee record could not be verified with input data.")




