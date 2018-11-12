# FRCPythonProcessing
Tools and Scrips for graphing and data visualtion of FRC scouting data.

### Origin Story
The First scrips for data analysis began in the tail-end of the 2018 season. The project was spearheaded by mentor Ted Larson-Freeman. 

### Mission
The code located in this repository serves the purpose of:

    1. Be a drive team resource
    2. Be an analysis/evaluation tool for other teams
    3. Act as a learning ground for programmers

### History
    2018/06/xx - The repository is currently being refactored from the end of the 2018 season. Code is being consolodated, .gitignore is being fixed, ect.
    
### Building
Currently, this repositroy acts as a collection point for many small, mutially exclusive scripts. Said scripts range from Python 3 to R. So long as you have the required dependencies and languages installed, everything should run smoothly. Note: Many of the scrips here will output graphs in a fairly un-sterlized manner.

Anaconda note: 
On Linux, one must run source /home/<user>/anaconda3/bin/activate root, then execute the binary to properly launch anaconda-navigator.

### Design Decisions
The project is designed to consolodate everything between multiple python scripts
Pros:
    - Full controll of image output
    - Compatible with design of scripts in juypter notebook
    - Theoreticaly easier to manage in a large group

Cons:
    - Fairly oddball method of consolodation
    - Long command-line entries 

### Workflow
If your objective is to design and implement your own graphing solution, these are the required steps.

### Project Structure
####Out
####R
####Python
---- The directory responsible for containing the
####Data
---- The directory responsible for containing the .csv files.

README.md
---- This document
compute.py 
---- The main script responsible for generating the graphs desired

### Planned Features

Score Robotss based on who they are paired with
