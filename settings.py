class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 255, 0)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (255, 0, 0)
        self.bullets_allowed = 4

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1#agar yaha 100 rahu to level 1 k ba alien 100 ki speed sy neechy giry gy see method increase speeed
        # How quickly the alien point values increase
        self.score_scale = 1.1#if i put 100 after one level points will increase in thousands

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2#ship ki speed
        self.bullet_speed = 3.0#bullets speed
        self.alien_speed = 1.0#alien speed

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """The increase_speed method of the Settings class increases the speed of the ship, bullets and aliens in          the game. It multiplies the current ship_speed, bullet_speed, and alien_speed by the speedup_scale                   attribute. This causes the game to speed up as the player progresses through levels.."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
