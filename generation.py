import numpy as np
from random import sample

class Generation:
    def __init__(self, rows=8, cols=32, percent_alive_cells=None, initial=False):
        self.rows = rows
        self.cols = cols
        self.matrix = np.zeros((rows, cols))

        if initial:
            self.initialize_state(percent_alive_cells or 30)

    def initialize_state(self, percent_alive_cells):
        # set some random cells to alive
        self.matrix[np.transpose(sample(list(np.ndindex(self.rows, self.cols)), int(round((self.rows*self.cols*percent_alive_cells)/100, 0)))).tolist()] = 1

    def get_state(self, x, y):
        # compute each neighbour assuming we're in a toroidal space (first row's cell are neigbour of last row's cells)
        # good luck trying to understand this
        neighbours = np.delete(self.matrix[np.ix_(*((z-1, z, z+1-S) for z,S in zip((y,x), self.matrix.shape)))], 4)
        return 1 if (self.matrix[y, x] and sum(neighbours) >= 2 and sum(neighbours) <= 3) or sum(neighbours) == 3 else 0 
        
    def next_generation(self):
        # compute each cell next state and stores it in a new generation instance
        next_gen = Generation(rows=self.rows, cols=self.cols)
        next_gen.matrix = np.array([[self.get_state(x, y) for x in range(self.cols)] for y in range(self.rows)])
        return next_gen

    def check_stationary(self, prev_gen):
        # deprecated - was used to check stationary states
        return 1 if np.array_equal(self.matrix, prev_gen.matrix) else 0

    def spontaneos_generation(self, new_alive_cells=None):
        # pick some random death cells (usually, 10%) and revive them to avoid stationary states
        self.matrix[np.transpose(sample(np.transpose(np.where(self.matrix == 0)).tolist(), new_alive_cells if new_alive_cells else int(round((self.rows*self.cols)/10, 0)))).tolist()] = 1

    def serialize_matrix_1d(self):
        # as the matrix is compound of lineal-connected led, each odd row must be reversed in order to keep the layout
        self.matrix[:, 1::2] = self.matrix[::-1, 1::2]
        return np.transpose(self.matrix).flatten()