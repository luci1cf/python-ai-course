# Learn how to use Logging like a Pro

# Logging Basics
#---------------------------------------------------------------------------------
import logging

# Setup Logger
# logging.basicConfig(level=logging.WARNING)

# Log Messages
# logging.debug("This is a debug msg.")           # 10
# logging.info("This is an info msg.")            # 20
# logging.warning("This is a warning msg.")       # 30
# logging.error("This is an error msg.")          # 40
# logging.exception("This is an exception msg.")  # 40 <- Includes Except Traceback
# logging.critical("This is a critical msg.")     # 50

# Simple Example
# a, b = 10, 0
#
# logging.debug(f'Executing: {a}/{b}')
# try:
#     c = a/b
#     logging.info(f'Result: {c}')
# except:
#     logging.exception('Something went wrong.')
#
# print('Hello World!')

# Log to a file
#-----------------------------------------------------------------------------------------------
# import logging
#
# log_format = """***[%(levelname)s]
# Time: %(asctime)s
# Msg: %(message)s
# File: %(filename)s Line: %(lineno)d
# ----------------------------------------------------
# """
#
# logging.basicConfig(level=logging.DEBUG, format = log_format, filename='ef_app.log')
#
# # Log Messages
# logging.debug("This is a debug msg2")           # 10
# logging.info("This is a info msg2")             # 20
# logging.warning("This is a warning msg2")       # 30
#
# print('Where are our logging messages=')

# Log to File and Console
#--------------------------------------------------------------------------------------------------
import logging

# Formatting
log_format = """***[%(levelname)s]
Time: %(asctime)s
Msg: %(message)s
File: %(filename)s Line: %(lineno)d
----------------------------------------------------
"""
formatter = logging.Formatter(log_format)

# Handler 1 - FileHandler
file_handler = logging.FileHandler('ef_app.log')
file_handler.setFormatter(formatter)

# Handler 2 - StreamHandler
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

# Configure Logger
ef_logger = logging.getLogger()
ef_logger.setLevel(logging.DEBUG)
ef_logger.addHandler(file_handler)
ef_logger.addHandler(console_handler)

ef_logger.debug('This is a DEBUG message')

# Recap
#-----------------------------------------------------------------------------------------------------
# Logger    -> The main object that holds configuration and create logging messages
# Handler   -> Determine where logs go (Console, File, Email, Discord, HTTP...)
# Formatter -> Controls how log messages appear
# Filter*   -> Applies filtering on the logs that can pass through

# Webhook - a way for apps to communicate using HTTP POST requests.
# In a nutshell, we can send JSON data to a URL, and the other app knows what to do...