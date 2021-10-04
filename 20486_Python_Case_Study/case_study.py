class Patient:
    def __init__(self, patient_id, patient_name, address, sex):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.address = address
        self.sex = sex

    def pat_dtails(self):
        print("Patient id:", self.patient_id)
        print("Patient name:", self.patient_name)
        print("Patient Gender:", self.sex)
        print("Patient address:", self.address)


class Appointment:
    def __init__(self, reqid, adate, slot, problem, description):
        self.reqid = reqid
        self.adate = adate
        self.slot = slot
        self.problem = problem
        self.description = description

    def appoint(self):
        print("Id:", self.reqid)
        print("date:", self.adate)
        print("No of Hours:", self.slot)
        print("problem:", self.problem)
        print("description:", self.description)


class Doctor:
    def __init__(self, doc_id, doctor_name, specialization, d_schedule):
        self.doc_id = doc_id
        self.doctor_name = doctor_name
        self.specialization = specialization
        self.d_schedule = d_schedule

    def d_display(self):
        print("doctor name: ", self.doctor_name)
        print("specialization:", self.specialization)
        print("schedule :", self.d_schedule)


class Prescription:
    def __init__(self, name, type, dosage, usage,):
        self.name = name
        self.type = type
        self.dosage = dosage
        self.usage = usage


class Review:
    def __init__(self, Doctor_name, Rating, Experience, Review_description,):
        self.Doctor_name = Doctor_name
        self.Rating = Rating
        self.Experience = Experience
        self.Review_description = Review_description
