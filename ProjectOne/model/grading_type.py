

class GradingType:

    def __init__(self, grading_type_id=0, graded=True, score=0, tr_instance_id=0):
        self.grading_type_id = grading_type_id
        self.graded = graded
        self.score = score
        self.tr_instance_id = tr_instance_id

    def json(self):
        return {
            'gradingTypeId': self.grading_type_id,
            'graded': self.graded,
            'score': self.score,
            'trInstanceId': self.tr_instance_id
        }

    @staticmethod
    def json_parse(json):
        grading_type = GradingType()
        grading_type.grading_type_id = json['gradingTypeId'] if "gradingTypeId" in json else 0
        grading_type.graded = json['graded'] if "graded" in json else True
        grading_type.score = json['score'] if "score" in json else 0
        grading_type.tr_instance_id = json['trInstanceId'] if "trInstanceId" in json else 0
        return grading_type

    def __repr__(self):
        str(self.json())
