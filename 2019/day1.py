#!/usr/bin/env python
import fileinput
import math

def fuel_required(mass: int) -> int:
    return max(math.floor(mass / 3) - 2, 0)

def total_fuel_required(mass: int) -> int:
    next_mass = total_fuel = fuel_required(mass)
    while next_mass > 0:
        next_mass = fuel_required(next_mass)
        total_fuel += next_mass
    return total_fuel

if __name__ == '__main__':
    assert fuel_required(12) == 2
    assert fuel_required(14) == 2
    assert fuel_required(1969) == 654
    assert fuel_required(100756) == 33583

    assert total_fuel_required(14) == 2
    assert total_fuel_required(1969) == 966
    assert total_fuel_required(100756) == 50346

    modules = list(fileinput.input())
    print("Fuel required = {:d}".format(sum(fuel_required(int(module)) for module in modules)))
    print("Total fuel required = {:d}".format(sum(total_fuel_required(int(module)) for module in modules)))
