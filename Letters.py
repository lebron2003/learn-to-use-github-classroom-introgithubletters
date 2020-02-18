# Python group student letter creation
# Authors: Whole class, each student is responsible for a different letter
# Will be practicing Merge and showing other GitHub features
#
# Begun: Feb. 18/20
import pygame *
import turtle *

surface = pygame.Surface((100, 100)) # setup a very basic surface - you may overload or change for your version or use this.
surface = pygame.Surface((100, 100), pygame.SRCALPHA) # transparent one, changed my mind...
image = pygame.image.load('LetterZ.png')
