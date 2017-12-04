#!/usr/bin/env python
import fileinput
from common import is_valid_v2

print(sum(is_valid_v2(p.strip()) for p in fileinput.input()))

