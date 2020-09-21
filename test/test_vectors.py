#!/usr/bin/env python3

import unittest
import math
import sys 
import io

from vectorsnek import * 

class TestVectors(unittest.TestCase):
    def test____str__(self):
        v1 = Vector([4,9,1])
        self.assertEqual(str(v1), "(4, 9, 1)")

    def test___repr__(self):
        v1 = Vector([4,9,1])
        # change output buffer
        old_stdout = sys.stdout
        sys.stdout = buffer = io.StringIO()
        print(v1)
        # restore output buffer
        sys.stdout = old_stdout
        # test if output representation worked
        self.assertEqual(buffer.getvalue(), "(4, 9, 1)\n")

    def test_magnitude(self):
        v1 = Vector([3,-4])
        self.assertEqual(v1.magnitude(), 5) 

    def test_dot(self):
        v1 = Vector([10, 2, 3])
        v2 = Vector([2, 3, 1])
        self.assertEqual(v1.dot(v2), 29)
        # magnitude-dot product identity
        v3 = Vector([4,-2,5])
        self.assertAlmostEqual(v3.dot(v3), v3.magnitude()**2)

    def test_scalar_multiplication(self):
        v1 = Vector([2,-3])
        self.assertEqual(v1.scalar_multiplication(5), Vector([10, -15]))

    def test__add__(self):
        v1 = Vector([-5, 2])
        v2 = Vector([1, -1])
        self.assertEqual(v1 + v2, Vector([-4, 1]))

    def test___sub__(self):
        v1 = Vector([0, 5, 10])
        v2 = Vector([-3, 4, 8])
        self.assertEqual(v1 - v2, Vector([3, 1, 2]))

    def test____mul__(self):
        # scalar multiplication
        v1 = Vector([2, -1])
        s1 = 6
        self.assertEqual(v1 * s1, Vector([12, -6]))
        # dot product
        v2 = Vector([3, 2])
        self.assertAlmostEqual(v1 * v2, 4)

    def test___rmul_(self):
        v1 = Vector([1, -2])
        s1 = 3
        self.assertEqual(s1 * v1, Vector([3, -6]))

    def test___ne__(self):
        v1 = Vector([2, -1])
        v2 = Vector([-2, 1])
        self.assertNotEqual(v1, v2)

    def test___iadd__(self):
        v1 = Vector([1, -6])
        v2 = Vector([-2, 1])
        v1 += v2
        self.assertEqual(v1, Vector([-1, -5]))

    def test___isub__(self):
        v1 = Vector([3, 9])
        v2 = Vector([1, 8])
        v1 -= v2
        self.assertEqual(v1, Vector([2, 1]))

    def test___imul__(self):
        v1 = Vector([1, -6])
        v2 = Vector([-2, 1])
        # dot product
        v1 *= v2
        self.assertAlmostEqual(v1, -8)
        # scalar multiplication
        v2 *= -2
        self.assertEqual(v2, Vector([4, -2]))

    def test___pos__(self):
        v1 = Vector([1,2])
        self.assertEqual(+v1, v1)

    def test___neg__(self):
        v1 = Vector([4,7,1])
        self.assertEqual(-v1, Vector([-4, -7, -1]))

    def test___round__(self):
        v1 = Vector([2.51, -3.2])
        self.assertEqual(round(v1, 0), Vector([3.0, -3.0]))

    def test___floor__(self):
        v1 = Vector([2.51, -3.2])
        self.assertEqual(math.floor(v1), Vector([2.0, -4.0]))

    def test___ceil__(self):
        v1 = Vector([2.51, -3.2])
        self.assertEqual(math.ceil(v1), Vector([3.0, -3.0]))

    def test___trun__(self):
        v1 = Vector([2.51, -3.2])
        self.assertEqual(math.trunc(v1), Vector([0.51, 0.2]))

    def test___len__(self):
        v1 = Vector([1,2,3,4])
        self.assertEqual(len(v1), 4)

    def test___getitem__(self):
        v1 = Vector([5, 6, -7, 3])
        self.assertEqual(v1[2], -7)

    def test___setitem__(self):
        v1 = Vector([5, 6, -7, 3])
        v1[1] = 10
        self.assertEqual(v1, Vector([5, 10, -7, 3]))

    def test___delitem__(self):
        v1 = Vector([5, 6, -7, 3])
        del v1[0]
        self.assertEqual(v1, Vector([6, -7, 3]))

    def test___iter__(self):
        l1 = [5, 6, -7, 3]
        v1 = Vector(l1)
        for a, b in zip(l1, v1):
            self.assertEqual(a, b)

    def test___reversed__(self):
        l1 = [5, 6, -7, 3]
        v1 = Vector([5, 6, -7, 3])
        for a, b in zip(reversed(l1), reversed(v1)):
            self.assertEqual(a, b)

class TestGlobalsFunctions(unittest.TestCase):
    
    def test___cross_product(self):
        # computation test
        v1 = Vector([2, -5, 1])
        v2 = Vector([-8, 2, -2])
        self.assertEqual(cross_product(v1, v2), Vector([8, -4, -36]))
        # ValueError test
        v3 = Vector([6,-2])
        v4 = Vector([0, 1])
        with self.assertRaises(ValueError):
            # wrong dimension for cross product
            v5 = cross_product(v3, v4)
        # AssertionErorr test
        with self.assertRaises(AssertionError):
            # different dimension vectors
            v4 = cross_product(v2, v3)

if __name__ == '__main__':
    unittest.main()