from marine_company import MarineCompany
from cruise_ship import CruiseShip
from cargo_ship import CargoShip
from customer import Customer
from booking import Booking

company = MarineCompany("Oceanic Lines")

# Ships
cruise1 = CruiseShip(1, "Sea Queen")
cargo1 = CargoShip(2, "Cargo King")

company.add_ship(cruise1)
company.add_ship(cargo1)

# Customers
c1 = Customer(1, "Alice")
c2 = Customer(2, "Bob")

# Bookings
b1 = Booking(1, c1, 5000)
b2 = Booking(2, c2, 7000)
b3 = Booking(3, c1, 10000)

cruise1.add_booking(b1)
cruise1.add_booking(b2)
cargo1.add_booking(b3)

print("Total Amount Collected:",
      company.total_amount_collected())

print("Amount by Ship:",
      company.amount_by_ship())

print("Customers for Sea Queen:",
      [c.name for c in company.customers_for_cruise_ship("Sea Queen")])
