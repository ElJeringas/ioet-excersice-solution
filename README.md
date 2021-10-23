# ioet-excersice-solution
A possible solution for the problem of the coincidence of workers' schedules.


## Abstract

The files below contain the solution to the problem raised by IOET.
The two files contain:
1. The .txt file contains the schedule organization that the .py solution will call. It contains the name of the workers, the day, and hours of work. Read only this format (Name, MO10: 00-12: 00 ....)
2. The .py file contains the solution and includes the comments for each line of code and a simple explanation of this.

## Solution
- Step-1: read the .txt file convert it to a csv format and delimit rows by (,) and store the values in a dictionary
- Step-2: save the fields in arrays within the dictionary, such as start time, departure time, employee name, day
- Step-3: access the saved data of each employee and store them in the variables for later comparison.
- Step-4: time comparison, if the range of check-in and check-out times match it is set as a match.
- Step-5: Show the solution for each combination of workers.

## Run this solution

There is no need to install external libraries, just consider version of Python in which this was coded: 3.9.5. Then run:
```
Python ioet.py
```
## Test Input
```
RENE,MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00
ASTRID,MO11:00-13:00,TH12:00-14:00,SU20:00-21:00
ANDRES,MO10:00-12:00,TH12:00-14:00,SU20:00-21:00
SANTIAGO,MO10:00-12:00,WE10:00-12:00,TH12:00-14:00,SA10:00-14:00,SU20:00-21:00
ALEX,MO11:45-13:00,TU10:00-12:00,WE10:00-12:00,TH12:00-14:00,SA14:00-18:00,SU17:00-20:00
PAUL,MO08:00-12:00,TU08:00-12:00,WE08:00-12:00,TH08:00-12:00
```
## Test Output
```
RENE-ASTRID 2
RENE-ANDRES 2
RENE-SANTIAGO 3
RENE-ALEX 4
RENE-PAUL 2
ASTRID-ANDRES 3
ASTRID-SANTIAGO 3
ASTRID-ALEX 3
ASTRID-PAUL 2
ANDRES-SANTIAGO 3
ANDRES-ALEX 3
ANDRES-PAUL 2
SANTIAGO-ALEX 5
SANTIAGO-PAUL 3
ALEX-PAUL 4
```
