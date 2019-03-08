#!/usr/bin/env python
# -*- coding: utf-8 -*-

def splitSArgs(args):
    argsList = list(args)
    tmp_list = []
    for item in argsList :
        tmp_list.append(item + ",")
    return tmp_list
