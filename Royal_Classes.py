from enum import Enum

# ENUMS
class Gender(Enum):
    """Class to represent Enumeration of available genders."""
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class RoomType(Enum):
    """Class to represent Enumeration of available room types."""
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"

class PaymentMethod(Enum):
    """Class to represent Enumeration of available payment methods."""
    CARD = "Card"
    CASH = "Cash"
    WALLET = "Wallet"


# Guest Class
class Guest:
    """Class to represent a hotel guest"""

    # Constructor (protected attributes due to being a parent in an inheritence relationship)
    def __init__(self, guest_name: str, guest_id: str, guest_number: int, guest_gender: Gender):
        self._guest_name = guest_name
        self._guest_id = guest_id
        self._guest_number = guest_number
        self._guest_gender = guest_gender
        self.__bookings = []  # Association relation with Guest

    # Setter / Getter
    def set_guest_name(self, guest_name=""):
        self._guest_name = guest_name
    def get_guest_name(self):
        return self._guest_name

    def set_guest_id(self, guest_id=""):
        self._guest_id = guest_id
    def get_guest_id(self):
        return self._guest_id

    def set_guest_number(self, guest_number=0):
        self._guest_number = guest_number
    def get_guest_number(self):
        return self._guest_number

    def set_guest_gender(self, guest_gender=Gender.OTHER):
        self._guest_gender = guest_gender
    def get_guest_gender(self):
        return self._guest_gender

    # Add booking to the guest's list
    def add_booking(self, booking):
        self.__bookings.append(booking)

    # Retrieve all bookings of the guest
    def get_bookings(self):
        return self.__bookings

    # Display guest information
    def display_guest_info(self):
        print(self.__str__())

    # String representation of the guest Class
    def __str__(self):
        return f"Guest[ID: {self._guest_id}, Name: {self._guest_name}, Number: {self._guest_number}, Gender: {self._guest_gender.value}]"


# LoyalGuest Class
class LoyalGuest(Guest):
    """Class to represent a loyal guest (Inherits Guest)"""

    # Constructor (private attributes)
    def __init__(self, guest_name, guest_id, guest_number, guest_gender, loyalty_points, loyalty_level):
        super().__init__(guest_name, guest_id, guest_number, guest_gender)  # Inheritance relation with Guest
        self.__loyalty_points = loyalty_points
        self.__loyalty_level = loyalty_level

    # Setter / Getter
    def set_loyalty_points(self, loyalty_points=0):
        self.__loyalty_points = loyalty_points
    def get_loyalty_points(self):
        return self.__loyalty_points

    def set_loyalty_level(self, loyalty_level=""):
        self.__loyalty_level = loyalty_level
    def get_loyalty_level(self):
        return self.__loyalty_level

    # Return current points
    def check_points(self):
        return self.__loyalty_points

    # Redeem a specific amount of points
    def redeem_points(self, amount):
        if amount <= self.__loyalty_points:
            self.__loyalty_points -= amount

    # Return loyalty tier and points
    def view_status(self):
        return f"{self.__loyalty_level} with {self.__loyalty_points} points"

    # String representation of loyal guest Class
    def __str__(self):
        return f"{super().__str__()}, Loyalty Level: {self.__loyalty_level}, Points: {self.__loyalty_points}"


# Amenity Class
class Amenity:
    """Class to represent room amenities"""

    # Constructor (private attributes)
    def __init__(self, name, description, availability, price):
        self.__amenity_name = name
        self.__amenity_description = description
        self.__amenity_availability = availability
        self.__amenity_price = price

    # Setter / Getter
    def set_amenity_name(self, name=""):
        self.__amenity_name = name
    def get_amenity_name(self):
        return self.__amenity_name

    def set_amenity_description(self, desc=""):
        self.__amenity_description = desc
    def get_amenity_description(self):
        return self.__amenity_description

    def set_amenity_availability(self, available=True):
        self.__amenity_availability = available
    def get_amenity_availability(self):
        return self.__amenity_availability

    def set_amenity_price(self, price=0.0):
        self.__amenity_price = price
    def get_amenity_price(self):
        return self.__amenity_price

    # Print amenity details
    def display_amenity_details(self):
        print(self.__str__())

    # String representation of an amenity Class
    def __str__(self):
        return f"Amenity: {self.__amenity_name}, Desc: {self.__amenity_description}, Available: {self.__amenity_availability}, Price: ${self.__amenity_price}"


# Room Class
class Room:
    """Class to represent a hotel room"""

    # Constructor (private attributes)
    def __init__(self, room_number, room_type, room_availability, room_price):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__room_availability = room_availability
        self.__room_price = room_price
        self.__amenities = []  # Composition relation with amenity

    # Setter / Getter
    def set_room_number(self, room_number=0):
        self.__room_number = room_number
    def get_room_number(self):
        return self.__room_number

    def set_room_type(self, room_type=RoomType.SINGLE):
        self.__room_type = room_type
    def get_room_type(self):
        return self.__room_type

    def set_room_availability(self, available=True):
        self.__room_availability = available
    def get_room_availability(self):
        return self.__room_availability

    def set_room_price(self, price=0.0):
        self.__room_price = price
    def get_room_price(self):
        return self.__room_price

    # Add an amenity to the room
    def add_amenity(self, amenity):
        self.__amenities.append(amenity)

    # Get all amenities in the room
    def get_amenities(self):
        return self.__amenities

    # Display room information
    def display_room_details(self):
        print(self.__str__())

    # String representation of the room Class
    def __str__(self):
        amenity_names = ", ".join([a.get_amenity_name() for a in self.__amenities])
        return f"Room #{self.__room_number}, Type: {self.__room_type.value}, Available: {self.__room_availability}, Price: ${self.__room_price}, Amenities: [{amenity_names}]"


# Receipt Class
class Receipt:
    """Class to represent a receipt"""

    # Constructor (private attributes)
    def __init__(self, receipt_id, issue_date, total_amount, payment_method):
        self.__receipt_id = receipt_id
        self.__receipt_issue_date = issue_date
        self.__total_amount = total_amount
        self.__payment_method = payment_method

    # Setter / Getter
    def set_receipt_id(self, receipt_id=""):
        self.__receipt_id = receipt_id
    def get_receipt_id(self):
        return self.__receipt_id

    def set_receipt_issue_date(self, issue_date=""):
        self.__receipt_issue_date = issue_date
    def get_receipt_issue_date(self):
        return self.__receipt_issue_date

    def set_total_amount(self, total_amount=0.0):
        self.__total_amount = total_amount
    def get_total_amount(self):
        return self.__total_amount

    def set_payment_method(self, method=PaymentMethod.CARD):
        self.__payment_method = method
    def get_payment_method(self):
        return self.__payment_method

    # Show receipt content
    def display_receipt_details(self):
        print(self.__str__())

    # Simulate sending receipt to guest
    def send_to_guest(self):
        print(f"Sending receipt {self.__receipt_id} to guest...")

    # String representation of receipt Class
    def __str__(self):
        return f"Receipt[ID: {self.__receipt_id}, Date: {self.__receipt_issue_date}, Total: ${self.__total_amount}, Payment: {self.__payment_method.value}]"


# Booking Class
class Booking:
    """Class to represent a booking"""

    # Constructor (private attributes)
    def __init__(self, booking_id, booking_date, booking_status, number_of_guests):
        self.__booking_id = booking_id
        self.__booking_date = booking_date
        self.__booking_status = booking_status
        self.__number_of_guests = number_of_guests
        self.__room = None  # Room assigned to the booking (Aggregation)
        self.__receipt = None  # Receipt associated with the booking (Composition)

    # Setter / Getter
    def set_booking_id(self, booking_id=""):
        self.__booking_id = booking_id
    def get_booking_id(self):
        return self.__booking_id

    def set_booking_date(self, booking_date=""):
        self.__booking_date = booking_date
    def get_booking_date(self):
        return self.__booking_date

    def set_booking_status(self, booking_status=""):
        self.__booking_status = booking_status
    def get_booking_status(self):
        return self.__booking_status

    def set_number_of_guests(self, number_of_guests=1):
        self.__number_of_guests = number_of_guests
    def get_number_of_guests(self):
        return self.__number_of_guests

    def set_room(self, room):
        self.__room = room
    def get_room(self):
        return self.__room

    def set_receipt(self, receipt):
        self.__receipt = receipt
    def get_receipt(self):
        return self.__receipt

    # Simulate booking management
    def manage_booking(self):
        print("Managing booking...")

    # Show booking info
    def display_booking_details(self):
        print(self.__str__())

    # String representation of booking Class
    def __str__(self):
        room_info = f"Room #{self.__room.get_room_number()}" if self.__room else "No Room"
        return f"Booking[ID: {self.__booking_id}, Date: {self.__booking_date}, Status: {self.__booking_status}, Guests: {self.__number_of_guests}, {room_info}]"
