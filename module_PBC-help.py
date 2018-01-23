#module_PBC
import numpy as np

## PBC stands for Periodic Boundary Conditions. ##
## in 2D, it would be equivalent to assuming the plane has been folded into a torus (donut-like shape)
## in 3D, the equivalent torus is only visible in 4D (i.e. needs 4D embedding)
## this trick is used in simulations to avoid the problems and peculiarities relative to fixed boundaries.

## concretely,
## if an atom is at x=-4 and its neihbor at x=4, their distance is not 8, but Lx-8,
## because the shortest path goes through the walls.

def applyPBC_pair_func(x1, x2):
    '''
    convert a pair of coordinates x1,x2 into its PBC-compatible value
    '''
    Lx = 9.4103602888102831
    dist = x1-x2
    if   dist > Lx/2.0:
        dist -= Lx
    elif dist < -Lx/2.0:
        dist += Lx
    return dist

def applyPBC_vector_func(displacements):
    '''
    convert an array "displacement" into its PBC-compatible value
    '''
    Lx = 9.4103602888102831
    displacements[(displacements >  Lx/2.0)] -= Lx
    displacements[(displacements <- Lx/2.0)] += Lx
    return displacements
