# Farmer Sales Calculation Program

segment_area = 80 / 5  

tomato_yield_1 = 10  # 30% land
tomato_yield_2 = 12  # 70% land
tomato_price = 7     # per kg

potato_yield = 10
potato_price = 20

cabbage_yield = 14
cabbage_price = 24

sunflower_yield = 0.7
sunflower_price = 200

sugarcane_yield = 45
sugarcane_price_per_tonne = 4000


# ---- SALES CALCULATIONS ----

# 1. Tomatoes
tomato_30 = 0.30 * segment_area * tomato_yield_1
tomato_70 = 0.70 * segment_area * tomato_yield_2
tomato_total_kg = (tomato_30 + tomato_70) * 1000
tomato_sales = tomato_total_kg * tomato_price

# 2. Potatoes
potato_total_kg = segment_area * potato_yield * 1000
potato_sales = potato_total_kg * potato_price

# 3. Cabbage
cabbage_total_kg = segment_area * cabbage_yield * 1000
cabbage_sales = cabbage_total_kg * cabbage_price

# 4. Sunflower
sunflower_total_kg = segment_area * sunflower_yield * 1000
sunflower_sales = sunflower_total_kg * sunflower_price

# 5. Sugarcane
sugarcane_total_tonnes = segment_area * sugarcane_yield
sugarcane_sales = sugarcane_total_tonnes * sugarcane_price_per_tonne

# Total sales from all 80 acres
total_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales + sugarcane_sales

# Chemical-free sales at 11 months (vegetables + sunflower)
chemical_free_sales = tomato_sales + potato_sales + cabbage_sales + sunflower_sales


# ---- OUTPUT ----
print("Total Sales From 80 Acres: ₹", total_sales)
print("Chemical-Free Sales at 11 Months: ₹", chemical_free_sales)
