# 

from os.path import abspath, dirname, exists, join
from optparse import OptionParser

import os
import logging
import functools

import webbrowser

if __name__ == '__main__':

    parser = OptionParser()

    # Foreward: Parsing arguments is a very powerful tool.
    # It may be a good idea to return to this, and find potentially more efficent ways to do this
    parser.add_option('-v', '--verbose', default=False, action='store_true',
                    help='Enable verbose logging')

    
    # The 'action' field revolves around what should be done when '-d' is entered in the terminal. 
    # In this case, it is told to 'store_true', which is self explanitory
    parser.add_option('-d', '--display', default=False, action='store_true',
                    help='Displays the generated graph in the default image viewer')

    
    parser.add_option('--delete',
                    help='Deletes the generated graph after it is displayed')

    options, args = parser.parse_args()

    print(options)
    
    # Note: With an action of 'store_true', the true or false is not put into the args array
    print(args)

    if options.display:
        webbrowser.open('Out/Graph number 7.png')



# Code for image deletion
'''
import os
os.remove(file) for file in os.listdir('path/to/directory') if file.endswith('.png')
'''
