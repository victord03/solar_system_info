from classes.solar_system import SolarSystem


def main():
    ss = SolarSystem()
    ss.sort_self_dicts()

    print(ss.radii)
    mercury = ss.planets["Venus"]
    print(mercury.give_trivia(ss.planets["Earth"]))


if __name__ == "__main__":
    main()
