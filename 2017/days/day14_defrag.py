#!/usr/bin/env python
import sys
from day14 import Grid
from day14_extra import Exporter
from PIL import Image, ImageDraw


class DefragExporter(Exporter):
    def start(self, grid):
        for y in xrange(128):
            for x in xrange(128):
                group = grid.get(x, y)
                if group is not None:
                    self.draw.ellipse(self._ellipse(x, y), fill = 'cornflowerblue' if group else 'cyan', outline = 'black')
        self.save()

    def next(self, grid):
        self.start(grid)

    def flood(self, blocks, group):
        color = 'limegreen'
        for (x, y) in blocks:
            self.draw.ellipse(self._ellipse(x, y), fill = color, outline = 'black')
        self.save()

grid = Grid(sys.argv[1], DefragExporter())

