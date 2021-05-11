

class EducationType:

    def __init__(self, education_type_id=0, type_name="", percent=0):
        self.education_type_id = education_type_id
        self.type_name = type_name
        self.percent = percent

    def json(self):
        return {
            'educationTypeId': self.education_type_id,
            'typeName': self.type_name,
            'percent': self.percent
        }

    @staticmethod
    def json_parse(json):
        education_type = EducationType()
        education_type.education_type_id = json['educationTypeId'] if "educationTypeId" in json else 0
        education_type.type_name = json['typeName'] if "typeName" in json else ""
        education_type.percent = json['percent'] if "percent" in json else 0
        return education_type

    def __repr__(self):
        return str(self.json())

