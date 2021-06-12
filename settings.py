#all the settings for game
class Settings():

     def __init__(self):
#initialise the game's static settings
         #screen settings
         self.screen_width=1000
         self.screen_height=700
         self.bg_color=(0, 190, 190)

         #ship settings
         self.ship_limit=3

         #bullet settings
         self.bullet_width=3
         self.bullet_height=15
         self.bullet_color=60,60,60
         self.bullets_allowed=3

         #alien settings
         self.fleet_drop_speed = 10

         #how quickly the game speeds up
         self.speedup_scale=1.1

         #how quickly the alien point values increases
         self.score_scale=2

         self.initialize_dynamic_settings()
     
     def initialize_dynamic_settings(self):
         #initialise settings that change throught the game
         self.ship_speed_factor = 1.5
         self.bullet_speed_factor = 3
         self.alien_speed_factor = 1
         self.bullet_width=3
         # fleet_direction of 1 represents right; -1 represents left.
         self.fleet_direction = 1

         #scoring
         self.alien_points=50

     def increase_speed(self):
         #increase speed settings and alien points 
         self.ship_speed_factor *= self.speedup_scale
         self.bullet_speed_factor *= self.speedup_scale
         self.alien_speed_factor *= self.speedup_scale

         self.alien_points =int(self.alien_points*self.score_scale)
         




  
