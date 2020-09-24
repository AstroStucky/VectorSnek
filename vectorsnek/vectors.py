#  --------------------------------------------------------------------------
#   PROJECT       : VectorSnek
#   AUTHOR        : Thomas R. Stucky
#   FILENAME      : vectors.py
#   CREATED       : 2020-09-20
#   TAB SIZE      : 4
#   DESCRIPTION   : Python module that defines vectors and vector math
#
#  -------------------------GPL 3.0 LICENSE-----------------------------------
#  Copyright (C) 2020 Thomas R. Stucky
# 
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
# 
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
# 
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>. 
#  ---------------------------------------------------------------------------

import math

__all__ = ['Vector']

class Vector(object):   

    # TODO:
    #  1. support cross product for 7 dimensions, and more if they exist
    #  2. support matrix-vector multiplication

    def __init__(self, value):
        if isinstance(value, Vector):
            self._arr = value._arr
            self._dim = value._dim
        else:        
            self._arr = list(value)
            self._dim = len(self._arr)

    def __str__(self):
        return str(tuple(self._arr))

    def __repr__(self):
        return self.__str__()

    ### Common accessors and setters for vectors
    ## cartesian up to 4 dimensions (x, y, z, w)
    @property
    def x(self):
        return self[0]
    @x.setter
    def x(self, value):
        self[0] = value

    @property
    def y(self):
        return self[1]
    @y.setter
    def y(self, value):
        self[1] = value

    @property
    def z(self):
        return self[2]
    @z.setter
    def z(self, value):
        self[2] = value

    @property
    def w(self):
        return self[3]
    @w.setter
    def w(self, value):
        self[3] = value

    ### Factories for common vectors 

    @classmethod
    def zeros(cls, dimension):
        if dimension < 0:
            raise ValueError('Dimension must be greater than 0')
        return Vector([0] * dimension)

    ### Common vector operations

    def norm(self, p):
        if p < 1:
            raise ValueError("The p-norm is not defined for p < 1")
        if p == math.inf:
            return max([abs(x) for x in self])
        sum_ = 0
        for a in self._arr:
            sum_ += abs(a)**p
        return sum_**(1.0/p)

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def scalar_multiply(self, other):
        result = Vector([] * self._dim)
        for a, c in zip(self._arr, result._arr):
            c = a * other
        return result

    ## vector products

    def dot(self, other):
        if self._dim != other._dim:
            raise ValueError("Vectors must be of the same dimension")
        sum_ = 0
        for a, b in zip(self._arr, other._arr):
            sum_ += a * b
        return sum_
        
    def cross(self, other):
        if self._dim != other._dim:
            raise ValueError("Vectors must be of the same dimension.")
        arr = list()
        if self._dim == 3:
            arr.append(self.y * other.z - self.z * other.y)
            arr.append(self.z * other.x - self.x * other.z)
            arr.append(self.x * other.y - self.y * other.x)
            return Vector(arr)
        else:
            raise ValueError("Unsupported/undefined dimension for the cross product.")
    
    ### operator overloading
 
    ## binary

    def __add__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self._arr, other._arr, result._arr):
            c = a + b
        return result

    def __sub__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self._arr, other._arr, result._arr):
            c = a - b
        return result

    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            # LHS scalar multiplication
            return self.scalar_multiply(other)

    # RHS scalar multiplication
    def __rmul__(self, scalar):
        return self.scalar_multiply(scalar)

    ## comparison

    def __eq__(self, other):
        return all([a == b for a, b in zip(self._arr, other._arr)])

    def __ne__(self, other):
        return ~self.__eq__(other)

    ## augmented assignment

    def __iadd__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self._arr, other._arr, result._arr):
            c = a + b
        return result

    def __isub__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self._arr, other._arr, result._arr):
            c = a - b
        return result

    def __imul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scalar_multiply(other)

    ## unary

    def __pos__(self):
        # no change
        return self

    def __neg__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self._arr, result._arr):
            b = -a
        return result

    def __round__(self, n):
        result = Vector([] * self._dim)
        for a, b in zip(self._arr, result._arr):
            b = math.round(a, n)
        return result

    def __floor__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self._arr, result._arr):
            b = math.floor(a)
        return result

    def __ceil__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self._arr, result._arr):
            b = math.ceil(a)
        return result

    def __trunc__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self._arr, result._arr):
            b = math.trunc(a)
        return result

    ### container definitions

    def __len__(self):
        return self._dim

    def __getitem__(self, key):
        return self._arr[key]

    def __setitem__(self, key, value):
        self._arr[key] = value

    def __delitem__(self, key):
        del self._arr[key]
        self._dim = len(self._arr)

    def __iter__(self):
        return iter(self._arr)

    def __reversed__(self):
        return reversed(self._arr)