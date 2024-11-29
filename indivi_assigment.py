from collections import deque

print('*' * 40)
print('|', "Welcome To Vacation Planning System", '|')
print('*' * 40)

booking_trip = []
trip_queue = deque()
destinations = {
    "A": {"name": "Huye_muhanga", "slots": 30},
    "B": {"name": "Huye_kigali", "slots": 30},
    "C": {"name": "Huye_musanze", "slots": 30},
    "D": {"name": "Huye_gicumbi", "slots": 30},
    "E": {"name": "Huye_rurindo", "slots": 30},
    "F": {"name": "Huye_nyabihu", "slots": 30}
}


def available_trip():
    print("\nAvailable destinations with slots:")
    for key, destination in destinations.items():
        print(f"{key}: {destination['name']} - {destination['slots']} slots available")


def booking_trips(letter, name_family):
    if destinations[letter]["slots"] > 0:
        trip_name = destinations[letter]["name"]
        request = f"Booking: {name_family} for {trip_name}"
        booking_trip.append(request)
        destinations[letter]["slots"] -= 1
        print(f"Booking request confirmed: {request}")
    else:
        print(f"Sorry, no available slots for {destinations[letter]['name']}.")


def undo_last_booking():
    if booking_trip:
        last_booking = booking_trip.pop()

        trip_name = last_booking.split(" for ")[1]


        for letter, destination in destinations.items():
            if destination["name"] == trip_name:
                destinations[letter]["slots"] += 1

                print(f"Undone: {last_booking}")
                print(f"Slot for {trip_name} restored. New slots: {destinations[letter]['slots']}")
                return
    else:
        print("No available bookings to undo.")


def add_trip_request(name_family, letter):
    if letter in destinations:
        trip_name = destinations[letter]["name"]
        trip_request = f"Request: {name_family} for {trip_name}"
        trip_queue.append(trip_request)
        print(f"Trip request added: {name_family} for {trip_name}")
    else:
        print(f"Sorry, invalid destination letter: {letter}.")


def process_trip():
    if trip_queue:
        next_request = trip_queue.popleft()
        trip_name = next_request.split(" for ")[1]
        for letter, destination in destinations.items():
            if destination["name"] == trip_name:
                print(f"Processing request: {next_request}")

                booking_trip.append(next_request)
                destinations[letter]["slots"] -= 1
                print(f"Trip booked successfully: {next_request}")
                return
        print(f"Invalid trip request for {trip_name}.")
    else:
        print("No processing requests available.")


def trip_booked():
    print("\nCurrent booked trips:")
    if booking_trip:
        for booking in booking_trip:
            print(f"- {booking}")
    else:
        print("No trips booked yet.")


def display_trip_request():
    print("\nCurrent trip requests:")
    if trip_queue:
        for request in trip_queue:
            print(request)
    else:
        print("No trip requests.")


def destination_trips():
    while True:
        print("\nMenu: ")
        print("1. Available destinations")
        print("2. Booking trips")
        print("3. Undo last booking")
        print("4. Add trip request")
        print("5. Process trip")
        print("6. View booked trips")
        print("7. Display trip requests")
        print("8. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            available_trip()
        elif choice == 2:
            name = input("Enter your name: ")
            available_trip()
            letter = input("Enter the destination letter (A, B, C, etc.): ").upper()
            if letter in destinations:
                booking_trips(letter, name)
            else:
                print("Invalid destination letter.")
        elif choice == 3:
            undo_last_booking()
        elif choice == 4:
            name = input("Enter your name: ")
            available_trip()
            letter = input("Enter the destination letter (A, B, C, etc.): ").upper()
            if letter in destinations:
                add_trip_request(name, letter)
            else:
                print("Invalid destination letter.")
        elif choice == 5:
            process_trip()
        elif choice == 6:
            trip_booked()
        elif choice == 7:
            display_trip_request()
        elif choice == 8:
            print("Exiting the system. Have a great day!")
            break
        else:
            print("Invalid choice. Please try again.")


destination_trips()
