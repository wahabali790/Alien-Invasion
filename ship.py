import pygame
 
from pygame.sprite import Sprite
"""Sprites with different properties like height, width, color, etc., and methods like moving right, left, up and down, jump, etc."""
 
class Ship(Sprite):
    """A class to manage the ship."""
 
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        """screen is a component of pygame It is a Pygame surface The screen surface is a Pygame surface that represents display window for game"""
        self.settings = ai_game.settings#ai_game.settings is an instance of another class settings.py
        self.screen_rect = ai_game.screen.get_rect()# a rect object representing the dimensions of the game screen

        # Load the ship image and get its rect.
        self.image = pygame.image.load('C:/Users/HP/Desktop/Alien_invesion/ship.bmp')
        self.rect = self.image.get_rect()# position and size of the spaceship image on the screen.

        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom#put ship midbottom

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)#represents the horizontal position of the spaceship

        # Movement flags
        self.moving_right = False#initially ship will stop no right movement
        self.moving_left = False

    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's x value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Update rect object from self.x.
        self.rect.x = self.x#new position after moving left or right will store in self.rect.x

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)#draw the image of the spaceship on the screen.

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
