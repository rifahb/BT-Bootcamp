# -------------------------------------------------------------
# HealWell Care Hospital Billing System
# Covers Levels 1 to 8
# -------------------------------------------------------------

# -------------------- LEVEL 7: ADMIN SERVICE SETUP --------------------

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
