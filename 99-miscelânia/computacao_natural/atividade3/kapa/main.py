# -*- coding: utf-8 -*-

"""
kapa.main

Contains main CLONALG function

"""

from .clone    import clone_antibody
from .affinity import calculate_affinity
from .mutate   import mutate_antibody
from .antibody import Antibody
import random
import operator
import sys
import copy

def print_shape(shape):
    x = -1
    output = ''
    for i in range(12):
        for j in range(10):
            x += 1
            if shape[x]:
                output += 'X'
            else:
                output += ' '
        output += '\n'
    print (output)


def kapa(
    antigens,             # Set of antigens to be recognised
    antibodies,           # Set of antibodies to be trained
    generations,          # Number of times to run algorithm over each antigen
    num_clone_antibodies, # Number of highest affinity antigens to clone
    num_kill_antibodies,  # Number of lowest affinity antigens to kill
    clone_multiplier      # Rate to clone an antibody relative to its affinity (how good it is)
    ):
    # Antibodies preserved between antigen runs
    memory_antibodies = random.sample(antibodies, len(antigens))
    affinity_graph    = []
    early_termination = False

    # Ensures memory antigens aren't killed
    num_kill_antibodies = min(num_kill_antibodies, len(antibodies) - len(antigens))

    for g in xrange(generations):
        if early_termination or all(antibody.memfinity == 0 for antibody in memory_antibodies):
            if not early_termination:
                print ('Terminating early at generation {0}'.format(g))
                early_termination = True

            for antigen_key in range(len(antigens)):
                affinity_graph.append({'key' : antigen_key, 'generation' : g, 'affinity' : 0})
            continue
        #print (g)
        """
        1. Select antigen and present it all antibodies
        """
        for antigen_key, antigen in enumerate(antigens):
            """
            2. Evaluate affinity of each antibody to current antigen
            """
            for antibody in antibodies:
                antibody.affinity = calculate_affinity(antigen, antibody)

            """
            3. Select number of highest affinity antibodies to clone (specified in $num_clone_antibodies)
            """
            antibodies.sort(key=lambda antibody: antibody.affinity) # Sorts by affinity

            num_antibodies = len(antibodies)
            affinity_rank  = 0
            clones         = []

            for antibody in antibodies[:num_clone_antibodies]:
                """
                4. Clone selected antibodies proportionally to their affinity
                """
                affinity_rank += 1

                antibody_clones = clone_antibody(antibody, clone_multiplier, num_antibodies, affinity_rank)

                """
                5. Mutate clones inversely proportional to their affinity
                  (Better affinity = less mutation)
                """
                for antibody in antibody_clones:
                    clones.append(mutate_antibody(antibody, affinity_rank))

            """
            6. Determine affinity of each matured (mutated) clone
            """
            for antibody in clones:
                antibody.affinity = calculate_affinity(antigen, antibody)

            """
            7. Replace memory antibody for current antigen if best clone beats current memory antibody
            """
            best_antibody = min(clones, key=operator.attrgetter('affinity'))

            if best_antibody.affinity < memory_antibodies[antigen_key].memfinity:
                old_antibody = memory_antibodies[antigen_key]
                antibodies.remove(old_antibody)

                best_antibody.memfinity = best_antibody.affinity
                antibodies.append(best_antibody)
                memory_antibodies[antigen_key] = best_antibody

            affinity_graph.append({'key' : antigen_key, 'generation' : g, 'affinity' : memory_antibodies[antigen_key].memfinity})

            """
            8. Replace number of worst antibodies (specified in $num_kill_antibodies)
            """
            if num_kill_antibodies > 0:
                antibodies.sort(key=lambda antibody: antibody.affinity)

                num_to_kill = num_kill_antibodies

                for i in range(len(antibodies) - 1, -1, -1):
                    if num_to_kill == 0:
                        break

                    if antibodies[i] not in memory_antibodies:
                        num_to_kill -= 1
                        del antibodies[i]

                antibodies = antibodies + [Antibody() for _ in range(num_kill_antibodies)]

    return affinity_graph
