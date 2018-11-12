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
    2018/06/xx - The repository is currently being refactored from the end of the 2018 season. 
    Code is being consolodated, .gitignore is being fixed, ect.
    2018/11/11 - The first stable version is complete! 
    The project now supports Python, and the importing of basic graph generation scripts.
    
### Building
Currently, this repositroy acts as a collection point for many small, mutially exclusive scripts. Said scripts range from Python 3 to R. So long as you have the required dependencies and languages installed, everything should run smoothly. Note: Many of the scrips here will output graphs in a fairly un-sterlized manner.

Anaconda note: 
On Linux, one must run source /home/[user]/anaconda3/bin/activate root, then execute the binary to properly launch anaconda-navigator.

### Design Decisions
The project is designed to consolodate everything between multiple python scripts
Pros:
    - Full control of image output
    - Compatible with design of scripts in Juypter notebook
    - Easier to manage graph generation methods/needs
    
Cons:
    - Requires learning of another style system
    - Long command-line entries 

### Workflow
For the majority of time, this will simply be simply be 'git clone'd onto a local computer and used to develop graphs there

### Project Structure

**Out**
- The directory responsible for containing output graphs. Images will never be 'commit'ed to this directory

**R**
- The directory responsible for containing R code. There is currently no support for R scripts based on this system

**Python**
- The directory responsible for containing the Python code to generate graphs. There is a standard for this code, layed out in TEMPALTE.py

**Data**
- The directory responsible for containing the .csv files/ data. This is currently unimplemented

README.md
- This document

compute.py 
- The main script responsible for generating the graphs desired. Documentation is located in the file

### Planned Features

Analysis-Wise:
    - Score Robots based on who they are paired with

Codebase-Wise:
    - Add a pip build file to handle dependecies
