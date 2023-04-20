# Do not modify these lines
__winc_id__ = "7b9401ad7f544be2a23321292dd61cb6"
__human_name__ = "arguments"

# Add your code after this line

# 1


def greet(name, greeting="Hello, <name>!"):
    new_greeting = greeting.replace("<name>", name)
    return new_greeting


# Use "replace()" to replace <name> with the name that is given as an argument.

# 2


def force(mass, body="earth"):
    bodies = {
        "sun": 274,
        "jupiter": 24.92,
        "neptune": 11.15,
        "saturn": 10.44,
        "earth": 9.798,
        "uranus": 8.87,
        "venus": 8.87,
        "mars": 3.71,
        "mercury": 3.7,
        "moon": 1.62,
        "pluto": 0.58,
    }

    force = mass * round(bodies[body], 1)
    return force


# The dictionary is preferred within the function since it pertains exclusively on this function
# Use "round()" to hard code rounding the key to 1 decimal.

# 3


def pull(m1, m2, d):
    G = 6.674 * 10 ** -11
    pull = G * ((m1 * m2) / d ** 2)
    return pull


if __name__ == "__main__":
    print(greet("Bob"))
    print(greet("Bob", "Hi there <name>!"))
    print(force(4, "sun"))
    print(pull(2, 5, 3))
# If you're running some examples or standard flow, make sure to do it in main