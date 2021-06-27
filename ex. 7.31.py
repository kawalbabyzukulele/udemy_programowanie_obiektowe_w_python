class MeanOfTransport:
    def __init__(self, capacity):
        self.capacity = capacity

    def transport_people(self, number):
        print(f'{self.__class__.__name__} transported {number} people')

    def display_info(self):
        print(self.info)


class Tram(MeanOfTransport):

    def __init__(self, type, capacity, max_speed):
        super().__init__(capacity)
        self.tram_type = type
        self.max_speed = max_speed
        self.info = {'Tram type': self.tram_type, 'Capacity': self.capacity, 'Max speed': self.max_speed}


class Bus(MeanOfTransport):

    def __init__(self, brand, capacity, color):
        super().__init__(capacity)
        self.brand = brand
        self.color = color
        self.info = {'Brand': self.brand, 'Capacity': self.capacity, 'Color': self.color}


class MercedesBenzBus(Bus):

    def __init__(self, brand, capacity, color, air_conditioning):
        super().__init__(brand, capacity, color)
        self.air_conditioning = air_conditioning
        self.info = {'Brand': self.brand, 'Capacity': self.capacity, 'Color': self.color, 'Air conditioning': self.air_conditioning}


def transport_people_to_citycenter(obj):
    print("Destination: City Center")
    obj.transport_people(obj.capacity)


def show_transport_specification(obj):
    obj.display_info


a = Tram('run', 20, 10)
a.transport_people(10)
a.display_info()

print(" ")

b = Bus('volvo', 15, 'yellow')
b.transport_people(2)
b.display_info()

print(" ")

c = MercedesBenzBus('mercedes', 5, 'red', True)
c.transport_people(3)
c.display_info()

print(" ")
print("///")
print(" ")

transport_people_to_citycenter(a)
print(" ")
transport_people_to_citycenter(b)
print(" ")
transport_people_to_citycenter(c)

print(" ")
print("///")
print(" ")

show_transport_specification(a)
print(" ")
show_transport_specification(b)
print(" ")
show_transport_specification(c)
