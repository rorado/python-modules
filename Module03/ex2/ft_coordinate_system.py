import math


def distance(p1, p2) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)


def ft_coordinate_system(input_positions) -> None:
    origin = (0, 0, 0)

    for pos_input in input_positions:
        print(f"Processing input: {pos_input}")

        if isinstance(pos_input, str):
            try:
                x_str, y_str, z_str = pos_input.split(',')
                pos = (int(x_str), int(y_str), int(z_str))
            except ValueError as e:
                print(f"Invalid coordinate string: \"{pos_input}\"")
                print(f"Error: {e}\n")
                continue
        elif isinstance(pos_input, tuple) and len(pos_input) == 3:
            pos = pos_input
        else:
            print(f"Invalid input type: {pos_input}\n")
            continue

        print(f"Parsed position: {pos}")
        print(f"Distance from origin {origin}: {distance(origin, pos):.1f}")

        x, y, z = pos
        print("Unpacking demonstration:")
        print(f"x={x}, y={y}, z={z}\n")


if __name__ == "__main__":
    test_inputs = ["3,4,0", (10, 20, 5), "abc,def,ghi"]
    ft_coordinate_system(test_inputs)
