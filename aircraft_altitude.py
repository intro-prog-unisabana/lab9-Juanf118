def main():
    from aircraft import Aircraft

    _ = input().rstrip()
    altitude = 0
    model_ship = input("Enter aircraft model:\n")
    aircraft = Aircraft(model_ship)
    while True:
        print("Enter command (A for ascent, D for descent, X to exit):")
        line = input().strip()
        if line == "X":
            break
        if not line:
            continue
        parts = line.split()
        cmd = parts[0]
        if cmd in ("A", "D") and len(parts) == 2:
            try:
                value = int(parts[1])
            except ValueError:
                # entrada inválida: ignorar y continuar leyendo
                continue
            if cmd == "A":
                altitude += value
            else:
                altitude -= value
        else:
            continue

    print(f"Final altitude: {altitude} feet")


if __name__ == "__main__":
    main()