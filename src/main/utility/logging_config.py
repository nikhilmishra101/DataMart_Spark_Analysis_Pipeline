import logging

"""
logging.DEBUG means that only messages with a severity of DEBUG or 
higher (DEBUG,INFO, WARNING, ERROR, CRITICAL) will be shown.
and DEBUG is the lowest level so nothing is lower than DEBUG
%(asctime)s: The time the log message was created.
%(levelname)s: The severity level of the log message (e.g., INFO, ERROR).
%(message)s: The actual log message that was passed to the logging function
"""
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
