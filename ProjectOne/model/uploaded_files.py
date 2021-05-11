class UploadedFiles:

    def __init__(self, uploaded_files_id=0, file_type="", file_name="", binary_data="", tr_instance_id=0):
        self.uploaded_files_id = uploaded_files_id
        self.file_type = file_type
        self.file_name = file_name
        self.binary_data = binary_data
        self.tr_instance_id = tr_instance_id

    def json(self):
        return {
            'uploadedFilesId': self.uploaded_files_id,
            'fileType': self.file_type,
            'fileName': self.file_name,
            'binaryData': self.binary_data,
            'trInstanceId': self.tr_instance_id
        }

    @staticmethod
    def json_parse(json):
        uploaded_file = UploadedFiles()
        uploaded_file.uploaded_files_id = json['uploadedFilesId'] if "uploadedFilesId" in json else 0
        uploaded_file.file_type = json['fileType']  if "fileType" in json else ""
        uploaded_file.file_name = json['fileName'] if "fileName" in json else ""
        uploaded_file.binary_data = json['binaryData'] if "binaryData" in json else 0
        uploaded_file.tr_instance_id = json['trInstanceId'] if "trInstanceId" in json else 0
        return uploaded_file

    def __repr__(self):
        return str(self.json())
