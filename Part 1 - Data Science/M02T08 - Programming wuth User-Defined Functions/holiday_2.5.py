"""functions to calculate the costs"""

def plane_cost(city):
    city = ["rome", "london", "newyork"]
    plane_cost = {"rome": 2000, "london": 1000, "newyork": 800}
    return plane_cost[city]

def hotel_cost(city, num_nights):
    hotel_cost = {"rome": 300,"london": 400,"newyork": 800}
    return hotel_cost(city) * num_nights

def car_rental(rental_days):
    return rental * rental_days

def holiday_cost(city, num_nights, rental_days, hotel_cost):
    total_flight = plane_cost(city)
    total_hotel = hotel_cost(hotel_cost, num_nights)
    total_rental = car_rental(rental_days)
    return total_flight + total_hotel + total_rental


user_city = input("Please choose a city: Rome, London, or New York").lower()
num_nights = int(input("How many nights are you staying in the city?"))
rental_days = int(input("How many days will you need a rental car?"))
rental = 200

total_cost = holiday_cost(user_city, num_nights, rental_days, hotel_cost)
print(f"The total cost of your holiday is ${holiday_cost}")
