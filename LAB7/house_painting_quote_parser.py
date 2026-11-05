def clean_colour_name(name):
    """
    Turns a colour name into a lower-case code, e.g. 'Ocean Blue' -> 'ocean_blue'.
    Assumes name is a non-empty string.
    """
    return name.strip().lower().replace(' ', '_')

def room_area(text):
    """
    Converts 'LENGTHxWIDTH' into an area in square feet.
    Assumes exactly one 'x' between two whole numbers.
    """
    length, width = text.lower().split('x')
    return int(length) * int(width)

def total_wall_area(text):
    """
    Adds up wall areas separated by semicolons.
    Assumes every area is a whole number.
    """
    return sum(int(area) for area in text.split(';'))

def main():
    print("==== Running clean_colour_name ====")
    value = input("Enter a paint colour name (e.g. Ocean Blue): ")
    print("Colour code:", clean_colour_name(value))

    print("\n==== Running room_area ====")
    value = input("Enter room size as LENGTHxWIDTH in feet (e.g. 12x10): ")
    print("Room area (sq ft):", room_area(value))

    print("\n==== Running total_wall_area ====")
    value = input("Enter wall areas separated by ; (e.g. 120;95;110): ")
    print("Total wall area (sq ft):", total_wall_area(value))

if __name__ == "__main__":
    main()
