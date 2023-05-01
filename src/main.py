from classes.solar_system import SolarSystem


def main():
    ss = SolarSystem()
    ss.sort_self_dicts()

    print(ss.dist_from_sun)


if __name__ == "__main__":
    main()
