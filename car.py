class Car:
    def __init__(self, name, manufacturer, license_plate):
        self.name = name
        self.manufacturer = manufacturer
        self.license_plate = license_plate

    def __str__(self):
        return f"{self.manufacturer} {self.name} with license plate number {self.license_plate}."