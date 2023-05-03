import os.path

class Patient:
    def __init__(self, name, age, gender, diagnosis, medications):
        self.name = name
        self.age = age
        self.gender = gender
        self.diagnosis = diagnosis
        self.medications = medications

def add_patient(patient):
    filename = "patient_records.txt"
    with open(filename, 'a') as f:
        f.write(f"{patient.name},{patient.age},{patient.gender},{patient.diagnosis},{patient.medications}\n")

def search_patient(name):
    filename = "patient_records.txt"
    if not os.path.exists(filename):
        return "No patient records found"
    with open(filename, 'r') as f:
        for line in f:
            patient_info = line.strip().split(",")
            if patient_info[0] == name:
                return Patient(*patient_info)
    return "Patient not found"

def update_patient(patient):
    filename = "patient_records.txt"
    if not os.path.exists(filename):
        return "No patient records found"
    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            patient_info = line.strip().split(",")
            if patient_info[0] == patient.name:
                line = f"{patient.name},{patient.age},{patient.gender},{patient.diagnosis},{patient.medications}\n"
            f.write(line)

# Example usage:
patient1 = Patient("John Doe", 35, "Male", "Flu", "Ibuprofen")
patient2 = Patient("Jane Smith", 42, "Female", "Broken Leg", "Codeine")

add_patient(patient1)
add_patient(patient2)

print(search_patient("John Doe").diagnosis)
print(search_patient("Jane Smith").medications)

patient1.medications = "Paracetamol"
update_patient(patient1)

print(search_patient("John Doe").medications)
