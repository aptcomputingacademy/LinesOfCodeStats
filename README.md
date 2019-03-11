# LinesOfCodeStats
Description:
============
Python script to find Lines of code and compare previous report.

Functionality Features:
=======================
1) Finds the lines of code of all the files (python, c, c++ configurable) from the current directory
  
      1.1) Skips empty lines
  
      1.2) Skips commented lines (In progress)
  
2) Checks all the files recursively
3) Generates report about each file
4) Generates difference between previous report and current report
5) Exclude directories 

Non functional features:
========================
1) Runs on Linux/Windows/Mac

How to work:
============
1) Download Python script
2) Open Python script and set the parameters
list_code_formats
remove_dirs
3) Execute the commands:
Command: python3 line_count.py ../../../AptComputingAcademy/Cpp/
Sample output:-
No of lines of c = 597 
Calculated in 0.00795888900756836secs
Diff =  {'../../../AptComputingAcademy/Cpp/day4/asser.cpp:8\n'}
