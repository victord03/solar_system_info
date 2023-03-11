from data.planet_data import planets
from logic.sorting_dicts import sort_dict_by_value_itemgetter, sort_dict_masses_lambda


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

    def sort_self_dicts(self):
        copy_radii = sort_dict_by_value_itemgetter(self.radii, 1)
        copy_masses = sort_dict_masses_lambda(self.masses, 1)
        copy_distances_from_the_sun = (sort_dict_by_value_itemgetter(self.distances_from_the_sun, 1))
        copy_distances_from_earth = (sort_dict_by_value_itemgetter(self.distances_from_earth, 1))

        self.radii = copy_radii
        self.masses = copy_masses
        self.distances_from_the_sun = copy_distances_from_the_sun
        self.distances_from_earth = copy_distances_from_earth
