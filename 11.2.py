# Extend the previosly written Car class by adding two subclasses: ElectricCar and GasolineCar. Electric cars have
# the capacity of the battery in kilowatt-hours as their property. Gasoline cars have the volume of the tank in
# liters as their property. Write initializers for the subclasses. For example, the initializer of electric cars
# receives the registration number, maximum speed and battery capacity as its parameter. It calls the initializer of
# the base class to set the first two properties and then sets its capacity. Write a main program where you create
# one electric car (ABC-15, 180 km/h, 52.5 kWh) and one gasoline car (ACD-123, 165 km/h, 32.3 l). Select speeds for
# both cars, make them drive for three hours and print out the values of their kilometer counters.

class Car:
    # class initializer that sets the first two of the properties based on parameter values. The current speed and
    # travelled distance of a new car are automatically set to zero.
    def __init__(self, reg_num, max_speed):
        self.reg_num = reg_num
        self.max_speed = max_speed
        self.curr_speed = 0
        self.travel_dist = 0

    # accerelate method, that receives the change of speed (km/h) as a parameter. If the change is negative,
    # the car reduces speed. The speed of the car is set below maximum and is not less than zero.
    def accelerate(self, change_of_speed):
        self.curr_speed = self.curr_speed + change_of_speed
        if change_of_speed >= 0:
            if self.curr_speed > self.max_speed:
                self.curr_speed = self.max_speed
            # print(f"The car has accelerated {change_of_speed} km/h.")
        if change_of_speed < 0:
            if self.curr_speed < 0:
                self.curr_speed = 0
            # print(f"The car has decelerated {change_of_speed} km/h.")

    # drive method that receives the number of hours as a parameter. The method increases the travelled distance by
    # how much the car has travelled in constant speed in the given time.
    def drive(self, num_of_hours):
        self.travel_dist = self.travel_dist + self.curr_speed * num_of_hours
        # print(f"The travelled distance is now {car.travel_dist} km.\n")

class ElectricCar(Car):
    def __init__(self, reg_num, max_speed, battery_cap):
        super().__init__(reg_num, max_speed)
        self.battery_cap = battery_cap

class GasolineCar(Car):
    def __init__(self, reg_num, max_speed, tank_volume):
        super().__init__(reg_num, max_speed)
        self.tank_volume = tank_volume


electric_car1 = ElectricCar("ABC-15", 180, 52.5)
gasoline_car1 = GasolineCar("ACD-123", 165, 32.3)

electric_car1.accelerate(40)
gasoline_car1.accelerate(50)
electric_car1.drive(3)
gasoline_car1.drive(3)
print(f"The travelled distance of a car with the register number {electric_car1.reg_num} is now {electric_car1.travel_dist} km.\n")
print(f"The travelled distance of a car with the register number {gasoline_car1.reg_num} is now {gasoline_car1.travel_dist} km.\n")