
class Employee:

    def __init__(self, employee_id=0, name="", direct_supervisor=0, department_head=0, available_reimbursement=1000, title=""):
        self.employee_id = employee_id
        self.name = name
        self.direct_supervisor = direct_supervisor
        self.department_head = department_head
        self.available_reimbursement = available_reimbursement
        self.title = title

    def json(self):
        return {
            'employeeId': self.employee_id,
            'name': self.name,
            'directSupervisor': self.direct_supervisor,
            'departmentHead': self.department_head,
            'availableReimbursement': self.available_reimbursement,
            'title': self.title
        }

    @staticmethod
    def json_parse(json):
        employee = Employee()
        employee.employee_id = json['employeeId'] if "employeeId" in json else 0
        employee.name = json['name'] if "name" in json else ""
        employee.direct_supervisor = json['directSupervisor'] if "directSupervisor" in json else 0
        employee.department_head = json['departmentHead'] if "departmentHead" in json else 0
        employee.available_reimbursement = json['availableReimbursement'] if "availableReimbursement" in json else 0
        employee.title = json['title'] if "title" in json else ""
        return employee

    def __repr__(self):
        return str(self.json())










