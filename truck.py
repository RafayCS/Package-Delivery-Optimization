# class for delivery trucks
class Truck:
    def __init__(self, number, max_capacity, mileage, avg_speed, load, depart_time, packages, address):
        self.number = number # truck number e.g. 1, 2, or 3
        self.max_capacity = max_capacity
        self.mileage = mileage
        self.avg_speed = avg_speed
        self.load = load
        self.depart_time = depart_time
        self.packages = packages
        self.address = address
        self.time = depart_time


    def __str__(self):
        return f"{self.number}, {self.max_capacity},{self.mileage}, {self.avg_speed}. {self.load}, {self.depart_time}, {self.packages}, {self.packages}, {self.address}"

