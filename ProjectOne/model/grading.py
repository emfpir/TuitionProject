

class Grading:

    def __init__(self, grading_id=0, status="", grade_final=None, verification_person=0, tr_instance_id=0):
        self.grading_id = grading_id
        self.status = status
        self.grade_final = grade_final
        self.verification_person = verification_person
        self.tr_instance_id = tr_instance_id

    def json(self):
        return {
            'gradingId': self.grading_id,
            'status': self.status,
            'gradeFinal': self.grade_final,
            'verificationPerson': self.verification_person,
            'trInstanceId': self.tr_instance_id
        }

    @staticmethod
    def parse_json(json):
        grading = Grading()
        grading.grading_id = json['gradingId'] if "gradingId" in json else 0
        grading.status = json['status']  if "status" in json else ""
        grading.grade_final = json['gradeFinal'] if "gradeFinal" in json else 0
        grading.verification_person = json['verificationPerson'] if "verificationPerson" in json else 0
        grading.tr_instance_id = json['trInstanceId'] if "trInstanceId" in json else 0
        return grading

    def __repr__(self):
        str(self.json())