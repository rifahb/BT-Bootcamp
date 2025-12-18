class Ward:
    def __init__(self, ward_number):
        self.ward_number = ward_number
        self.patients = []

    def admit_patient(self, patient):
        self.patients.append(patient)
