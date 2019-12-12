#!/usr/bin/env python3
import fileinput
from collections import Counter

def image_checksum(counter):
    return counter['1'] * counter['2']

def render_pixel(pixels):
    for pixel in list(pixels):
        if pixel == '0':
            return ' '
        elif pixel == '1':
            return '#'

def print_image(image, width, height):
    for i in range(height):
        print("".join(image[width * i: width * (i + 1)]))

if __name__ == "__main__":
    width, height = 25, 6
    image_size = width * height

    image = fileinput.input().readline()

    layers = [image[start:start + image_size] for start in range(0, len(image), image_size)]
    
    print("Image checksum: {:d}".format(image_checksum(min([Counter(layer) for layer in layers], key=lambda counter: counter['0']))))

    print_image(list(map(render_pixel, zip(*layers))), width, height)
