class HospitalService:

    # 1. Total number of patients being operated
    @staticmethod
    def total_patients_operated(surgeons):
        count = 0
        for surgeon in surgeons:
            count += len(surgeon.operations)
        return count

    # 2. List all patients being operated by a surgeon
    @staticmethod
    def patients_by_surgeon(surgeon):
        return [op.patient for op in surgeon.operations]

    # 3. List all patients admitted to a ward
    @staticmethod
    def patients_in_ward(ward):
        return ward.patients
