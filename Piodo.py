def normalize_direction(input_stri):         # A function based on cartesian plane coordinates
    input_stri = input_stri.strip().lower()
    if input_stri in ['n', 'north']:
        return 'N'
    elif input_stri in ['s', 'south']:
        return 'S'
    elif input_stri in ['e', 'east']:
        return 'E'
    elif input_stri in ['w', 'west']:
        return 'W'
    else:
        return None

def main():
    x, y = 0, 0
    print("Starting position: (0, 0)")
    while True:
        command = input("Enter direction (N/S/E/W) or STOP to end: ").strip()
        if command.lower() == "stop":
            break
        direction = normalize_direction(command)
        if direction is None:
            print("Invalid input. Please enter N, S, E, W or STOP.")
            continue
        if direction == 'N':    # Coordinates goes to upper positive value domain quadrant (Represented by Y)
            y += 1
        elif direction == 'S': # Coordinates goes to negative value domain quadrant (Represented by -Y)
            y -= 1
        elif direction == 'E': # Coordinates goes to right positive value   (Represented by X)
            x += 1
        elif direction == 'W': # Coordinates goes to left positive value    (Represented by -X)
            x -= 1
        print(f"Current position: ({x}, {y})") # Computes for the partial position based on user input

    print(f"Final position: ({x}, {y})")    # Computes for the partial position based on user input
    if x == 0 and y == 0:
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")

if __name__ == "__main__":
    main()
