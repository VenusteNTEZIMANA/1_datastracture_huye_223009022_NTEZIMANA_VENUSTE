from collections import deque

print('*' * 40)
print('|', "Welcome To Vacation Planning System", '|')
print('*' * 40)

booking_trip = []  # List to hold confirmed bookings
trip_queue = deque()  # Queue to hold pending trip requests
destinations = ["Huye_kigali", "Huye_musanze", "huye_gicumbi", "huye_muhanga", "huye_rurindo", "huye_nyabihu"]


def available_trip():
    print("\nAvailable destinations:")
    for trip in destinations:
        print(trip)


def booking_trips(trip, name_family):
    request = f"Request: {name_family} for {trip}"
    booking_trip.append(request)
    print(f"Request added: {request}")


def undo_last_booking():
    if booking_trip:
        last_booking = booking_trip.pop()
        print(f"Undone: {last_booking}")
    else:
        print("No available bookings to undo.")


def add_trip_request(name_family, trip):
    trip_request = f"Trip: {name_family} for {trip}"
    trip_queue.append(trip_request)
    print(f"Trip request added: {name_family} for {trip}")


def process_trip():
    if trip_queue:
        next_request = trip_queue.popleft()  # Get the first request in the queue
        print(f"Next to process: {next_request}")
        # After processing, move the request to the booking list
        booking_trip.append(next_request)
        print(f"Trip booked successfully: {next_request}")
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
            trip = input("Enter the trip you choose from available destinations: ")
            if trip in destinations:
                booking_trips(trip, name)
            else:
                print("Trip does not exist.")
        elif choice == 3:
            undo_last_booking()
        elif choice == 4:
            name = input("Enter your name: ")
            available_trip()
            trip = input("Enter the trip you want to request: ")
            if trip in destinations:
                add_trip_request(name, trip)
            else:
                print("Trip does not exist.")
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
