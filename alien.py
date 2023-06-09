import pygame
from pygame.sprite import Sprite
 
class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_game):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('C:/Users/HP/Desktop/Alien_invesion/alien.bmp')
        self.rect = self.image.get_rect()#pygame method

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width#starting position of the alien is set near the top left of the screen.
        self.rect.y = self.rect.height

        # Store the alien's exact horizontal position.
        self.x = float(self.rect.x)#The "rect.x" attribute of the alien represents the x-coordinate of the top left            corner of the alien's rect on the screen but storing it as a floating point number allows for more precise positioning of the alien

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        """returns "True" if the right edge of the alien's rect is beyond the right edge of the screen or if the left edge of the alien's rect is beyond the left edge of the screen."""

    def update(self):
        """Move the alien right or left."""
        self.x += (self.settings.alien_speed *
                        self.settings.fleet_direction)#see setting.py method increase_speed
        self.rect.x = self.x
