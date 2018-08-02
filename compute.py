from os.path import abspath, dirname, exists, join
from optparse import OptionParser

from argparse import ArgumentParser

import os
import logging
import functools

import webbrowser

# Nessissary to import files based on a string
import importlib

# Nessissary to import files lower in the directory chain
import sys

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

    
    optParser.add_option('--delete',default=True, action='store_false',
                    help='Deletes the generated graph after it is displayed')

    # Can add support for parsing multiple files
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
    # Support for multiple files
    imported_modules = []
    
    # For every argument given
    for argument in args:
        
        # List all the scripts in the 'python' directory
        scripts = os.listdir('Python')
        logger.info("Searching for %s in /Python...",argument)
        
        # For all the scripts(strings ATM)
        for fileNames  in scripts:
            
            # If the Script name(string) is the same as an argumen tgiven
            if argument == fileNames:
                
                # Log it
                logger.info("Found %s in /Python...",argument)
                
                
                # Import it(But remove .py from the end of it)   
                imported_modules.append(__import__(argument[:-3]))


         
            
    
'''
import os
os.remove(file) for file in os.listdir('path/to/directory') if file.endswith('.png')
'''
