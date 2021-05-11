from exceptions.resource_not_found import ResourceNotFound
from services.tr_instance_service import TRInstanceService
from services.employee_service import EmployeeService


class MethodController:

    def createRT_create_grading_type(grading_type):
        try:
            grading_type = TRInstanceService.create_grading_type(grading_type)
            return grading_type
        except ResourceNotFound as r:
            return r.message, 400

    def createRT_get_employee_by_id(tr_instance):
        try:
            employee = EmployeeService.get_employee_by_id(tr_instance.employee_id)
            return employee
        except ResourceNotFound as r:
            return r.message, 400

    def createRT_create_tr_instance(tr_instance):
        try:
            grading_type = TRInstanceService.create_tr_instance(tr_instance)
            return grading_type
        except ResourceNotFound as r:
            return r.message, 400

    def createRT_setup_process_for_tr(employee):
        try:
            process = TRInstanceService.setup_process_for_tr(employee)
            return process
        except ResourceNotFound as r:
            return r.message, 400

    def createRT_create_grading(process):
        try:
            grading = TRInstanceService.create_grading_type(process)
            return grading
        except ResourceNotFound as r:
            return r.message, 400















