numsensors = 5
trackwidth = 1.0
gridwidth = 50.0
startx = 0.0


def highlight_cyan(thetext):
    return f"\033[1m\033[36m{thetext}\033[0m"


def highlight_red(thetext):
    return f"\033[1m\033[31m{thetext}\033[0m"


def get_parameters():
    global numsensors
    global trackwidth
    global gridwidth
    global startx

    # Input the physical characteristics of the sensor array.
    _ = input(f"\nHow many sensors, left-to-right are in your array? [{numsensors}] ")
    if _ != "":
        numsensors = int(_)
    _ = input(
        f"What is the overall width of your sensor array, from the first sensor to the last one? [{trackwidth}] "
    )
    if _ != "":
        trackwidth = float(_)

    # Input the width and starting coordinate of the grid.
    _ = input(f"How wide is your survey grid? [{gridwidth}] ")
    if _ != "":
        gridwidth = float(_)
    _ = input(f"What is the starting X value of your leftmost sensor? [{startx}] ")
    if _ != "":
        startx = float(_)


def show_transects():
    directions = [highlight_red("back"), highlight_cyan("away")]
    transectnumber = 1
    closestsensor = float(startx)
    print(f"\n{'-' * 37}\nNumber of Sensors: {numsensors}")
    print(f"Track Width: {trackwidth}")
    print(f"Grid Width: {gridwidth}")
    print(f"Starting Position of Sensor #1: {startx}\n{'-' * 37}")
    if numsensors == 1:
        print(f"Transect\t#1")
        print(f"--------\t--")
        while closestsensor < gridwidth:
            transectdirection = directions[transectnumber % 2]
            print(f"{transectnumber} ({transectdirection}):\t{closestsensor}")
            transectnumber += 1
            closestsensor += trackwidth
    else:
        spacing = trackwidth / (numsensors - 1)
        print(f"Transect\t #1\t CL\t #{numsensors}")
        print(f"--------\t----\t----\t----")
        while closestsensor + trackwidth < gridwidth:
            transectdirection = directions[transectnumber % 2]
            farthestsensor = closestsensor + trackwidth
            centerline = (closestsensor + farthestsensor) / 2
            if transectdirection == directions[0]:
                print(
                    f"{transectnumber} ({transectdirection}):\t{farthestsensor:.2f}\t{highlight_red(f'{centerline:.2f}')}\t{closestsensor:.2f}"
                )
            else:
                print(
                    f"{transectnumber} ({transectdirection}):\t{closestsensor:.2f}\t{highlight_cyan(f'{centerline:.2f}')}\t{farthestsensor:.2f}"
                )
            transectnumber += 1
            closestsensor = farthestsensor + spacing
    if gridwidth % numsensors:
        print(
            f"\n>>> {highlight_red('WARNING')} <<<\nThe indicated grid width ({gridwidth}) is not evenly divisible by the number of sensors ({numsensors})."
        )
        print(
            "If you don’t modify your grid or your sensor array to correct this, your survey will have gaps.\n"
        )


get_parameters()
show_transects()
