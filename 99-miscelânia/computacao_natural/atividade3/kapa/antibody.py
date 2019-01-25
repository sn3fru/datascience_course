# -*- coding: utf-8 -*-

import random

"""
kapa.antigen

Represents parts of pathogens that can be recognised by antigens

"""

class Antibody:
    def __init__(self, shape = None):
        if shape:
            self.shape = shape
        else:
            self.shape = [random.random() >= .5 for s in range(120)]

        self.affinity = float('inf')
        self.memfinity = float('inf')
