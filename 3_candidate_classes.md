# 3. Candidate Classes

## Purpose
This document identifies the candidate classes for the Clinic Appointments system based on the functional requirements and the current implementation in `main.py`.

## Candidate Classes

| Class Name | Decision | Evidence / Reason |
|---|---|---|
| Patient | Accepted | R1 requires patients to register and log in, and R3 and R4 require patients to book appointments and follow the active appointment limit. The current implementation stores the patient's ID, name, and appointments. |
| Doctor | Accepted | R2 requires displaying doctor schedules, and R5 requires doctors to view their daily appointments. The current implementation stores the doctor's ID, name, specialty, and appointments. |
| Appointment | Accepted | R3 requires booking appointments, and R6 requires updating appointment status. The current implementation represents an appointment with an ID, patient, doctor, date and time, and status. |
| ClinicSystem | Accepted | The system coordinates appointment booking and enforces the maximum number of active appointments specified in R4. The current implementation contains the `ClinicSystem` class. |
| Schedule | Inferred | R2 refers to available doctor schedules. This could become a separate class if schedule management requires more detail, but it is not implemented as a separate class in the current code. |
| TimeSlot | Inferred | R2 and R3 refer to available time slots and appointment booking. A separate class could represent individual slots and their availability, but it is not implemented in the current code. |
| UserAccount | Inferred | R1 requires secure registration and login. A separate account class could manage authentication details, but the current implementation does not include one. |
| Payment | Rejected | None of the listed requirements specifies appointment payments, so a Payment class is outside the current scope. |
| Clinic | Rejected | The listed requirements do not require managing clinic branches or clinic records, so a separate Clinic class is not currently necessary. |

## Conclusion

The four accepted classes that match the current implementation are `Patient`, `Doctor`, `Appointment`, and `ClinicSystem`. The inferred classes represent possible future design improvements based on the requirements and should not be considered implemented in the current code.