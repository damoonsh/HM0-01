"""
    Generates the map and holds it's properties
"""
# Needed modules for the pygame and random
import pygame
import random
# Minor utilities used to ease the data transfering process
from utilities.Consts import vals
from mover import Mover
from utilities import Consts


# Map module
class Map:
    def __init__(self, consts):
        """Initializing the Object with the default values for rows, cols and
        scale."""
        # The core blocks of the object that helps
        # us build the map and manipulate it
        self.row = consts.row
        self.col = consts.col
        self.scale = consts.scale
        # Holds the blocks
        self.blocks = []
        # The difficulty level of the maze
        self.diff = 0.32
        # The delay time for the mover object
        self.delay = 1000

    # -------------------------------------------------------------------
    # Verification of the map--------------------------------------------
    # -------------------------------------------------------------------
    def get_array(self):
        """ Gets the map in the format of 1/0 array """
        # Keeps track of the map as an array
        self.array = []
        # The two for loops have the same functionality as the x-y system
        for r in range(self.row):
            # Instantiating the
            self.array.append([])
            for c in range(self.col):
                # Checks to see if the coordinates are in the blocks arrays or not
                if (r, c) in self.blocks:
                    self.array[r].append("0")
                else:
                    self.array[r].append("1")

    # --------------------------------------------------------------------------
    def run(self):
        """Runs the main process"""
        # Instantiating the initial properties for the application
        pygame.init()
        height, width = self.col * self.scale, self.row * self.scale
        # Setting the logo
        gameIcon = pygame.image.load('logo.png')
        pygame.display.set_icon(gameIcon)
        # Setting the height and width
        self.gameDisplay = pygame.display.set_mode((height, width))
        # Setting the caption
        pygame.display.set_caption('HM0-01')
        # Initializing the pixel property
        self.pixel = pygame.PixelArray(self.gameDisplay)

        # Drawing the map
        # Instantiating the mover object
        self.obj = Mover(self.pixel)
        self.obj.set_dimensions(self.col, self.row)
        # Setting the scale for that
        self.obj.set_scale(self.scale)

        # generating the blocks within the maze
        self.maze()
        # Finalizing the process of making the map
        self.generate_map()

    def generate_map(self):
        """Generates the map"""
        for r in range(self.row):
            for c in range(self.col):
                # Checks to see if the coordinates are in the blocks arrays or not
                if (r, c) in self.blocks:
                    self.block(c * self.scale, r * self.scale, Consts.Black)
                else:
                    self.block(c * self.scale, r * self.scale)

        # Instantiating the mover object on the domain of the movement
        self.block(0, 0, Consts.Item)

    def maze(self):
        """Generates the random blocks within the map"""
        # Getting the number of blocks in the map
        num = int((self.row * self.col) * self.diff)
        for i in range(num):
            self.blocks.append(((random.randrange(self.row)), (random.randrange(self.col))))
        # Generate the array of the map
        self.get_array()

    def block(self, x, y, color=Consts.White):
        """Draws blocks pixel by pixel"""
        for r in range(self.scale):
            for c in range(self.scale):
                self.pixel[x + r][y + c] = color

    # --------------------------------------------------------------------------
    # Logic related functions---------------------------------------------------
    # --------------------------------------------------------------------------
    def move(self, dx, dy):
        """Movement functionality for random movement."""
        # At the beginning it should be checked to see if the co-ordinates are
        # in the demanded range so we won't have any, errors regarding the
        # function not being in the range.
        if self.obj.check_range(self.obj.x + self.scale * dx, self.obj.y + self.scale * dy):
            # After checking to see for the co-ordinates it is up to the mover object to decide the movement
            if self.pixel[self.obj.x + self.scale * dx][self.obj.y + self.scale * dy] != 6556180:
                self.block(self.obj.x, self.obj.y)
                self.obj.set_coordinates(self.obj.x + self.scale * dx, self.obj.y + self.scale * dy)
                self.block(self.obj.x, self.obj.y, Consts.Item)

    def autoMove(self):
        """The automatic way of moving in the maze."""
        x, y = self.obj.move_logic()

        # The process of movement:
        # print('Deleting ', int(self.obj.x), int(self.obj.y), end='')
        self.block(self.obj.x, self.obj.y)  # Delete the current place of the block
        self.obj.set_coordinates(x, y)  # Set the new coordinates for the moving object
        # print(', Drawing', int(self.obj.x), int(self.obj.y))
        self.block(self.obj.x, self.obj.y, Consts.Item)  # Draw the block with it's new place
        self.obj.visited.append((x, y))  # Track the visited coordinates
        pygame.time.wait(self.delay)
