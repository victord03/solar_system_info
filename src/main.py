from classes.solar_system import SolarSystem


def main():
    ss = SolarSystem()
    ss.sort_self_dicts()

    mercury = ss.planets["Venus"]
    mercury_trivia = mercury.give_trivia(ss)

    print(mercury_trivia)


if __name__ == "__main__":
    main()
