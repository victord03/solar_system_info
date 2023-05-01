from data.planet_data import planets
from logic.sorting_dicts import sort_by_value_itemgetter, sort_dict_masses_lambda


class Planet:
    name: str
    radius: int
    mass: int
    dist_from_sun: int
    dist_from_earth: int

    def __init__(
        self,
        name: str,
        radius: int,
        mass: int,
        dist_from_sun: int,
        dist_from_earth: int,
    ):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.dist_from_sun = dist_from_sun
        self.dist_from_earth = dist_from_earth


class SolarSystem:
    planets: list[Planet]
    number_of_planets: int
    radii: dict[str:int]
    masses: dict[str:int]
    dist_from_sun: dict[str:int]
    dist_from_earth: dict[str:int]

    def __init__(self):
        list_of_planets = list()

        for planet_name, planet_data in planets.items():
            list_of_planets.append(Planet(*list(planet_data.values())))

        self.planets = list_of_planets
        self.number_of_planets = len(self.planets)
        self.radii = dict()
        self.masses = dict()
        self.dist_from_sun = dict()
        self.dist_from_earth = dict()

        for planet in self.planets:
            self.radii[planet.name] = planet.radius
            self.masses[planet.name] = planet.mass
            self.dist_from_sun[planet.name] = planet.dist_from_sun
            self.dist_from_earth[planet.name] = planet.dist_from_earth

    def sort_self_dicts(self):
        copy_radii = sort_by_value_itemgetter(self.radii, 1)
        copy_masses = sort_dict_masses_lambda(self.masses, 1)
        copy_dist_from_sun = sort_by_value_itemgetter(self.dist_from_sun, 1)
        copy_dist_from_earth = sort_by_value_itemgetter(self.dist_from_earth, 1)

        self.radii = copy_radii
        self.masses = copy_masses
        self.dist_from_sun = copy_dist_from_sun
        self.dist_from_earth = copy_dist_from_earth
