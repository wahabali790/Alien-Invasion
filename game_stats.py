class GameStats:
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """Initialize statistics."""
        self.settings = ai_game.settings#ai_game.settings is an instance of another class settings.py
        self.reset_stats()

        # Start game in an inactive state.
        self.game_active = False#initial game ruki hui ho gi

        # High score should never be reset.
        self.high_score = 0#initially topmid me score 0 ho ga
        
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit#ship_limit is a property of the settings class that represents the total number of ships the player has in the game. 
        self.score = 0#when the game is restarted or a new game is started to reset the statistics to their initial values.
        self.level = 1