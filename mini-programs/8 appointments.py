from datetime import datetime, timedelta

class Appointment:
    """Class to represent an appointment."""

    def __init__(self, date, time, name):
        """Initialize an appointment with the given date, time, and name."""
        self.date = date
        self.time = time
        self.name = name

    def __str__(self):
        """Return a string representation of the appointment."""
        return f"{self.name} on {self.date} at {self.time}"

class AppointmentManager:
    """Class to manage a list of appointments."""

    def __init__(self):
        """Initialize an empty list of appointments."""
        self.appointments = []

    def add_appointment(self, appointment):
        """Add an appointment to the list."""
        self.appointments.append(appointment)

    def remove_appointment(self, appointment):
        """Remove an appointment from the list."""
        self.appointments.remove(appointment)

    def upcoming_appointments(self, days=7):
        """Return a list of upcoming appointments within the given number of days."""
        end_date = datetime.now() + timedelta(days=days)
        return [a for a in self.appointments if a.date <= end_date]

def main():
    """Main function to run the program."""
    # Create an AppointmentManager object to manage the appointments.
    manager = AppointmentManager()

    # Prompt the user to input appointment information.
    while True:
        date_str = input("Enter appointment date (MM/DD/YYYY): ")
        time_str = input("Enter appointment time (HH:MM AM/PM): ")
        name = input("Enter name of appointment: ")

        # Convert the date and time strings to datetime objects.
        date = datetime.strptime(date_str, "%m/%d/%Y")
        time = datetime.strptime(time_str, "%I:%M %p").time()

        # Create an Appointment object with the input information.
        appointment = Appointment(date, time, name)

        # Add the appointment to the manager.
        manager.add_appointment(appointment)

        # Ask the user if they want to input another appointment.
        choice = input("Add another appointment? (y/n) ")
        if choice.lower() != "y":
            break

    # Display the upcoming appointments.
    print("\nUpcoming Appointments:")
    for appointment in manager.upcoming_appointments():
        print(appointment)

    # Ask the user if they want to cancel an appointment.
    choice = input("\nCancel an appointment? (y/n) ")
    if choice.lower() == "y":
        name = input("Enter the name of the appointment to cancel: ")
        appointments = [a for a in manager.appointments if a.name == name]
        if len(appointments) == 0:
            print("No appointments with that name found.")
        else:
            appointment = appointments[0]
            manager.remove_appointment(appointment)
            print(f"{appointment} has been cancelled.")

if __name__ == "__main__":
    main()
