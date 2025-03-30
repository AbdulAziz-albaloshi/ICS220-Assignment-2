from Royal_Classes import *  # [Used from Royal_Classes.py] — All class, enum, and method definitions
import re  # For input validation using regular expressions

# Create a Guest object with validation
def create_guest():
    print("\n--- Guest Account Creation ---")

    while True:
        guest_name = input("Enter guest_name: ").strip()
        if re.fullmatch(r"[A-Za-z ]+", guest_name):
            break
        else:
            print("Invalid name. Only letters and spaces are allowed.")

    guest_id = input("Enter guest_id: ").strip()

    while True:
        phone_number = input("Enter phone_number (10-digit): ").strip()
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Phone number must be a 10-digit number with no letters or symbols.")

    while True:
        gender = input("Enter gender (Male/Female/Other): ").strip().lower()
        if gender in ["male", "female", "other"]:
            gender_enum = Gender[gender.upper()]  # [Used from Royal_Classes.py] — Gender Enum
            break
        else:
            print("Invalid gender. Please enter Male, Female, or Other.")

    return Guest(guest_name, guest_id, int(phone_number), gender_enum)  # [Used from Royal_Classes.py] — Creates an object for the Guest class


# Upgrade a regular guest to a LoyalGuest if user confirms
def upgrade_to_loyal_guest(guest):
    while True:
        response = input("Is this a loyal guest? (yes/no): ").strip().lower()
        if response in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please answer only with 'yes' or 'no'.")

    if response == "yes":
        while True:
            loyalty_level = input("Enter loyalty level (Gold/Silver/Bronze): ").strip().capitalize()
            if loyalty_level in ["Gold", "Silver", "Bronze"]:
                break
            else:
                print("Invalid loyalty level. Please choose Gold, Silver, or Bronze.")

        while True:
            try:
                points = int(input("Enter loyalty points: "))
                break
            except ValueError:
                print("Loyalty points must be a number.")

                # Creates an Object for the Loyalguest Class using the info from the Guest Class
        return LoyalGuest(
            guest.get_guest_name(),
            guest.get_guest_id(),
            guest.get_guest_number(),
            guest.get_guest_gender(),
            points,
            loyalty_level
        )

    else:
        return guest  # Return original Guest object if not loyal



# Book a Room and add Amenity and Booking
def book_room_for_guest(guest):
    print("\n--- Book a Room ---")

    while True:
        try:
            room_number = int(input("Enter room_number: "))
            break
        except ValueError:
            print("Invalid input. Room number must be numeric.")

    while True:
        room_type = input("Enter room_type (Single/Double/Suite): ").strip().lower()
        if room_type in ["single", "double", "suite"]:
            room_enum = RoomType[room_type.upper()]  # [Used from Royal_Classes.py] — RoomType Enum
            break
        else:
            print("Invalid room type. Please enter Single, Double, or Suite.")

    while True:
        try:
            price_per_night = float(input("Enter price_per_night: "))
            break
        except ValueError:
            print("Invalid input. Price must be numeric.")

    while True:
        available = input("Is the room available? (yes/no): ").strip().lower()
        if available in ["yes", "no"]:
            is_available = (available == "yes")
            if not is_available:
                retry = input("Room is not available. Do you want to try another room? (yes/no): ").strip().lower()
                if retry == "yes":
                    return book_room_for_guest(guest)
                else:
                    exit()
            break
        else:
            print("Please answer with yes or no.")

    room = Room(room_number, room_enum, is_available, price_per_night)  # [Used from Royal_Classes.py] — Create an object for the Room class

    print("\n--- Add Amenity ---")
    while True:
        amenity_name = input("Amenity name: ").strip()
        if re.fullmatch(r"[A-Za-z ]+", amenity_name):
            break
        else:
            print("Amenity name must contain only letters and spaces.")

    while True:
        is_amenity_available = input("Is the amenity available? (yes/no): ").strip().lower()
        if is_amenity_available in ["yes", "no"]:
            amenity_avail = is_amenity_available == "yes"
            break
        else:
            print("Please answer with yes or no.")

    if amenity_avail:
        amenity_desc = input("Amenity description: ")
        while True:
            try:
                amenity_price = float(input("Amenity price: "))
                break
            except ValueError:
                print("Amenity price must be a valid number.")
    else:
        print("Sorry, amenity is not available.")
        amenity_desc = "Not available"
        amenity_price = 0.0

    amenity = Amenity(amenity_name, amenity_desc, amenity_avail, amenity_price)  # [Used from Royal_Classes.py] — Creaates an object for the Amenity class
    room.add_amenity(amenity)  # [Used from Royal_Classes.py] — Room.add_amenity()

    booking_id = input("Enter booking_id: ").strip()

    while True:
        booking_date = input("Enter booking_date (YYYY-MM-DD): ").strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", booking_date):
            break
        else:
            print("Invalid format. Date must be in YYYY-MM-DD format.")

    while True:
        booking_status = input("Enter booking_status (confirmed/pending/cancelled): ").strip().lower()
        if booking_status in ["confirmed", "pending", "cancelled"]:
            break
        else:
            print("Invalid status. Please enter confirmed, pending, or cancelled.")

    while True:
        try:
            number_of_guests = int(input("Enter number_of_guests: "))
            break
        except ValueError:
            print("Invalid input. Number of guests must be numeric.")

    booking = Booking(booking_id, booking_date, booking_status, number_of_guests)  # [Used from Royal_Classes.py] — Creates an object for the Booking class
    booking.set_room(room)  # [Used from Royal_Classes.py] — Booking.set_room()
    guest.add_booking(booking)  # [Used from Royal_Classes.py] — Guest.add_booking()

    return booking


# Generate receipt and calculate total
def generate_receipt(booking):
    print("\n--- Generate Receipt ---")
    receipt_id = input("Enter receipt_id: ").strip()

    while True:
        issue_date = input("Enter issue_date (YYYY-MM-DD): ").strip()
        if re.fullmatch(r"\d{4}-\d{2}-\d{2}", issue_date):
            break
        else:
            print("Date must be in YYYY-MM-DD format.")

    room = booking.get_room()  # [Used from Royal_Classes.py] — Booking.get_room()
    room_price = room.get_room_price()  # [Used from Royal_Classes.py] — Room.get_room_price()
    amenity_prices = sum(amenity.get_amenity_price() for amenity in room.get_amenities())  # [Used from Royal_Classes.py] — Amenity.get_amenity_price()
    total_amount = room_price + amenity_prices

    print(f" total price: Room (${room_price}) + Amenities (${amenity_prices}) = ${total_amount:.2f}")

    while True:
        payment_method = input("Payment method (Card/Cash/Wallet): ").strip().lower()
        if payment_method in ["card", "cash", "wallet"]:
            payment_enum = PaymentMethod[payment_method.upper()]  # [Used from Royal_Classes.py] — PaymentMethod Enum
            break
        else:
            print("Please enter a valid payment method.")

    receipt = Receipt(receipt_id, issue_date, total_amount, payment_enum)  # [Used from Royal_Classes.py] — Creates an object for the Receipt class
    booking.set_receipt(receipt)  # [Used from Royal_Classes.py] — Booking.set_receipt()
    return receipt


# Show full history of guest, bookings, and receipts
def show_history(guest):
    print("\n--- Reservation History ---")
    print(guest)  # [Uses __str__() from Royal_Classes.py] — Guest or LoyalGuest

    for booking in guest.get_bookings():  # [Used from Royal_Classes.py] — Guest.get_bookings()
        print(booking)  # [Uses __str__() from Royal_Classes.py] — Booking
        if booking.get_receipt():  # [Used from Royal_Classes.py] — Booking.get_receipt()
            print(booking.get_receipt())  # [Uses __str__() from Royal_Classes.py] — Receipt
        else:
            print("No receipt available for this booking.")

        print("Room Info:")
        print(booking.get_room())  # [Uses __str__() from Royal_Classes.py] — Room

        print("Amenities:")
        for amenity in booking.get_room().get_amenities():  # [Used from Royal_Classes.py] — Room.get_amenities()
            print(amenity)  # [Uses __str__() from Royal_Classes.py] — Amenity


# Run a single full test case
def run_test_case():
    guest = create_guest()
    guest = upgrade_to_loyal_guest(guest)  # [Optional upgrade to LoyalGuest]

    booking = book_room_for_guest(guest)
    status = booking.get_booking_status().lower()  # [Used from Royal_Classes.py] — Booking.get_booking_status()

    if status == "confirmed":
        confirm = input("Confirm booking and send notification? (yes/no): ").strip().lower()
        if confirm == "yes":
            print("Booking confirmed. Sending notification...")
            receipt = generate_receipt(booking)
            receipt.send_to_guest()  # [Used from Royal_Classes.py] — Receipt.send_to_guest()
            show_history(guest)
        else:
            print("Booking was not confirmed. No receipt generated.")

    elif status == "pending":
        print("Booking is pending. Sending notification...")
        print("Thank you for booking with us. We'll notify you once it's confirmed.")

    elif status == "cancelled":
        print("Booking has been cancelled. Sending notification...")
        print("We're sorry to see you cancel. Hope to host you in the future!")


# Entry point
def main():
    print("==== HOTEL MANAGEMENT TEST ====")
    try:
        run_test_case()
    except Exception as e:
        print(f"An error occurred: {e}")  # Basic error handler
    finally:
        print("\nThank you for choosing Royal Hotel. We look forward to serving you again!")  # Always prints

if __name__ == "__main__":
    main() # Runs the programs


