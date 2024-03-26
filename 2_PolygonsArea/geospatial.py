# Classes and methods for geospatial algorithms based on points with x, y coordinates

# for GEO877 Spatial Algorithms
# - requires Python 3.6 or later (or replace f-string with older print format)
# - Point distance measures return results in metres (or assume metres)

# release history:
# 2021-03-27, v1.0: updated version of points.py (v1.0) for solution 1 (comparing distance measures)
# author:  Sharon Richardson
# version: 1.0

# 2022-03-25, v2.1: Modified Sharon's original polygon code slightly
# author:  Ross Purves
# version: 2.02

# --------------------------

from numpy import sqrt, radians, arcsin, sin, cos

# class and methods for a geometric point
# =======================================
from numpy import sqrt

class Point():
    # initialise
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
    
    # representation
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

        # Test for equality between Points
    def __eq__(self, other): 
        if not isinstance(other, Point):
            # don't attempt to compare against unrelated types
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # We need this method so that the class will behave sensibly in sets and dictionaries
    def __hash__(self):
        return hash((self.x, self.y))
    
    # calculate Euclidean distance between two points
    def distEuclidean(self, other):
        return sqrt((self.x-other.x)**2 + (self.y-other.y)**2)
    
    # calculate Manhattan distance between two points
    def distManhattan(self, other):
        return abs(self.x-other.x) + abs(self.y-other.y)

    # Haversine distance between two points on a sphere - requires lat/lng converted to radians
    def distHaversine(self, other):
        r = 6371000  # Earth's radius in metres (will return result in metres)
        phi1 = radians(self.y) # latitudes
        phi2 = radians(other.y)
        lam1 = radians(self.x) # longitudes
        lam2 = radians(other.x)

        d = 2 * r * arcsin(sqrt(sin((phi2 - phi1)/2)**2 + 
                                      cos(phi1) * cos(phi2) * sin((lam2 - lam1)/2)**2))
        return d   
    
# FOR GROUPS OF POINTS

# data provided should be as an array of points with x, y coordinates.

# class for a group of Points, assumes initial data is unsorted, spatially
class PointGroup(): 
    # initialise
    def __init__(self, data=None, xcol=None, ycol=None):
        self.points = []
        self.size = len(data)
        for d in data:
            self.points.append(Point(d[xcol], d[ycol]))
    
    # representation
    def __repr__(self):
        return f'PointGroup containing {self.size} points' 
 
    # create index of points in group for referencing
    def __getitem__(self, key):
        return self.points[key]
    

# Polygon class for polygons, assumes initial data is in a spatially sorted order
class Polygon(PointGroup):  
    # initialise
    def __init__(self, data=None, xcol=None, ycol=None):
        self.points = []
        self.size = len(data)
        for d in data:
            self.points.append(Point(d[xcol], d[ycol]))
    
    # representation
    def __repr__(self):
        return f'Polygon PointGroup containing {self.size} points' 
  
    # test if polygon is closed: first and last point should be identical
    def isClosed(self):
        start = self.points[0]
        end = self.points[-1]
        return start == end

    def removeDuplicates(self):
        oldn = len(self.points)
        self.points = list(dict.fromkeys(self.points)) # Get rid of the duplicates
        self.points.append(self.points[0]) # Our polygon must have one duplicate - we put it back now
        n = len(self.points)
        print(f'The old polygon had {oldn} points, now we only have {n}.')