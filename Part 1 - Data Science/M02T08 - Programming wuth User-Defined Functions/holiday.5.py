# ==============================
# Holiday Cost Calculator Script
# ==============================

# Constants
rental_cost_per_day = 200     # Daily cost of rental car
hotel_night = 600             # Cost per night at hotel

# Functions
def calculate_hotel_cost(num_nights):
    return hotel_night * num_nights

def calculate_flight_cost(city_flight):
    if city_flight == "rome":
        return 2000
    elif city_flight == "london":
        return 1000
    elif city_flight == "new york":
        return 500
    else:
        return 0  # Fallback if city not recognized

def calculate_rental_cost(rental_days):
    return rental_days * rental_cost_per_day

def calculate_total_holiday_cost(num_nights, city_flight, rental_days):
    total_hotel = calculate_hotel_cost(num_nights)
    total_flight = calculate_flight_cost(city_flight)
    total_rental = calculate_rental_cost(rental_days)
    return total_hotel + total_flight + total_rental

# ===================
# User Input Section
# ===================

city_flight = input("Please pick a city from the choices: Rome, London, or New York. Type your choice: ").lower()
num_nights = int(input("How many nights are you staying in the city? "))
rental_days = int(input("How many days will you need the rental car? "))

# =====================
# Cost Calculation Logic
# =====================

if city_flight not in ["rome", "london", "new york"]:
    print("Invalid city. Please choose from Rome, London, or New York.")
else:
    total_cost = calculate_total_holiday_cost(num_nights, city_flight, rental_days)
    print(f"\n--- Holiday Cost Summary ---")
    print(f"Destination: {city_flight.title()}")
    print(f"Hotel Cost: ${calculate_hotel_cost(num_nights)}")
    print(f"Flight Cost: ${calculate_flight_cost(city_flight)}")
    print(f"Car Rental Cost: ${calculate_rental_cost(rental_days)}")
    print(f"Total Cost of Your Holiday: ${total_cost}")

exit()
