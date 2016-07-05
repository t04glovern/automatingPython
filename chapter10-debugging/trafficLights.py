market_2nd = {'ns': 'green', 'ew': 'red'}
mission_16th = {'ns': 'red', 'ew': 'green'}

def switchLights(stoplight):
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

        assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
        """
        Traceback (most recent call last):
          File "C:/Users/Nathan/Documents/Git/automatingPython/chapter10-debugging/trafficLights.py", line 14, in <module>
            switchLights(market_2nd)
          File "C:/Users/Nathan/Documents/Git/automatingPython/chapter10-debugging/trafficLights.py", line 12, in switchLights
            assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
        AssertionError: Neither light is red! {'ew': 'green', 'ns': 'green'}
        """

switchLights(market_2nd)

# Assertions can be disabled by passing the  -O option when running Python.