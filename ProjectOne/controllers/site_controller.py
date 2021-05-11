from flask import jsonify, request
from werkzeug.exceptions import abort
from exceptions.resource_not_found import ResourceNotFound
from model.employee import Employee
from model.grading_type import GradingType
from model.tr_instance import TRInstance
from services import tr_instance_service
from services.employee_service import EmployeeService
from controllers.method_controller import MethodController
from services.tr_instance_service import TRInstanceService


def route(app):
    @app.route("/authentication", methods=["POST"])
    def post_authentication_employee():
        try:
            print("here")
            employee = Employee.json_parse(request.json)
            print(f"name: {employee.name} title: {employee.title}")
            employee = EmployeeService.employee_authentication(employee)
            # before returning any data after an employee is verified
            # need to check if any pending process have taken too long
            # I decided each manager gets five day to approve or deny
            # if it is day five and the requester still needs to add info
            # The claim could be auto-rejected and if the manager requests
            # addition information on the fifth day I could add one day
            return jsonify(employee.json()), 202  # accepted
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/createRT", methods=["POST"])
    def post_tuition_reimbursement():
        try:
            tr_instance = TRInstance.json_parse(request.json)
            grading_type = MethodController.createRT_create_tr_instance(tr_instance)
            employee = MethodController.createRT_get_employee_by_id(tr_instance)
            grading_type_item = MethodController.createRT_create_grading_type(grading_type)
            employee.employee_id = grading_type_item.tr_instance_id
            process = MethodController.createRT_setup_process_for_tr(employee)
            MethodController.createRT_create_grading(process)
            return jsonify(tr_instance.json()), 202
        except ResourceNotFound as r:
            return r.message, 400  # bad request

    # def createRT_create_grading_type(grading_type):
    #     try:
    #         grading_type = tr_instance_service.create_grading_type(grading_type)
    #         return grading_type
    #     except ResourceNotFound as r:
    #         return r.message, 400
    #
    # def createRT_get_employee_by_id(tr_instance):
    #     try:
    #         employee = EmployeeService.get_employee_by_id(tr_instance.employee_id)
    #         return employee
    #     except ResourceNotFound as r:
    #         return r.message, 400
    #
    # def createRT_create_tr_instance(tr_instance):
    #     try:
    #         grading_type = tr_instance_service.create_tr_instance(tr_instance)
    #         return grading_type
    #     except ResourceNotFound as r:
    #         return r.message, 400

    # @app.route("/get", methods=["GET"])
    # def get_authentication_employee():
    #     print("here")
    #     return "worked", 202
