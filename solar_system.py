class System:
    def __init__(self):
        self.bodies = []

    def add(self, celestial_body):
        self.bodies.append(celestial_body)

    def total_mass(self):
        total = sum(body for body in self.celestial_body)
        return toral

class Body:
    def __init__(self, planet_name, planet_mass):
        self.name = planet_name
        self.mass = planet_mass

    
class Planet(Body):
    def __init__(self, planet_name, planet_mass, day_length, year_length):
        super().__init__(planet_name, planet_mass)
        self.day = day_length
        self.year = year_length

class Star(Body):
    def __init__(self, planet_name, planet_mass, star_type):
        super().__init__(planet_name, planet_mass)
        self.type = star_type

class Moon(Body):
    def __init__(self, planet_name, planet_mass, month_length, orbit_planet):
        super().__init__(planet_name, planet_mass)
        self.month = month_length
        self.orbit = orbit_planet


# Creating system and bodies
solar_system = System()
earth = Planet("Earth", 150, 24, 365)
sun = Star("Sun", 200, 'G-type')
earth_moon = Moon("Earth's Moon", 100, 30, earth)
solar_system.add(earth)
solar_system.add(sun)
solar_system.add(earth_moon)

# Printing each item in the solar system to see if they have been added correctly
for body in solar_system.bodies:
    print(body.name)