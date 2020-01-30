import numpy as np
import time
import os
from keypress_nonblocking import KBHit


class Game:
    def __init__(self, h=10, w=50):
        self.height = h
        self.width = w
        self.c = w-1
        self.r = h-1
        self.matrix = np.full((self.height, self.width), ' ', dtype=str)
        self.linepos = 0
        self.linewidth = 5
        self.line_lane_height = 2
        self.dir = 'right'
        self.make_board()

    def make_board(self):
        self.matrix[self.line_lane_height, self.linepos:self.linepos + self.linewidth] = 'X'
        self.matrix[self.line_lane_height+1:self.r, int(self.c / 2):int(self.c / 2) + self.linewidth] = 'X'

    def move_line(self):
        # Starts at 0-4
        # Move 1 forward by setting origin to 0, end to 1
        if self.dir == 'right':
            # Erase old position
            self.matrix[self.line_lane_height, self.linepos] = ' '
            # Move forward and draw
            self.linepos += 1
            self.matrix[self.line_lane_height, self.linepos + self.linewidth] = 'X'
            # Test for bumping the edge
            if self.linepos >= self.c - self.linewidth:
                self.dir = 'left'
        else:
            # Erase old position
            self.matrix[self.line_lane_height, self.linepos + self.linewidth] = ' '
            # Move backwards and draw
            self.linepos -= 1
            self.matrix[self.line_lane_height, self.linepos] = 'X'
            # Test for bumping the edge
            if self.linepos <= 0:
                self.dir = 'right'

    def draw(self):
        os.system('cls')

        print('\n'.join([''.join(i) for i in self.matrix]))

    def capture(self):
        # Check to see if it lines up with the current stack
        if 'X' not in self.matrix[self.line_lane_height+1, self.linepos:self.linepos + self.linewidth+1]:
            return False
        #self.matrix[self.line_lane_height+1, self.linepos:self.linepos + self.linewidth] = 'X'
        # Move everything under the line
        self.matrix = np.roll(self.matrix, 1, axis=0)
        # Erase the top line
        self.matrix[0, :] = ' '
        return True

    def run(self):
        # Create a field
        kb = KBHit()
        while True:
            if kb.kbhit():
                kb.getch()
                status = self.capture()
                if not status:
                    print("LOSE")
                    break
            self.draw()
            self.move_line()



my_game = Game()
my_game.run()
