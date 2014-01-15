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
print "We have %d to carpool today" % passengers
print "We need to put %d people in each of the %d cars" % (average_pass_per_car, cars_driven)