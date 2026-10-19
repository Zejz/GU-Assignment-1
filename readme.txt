HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
Python version tested: 3.13

Team members and concrete contributions
---------------------------------------
Name: Rafael Siverbo
Contribution:
Coded task 1, 2, 7, 8 and 9
implimented task 1 - 9
Tested task 1 - 7

Name: Mykhailo Asmar
Contribution:
Coded task 3 - 6
Tested task 8 and 9
Tested the final product

Name:
Contribution:

Name (if applicable):
Contribution:

Design notes
------------
Main function boundaries:
The code groups tasks into service functions that coordinate input, processing, and output, supported by calculation and reporting helpers.
How input validation is organized:
Dedicated validators check booking references, numeric inputs, service codes, parcel weights, and weekly delivery counts, usually repeating prompts until valid input is provided.
How shared calculations are reused:
Quoting and comparison reuse the same pricing formula and service multipliers, while the weekly report reuses the delivery total to calculate its average.

Known limitations
-----------------
None known.
