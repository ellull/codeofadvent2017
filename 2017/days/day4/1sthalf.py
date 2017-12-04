#!/usr/bin/env python
import fileinput
from common import is_valid

print(sum(is_valid(p.strip()) for p in fileinput.input()))

