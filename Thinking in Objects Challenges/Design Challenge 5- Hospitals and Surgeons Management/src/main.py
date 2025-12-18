from patient import Patient
from ward import Ward
from operation import Operation
from senior_surgeon import SeniorSurgeon
from non_senior_surgeon import NonSeniorSurgeon
from hospital_service import HospitalService

# Patients
p1 = Patient(1, "John")
p2 = Patient(2, "Mary")

# Ward
ward1 = Ward(101)
ward1.admit_patient(p1)
ward1.admit_patient(p2)

# Surgeons
s1 = SeniorSurgeon(1, "Dr. Smith")
s2 = NonSeniorSurgeon(2, "Dr. Brown")

# Operations
op1 = Operation(1, p1)
op2 = Operation(2, p2)

s1.add_operation(op1)
s2.add_operation(op2)

surgeons = [s1, s2]

print("Total Patients Operated:",
      HospitalService.total_patients_operated(surgeons))

print("Patients operated by Dr. Smith:",
      [p.name for p in HospitalService.patients_by_surgeon(s1)])

print("Patients in Ward 101:",
      [p.name for p in HospitalService.patients_in_ward(ward1)])
