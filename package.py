import datetime

class Package:
    def __init__(self, ID, address, city, state, zip_code, delivery_deadline, weight, status):
        self.ID = ID
        self.address = address
        self.old_address = address # for storing the incorrect address
        self.corrected_address = '410 S State St' if ID == 9 else address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight = weight
        self.status = status
        self.departure_time = None
        self.delivery_time = None
        self.truck_number = None # for storing truck number

    # update package number 9's address based on time
    def update_address(self, current_time):
        correction_time = datetime.timedelta(hours=10, minutes=20)
        if self.ID == 9:
            if current_time >= correction_time:
                self.address = self.corrected_address
                self.zip_code = '84111'
            else:
                self.address = self.old_address


    # method updates the package status based on the current time
    def update_package_status(self, current_time):

        self.update_address(current_time)

        if current_time >= self.delivery_time:
            self.status = "Package delivered"
        elif current_time < self.departure_time:
            self.status = "Package at hub"
        else:
            self.status = "Package is on its way"

    def __str__(self):
        return f"{self.ID}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.delivery_time}, {self.delivery_deadline}, {self.weight}, {self.status}, truck {self.truck_number}"


