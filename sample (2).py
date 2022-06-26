from logging.handlers import *
import logging
import time

logging.basicConfig(filename='app.log',filemode='a',level=logging.DEBUG)#,format='%(asctime)s - %(levelno)s - %(name)s - %(levelname)s - %(message)s')

#display_log_this_way = "[%(levelname)s] - %(asctime)s - %(name)s - : %(message)s in %(pathname)s:%(lineno)d"



#formatterObj = logging.Formatter(display_log_this_way)



# Main logger
main_logger = logging.getLogger()
main_logger.setLevel(logging.INFO)      #root


#output --> console pr ---> Info ---> Formatter -->
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)      # console wale ka
# console_handler.setFormatter(formatterObj)
#
# #on size basis -- new file..
# rotating_file_handler = RotatingFileHandler('r_app.log', maxBytes=100000000, backupCount=5)
# rotating_file_handler.setLevel(logging.DEBUG)
# rotating_file_handler.setFormatter(formatterObj)
#
# #on time basis -- new file
# time_rotating_handler = TimedRotatingFileHandler('time_app.log',when='M')
# time_rotating_handler.setLevel(logging.DEBUG)
# time_rotating_handler.setFormatter(formatterObj)


#main_logger.addHandler(console_handler)
#main_logger.addHandler(rotating_file_handler)
#main_logger.addHandler(time_rotating_handler)

"nonset---0"
while True:
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')
    time.sleep(3)

#logging.basicConfig(filename='app.log',filemode='a',format=)






import sys
sys.exit(0)

'''

levels

    NOTSET=0
    DEBUG=10
    INFO=20
    WARN=30     *
    ERROR=40
    CRITICAL=50


handlers --> where you want that log to be recorded
        file
        db
        email
        and so on....
        
        
formatters --> how you want that log to be displayed....


'''


# these are the diff categories of messages...      logging levels...
logging.info('This is method one...!')
logging.debug()
logging.warn()
logging.error('Divide by Zero')
logging.critical()


print('This is method one...!') #