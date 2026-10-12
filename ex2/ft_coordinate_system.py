#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        coordinates = input(
            "Enter new coordinates as floats in format 'x,y,z': ")
        parts = coordinates.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(parts[0])
            y = float(parts[1])
            z = float(parts[2])
            return (x, y, z)
        except ValueError as e:
            print(e)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    position = get_player_pos()
    print(f"Got a first tuple: {position}")
    print(f"It includes: X={position[0]}, Y={position[1]}, Z={position[2]}")
    distance = math.sqrt(
        position[0] ** 2
        + position[1] ** 2
        + position[2] ** 2)
    distance = round(distance, 4)
    print(f"Distance to center: {distance}")
    print("Get a second set of coordinates")
    position2 = get_player_pos()
    distance = math.sqrt(
        (position2[0] - position[0]) ** 2
        + (position2[1] - position[1]) ** 2
        + (position2[2] - position[2]) ** 2)
    distance = round(distance, 4)
    print(f"Distance between the 2 sets of coordinates: {distance}")


if __name__ == "__main__":
    main()
