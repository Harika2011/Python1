hotel_per_day = float(input("Enter the amount that the hotel stay costs per day: "))
num_days = int(input("Enter the number of days you stayed at the hotel: "))
vehicle_per_day = float(input("Enter the amount that the vehicle rent costs per day: "))
num_days1 = int(input("Enter the number of days you rented a vehicle : "))
plane_ticket = float(input("Enter the total amount of one person's plane ticket: "))
num_ppl = int(input("Enter the number of people traveling (1 if only you): "))


hotel_total = hotel_per_day * num_days
vehicle_total = vehicle_per_day * num_days1
plane_ticket_total = plane_ticket * num_ppl
trip_expenditure = hotel_total + vehicle_total + plane_ticket_total

print("\nThe amount you spent on the HOTEL: $" + str(hotel_total))
print("The amount you spent on the VEHICLE: $" + str(vehicle_total))
print("The amount you spent on PLANE TICKETS: $" + str(plane_ticket_total))
print("\nThe total expenditure of your trip concludes at: $" + str(trip_expenditure))
