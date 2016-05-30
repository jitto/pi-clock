import scene, pygame, time, pywapi

class TitleScene(scene.SceneBase):
    def __init__(self):
        scene.SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                # Move to the next scene when the user pressed Enter 
                self.SwitchToScene(GameScene())
    
    def Update(self):
        pass
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen 
        font_big = pygame.font.Font('digital-7 (mono).ttf', 130)
        font_med = pygame.font.Font(None, 80)
        font_small = pygame.font.Font(None, 40)
        weather_com_result = pywapi.get_weather_from_weather_com('75056', 'imperial')
        temp = '{:2.1f}'.format((float(weather_com_result['current_conditions']['temperature']) * 9 / 5) + 32)
        screen.fill((0, 0, 0))
        time_text  = time.strftime('%H:%M:%S', time.localtime())
        self.drawText(time_text, font_big, (255,255,255), (240,48), screen)
        self.drawText(weather_com_result['current_conditions']['text'], font_med, (255,255,255), (240,148), screen)
        self.drawText(weather_com_result['current_conditions']['moon_phase']['text'], font_small, (255,255,255), (240, 199), screen)
        self.drawText(weather_com_result['current_conditions']['temperature'], font_med, (255,255,255), (40, 260), screen)
        x = 99
        for forecast in weather_com_result['forecasts']:
          self.drawText(forecast['high'], font_small, (255,255,255), (x, 259), screen)
          self.drawText(forecast['low'], font_small, (255,255,255), (x, 289), screen)
          x = x + 40

    def drawText(self, text, font, color, center, screen):
        surface = font.render(text, True, color)
        rect = surface.get_rect(center=center)
        screen.blit(surface, rect)

class GameScene(scene.SceneBase):
    def __init__(self):
        scene.SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        pass
        
    def Update(self):
        pass
    
    def Render(self, screen):
        # The game scene is just a blank blue screen 
        screen.fill((0, 0, 255))
