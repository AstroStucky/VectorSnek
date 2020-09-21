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

class Vector:
    def __init__(self, value):
        if isinstance(value, Vector):
            self.arr = value.arr
            self._dim = len(self.arr)
        else:        
            self.arr = list(value)
            self._dim = len(self.arr)

    def __setattr__(self, name, value):
        if name == 'arr':
            self.__dict__['_dim'] = len(value)
        self.__dict__[name] = value

    def __str__(self):
        return str(tuple(self.arr))

    def __repr__(self):
        return self.__str__()

    def magnitude(self):
        return math.sqrt(self.dot(self))

    def dot(self, other):
        sum_ = 0
        for a, b in zip(self.arr, other.arr):
            sum_ += a * b
        return sum_

    def scalar_multiplication(self, other):
        result = Vector([] * self._dim)
        for a, c in zip(self.arr, result.arr):
            c = a * other
        return result
    
    ### operator overloading
    ## binary

    def __add__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self.arr, other.arr, result.arr):
            c = a + b
        return result

    def __sub__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self.arr, other.arr, result.arr):
            c = a - b
        return result

    def __mul__(self, other):
        # TODO: support matrix multiplication
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            # LHS scalar multiplication
            return self.scalar_multiplication(other)

    # RHS scalar multiplication
    def __rmul__(self, scalar):
        return self.scalar_multiplication(scalar)

    ## comparison

    def __eq__(self, other):
        return all([a == b for a, b in zip(self.arr, other.arr)])

    def __ne__(self, other):
        return ~self.__eq__(other)

    ## augmented assignment

    def __iadd__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self.arr, other.arr, result.arr):
            c = a + b
        return result

    def __isub__(self, other):
        result = Vector([] * self._dim)
        for a, b, c in zip(self.arr, other.arr, result.arr):
            c = a - b
        return result

    def __imul__(self, other):
        if isinstance(other, Vector):
            return self.dot(other)
        else:
            return self.scalar_multiplication(other)

    ## unary

    def __pos__(self):
        # no change
        return self

    def __neg__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self.arr, result.arr):
            b = -a
        return result

    def __round__(self, n):
        result = Vector([] * self._dim)
        for a, b in zip(self.arr, result.arr):
            b = math.round(a, n)
        return result

    def __floor__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self.arr, result.arr):
            b = math.floor(a)
        return result

    def __ceil__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self.arr, result.arr):
            b = math.ceil(a)
        return result

    def __trunc__(self):
        result = Vector([] * self._dim)
        for a, b in zip(self.arr, result.arr):
            b = math.trunc(a)
        return result

    ### container defines

    def __len__(self):
        return self._dim

    def __getitem__(self, key):
        return self.arr[key]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def __delitem__(self, key):
        del self.arr[key]
        self._dim = len(self.arr)

    def __iter__(self):
        return iter(self.arr)

    def __reversed__(self):
        return reversed(self.arr)

def dot_product(v1, v2):
    return v1 * v2

def cross_product(v1, v2):
    assert len(v1) == len(v2), "Vectors must be of the same dimension"
    arr = list()
    if len(v1) == 3:
        arr.append(v1[1] * v2[2] - v1[2] * v2[1])
        arr.append(v1[2] * v2[0] - v1[0] * v2[2])
        arr.append(v1[0] * v2[1] - v1[1] * v2[0])
        return Vector(arr)
    else:
        raise ValueError("Vectors are of an unsupported dimension for the cross product")
