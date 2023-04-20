# Do not modify these lines
import os

__winc_id__ = "534d85ea1ab14924a91f9eccf6f3f30d"
__human_name__ = "errors"


# Test your functions here to make sure the functionality remains the same.
def main():
    foo = list(range(10))
    print(
        get_item_from_list(foo, 9),
        get_item_from_list(foo, -1),
        get_item_from_list(foo, 10),
    )
    print(add(2, "test"))
    print(add(2, 2))
    print(add("x", 4))

    print(read_file("C:\\Users\\Romulo\\OneDrive\\Documentos\\Winc_Academy\\Back-end\\errors\\test_me.txt"))


"""Change the three functions below from Look Before You Leap (LBYL) to Easier
to Ask for Forgiveness than Permission (EAFP)"""

# 1.

# Returns the addition of x and y if it's defined, otherwise returns 0

'''
LBYL
def add(x, y):
    if type(x) is str and (type(y) is int or type(y) is float):
        return 0
    elif type(y) is str and (type(x) is int or type(x) is float):
        return 0
    return x + y
'''

# EAFP
def add(x, y):
    try:
        z = x + y
        return z
    except TypeError:
        return 0


# 2.

# Returns the contents of the file at 'filename', or an empty string if the
# file does not exist

'''
LBYL
def read_file(filename):
    if os.path.exists(filename):
        return open(filename, "r").read()
    else:
        return "File not found"
'''

# EAFP
def read_file(filename):
    try:
        return open(filename, "r").read()
    except FileNotFoundError:
        return ""


# 3.

# Returns item at `index` from list `l` if possible, otherwise returns None

'''
LBYL
def get_item_from_list(l, index):
    max_index = len(l) - 1
    min_index = -1 - max_index
    if index <= max_index and index >= min_index:
        return l[index]
    else:
        return None
'''

# EAFP
def get_item_from_list(l, index):
    try:
        return l[index]
    except IndexError:
        return None


if __name__ == "__main__":
    main()
