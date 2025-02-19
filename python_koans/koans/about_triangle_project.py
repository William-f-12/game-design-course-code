#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to write the triangle method in the file 'triangle.py'
from .triangle import *

class AboutTriangleProject(Koan):
    def test_equilateral_triangles_have_equal_sides(self): # equilateral
        self.assertEqual(None, triangle(2, 2, 2))
        self.assertEqual(None, triangle(10, 10, 10))

    def test_isosceles_triangles_have_exactly_two_sides_equal(self): # isosceles
        self.assertEqual(None, triangle(3, 4, 4))
        self.assertEqual(None, triangle(4, 3, 4))
        self.assertEqual(None, triangle(4, 4, 3))
        self.assertEqual(None, triangle(10, 10, 2))

    def test_scalene_triangles_have_no_equal_sides(self): # scalene
        self.assertEqual(None, triangle(3, 4, 5))
        self.assertEqual(None, triangle(10, 11, 12))
        self.assertEqual(None, triangle(5, 4, 2))
