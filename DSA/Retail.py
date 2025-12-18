

class Item:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class CartItem:
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity

    def total_price(self):
        return self.item.price * self.quantity



class ShoppingCart:
    def __init__(self):
        self.cart_items = []

    def add_item(self, item, quantity):
        self.cart_items.append(CartItem(item, quantity))

    def calculate_subtotal(self):
        subtotal = 0
        for ci in self.cart_items:
            subtotal += ci.total_price()
        return subtotal

    def calculate_bulk_discount(self):
        discount = 0
        for ci in self.cart_items:
            if ci.quantity >= 3:
                discount += 0.10 * ci.total_price()
        return discount

    def calculate_cart_discount(self, subtotal):
        if subtotal > 1000:
            return 0.05 * subtotal
        return 0

    def calculate_surcharge(self):
        surcharge = 0
        for ci in self.cart_items:
            if ci.item.category.lower() == "luxury":
                surcharge += 0.02 * ci.total_price()
        return surcharge

    def generate_invoice(self):
        print("\n=========== INVOICE ===========")
        print(f"{'Item':15}{'Qty':5}{'Price':10}{'Total'}")
        print("-" * 40)

        for ci in self.cart_items:
            print(
                f"{ci.item.name:15}"
                f"{ci.quantity:<5}"
                f"{ci.item.price:<10}"
                f"{ci.total_price():.2f}"
            )

        subtotal = self.calculate_subtotal()
        bulk_discount = self.calculate_bulk_discount()
        cart_discount = self.calculate_cart_discount(subtotal)
        surcharge = self.calculate_surcharge()

        total_discount = bulk_discount + cart_discount
        taxable_amount = subtotal - total_discount + surcharge
        tax = 0.05 * taxable_amount
        final_amount = taxable_amount + tax

        print("-" * 40)
        print(f"Subtotal:            ₹{subtotal:.2f}")
        print(f"Bulk Discount:       -₹{bulk_discount:.2f}")
        print(f"Cart Discount:       -₹{cart_discount:.2f}")
        print(f"Surcharge:           +₹{surcharge:.2f}")
        print(f"Tax (5% GST):        +₹{tax:.2f}")
        print("=" * 40)
        print(f"TOTAL PAYABLE:       ₹{final_amount:.2f}")
        print("=" * 40)



if __name__ == "__main__":
    # Create items
    apple = Item("Apple", 50, "grocery")
    perfume = Item("Perfume", 500, "luxury")
    tshirt = Item("T-Shirt", 300, "clothing")

    # Create cart
    cart = ShoppingCart()
    cart.add_item(apple, 3)
    cart.add_item(perfume, 1)
    cart.add_item(tshirt, 2)

    # Generate invoice
    cart.generate_invoice()
