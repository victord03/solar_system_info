from data.planet_data import planets


class SolarSystem:
    planets: list[str]
    number_of_planets: int
    radii: dict[str: int]
    masses: dict[str: int]
    distances_from_the_sun: dict[str: int]
    distances_from_earth: dict[str: int]

    def __init__(self):
        self.planets = list(planets.keys())
        self.number_of_planets = len(self.planets)

        self.radii = dict()
        self.masses = dict()
        self.distances_from_the_sun = dict()
        self.distances_from_earth = dict()

        for planet_name in planets:
            self.radii[planet_name] = planets[planet_name]["radius"]
            self.masses[planet_name] = planets[planet_name]["mass"]
            self.distances_from_the_sun[planet_name] = planets[planet_name]["distance from the sun"]
            self.distances_from_earth[planet_name] = planets[planet_name]["distance from earth"]
