from data.planet_data import planets
from logic.sorting_dicts import sort_by_value_itemgetter, sort_dict_masses_lambda


class Planet:
    name: str
    radius: int
    mass: tuple[int, int]
    dist_from_sun: int
    dist_from_earth: int

    def __init__(
        self,
        name: str,
        radius: int,
        mass: tuple[int, int],
        dist_from_sun: int,
        dist_from_earth: int,
    ):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.dist_from_sun = dist_from_sun
        self.dist_from_earth = dist_from_earth


    def __str__(self):
        return f"<class Planet: `{self.name}`>"

    def give_trivia(self, ss):

        planet_earth = ss.planets["Earth"]

        text = str()

        if self.name == "Earth":
            formatted_text_radius = str()
            formatted_text_mass = str()

        else:

            text_radius = "{} is a {} planet, with a radius of {} kilometers. It is a {} planet compared to Earth, approximately {} times the size of Earth, which is {} kilometers in radius."
            text_mass = "Its mass is {}x10^{} which gives it the {}th place out of the {} planets (excluding the Sun)."

            larger_than_earth = self.radius > planet_earth.radius

            if larger_than_earth:
                size_comparison = "larger"
                size_class = "large"
                size_to_earth_ratio = round((planet_earth.radius / self.radius * 100), 2)
            else:
                size_comparison = "smaller"
                size_class = "small"
                size_to_earth_ratio = round(self.radius / planet_earth.radius, 2)

            formatted_text_radius = text_radius.format(
                self.name.title(),
                size_class,
                self.radius,
                size_comparison,
                size_to_earth_ratio,
                planet_earth.radius,
            )

            formatted_text_mass = text_mass.format(
                self.mass[0],
                self.mass[1],
                8 - list(ss.masses.keys()).index(self.name),
                ss.number_of_planets
            )

        return formatted_text_radius + "\n" + formatted_text_mass


class SolarSystem:
    planets: dict[str:Planet]
    number_of_planets: int
    radii: dict[str:int]
    masses: dict[str:int]
    dist_from_sun: dict[str:int]
    dist_from_earth: dict[str:int]

    def __init__(self):
        self.planets = dict()

        for planet_name, planet_data in planets.items():

            name = planet_data["Name"]
            radius = planet_data["Radius"]
            mass = planet_data["Mass"]
            distance_sun = planet_data["Distance from the Sun"]
            distance_earth = planet_data["Distance from Earth"]

            self.planets[planet_name] = Planet(
                name=name,
                radius=radius,
                mass=mass,
                dist_from_sun=distance_sun,
                dist_from_earth=distance_earth
            )

        self.number_of_planets = len(self.planets)
        self.radii = dict()
        self.masses = dict()
        self.dist_from_sun = dict()
        self.dist_from_earth = dict()

        for planet_name, planet_instance in self.planets.items():
            self.radii[planet_name] = planet_instance.radius
            self.masses[planet_name] = planet_instance.mass
            self.dist_from_sun[planet_name] = planet_instance.dist_from_sun
            self.dist_from_earth[planet_name] = planet_instance.dist_from_earth

    def sort_self_dicts(self):
        copy_radii = sort_by_value_itemgetter(self.radii, 1)
        copy_masses = sort_dict_masses_lambda(self.masses, 1)
        copy_dist_from_sun = sort_by_value_itemgetter(self.dist_from_sun, 1)
        copy_dist_from_earth = sort_by_value_itemgetter(self.dist_from_earth, 1)

        self.radii = copy_radii
        self.masses = copy_masses
        self.dist_from_sun = copy_dist_from_sun
        self.dist_from_earth = copy_dist_from_earth
