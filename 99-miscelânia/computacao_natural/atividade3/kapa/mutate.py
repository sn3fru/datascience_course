# -*- coding: utf-8 -*-

"""
kapa.mutate

Mutates an antibody inversely proportional to its affinity
(Bad antigens get more mutations)

"""

import random

def mutate_antibody(antibody, affinity_rank):
    num_mutations = min(affinity_rank, len(antibody.shape)) # TODO: Replace
    
    mutation_keys = random.sample(range(len(antibody.shape)), num_mutations)
    
    for key in mutation_keys:
        antibody.shape[key] = not antibody.shape[key]
    
    return antibody
