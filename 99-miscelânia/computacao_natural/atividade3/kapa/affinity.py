# -*- coding: utf-8 -*-

"""
kapa.affinity

Calculates the similarity of an antibody to antigen using the hamming distance

"""

def calculate_affinity(antigen, antibody):
    differences = 0
    
    for i in xrange(len(antigen.shape)):
        if antigen.shape[i] != antibody.shape[i]:
            differences += 1
    
    return differences
