from abc import ABC, abstractmethod

class TRInstanceDAO(ABC):

    @abstractmethod
    def create_tr_instance(self, tr_instance):
        pass


    @abstractmethod
    def create_grading_type(self, grading_type):
        pass



    @abstractmethod
    def setup_process_for_tr(self, employee):
        pass

    @abstractmethod
    def create_grading(self, process):
        pass




