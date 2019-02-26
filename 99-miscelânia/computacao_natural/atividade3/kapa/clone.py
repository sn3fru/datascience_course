# -*- coding: utf-8 -*-

"""
kapa.clone

Creates a number of clones of an antibody, proportional to its affinity

"""

import copy

def clone_antibody(antibody, clone_multiplier, num_antigens, affinity_rank):
    num_clones = int(round(clone_multiplier * num_antigens / float(affinity_rank)))
    
    return [copy.deepcopy(antibody) for i in xrange(num_clones)]
