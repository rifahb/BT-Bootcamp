

services = ["General Consultation", "Blood Test", "Covid Test", "X-Ray", "CT Scan", "MRI"]
costs = [500, 300, 800, 1500, 4000, 7000]

# -------------------- LEVEL 1: PATIENT DETAILS ------------------------

print("--------------------------------------------------")
print("        Welcome to HealWell Care Hospital         ")
print("--------------------------------------------------")

name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ")
contact = input("Enter Contact Number: ")

# -------------------- LEVEL 2: DISPLAY SERVICES -----------------------

print("\n------------------ Available Services ------------------")
for i in range(len(services)):
    print(f"{i+1}. {services[i]} - ₹{costs[i]}")

selected_numbers = input("\nSelect services (comma separated numbers): ")
selected_numbers = list(map(int, selected_numbers.split(",")))
# =============================================================
# HealWell Care Hospital Billing System (Enterprise Version)
# =============================================================

GST_RATE = 0.18
SENIOR_DISCOUNT_RATE = 0.10
HIGH_BILL_DISCOUNT_RATE = 0.05
HIGH_BILL_THRESHOLD = 5000

SERVICES = {
    1: ("General Consultation", 500),
    2: ("Blood Test", 300),
    3: ("Covid Test", 800),
    4: ("X-Ray", 1500),
    5: ("CT Scan", 4000),
    6: ("MRI", 7000),
}


def get_patient_details():
    print("\nPatient Registration")
    print("-" * 40)
    name = input("Patient Name       : ").strip()
    age = int(input("Age                : "))
    gender = input("Gender             : ").strip()
    contact = input("Contact Number     : ").strip()
    return name, age, gender, contact


def display_services():
    print("\nAvailable Medical Services")
    print("-" * 40)
    for key, (service, cost) in SERVICES.items():
        print(f"{key}. {service:<25} ₹{cost}")


def get_selected_services():
    selections = input("\nSelect services (comma separated): ")
    selected_ids = [int(x.strip()) for x in selections.split(",")]
    return selected_ids


def calculate_discounts(subtotal, age):
    senior_discount = subtotal * SENIOR_DISCOUNT_RATE if age >= 60 else 0
    amount_after_senior = subtotal - senior_discount

    high_bill_discount = (
        amount_after_senior * HIGH_BILL_DISCOUNT_RATE
        if amount_after_senior > HIGH_BILL_THRESHOLD
        else 0
    )

    total_discount = senior_discount + high_bill_discount
    return senior_discount, high_bill_discount, total_discount


def generate_invoice(patient, services, costs, subtotal, discounts, gst, total):
    name, age, gender, contact = patient
    senior_discount, high_bill_discount, total_discount = discounts

    print("\n" + "=" * 55)
    print("              HEALWELL CARE HOSPITAL")
    print("                    INVOICE")
    print("=" * 55)

    print("\nPatient Details")
    print("-" * 40)
    print(f"Name    : {name}")
    print(f"Age     : {age}")
    print(f"Gender  : {gender}")
    print(f"Contact : {contact}")

    print("\nServices Availed")
    print("-" * 40)
    for i, service in enumerate(services, 1):
        print(f"{i}. {service:<25} ₹{costs[i-1]}")

    print("\nBilling Summary")
    print("-" * 40)
    print(f"Subtotal                 : ₹{subtotal:.2f}")
    print(f"Senior Citizen Discount  : ₹{senior_discount:.2f}")
    print(f"High-Bill Discount       : ₹{high_bill_discount:.2f}")
    print(f"Total Discounts          : ₹{total_discount:.2f}")
    print(f"GST (18%)                : ₹{gst:.2f}")
    print("-" * 40)
    print(f"GRAND TOTAL              : ₹{total:.2f}")
    print("=" * 55)
    print("Thank you for choosing HealWell Care Hospital")
    print("=" * 55)


def main():
    
    print("      Welcome to HealWell Care Hospital System")
    patient = get_patient_details()
    display_services()
    selected_ids = get_selected_services()

    selected_services = []
    selected_costs = []

    for sid in selected_ids:
        service, cost = SERVICES[sid]
        selected_services.append(service)
        selected_costs.append(cost)

    subtotal = sum(selected_costs)

    senior_discount, high_bill_discount, total_discount = calculate_discounts(
        subtotal, patient[1]
    )

    subtotal_after_discount = subtotal - total_discount
    gst = subtotal_after_discount * GST_RATE
    grand_total = subtotal_after_discount + gst

    generate_invoice(
        patient,
        selected_services,
        selected_costs,
        subtotal,
        (senior_discount, high_bill_discount, total_discount),
        gst,
        grand_total,
    )



if __name__ == "__main__":
    main()

selected_services = []
selected_costs = []

# -------------------- LEVEL 3: FETCH SELECTED COSTS -------------------

for num in selected_numbers:
    index = num - 1
    selected_services.append(services[index])
    selected_costs.append(costs[index])

# -------------------- LEVEL 4: CALCULATE SUBTOTAL ---------------------

subtotal = sum(selected_costs)

# -------------------- LEVEL 8: DISCOUNT LOGIC -------------------------

discount = 0

# Senior Citizen Discount (10%)
if age >= 60:
    senior_discount = subtotal * 0.10
    discount += senior_discount
else:
    senior_discount = 0

# Amount after senior discount
after_senior = subtotal - discount

# High-Bill Discount (5% if subtotal > 5000)
if after_senior > 5000:
    high_bill_discount = after_senior * 0.05
    discount += high_bill_discount
else:
    high_bill_discount = 0

subtotal_after_discount = subtotal - discount

# -------------------- LEVEL 5: APPLY GST (18%) ------------------------

gst = subtotal_after_discount * 0.18
grand_total = subtotal_after_discount + gst

# -------------------- LEVEL 6: GENERATE INVOICE -----------------------

print("\n--------------------------------------------------")
print("                HealWell Care Hospital            ")
print("                    Patient Invoice               ")
print("--------------------------------------------------")

print("Patient Information:")
print(f"Name    : {name}")
print(f"Age     : {age}")
print(f"Gender  : {gender}")
print(f"Contact : {contact}")

print("\nServices Availed:")
for i in range(len(selected_services)):
    print(f"{i+1}. {selected_services[i]} : ₹{selected_costs[i]}")

print("\n----------------------- BILL SUMMARY -----------------------")
print(f"Subtotal (Before Discounts) : ₹{subtotal}")
print(f"Senior Citizen Discount     : ₹{senior_discount}")
print(f"High-Bill Discount          : ₹{high_bill_discount}")
print(f"Subtotal After Discounts    : ₹{subtotal_after_discount}")
print(f"GST (18%)                   : ₹{gst}")
print("-------------------------------------------------------------")
print(f"Grand Total                 : ₹{grand_total}")
print("-------------------------------------------------------------")
print("Thank you for choosing HealWell Care Hospital!")
print("-------------------------------------------------------------")
