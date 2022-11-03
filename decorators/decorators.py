# !!!>>> File utilizied for study purposes only !!!<<<

# Decorators are functions that take another function as an argument and extend the behavior of the latter function without explicitly modifying it.

# Articles used as reference: https://sureshdsk.dev/series/python-decorators
# Author: Suresh D

# Article 1: https://sureshdsk.dev/python-decorators-101

# > Simple decorator function example
# def hello_decorator(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#     return wrapper


# @hello_decorator
# def add(a, b):
#     return a + b


# if __name__ == '__main__':
#     output = add(2, 2)
#     print(output)

# > 
# def hello_decorator(func):
#     print(f'Decorator Init :: Begins for {func.__name__}')

#     def wrapper(*args, **kwargs):
#         print(f'Decorator execution :: Begins for {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'Decorator execution :: Ends for {func.__name__}')
#         return result

#     print(f'Decorator Init :: Ends for {func.__name__}')
#     return wrapper


# @hello_decorator
# def add(a, b):
#     return a + b


# if __name__ == '__main__':
#     output1 = add(2, 2)
#     print('Result:: ', output1)

#     output2 = add(4, 2)
#     print('Result:: ', output2)

# > What happens under the hood
# def hello_decorator(func):
#     print(f'Decorator Init :: Begins for {func.__name__}')

#     def wrapper(*args, **kwargs):
#         print(f'Decorator execution :: Begins for {func.__name__}')
#         result = func(*args, **kwargs)
#         print(f'Decorator execution :: Ends for {func.__name__}')
#         return result

#     print(f'Decorator Init :: Ends for {func.__name__}')
#     return wrapper



# def add(a, b):
#     return a + b

# # This is equivalent to the @ syntax
# add = hello_decorator(add)

# if __name__ == '__main__':
#     output1 = add(2, 2)
#     print('Result:: ', output1)

#     output2 = add(4, 2)
#     print('Result:: ', output2)

# Article 2: https://sureshdsk.dev/python-decorators-201

# > Add some docstrings to the decorator

# def hello_decorator(func):
#     """Simple decorator function"""

#     def wrapper(*args, **kwargs):
#         """Simple decorator wrapper function"""
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @hello_decorator
# def add(a, b):
#     """Simple function that returns sum of two numbers"""
#     return a + b


# @hello_decorator
# def multiply(a, b):
#     """Simple function that returns multiplication of two numbers"""
#     return a * b


# if __name__ == '__main__':

#     help(add)

#     print(add.__name__)
#     print(add.__doc__)

# > Fix decorated function docs using functools
# from functools import wraps


# def hello_decorator(func):
#     """Simple decorator function"""

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         """Simple decorator wrapper function"""
#         result = func(*args, **kwargs)
#         return result

#     return wrapper


# @hello_decorator
# def add(a, b):
#     """Simple function that returns sum of two numbers"""
#     return a + b


# @hello_decorator
# def multiply(a, b):
#     """Simple function that returns multiplication of two numbers"""
#     return a * b


# if __name__ == '__main__':

#     help(add)

#     print(add.__name__)
#     print(add.__doc__)

#     output1 = add(2, 2)
#     print('Result:: ', output1)

#     print("=" * 25)
#     help(multiply)
#     print(multiply.__name__)
#     print(multiply.__doc__)
#     output2 = multiply(4, 2)
#     print('Result:: ', output2)

# Article 3: https://sureshdsk.dev/class-based-decorators-in-python

# > Create a class based decorator

# class HelloDecorator:
#     """Simple class decorator"""

#     def __init__(self, func):
#         self.func = func

#     def __call__(self, *args, **kwargs):
#         """Simple class call method"""
#         print(f'Calling {self.func.__name__}')
#         result = self.func(*args, **kwargs)
#         return result


# @HelloDecorator
# def add(a, b):
#     """Simple function that returns sum of two numbers"""
#     return a + b


# if __name__ == '__main__':
#     output1 = add(2, 2)
#     print('Result:: ', output1)
    
#     help(add) # --> prints class definition
#     print(add.__doc__) # --> prints Simple class decorator
#     print(add.__name__) # --> Raises AttributeError

# > Try to fix the doc strings
# from functools import update_wrapper, partial


# class HelloDecorator:
#     """Simple class decorator"""

#     def __init__(self, func):
#         self.func = func
#         # fixes __name__ and __doc__ attributes
#         update_wrapper(self, func)

#     def __get__(self, obj):
#         """Fixes help description"""
#         return partial(self, obj)

#     def __call__(self, *args, **kwargs):
#         """Simple class call method"""
#         print(f'Calling {self.func.__name__}')
#         result = self.func(*args, **kwargs)
#         return result

# @HelloDecorator
# def add(a, b):
#     """Simple function that returns sum of two numbers"""
#     return a + b

# if __name__ == '__main__':
#     output1 = add(2, 2)
#     print('Result:: ', output1)
    
#     help(add) # --> prints class definition
#     print(add.__doc__) # --> prints Simple class decorator
#     print(add.__name__) # --> Raises AttributeError

# Article 4: https://sureshdsk.dev/python-decorators-with-parameters

# > Function based decorator with parameters
# from functools import wraps


# def hello_decorator(num):
#     """Simple decorator function that supports parameters"""

#     def inner_func(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             """Simple decorator wrapper function"""
#             result = func(*args, **kwargs)
#             result = result + num
#             return result
#         return wrapper
#     return inner_func


# @hello_decorator(100)
# def add(a, b):
#     """Simple function that returns sum of two numbers"""
#     return a + b


# @hello_decorator(200)
# def multiply(a, b):
#     """Simple function that returns multiplication of two numbers"""
#     return a * b


# if __name__ == '__main__':
#     output1 = add(2, 2)
#     print('Result:: ', output1)
#     print("=" * 25)

#     output2 = multiply(4, 2)
#     print('Result:: ', output2)

# > Class based decorator with parameters
# from functools import wraps


# class HelloDecorator:
#     """Simple class decorator"""

#     def __init__(self, num):
#         self.num = num

#     def __call__(self, func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             """Simple class call method"""
#             result = func(*args, **kwargs)
#             result = result + self.num
#             return result
#         return wrapper


# @HelloDecorator(100)
# def add(a, b):
#     """Simple function that returns sum of two numbers"""
#     return a + b


# @HelloDecorator(200)
# def multiply(a, b):
#     """Simple function that returns multiplication of two numbers"""
#     return a * b


# if __name__ == '__main__':
#     output1 = add(2, 2)
#     print('Result:: ', output1)

#     output2 = multiply(4, 2)
#     print('Result:: ', output2)

# Article 5: https://sureshdsk.dev/python-decorator-to-measure-execution-time

# > Measure execution time of a function
# from functools import wraps
# import time


# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
#         return result
#     return timeit_wrapper


# @timeit
# def calculate_something(num):
#     """
#     Simple function that returns sum of all numbers up to the square of num.
#     """
#     total = sum((x for x in range(0, num**2)))
#     return total

# if __name__ == '__main__':
#     calculate_something(10)
#     calculate_something(100)
#     calculate_something(1000)
#     calculate_something(5000)
#     calculate_something(10000)

# > Measure execution time of a method inside a class
# from functools import wraps
# import time


# def timeit(func):
#     @wraps(func)
#     def timeit_wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         result = func(*args, **kwargs)
#         end_time = time.perf_counter()
#         total_time = end_time - start_time
#         # first item in the args, ie `args[0]` is `self`
#         print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
#         return result
#     return timeit_wrapper


# class Calculator:
#     @timeit
#     def calculate_something(self, num):
#         """
#         an example function that returns sum of all numbers up to the square of num
#         """
#         total = sum((x for x in range(0, num**2)))
#         return total

#     def __repr__(self):
#         return f'calc_object:{id(self)}'


# if __name__ == '__main__':
#     calc = Calculator()
#     calc.calculate_something(10)
#     calc.calculate_something(100)
#     calc.calculate_something(1000)
#     calc.calculate_something(5000)
#     calc.calculate_something(10000)

# Article 6: https://sureshdsk.dev/memoization-decorator-in-python

# > Factorial of a number

# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)


# if __name__ == '__main__':
#     print(factorial(20))
#     print(factorial(10))
#     print(factorial(15))
#     print(factorial(5))

# > We can optimize this function by caching results for the given value
# from functools import wraps


# def memoize(func):
#     cache = {}

#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         if args not in cache:
#             print(f"Calling for {func.__name__}({args})")
#             cache[args] = func(*args, **kwargs)
#         else:
#             print(f"Using cached result for {func.__name__}({args})")
#         return cache[args]

#     return wrapper


# @memoize
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)


# if __name__ == '__main__':
#     print(factorial(20))
#     print(factorial(10))
#     print(factorial(15))
#     print(factorial(5))

# Article 7: https://sureshdsk.dev/flask-decorator-to-measure-time-taken-for-a-request

# > Measure time taken for a request to complete

import time
from flask import Flask, request, jsonify, current_app, g as app_ctx

app = Flask(__name__)


@app.before_request
def logging_before():
    # Store the start time for the request
    app_ctx.start_time = time.perf_counter()


@app.after_request
def logging_after(response):
    # Get total time in milliseconds
    total_time = time.perf_counter() - app_ctx.start_time
    time_in_ms = int(total_time * 1000)
    # Log the time taken for the endpoint 
    current_app.logger.info('%s ms %s %s %s', time_in_ms, request.method, request.path, dict(request.args))
    return response


@app.get('/')
def home():
    # artificial delay
    time.sleep(1.3)
    return jsonify({'Hello': 'World!!'})


@app.get('/slow-request')
def slow_request():
    # artificial delay
    time.sleep(5)
    return jsonify({'msg': 'slow request'})


if __name__ == '__main__':
    app.run(debug=True)
