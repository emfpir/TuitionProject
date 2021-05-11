from datetime import date, timedelta
from exceptions.resource_not_found import ResourceNotFound
from model.grading import Grading
from model.grading_type import GradingType
from model.process import Process
from util.db_connection import connection
from dao.tr_instance_dao import TRInstanceDAO

class TRInstanceDAOImpl(TRInstanceDAO):

    def create_tr_instance(self, tr_instance):
        grading_type = GradingType.json_parse(tr_instance.education_type_id)
        tr_instance.education_type_id = grading_type.tr_instance_id
        sql = "INSERT INTO  tr_instance (date_current, training_location, description,full_cost, work_justification, start_date," \
              " days_long, education_type_id, employee_id) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s) returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (tr_instance.date_current, tr_instance.training_location, tr_instance.description,
                             tr_instance.full_cost, tr_instance.work_justification, tr_instance.start_date,
                             tr_instance.days_long, tr_instance.education_type_id, tr_instance.employee_id))
        connection.commit()
        record = cursor.fetchone()
        cursor.close()
        if record:
            grading_type.tr_instance_id = record[0]
            return grading_type
        else:
            raise ResourceNotFound(f"The tr instance data was not formatted for the database.")

    def create_grading_type(self, grading_type):
        sql = "INSERT INTO  grading_type (graded, score, tr_instance_id) VALUES (%s,%s,%s) returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (grading_type.graded, grading_type.score, grading_type.tr_instance_id))
        connection.commit()
        record = cursor.fetchone()
        cursor.close()
        if record:
            return GradingType(record[0], record[1], record[2], record[3])
        else:
            raise ResourceNotFound(f"The grading data was not formatted for the database.")

    def setup_process_for_tr(self, employee):
        if employee.direct_supervisor == 0:
            if employee.department_head == 0:
                step = 9
            else:
                step = 5
        else:
            step = 1
        end_date = date.today() + timedelta(days=5)
        process_item = Process(0, "pending", step, str(end_date), str(False), employee.employee_id)
        sql = "INSERT INTO  process (process_name, step, begin_date, completed, tr_instance_id) " \
              "VALUES (%s,%s,%s,%s,%s) returning *"
        cursor = connection.cursor()
        cursor.execute(sql, (process_item.process_name, process_item.step, process_item.begin_date, process_item.completed, process_item.tr_instance_id))
        connection.commit()
        record = cursor.fetchone()
        cursor.close()
        if record:
            return Process(record[0], record[1], record[2], record[3], record[4], record[5])
        else:
            raise ResourceNotFound(f"The grading data was not formatted for the database.")

#grading table status is open placeholder or set to complete string when final grade is submitted.
    #if stauts is complete check if process is complete and grade_final vs score in gradingtype table
    def create_grading(self, process):
        sql = "INSERT INTO grading (verification_person, tr_instance_id) VALUES RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (process.step, process.tr_instance_id))
        connection.commit()
        record = cursor.fetchone()
        cursor.close()
        if record:
            return Grading(record[0],record[1],record[2],record[3],record[4])
        else:
            raise ResourceNotFound(f"The database doesn't accept the input types entered")












