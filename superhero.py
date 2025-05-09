class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self.power = power
        self.origin = origin

    def display_info(self):
        print(f"{self.name} is from {self.origin} and has the power of {self.power}!")

    def use_power(self):
        print(f"{self.name} uses {self.power}!")



class FlyingHero(Superhero):
    def __init__(self, name, power, origin, flight_speed):
        super().__init__(name, power, origin)
        self.flight_speed = flight_speed

    def use_power(self):
        print(f"{self.name} soars through the sky at {self.flight_speed} km/h using {self.power}!")



class StrengthHero(Superhero):
    def __init__(self, name, power, origin, lifting_capacity):
        super().__init__(name, power, origin)
        self.lifting_capacity = lifting_capacity

    def use_power(self):
        print(f"{self.name} lifts {self.lifting_capacity} tons with {self.power}!")



hero1 = FlyingHero("Sky Hawk", "Wind Control", "Cloud City", 500)
hero2 = StrengthHero("Mighty Man", "Super Strength", "Earth", 100)

hero1.display_info()
hero1.use_power()
hero2.display_info()
hero2.use_power()
