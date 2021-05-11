from datetime import date, datetime


class TRInstance:
#date.today() == 2021-01-01 yyyy-mm-dd
    def __init__(self, tr_instance_id=0, date_current=date.today(), training_location="", description="", full_cost=0, work_justification="", start_date=date.today(),
              days_long=0, education_type_id=0, employee_id=0):
        self.tr_instance_id = tr_instance_id
        self.date_current = date_current
        self.training_location = training_location
        self.description = description
        self.full_cost = full_cost
        self.work_justification = work_justification
        self.start_date = start_date
        self.days_long = days_long
        self.education_type_id = education_type_id
        self.employee_id = employee_id

    def json(self):
        return {
            'trInstanceId': self.tr_instance_id,
            'dateCurrent': self.date_current,
            'trainingLocation': self.training_location,
            'description': self.description,
            'fullCost': self.full_cost,
            'workJustification': self.work_justification,
            'startDate': self.start_date,
            'daysLong': self.days_long,
            'educationTypeId': self.education_type_id,
            'employeeId': self.employee_id
        }

    @staticmethod
    def json_parse(json):
        tr_instance = TRInstance()
        tr_instance.tr_instance_id = json['trInstanceId'] if "trInstanceId" in json else 0
        tr_instance.date_current = json['dateCurrent'] if "dateCurrent" in json else datetime.today()
        tr_instance.training_location = json['trainingLocation'] if 'trainingLocation' in json else ""
        tr_instance.description = json['description'] if 'description' in json else ""
        tr_instance.full_cost = json['fullCost'] if 'fullCost' in json else 0
        tr_instance.work_justification = json['workJustification'] if 'workJustification' in json else ""
        tr_instance.start_date = json['startDate'] if 'startDate' in json else datetime.today()
        tr_instance.days_long = json['daysLong'] if 'daysLong' in json else 0
        tr_instance.education_type_id = json['educationTypeId'] if "educationTypeId" in json else 0
        tr_instance.employee_id = json['employeeId'] if "employeeId" in json else 0
        return tr_instance

    def __repr__(self):
        return str(self.json())




