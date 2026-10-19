HARBORFLOW DISPATCH CONSOLE - TEAM README

Run instructions
----------------
Command:
run python harborflow_app.py
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
The console menu dispatches to separate services for reference validation, delivery quotes, label consolidation, capacity checks, performance classification, weekly reporting, and service comparison. Each service handles its task's input and output, with helper functions for validation and calculations.
How input validation is organized:
Dedicated validators and input loops check booking references, positive numeric values, service codes, parcel weights, non-negative performance values, and weekly delivery counts. Most invalid values cause the relevant prompt to repeat.
How shared calculations are reused:
Single-service quotes and service comparisons use the same quote formula and service multipliers. The weekly report calculates totals and averages from the same seven daily delivery counts and uses helper functions to find high and low days.

Known limitations
-----------------
The weekly report accepts only positive daily delivery counts and reads the weekly target directly as an integer, so zero counts and invalid target input are not supported. The menu's invalid-selection message may also appear after selecting options 1 through 7.
