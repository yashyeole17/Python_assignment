# Q 29) create a class vehicle with attributes(color,enginepower,tyre)and behaviour(start, stop)
# create class car which inherit vehicle class with attributes(airbag, gear, speed, fuel)and
# methods(accelerate,fullfuel,paymusic(),onAC())
# create class electric car with attribute(battery) and behaviour(charging(),batterylevel())

class vehicle:
    def __init__(self, color, epower, tyre):
        self.color = color
        self.epower = epower
        self.tyre = tyre

        def display(self):
            print(f" colour = {color} , engine power = {epower} , tyre= {tyre}")


class behaviour:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

        def charging(self):
            print(f"Charging is full")

        def batterylvl(self):
            print(f"Inside battery level function")

        def display(self):
            print(f" start= {start} , Stop= {stop}")


class car(vehicle):
    def __init__(self, color, epower, tyre, airbag, gear, speed, fuel):
        vehicle.__init__(self, color, epower, tyre)
        self.airbag = airbag
        self.gear = gear
        self.speed = speed
        self.fuel = fuel

        def accelerate(self):
            print("Inside accelerate function")

        def fullfuel(self):
            print("Inside fullfuel function")

        def playmusic(self):
            print("Inside playmusic function")

        def onAC(self):
            print("Inside onAC function")

class electriccar(vehicle):
    def __init__(self, color, epower, tyre, battery):
        vehicle.__init__(self, color, epower, tyre)
        self.battery = battery

    def display(self):
        vehicle.display(self)
        print(f"battery= {battery}")


