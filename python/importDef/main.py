#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functions
import sys

args = sys.argv

list = functions.splitSArgs(args[1])

for item in list:
    print(item),
