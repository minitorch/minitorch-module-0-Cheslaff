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


"""HIGH-ORDER FUNCTIONS"""
# Personal Note: Callable[[float], float] takes one float & returns float
def map(function: Callable[[float], float]) -> Callable[[Iterable[float]], Iterable[float]]:
    """
    map function - Higher-order.

    Arguments:
        function: Function being mapped to iterable
    Returns:
        a function, which takes lst argument & applies function to each element
    """
    
    return lambda lst: [function(x) for x in lst]


def zipWith(zip_key: Callable[[float, float], float]) -> Callable[[Iterable[float], Iterable[float]], Iterable[float]]:
    """
    zipWith function - High-order.

    Arguments:
        zip_key: function used for zipping two iterables
    Returns:
        a function, which zips two Iterables using zip_key
    """

    return lambda lst1, lst2: [zip_key(a, b) for a, b in zip(lst1, lst2)]


def reduce(function: Callable[[Iterable[float]], float]) -> Callable[[Iterable[float]], float]:
    """
    reduce function - High-order.

    Arguments:
        function: function used to reduce Iterable to one float scalar.
    Returns:
        a function, which takes array and reduces it using function argument.
    """
    return lambda lst: function(lst)


"""COMMON FUNCTIONS"""
def negList(lst: Iterable[float]) -> Iterable[float]:
    """
    negList function.
    Arguments:
        lst: Iterable to which neg function (see above) will be mapped.
    Returns:
        an Iterable object where each item was multiplied by -1
    """
    negative_map = map(neg)
    return negative_map(lst)


def addLists(lst1: Iterable[float], lst2: Iterable[float]) -> Iterable[float]:
    """
    addLists function.
    Arguments:
        lst1: Iterable term 1
        lst2: Iterable term 2
    Returns:
        an Iterable, which is a result of elementwise addition of two lists.
    """
    zip_sum = zipWith(lambda a, b: a + b)
    return zip_sum(lst1, lst2)


def sum(lst: Iterable[float]) -> float:
    """
    sum function.
    Arguments:
        lst: List to be reduced using summation accross it.
    Returns:
        scalar value, which is a sum of Iterable.
    """
    def sum_function(lst: Iterable[float]):
        out = 0
        for item in lst:
            out += item
        return out
    reduce_sum = reduce(sum_function)
    return reduce_sum(lst)
    

def prod(lst: Iterable[float]) -> float:
    """
    prod function.
    Arguments:
        lst: Iterable to be reduced using multiplication accross it.
    Returns:
        scalar value, which is a product of Iterable
    """
    def mul_function(lst: Iterable[float]):
        out = 1
        for item in lst:
            out *= item
        return out
    reduce_prod = reduce(mul_function)
    return reduce_prod(lst)
