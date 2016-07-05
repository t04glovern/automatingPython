import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')


def factorial_incorrect(n):
    logging.debug('Start of incorrect factorial(%s%%)' % (n))
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of incorrect factorial(%s%%)' % (n))
    return total


def factorial_correct(n):
    logging.debug('Start of correct factorial(%s%%)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of correct factorial(%s%%)' % (n))
    return total

logging.debug('Start of incorrect program')
print(factorial_incorrect(5))
logging.debug('End of incorrect program')

logging.debug('Start of correct program')
print(factorial_correct(5))
logging.debug('End of correct program')

"""
DEBUG - logging.debug()
------------------------------
The lowest level.Used for small details.
Usually you care about these messages only
when diagnosing problems .

INFO - logging.info()
------------------------------
Used to record information on general events
in your program or confirm that things are
working at their point in the program.

WARNING - logging.warning()
------------------------------
Used to indicate a potential problem that
doesn’t prevent the program from working but
might do so in the future.

ERROR - logging.error()
------------------------------
Used to record an error that caused the
program to fail to do something.

CRITICAL - logging.critical()
------------------------------
The highest level. Used to indicate a fatal
error that has caused or is about to cause
the program to stop running entirely.
"""

"""
Disable Logging
"""
logging.critical('Critical error! Critical error!')
logging.disable(logging.CRITICAL)
logging.critical('Critical error! Critical error!')
logging.error('Error! Error!')