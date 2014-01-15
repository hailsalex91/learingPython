cars = 100
passengers = 90
space_in_car = 4
drivers = 30
cars_driven = min(cars, drivers)
cars_not_driven = (cars - drivers,0)
carpool_capacity = cars*space_in_car
average_pass_per_car = passengers/cars_driven

print average_pass_per_car
print "There are", cars, "available"
print "There are only", drivers, "available"
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today"
print "We need to put", average_pass_per_car, "people in every car"