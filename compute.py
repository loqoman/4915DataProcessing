from os.path import abspath, dirname, exists, join
from optparse import OptionParser

from argparse import ArgumentParser

import os
import logging
import functools

# Needed to show images
from PIL import Image

# Nessissary to import files based on a string
import importlib

# Nessissary to import files lower in the directory chain
import sys

#sys.path.append('./Python')

logger = logging.getLogger('4915DataAnalysis')
if __name__ == '__main__':

    optParser = OptionParser()

    argParser = ArgumentParser()
    # Foreward: Parsing arguments is a very powerful tool.
    # It may be a good idea to return to this, and find potentially more efficent ways to do this
    optParser.add_option('-v', '--verbose', default=False, action='store_true',
                    help='Enable verbose logging')

    
    # The 'action' field revolves around what should be done when '-d' is entered in the terminal. 
    # In this case, it is told to 'store_true', which is self explanitory
    optParser.add_option('-d', '--display', default=False, action='store_true',
                    help='Displays the generated graph in the default image viewer')

    # ???: Should delete really default to FALSE? 
    optParser.add_option('--delete',default=False, action='store_true',
                    help='Deletes the generated graph after it is displayed')

    # TODO: add support for parsing multiple files
    # nArgs > 1
    argParser.add_argument('file',nargs='?')
    
    options, args = optParser.parse_args()

    log_datefmt = "%H:%M:%S"
    log_format = "%(asctime)s %(levelname)-6s: %(name)-8s: %(message)s"

    logging.basicConfig(datefmt=log_datefmt,
                        format=log_format,
                        level=logging.DEBUG if options.verbose else logging.INFO)
    
    sys.path.append('./Python')

    logger.info("Initilized %(file)s with the following options: %(options)s",dict(file=__file__,options=options))

    logger.debug("Current sys.path: %s",sys.path)
    
    # For every argument given
    for argument in args:
        
        # List all the scripts in the 'python' directory
        scripts = os.listdir('Python')
        logger.info("Searching for %s in /Python...",argument)
        
        # For all the scripts(strings ATM)
        for fileNames  in scripts:
            
            # If the Script name(string) is the same as an argumen tgiven
            if argument == fileNames:
                # argument is the script name (currently template.py)
                # Log it
                logger.info("Found %s in /Python...",argument)
                
                
                # Import it(But remove .py from the end of it)   
                logger.debug("Importing " + argument + "...")
                 

                # String of the filename
                strProcessor = argument


                #Importing the processor
                processor = importlib.import_module("Python.TEMPLATE")

                logger.info("Processor init message: %s",processor.import_message()) 
                
    
    '''Now comes the part where we deccide to do things with the data'''

    # HACK: Deliver this string in a more conventional manner
    logger.info("Reading data using processor %s, ", strProcessor)

    data = processor.read_data()

    #TODO: Make this information more useful/ maybe move to verbose-only? 
    logger.info("Information read about the data:\n %s" ,data[200:])

    logger.info("Generating graphs...")

    # Save the graph
    # graphs is an array of strings
    # FAQ: The graphs are saved first because potentially the user may want to view the graphs, and not save them, in which case they will be deleted after they are read from the image viewer of choice

    graphs = processor.gen_graphs(data)

    logger.debug("gen_graphs returned %s", graphs)

    # NOTE: Graph will be saved no matter the options parsed
    for string in graphs:

        # Show the graph
        if (options.display):

            logger.info("Showing graphs...")
            image = Image.open(string)
            image.show()

        # Move the graphs
        os.rename(string,"./Out/" + string)

        # Kill the graph 
     
        if (options.delete):
  
            logger.info("Deleting graph...")
            os.remove("./Out/" + string) 


# Misc code snippits.
'''
import os
os.remove(file) for file in os.listdir('path/to/directory') if file.endswith('.png')
'''

'''
sys.path.append(path_to_/python)
from TEMPLATE import * 
'''
