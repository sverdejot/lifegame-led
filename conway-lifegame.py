import board
import numpy as np
from random import sample
from patterns import GLIDER, DIEHARD, SPACESHIP1, transpose_pattern, to_matrix_index
from generation import Generation
from neopixel import NeoPixel

ON = (128, 128, 128)
OFF = (0, 0, 0)

if __name__ == '__main__':
    # initial generation
    gen = Generation(rows=8, cols=64, initial=True)

    led = NeoPixel(board.D18, 512, auto_write=False)
    cycles = 0

    while True:
        try:
            # each 300 cycles, revive some random cells to avoid stationary states
            if cycles == 300:
                gen.spontaneos_generation()

            # write led data
            for px, st in enumerate(gen.serialize_matrix_1d()):
                led[px] = ON if st else OFF

            led.show()
            cycles += 1

            gen = gen.next_generation()
        except KeyboardInterrupt:
            # shut-down every led
            led.fill(color=0)
            led.show()
            sys.exit(0)