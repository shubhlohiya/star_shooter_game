class Settings:

    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 960
        self.screen_height = 540
        self.bg_color = (230, 230, 230)

        #Ship settings
        self.ship_size = (55,50)        
        self.ship_limit = 2 # 2 extra ships ie. total 3 ships

        #Bullet settings        
        self.bullet_width = 3.5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 4

        #Alien settings
        self.alien_size = (39, 50)  #(50, 64)        
        self.fleet_drop_speed = 10        
        
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game"""

        self.ship_speed = 2
        self.bullet_speed = 2
        self.alien_speed = 0.5

        self.fleet_direction = 1 # 1 - right / -1 - left.

        self.alien_points = 50


    def increase_speed(self):
        """Increase speeds and stats settings"""

        self.ship_speed *= self.speedup_scale            
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
