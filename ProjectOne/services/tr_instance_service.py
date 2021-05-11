from dao.tr_instance_dao_impl import TRInstanceDAOImpl


class TRInstanceService:
    tr_instance_dao = TRInstanceDAOImpl()

    @classmethod
    def create_tr_instance(cls, tr_instance):
        return cls.tr_instance_dao.create_tr_instance(tr_instance)

    @classmethod
    def create_grading_type(cls, grading_type):
        return cls.tr_instance_dao.create_grading_type(grading_type)

    @classmethod
    def setup_process_for_tr(cls, employee):
        return cls.tr_instance_dao.setup_process_for_tr(employee)














