# FRCPythonProcessing
Tools and Scrips for graphing and data visualtion of FRC scouting data.

### Varible naming conventions:
	ALL CAPS - A fial varible name, something that is acting as a psudo const.
	foo2bar  - Simple convention for dictionaries that contain very basic data.

### Certain varible documentation:
	dict_data - This is the varible that the entire script is based off of. It is a massive 2D dictionary object, the objective is to contain all the stats about teams in a easy to reference manner. 
Currently it is in the form:
		team# ( '4915.0')
			statA ( 'cubescale' )
			statB ( 'cubesexc' )
What this means is taht we can handle a lot more complicated .csv files, and have everything be fairly universal. Uing this method, after we process the entire raw data, no matter the format or type, we will end up with the same datastructure at the end of the day.

