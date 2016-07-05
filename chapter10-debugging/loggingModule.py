import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
"""
when Python logs an event, it creates a  LogRecord object that holds informa-
tion about that event. The  logging module’s  basicConfig() function lets you
specify what details about the  LogRecord object you want to see and how you
want those details displayed.
"""