import math

def create_position(x: int, y: int, z: int) -> tuple:
    return (x, y, z)

def distance(point1: tuple, point2: tuple) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def parse_coordinates(coord_str: str) -> tuple:
    try:
        x_str, y_str, z_str = coord_str.split(',')
        x, y, z = int(x_str), int(y_str), int(z_str)
        return (x, y, z)
    except ValueError as e:
        print(f"Parsing invalid coordinates: \"{coord_str}\"")
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")
        return None

def ft_coordinate_system():
    print("=== Game Coordinate System ===")
    print()
    origin = create_position(0, 0, 0)

    default_pos = create_position(10, 20, 5)
    print(f"Position created: {default_pos}")
    print(f"Distance between {origin} and {default_pos}: {distance(origin, default_pos):.2f}")

    test_inputs = ["3,4,0", "abc,def,ghi"]

    for inp in test_inputs:
        print(f"Parsing coordinates: \"{inp}\"")
        pos = parse_coordinates(inp)
        if pos:
            print()
            print(f"Parsed position: {pos}")
            print(f"Distance between {origin} and {pos}: {distance(origin, pos):.1f}")
            print()
            x, y, z = pos
            print("Unpacking demonstration:")
            print(f"Player at x={x}, y={y}, z={z}")
            print(f"Coordinates: X={x}, Y={y}, Z={z}")
            print()

if __name__ == "__main__":
    ft_coordinate_system()
