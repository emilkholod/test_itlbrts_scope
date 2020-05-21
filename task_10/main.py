class TransportVehicle:
    def __init__(self, max_speed=0, curr_speed=0):
        self.max_speed = max_speed
        self.curr_speed = curr_speed

    def set_curr_speed(self, new_curr_speed):
        self.curr_speed = new_curr_speed


def Bike(TransportVehicle):
    def set_tire(self, tire):
        self.tire = tire


def Car(TransportVehicle):
    def set_color(self, color):
        self.color = color

    def set_gearshift(self, gearshift):
        self.gearshift = gearshift
