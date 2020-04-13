from car import Car
from parkinglot import ParkingLot


class ParkingSystem:

    @staticmethod
    def check_availability(parking_lot):
        if parking_lot.space_left > 0:
            availability_list = [key for key in parking_lot.parking_allotment.keys() if parking_lot.parking_allotment[key] == "Empty"]
            print(f"Space available at: {availability_list}")
        else:
            print("No parking space is currently available in this parking.")


def main():
    ps = ParkingSystem()
    parking = ParkingLot("TCS Parking", 3)
    car1 = Car("Swift", "Maruti Suzuki", "MH04T1995")
    car2 = Car("Fabia", "Skoda", "MH44T2012")
    car3 = Car("SL535", "Mercedes Benz", "MP19T1221")
    car4 = Car("X6", "BMW", "MP22110")
    ps.check_availability(parking)
    parking.add_car(car1)
    parking.add_car(car2)
    ps.check_availability(parking)
    parking.remove_car(car1)
    parking.add_car(car3)
    parking.get_parking_spot_details("P2")
    parking.add_car(car4)
    ps.check_availability(parking)


if __name__ == '__main__':
    main()
