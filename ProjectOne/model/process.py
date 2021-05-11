from datetime import date, datetime


class Process:

    def __init__(self, process_id=0, process_name=0, step="", begin_date=date.today(), completed=False, tr_instance_id=0):
        self.process_id = process_id
        self.process_name = process_name
        self.step = step
        self.begin_date = begin_date
        self.completed = completed
        self.tr_instance_id = tr_instance_id

    def json(self):
        return {
            'processId': self.process_id,
            'processName': self.process_name,
            'step': self.step,
            'beginDate': self.begin_date,
            'completed': self.completed,
            'trInstanceId': self.tr_instance_id
        }

    @staticmethod
    def json_parse(json):
        process = Process()
        process.process_id = json['processId'] if "processId" in json else 0
        process.process_name = json['processName'] if "processName" in json else ""
        process.step = json['step'] if "step" in json else 0
        process.begin_date = json['beginDate'] if "beginDate" in json else datetime.today()
        process.completed = json['completed'] if "completed" in json else False
        process.tr_instance_id = json['trInstanceId'] if "trInstanceId" in json else 0
        return process

    def __repr__(self):
        str(self.json())

# process management will move in steps. The process for management approval can take up
# to 14 steps and depending on your title there can be less steps. Each manager's approval
# only has five day to make a decision expect the BC.
#supervisor steps: 1.pending, 2.additional info, 3.pending2, 4.approve/deny it could end here
#department head steps: 5. pending, 6.additional info, 7.pending2 8.aprove/deny
#BC steps: 9. pending, 10. additional info, 11.pending2, 12.ReducedAmount (if employee accepts
#   reduced amount the process is over with an approval), 13.Approval/Deny
# any management denial the manager should upload a documented reason .