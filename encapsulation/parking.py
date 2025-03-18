import time

class Car:
    def __init__(self, plate_number):
        self.plate_number = plate_number
        self.__entry_time = time.time()  # Private attribute

    def get_parking_duration(self):
        return time.time() - self.__entry_time


class ParkingLot:
    def __init__(self, hourly_rate=2):
        self.__cars = {}  # Private dictionary for parked cars
        self.hourly_rate = hourly_rate

    def park_car(self, plate_number):
        if plate_number in self.__cars:
            return "Car is already parked."
        self.__cars[plate_number] = Car(plate_number)
        return f"Car {plate_number} parked successfully."

    def remove_car(self, plate_number):
        if plate_number in self.__cars:
            car = self.__cars.pop(plate_number)
            duration = car.get_parking_duration() / 3600  # Convert seconds to hours
            fee = round(duration * self.hourly_rate, 2)
            return f"Car {plate_number} removed. Parking fee: ${fee}"
        return "Car not found."

    def list_parked_cars(self):
        return list(self.__cars.keys())


# გამოყენება
parking = ParkingLot()
print(parking.park_car("ABC-123"))
time.sleep(5)  # პარკირების სიმულაცია 5 წამით
print(parking.list_parked_cars())
print(parking.remove_car("ABC-123"))
print(parking.list_parked_cars())
