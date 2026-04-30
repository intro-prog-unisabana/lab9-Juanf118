from aircraft import Aircraft

def main():
    model = input("Enter aircraft model:")
    aircraft = Aircraft(model)

    while True:
        line = input("Enter command (A for ascent, D for descent, X to exit):").strip()
        if line.upper() == "X":
            break
        parts = line.split()
        if len(parts) != 2:
            continue
        cmd = parts[0].upper()
        try:
            feet = int(parts[1])
        except ValueError:
            continue

        if cmd == "A":
            aircraft.climb(feet)
        elif cmd == "D":
            aircraft.descend(feet)
        else:
            continue

    print(f"Final altitude: {aircraft.altitude} feet")

if __name__ == "__main__":
    main()