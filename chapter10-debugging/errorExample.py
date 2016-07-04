def spam():
    bacon()


def bacon():
    raise Exception('This is the error message.')

spam()

"""
The Traceback error message generated

Traceback (most recent call last):
  File "C:/Users/Nathan/Documents/GitHub/automatingPython/chapter10-debugging/errorExample.py", line 7, in <module>
    spam()
  File "C:/Users/Nathan/Documents/GitHub/automatingPython/chapter10-debugging/errorExample.py", line 2, in spam
    bacon()
  File "C:/Users/Nathan/Documents/GitHub/automatingPython/chapter10-debugging/errorExample.py", line 5, in bacon
    raise Exception('This is the error message.')
Exception: This is the error message.
"""
