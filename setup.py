import logging
import time

def loggingConfig():
    logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')

def log(message):
    logging.info(message)

def quickConfig(deployment=False):
    print('Began config process...', end='\r')
    if not deployment:
        print('Setting up logging...', end='\r')
        loggingConfig()
    print('Done!                   ', end='\r')

        
