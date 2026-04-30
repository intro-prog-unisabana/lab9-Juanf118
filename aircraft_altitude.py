from aircraft import Aircraft
def main():
    model_ship = input("Enter aircraft model: ")
    aircraft = Aircraft(model_ship)

    while True:
        loop = input("Enter command (A for ascent, D for descent, X for exit): ")
        process = loop.split()
        command = process[0].upper()
        if command == "X":
            break
        elif command == "A":
            if len(process) > 1:
                feet = int(process[1])
                Aircraft.ascend(feet)
        elif command == "D":
            if len(process) > 1:
                feet = int(process[1])
                Aircraft.descend(feet)
        else:
            print("Invalid command. Please enter A, D, or X.")
    print(f"Final altitude: {aircraft.altitude} feet")
if __name__ == "__main__":
    main()
