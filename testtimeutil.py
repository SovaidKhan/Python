"""
>>> import timeutil
>>> timeutil.validate('12 59 pm')
False
>>> timeutil.validate('12:59 lm')
False
>>> timeutil.validate('12:5 pm')
False
>>> timeutil.validate('123:59 pm')
False
>>> timeutil.validate('12:59 pm')
True


"""
import doctest
doctest.testmod(verbose=True)