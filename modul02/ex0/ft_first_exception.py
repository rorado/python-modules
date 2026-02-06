
def check_temperature(temp_str: str) -> None:

    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        return None
    elif temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return None
    else:
        print(f"Temperature {temp}°C is perfect for plants!")
        return temp
