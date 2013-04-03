#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c): 
    # DELETE 'PASS' AND WRITE THIS CODE
    list = [a, b, c]
    list.sort()
    sum = a + b + c 
    max = list[-1:][0]
    #print list, sum, max 
    if (a >= 1 and b >= 1 and c >= 1) and ((sum) > max * 2):
        if (a == b) and (b == c): 
            return 'equilateral' 
        elif (a != b) and (b !=c) and (a != c): 
            return 'scalene'
        else:
            return 'isosceles'
    else:
    #    print "BOO"
        raise TriangleError

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
