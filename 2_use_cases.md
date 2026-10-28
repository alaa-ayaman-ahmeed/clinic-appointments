# 2. Use Cases

## Use Case: Book Appointment
- **Actors:** Patient, System, Doctor
- **Precondition:** Patient is logged in and has fewer than 5 active appointments.
- **Main Flow:**
  1. Patient requests to view available doctor schedules.
  2. System displays available doctors and time slots.
  3. Patient selects a doctor and time slot and requests to book.
  4. System verifies that the patient's active appointment count is less than $N = 5$.
  5. System creates the appointment and confirms the booking to the patient.

- **Alternative Flow (4a. Limit Exceeded):**
  1. At step 4, if the patient already has 5 active appointments ($N = 5$), the system rejects the booking request.
  2. System displays an error message informing the patient of the maximum limit.
  3. Use case ends.

## Use Case Diagram
```mermaid
graph TD
    Patient([Patient]) --> UC1(Register / Login)
    Patient --> UC2(View Doctor Schedules)
    Patient --> UC3(Book Appointment)
    Doctor([Doctor]) --> UC4(View Daily Appointments)
    Doctor --> UC5(Update Appointment Status)
    UC3 -->|Includes Check N=5| System[(Clinic System)]
