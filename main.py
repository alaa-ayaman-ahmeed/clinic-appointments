
class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)


class Doctor:
    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty
        self.appointments = []

    def view_appointments(self):
        return [str(app) for app in self.appointments]


class Appointment:
    def __init__(self, appointment_id, patient, doctor, date_time):
        self.appointment_id = appointment_id
        self.patient = patient
        self.doctor = doctor
        self.date_time = date_time
        self.status = "Confirmed"

    def __str__(self):
        return f"Appointment {self.appointment_id}: Dr. {self.doctor.name} with {self.patient.name} at {self.date_time} [{self.status}]"


class ClinicSystem:
    def __init__(self, max_limit=5):
        self.max_limit = max_limit
        self.all_appointments = []

    def book_appointment(self, app_id, patient, doctor, date_time):
        active_count = len([
            a for a in patient.appointments
            if a.status == "Confirmed"
        ])

        if active_count >= self.max_limit:
            print(
                f"Booking Failed for {patient.name}: "
                f"Maximum limit of {self.max_limit} active appointments reached."
            )
            return None

        new_app = Appointment(app_id, patient, doctor, date_time)

        patient.add_appointment(new_app)
        doctor.appointments.append(new_app)
        self.all_appointments.append(new_app)

        print(f"Booking Successful: {new_app}")
        return new_app


if __name__ == "__main__":
    print("--- Running Clinic Appointments Simulation (N = 5) ---")

    system = ClinicSystem(max_limit=5)

    patient = Patient(1, "Ahmed Ali")
    doctor = Doctor(101, "Mona", "Cardiology")

    # Book 5 appointments
    for i in range(1, 6):
        system.book_appointment(
            i,
            patient,
            doctor,
            f"2026-11-0{i} 10:00 AM"
        )

    # Attempt to book the 6th appointment
    print("\nAttempting 6th appointment (exceeding limit):")

    system.book_appointment(
        6,
        patient,
        doctor,
        "2026-11-06 10:00 AM"
    )

    # Display patient appointments
    print("\nPatient Active Appointments:")

    for app in patient.appointments:
        print(app)
