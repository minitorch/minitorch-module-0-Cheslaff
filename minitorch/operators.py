"""Collection of the core mathematical operators used throughout the code base."""

import math

# ## Task 0.1
from typing import Callable, Iterable

#
# Implement basic operations
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$

def mul(x: float, y: float) -> float:
    "$f(x, y) = x * y$"
    return x * y

def id(x: float) -> float:
    "$f(x) = x$"
    return x

def add(x: float, y: float) -> float:
    "$f(x, y) = x + y$"
    return x + y

def neg(x: float) -> float:
    "$f(x) = -x$"
    return -x

def lt(x: float, y: float) -> bool:
    "$f(x, y) = x < y$"
    return x < y

def eq(x: float, y: float) -> bool:
    "$f(x, y) = x == y$"
    return x == y

def max(x: float, y: float) -> float:
    "$f(x, y) = max(x, y)$"
    return x if x > y else y  # decided to avoid built-in function

def is_close(x: float, y: float) -> bool:
    "$f(x, y) = |x - y| < 1e-2$"
    return abs(x - y) < 1e-2

def sigmoid(x: float) -> float:
    "$f(x) = 1 / (1 + e^{-x})$"
    return 1 / (1 + math.exp(-x))

def relu(x: float) -> float:
    "$f(x) = x if x > 0 else 0$"
    return x if x > 0 else 0.

def log(x: float) -> float:
    "$f(x) = log(x)$"
    return math.log(x)

def exp(x: float) -> float:
    "$f(x) = e^x$"
    return math.exp(x)

def inv(x: float) -> float:
    "$f(x) = 1 / x$"
    return 1 / x

def log_back(x: float, y: float) -> float:
    "$(log(x))' * y$"
    return inv(x) * y

def inv_back(x: float, y: float) -> float:
    "$(1 / x)' * y$"
    return -1 / x**2 * y

def relu_back(x: float, y: float) -> float:
    "$ReLU(x)' * y$"
    return (x > 0) * y



# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists

def negList():
    pass

def addLists():
    pass

def prod():
    pass


# TODO: Implement for Task 0.3.
