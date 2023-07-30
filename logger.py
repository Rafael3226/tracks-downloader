import logging

# Basic configuration
logging.basicConfig(
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='app.log',  # Specify the log file name
    filemode='a'  # Use 'a' for append mode, 'w' for overwrite
)

# Additional configuration (optional)
# Create a logger instance
logger = logging.getLogger('my_logger')

# Set the logging level for the logger
logger.setLevel(logging.DEBUG)

# Create a file handler (optional, if not using basicConfig's filename)
file_handler = logging.FileHandler('app.log')
file_handler.setLevel(logging.DEBUG)

# Create a console handler (optional, for displaying logs in the console)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Create a formatter and attach it to the handlers
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Attach the handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)