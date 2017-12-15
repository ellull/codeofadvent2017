#!/usr/bin/env python
import sys
from day14 import Grid
from PIL import Image, ImageDraw


class Exporter(object):
    PALETTE = [(158,1,66),(213,62,79),(244,109,67),(253,174,97),(254,224,139),(255,255,191),(230,245,152),(171,221,164),(102,194,165),(50,136,189),(94,79,162)]

    def __init__(self, block_size = 8):
        self.image = Image.new('RGB', (128 * block_size, 128 * block_size), color = (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)
        self.block_size = block_size
        self.images = 0

    def start(self, grid):
        for y in xrange(128):
            for x in xrange(128):
                group = grid.get(x, y)
                if group is not None:
                    self.draw.ellipse(self._ellipse(x, y), fill = 'black')
        self.save()

    def next(self, grid):
        pass

    def flood(self, blocks, group):
        for (x, y) in blocks:
            self.draw.ellipse(self._ellipse(x, y), fill = self.PALETTE[group % len(self.PALETTE)])
        self.save()

    def save(self):
        self.image.save('grid/%05d.png' % self.images)
        self.images += 1

    def _ellipse(self, x, y):
        return map(lambda i: i * self.block_size, (x, y, x + 1, y + 1))

if __name__ == '__main__':
    grid = Grid(sys.argv[1], Exporter())

