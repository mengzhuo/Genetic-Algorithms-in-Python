#!/usr/bin/env python
# encoding: utf-8

TEST_MAP = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,1,0,0,0,0,0,1,1,1,0,0,0,1],
[5,0,0,0,0,0,0,0,1,1,1,0,0,0,1],
[1,0,0,0,1,1,1,0,0,1,0,0,0,0,1],
[1,0,0,0,1,1,1,0,0,0,0,0,1,0,1],
[1,1,0,0,1,1,1,0,0,0,0,0,1,0,1],
[1,0,0,0,0,1,0,0,0,0,1,1,1,0,1],
[1,0,1,1,0,0,0,1,0,0,0,0,0,0,8],
[1,0,1,1,0,0,0,1,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] ]

class Grid(object):

    __slots__ = ['x', 'y', 'point']

    def __init__(self, x, y, point):

        self.x = x
        self.y = y
        self.point = point
    
    def __str__(self):
        return "{0.x}:{0.y}|{0.point}".format(self)
    
    __repr__ = __unicode__ = __str__

class Map(object):

    def __init__(self, grid_array):
        
        row = grid_array[0]
        self._map = [[0 for x in row] for y in grid_array]
         
        for row in xrange(len(grid_array)):
            for col, val in enumerate(grid_array[row]):
                self._map[row][col] = Grid(col, row, val)

    def __unicode__(self):
        return self.__str__()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        
        result = ""

        for row in self._map:
            result += "{0}\n".format(", ".join([str(c.point) for c in row]))

        return result

    def __getitem__(self, k):
        return self._map[k]
