import this
from time import sleep
import math
import datetime
import sys
import greet

# Do not modify these lines
__winc_id__ = '78029e0e504a49e5b16482a7a23af58c'
__human_name__ = 'modules'

# Add your code after this line

# 1.
print(this)


# 2.

def wait(seconds):
    sleep(seconds)
    return ''


print(wait(1))


# 3.

def my_sin(number):
    return math.sin(number)


print(my_sin(25))


# 4.

def iso_now():
    result = datetime.datetime.now().isoformat("T", "minutes")
    return result


print(iso_now())


# 5.

def platform():
    return sys.platform


print(platform())


# 6.

def supergreeting_wrapper(name):
    return greet.supergreeting(name)


print(supergreeting_wrapper('Romulo'))
