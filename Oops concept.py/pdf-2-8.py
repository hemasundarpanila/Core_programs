class HotelRoom:
    base_price = 2000   # Class variable

    def __init__(self, room_number, nights_booked, guest_name):
        self.room_number = room_number
        self.nights_booked = nights_booked
        self.guest_name = guest_name

    def calculate_bill(self):
        return self.nights_booked * HotelRoom.base_price

    @classmethod
    def update_base_price(cls, new_price):
        cls.base_price = new_price

    @staticmethod
    def valid_nights(nights):
        return isinstance(nights, int) and nights > 0


# Creating rooms
r1 = HotelRoom(101, 3, "Rahul")
r2 = HotelRoom(102, 5, "Anjali")

print("Before Price Update")
print(r1.guest_name, "Bill =", r1.calculate_bill())
print(r2.guest_name, "Bill =", r2.calculate_bill())

HotelRoom.update_base_price(2500)

print("\nAfter Price Update")
print(r1.guest_name, "Bill =", r1.calculate_bill())
print(r2.guest_name, "Bill =", r2.calculate_bill())

print("\nValidation")
print(HotelRoom.valid_nights(4))
print(HotelRoom.valid_nights(-2))