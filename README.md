# About
The Transect Calculator is a simple script that outputs the number of transects, direction of each transect, and locations of the first sensor, centerline, and last sensor along the baseline of a rectangular survey unit. This script was designed to assist in planning the magnetometry survey of the fall 2022 season of the [Lagash Archaeological Project](https://web.sas.upenn.edu/lagash/), which uses a [Sensys MXPDA](https://sensys2.kora-media.de/products/mxpda/) cart-based sensor array. There is no reason, however, that it cannot be used to calculate the transects of any other system that collects data in a zig-zag pattern across a rectangular survey unit.

# Usage
This script in Python (version 3.6 and later), and has no external dependencies. It can be run with ```python3 transect_calculator.py```. You will be promted to enter 4 pieces of information:

* The number of sensors in the array.
* The overall width of the sensor array.
* The width of the survey grid.
* The starting X value of the leftmost sensor.

This script is unit agnostic. Most likely the width of your cart track and the width of your survey grid are in meters, but since units aren’t specified, the measurements could be in feet or yards or cubits to yield the same results. Mixed measurement units, however, are not possible.

The script also assumes that you will be walking transects across the grid square in a zig-zag fashion from left to right (as the Sensys data collection software is designed). Typically, this would be starting in the southwest corner of the grid square and walking northward for the first transect.

# Sample Output
A five-sensor array on a 1m wide cart, with a 50m grid square: 
```
----------------------------------------
Number of Sensors: 5
Track Width: 1
Grid Width: 50
Starting Position of Sensor #1: 0
----------------------------------------
Transect         #1      CL      #5
--------        ----    ----    ----
1 (forward):    0.00    0.50    1.00
2 (backward):   2.25    1.75    1.25
3 (forward):    2.50    3.00    3.50
4 (backward):   4.75    4.25    3.75
5 (forward):    5.00    5.50    6.00
6 (backward):   7.25    6.75    6.25
7 (forward):    7.50    8.00    8.50
8 (backward):   9.75    9.25    8.75
9 (forward):    10.00   10.50   11.00
10 (backward):  12.25   11.75   11.25
11 (forward):   12.50   13.00   13.50
12 (backward):  14.75   14.25   13.75
13 (forward):   15.00   15.50   16.00
14 (backward):  17.25   16.75   16.25
15 (forward):   17.50   18.00   18.50
16 (backward):  19.75   19.25   18.75
17 (forward):   20.00   20.50   21.00
18 (backward):  22.25   21.75   21.25
19 (forward):   22.50   23.00   23.50
20 (backward):  24.75   24.25   23.75
21 (forward):   25.00   25.50   26.00
22 (backward):  27.25   26.75   26.25
23 (forward):   27.50   28.00   28.50
24 (backward):  29.75   29.25   28.75
25 (forward):   30.00   30.50   31.00
26 (backward):  32.25   31.75   31.25
27 (forward):   32.50   33.00   33.50
28 (backward):  34.75   34.25   33.75
29 (forward):   35.00   35.50   36.00
30 (backward):  37.25   36.75   36.25
31 (forward):   37.50   38.00   38.50
32 (backward):  39.75   39.25   38.75
33 (forward):   40.00   40.50   41.00
34 (backward):  42.25   41.75   41.25
35 (forward):   42.50   43.00   43.50
36 (backward):  44.75   44.25   43.75
37 (forward):   45.00   45.50   46.00
38 (backward):  47.25   46.75   46.25
39 (forward):   47.50   48.00   48.50
40 (backward):  49.75   49.25   48.75
```

A three-sensor array on a 1m wide cart, with a 20m grid square. This results an error that would cause a gap between the transects in the first grid square and those in the next square to its immediate right: 
```
----------------------------------------
Number of Sensors: 3
Track Width: 1
Grid Width: 20
Starting Position of Sensor #1: 0
----------------------------------------
Transect         #1      CL      #3
--------        ----    ----    ----
1 (forward):    0.00    0.50    1.00
2 (backward):   2.50    2.00    1.50
3 (forward):    3.00    3.50    4.00
4 (backward):   5.50    5.00    4.50
5 (forward):    6.00    6.50    7.00
6 (backward):   8.50    8.00    7.50
7 (forward):    9.00    9.50    10.00
8 (backward):   11.50   11.00   10.50
9 (forward):    12.00   12.50   13.00
10 (backward):  14.50   14.00   13.50
11 (forward):   15.00   15.50   16.00
12 (backward):  17.50   17.00   16.50
13 (forward):   18.00   18.50   19.00

>>> WARNING <<<
The indicated grid width (20) is not evenly divisible by the number of sensors (3).
If you don’t modify your grid or your sensor array to correct this, your survey will have gaps.
```
