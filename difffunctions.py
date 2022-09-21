
import math


class function:


    def __init__(self, f, df):
        self.f = f
        self.df = df

    def __call__(self, f):
        if isinstance(f, function):
            # we are composing two functions!
            return function(lambda x: self(f(x)), lambda x: self.d(f(x)) * f.d(x))
        else:
            return self.f(f)

    def d(self, x):
        return self.df(x)

    def __add__(self, other : "function"):
        if isinstance(other, function):
            return function(lambda x: self(x) + other(x), lambda x: self.d(x) + other.d(x))
        else:
            return function(lambda x: self(x) + other, lambda x: self.d(x))

    def __sub__(self, other : "function"):
        if isinstance(other, function):
            return function(lambda x: self(x) - other(x), lambda x: self.d(x) - other.d(x))
        else:
            return function(lambda x: self(x) - other, lambda x: self.d(x))
    
    def __mul__(self, other : "function"):
        if isinstance(other, function):
            return function(lambda x: self(x) * other(x), lambda x: self.d(x) * other(x) + self(x) * other.d(x))
        else:
            return function(lambda x: self(x) * other, lambda x: self.d(x) * other)
    
    def __truediv__(self, other : "function"):
        if isinstance(other, function):
            return function(lambda x: self(x) / other(x), lambda x: (self.d(x) * other(x) - self(x) * other.d(x)) / other(x)**2)
        else:
            return function(lambda x: self(x) / other, lambda x: self.d(x) / other)

    def __pow__(self, other : "function"):
        if isinstance(other, function):
            return function(lambda x: self(x) ** other(x), lambda x: other(x) * self(x)**(other(x)-1) * self.d(x) + math.log(self(x)) * self(x)**other(x) * other.d(x))
        else:
            return function(lambda x: self(x) ** other, lambda x: other * self(x)**(other-1) * self.d(x))


    def __neg__(self):
        return function(lambda x: -self(x), lambda x: -self.d(x))

    def __radd__(self, other : "function"):
        return other.__add__(self)

    def __rsub__(self, other : "function"):
        return other.__sub__(self)

    def __rmul__(self, other : "function"):
        return other.__mul__(self)
    
    def __rtruediv__(self, other : "function"):
        return other.__truediv__(self)

    def __rpow__(self, other : "function"):
        return other.__pow__(self)

x = function(lambda x: x, lambda x: 1)

sin = function(lambda x: math.sin(x), lambda x: math.cos(x))

cos = function(lambda x: math.cos(x), lambda x: -math.sin(x))

