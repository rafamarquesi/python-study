# !!!>>> File utilizied for study purposes only !!!<<<

# Decorators are functions that take another function as an argument and extend the behavior of the latter function without explicitly modifying it.

# Articles used as reference: https://sureshdsk.dev/series/python-decorators
# Author: Suresh D

# https://sureshdsk.dev/python-decorators-101
# Simple decorator
def hello_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result
    return wrapper


@hello_decorator
def add(a, b):
    return a + b


if __name__ == '__main__':
    output = add(2, 2)
    print(output)
