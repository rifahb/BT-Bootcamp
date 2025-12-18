from cruise_ship import CruiseShip

class MarineCompany:
    def __init__(self, name):
        self.name = name
        self.ships = []

    def add_ship(self, ship):
        self.ships.append(ship)

    # 1. Total amount collected by company
    def total_amount_collected(self):
        return sum(ship.total_amount() for ship in self.ships)

    # 2. Total amount collected for every ship
    def amount_by_ship(self):
        return {ship.name: ship.total_amount() for ship in self.ships}

    # 3. Customer details for a particular cruise ship
    def customers_for_cruise_ship(self, ship_name):
        for ship in self.ships:
            if isinstance(ship, CruiseShip) and ship.name == ship_name:
                return [booking.customer for booking in ship.bookings]
        return []
