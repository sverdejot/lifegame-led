import numpy as np

GLIDER = [[0,1], [1,2], [2,0], [2,1], [2,2]]
DIEHAR = [[1,0], [1,1], [2,1], [2,5], [2,6], [2,7], [0,6]]
SPACESHIP1 = [[0,0], [0,3], [1,4], [2,0], [2,4], [3,1], [3,2], [3,3], [3,4]]

def transpose_pattern(pattern, x_offset, y_offset):
    return [[x+x_offset, y+y_offset] for [x,y] in pattern]

def to_matrix_index(pattern):
    return np.transpose(pattern).tolist()