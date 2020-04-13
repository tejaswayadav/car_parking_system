class ParkingLot:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.space_left = capacity
        self.parking_allotment = dict()
        self.__allotment_creator()

    def __str__(self):
        return f"Parking lot {self.name} with capacity of {self.capacity} cars."

    # creates a dictionary with mapping of Parking spots to car objects.
    def __allotment_creator(self):
        for position in range(1, self.capacity + 1):
            self.parking_allotment[f"P{position}"] = "Empty"

    # adds a car object to an empty parking spot in the current parking.
    def add_car(self, car):
        if self.space_left > 0:
            for key in self.parking_allotment.keys():
                if self.parking_allotment[key] == "Empty":
                    self.parking_allotment[key] = car
                    print(f"Car {car.manufacturer} {car.name} with plates {car.license_plate} parked at {key} in {self.name}")
                    self.space_left -= 1
                    break
        else:
            print("Parking space not available in this lot.")

    # removes a car object from current parking and marks that spot as empty.
    def remove_car(self, car):
        for key in self.parking_allotment.keys():
            if self.parking_allotment[key] == car:
                self.parking_allotment[key] = "Empty"
                print(f"Car {car.manufacturer} {car.name} with plates {car.license_plate} has left from {key}")
                self.space_left += 1
    
    # gets details of a car parked at a particular parking spot in current parking.
    def get_parking_spot_details(self, parking_spot):
        if self.parking_allotment[parking_spot] == "Empty":
            print(f"Parking space {parking_spot} is currently empty.")
        else:
            car = self.parking_allotment[parking_spot]
            print(f"The details of car parked at {parking_spot} are below:")
            print(car)
