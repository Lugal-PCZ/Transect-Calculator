# Sensor Array
trackwidth = 1
numsensors = 3

# Survey Grid
gridwidth = 45
startx = 0


def showtransects():
    global startx
    global gridwidth
    spacing = trackwidth / (numsensors - 1)
    centerline = startx + (trackwidth / 2)
    transect = 1
    directions = ["backward", "forward"]
    print(f"Transect\t#1\tCL\t#{numsensors}")
    print(f"--------\t--\t--\t--")
    while startx + trackwidth < gridwidth:
        direction = directions[transect % 2]
        if direction == "forward":
            print(
                f"{transect} ({direction}):\t{startx}\t{centerline}\t{startx + trackwidth}"
            )
        else:
            print(
                f"{transect} ({direction}):\t{startx + trackwidth}\t{centerline}\t{startx}"
            )
        transect += 1
        startx += trackwidth + spacing
        centerline = startx + spacing
    if gridwidth % numsensors:
        print(
            f"\nWARNING:\nThe indicated grid width ({gridwidth}m) is not evenly divisible by the number of sensors ({numsensors})."
        )
        print("If you don’t correct this, your survey will have gaps.")


showtransects()
