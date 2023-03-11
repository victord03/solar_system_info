from classes.solar_system import SolarSystem


def main():
    ss = SolarSystem()
    ss.sort_self_dicts()

    print(
        "\n",
        ss.radii,
        "\n",
        ss.masses,
        "\n",
        ss.distances_from_the_sun,
        "\n",
        ss.distances_from_earth,
        "\n",
    )


if __name__ == "__main__":
    main()
