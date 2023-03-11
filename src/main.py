from classes.solar_system import SolarSystem
from ui import sorting_displays as displays_sorted


def main():
    ss = SolarSystem()

    print(displays_sorted.sort_dict_by_value(ss.radii, 1))
    print(displays_sorted.sort_dict_by_value(ss.masses, 1))
    print(displays_sorted.sort_dict_by_value(ss.distances_from_the_sun, 1))
    print(displays_sorted.sort_dict_by_value(ss.distances_from_earth, 1))


if __name__ == "__main__":
    main()
