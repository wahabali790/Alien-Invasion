import pygame.font
from pygame.sprite import Group
"""Pygame's Group class provides useful methods for adding, removing, and checking if a sprite exists in the group. In this code, the prep_ships() method creates a new Group object to store instances of the Ship class, representing the remaining ships in the game."""
 
from ship import Ship

class Scoreboard:#keep track of the score, high score, level, and remaining number of ships in a game
    """A class to report scoring information."""

    def __init__(self, ai_game):
        """Initialize scorekeeping attributes."""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        # Font settings for scoring information.
        self.text_color = (255, 0, 0)
        self.font = pygame.font.SysFont(None, 48)#scores ka font size

        # Prepare the initial score images.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
        """ The prep_score(), prep_high_score(), and prep_level() methods use Pygame's font module to render text-based images of the score, high score, and level, respectively"""

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)# In this case, -1 means to round to the nearest ten. 123.45=120
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                self.text_color, self.settings.bg_color)
        
        # Display the score at the top right of the screen.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20#margin of 20 pixels from the right edge of the screen to the right edge of the score.
        self.score_rect.top = 20#agar 200 kru to ye 2nd row me sary scores ko ly ay ga

    def prep_high_score(self):#center wala high score
        """Turn the high score into a rendered image."""
        high_score = round(self.stats.high_score, -1)#-1 means to round to the nearest ten. 123.45=120
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                self.text_color, self.settings.bg_color)
            
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        """Turn the level into a rendered image."""
        level_str = str(self.stats.level)
        self.level_image = self.font.render(level_str, True,
                self.text_color, self.settings.bg_color)
    
        # Position the level below the score.
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10#top sy 10 pixel neechy

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10#10 pixel uper left corner of the screen
            self.ships.add(ship)

    def check_high_score(self):
        """Check to see if there's a new high score.The method check_high_score checks if the current score self.stats.score is greater than the current high score self.stats.high_score. If it is, then the current high score is updated to the current score and the method prep_high_score is called to update the high score display on the screen. This method is used to keep track of the highest score achieved in the game, so that it can be displayed to the user."""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()

    def show_score(self):
        """Draw scores, level, and ships to the screen."""#draw the image of the score on the screen.
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
