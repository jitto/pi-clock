import scene, pygame, time, pywapi
import wiringpi

weather_com_result = pywapi.get_weather_from_weather_com('75056', 'imperial')
lastWeatherUpdateTime = time.time()
wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(18,2)
wiringpi.pwmWrite(18, 999)

def updateWeather():
  global weather_com_result
  global lastWeatherUpdateTime
  if (weather_com_result is None or (time.time() - lastWeatherUpdateTime > 61)):
    weather_com_result = pywapi.get_weather_from_weather_com('75056', 'imperial')
    lastWeatherUpdateTime = time.time()

def drawText(text, font, color, center, screen):
  surface = font.render(text, True, color)
  rect = surface.get_rect(center=center)
  screen.blit(surface, rect)

class TitleScene(scene.SceneBase):
    pygame.font.init()
    font_big = pygame.font.Font('digital-7 (mono).ttf', 130)
    font_med = pygame.font.Font(None, 80)
    font_small = pygame.font.Font(None, 40)
    brightStart = time.time()

    def __init__(self):
        scene.SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            wiringpi.pwmWrite(18, 1023)
            self.brightStart = time.time()
    
    def Update(self):
        updateWeather()
        if (time.time() - self.brightStart > 5):
            wiringpi.pwmWrite(18, 100)
    
    def Render(self, screen):
        # For the sake of brevity, the title scene is a blank red screen 
        screen.fill((0, 0, 0))
        time_text  = time.strftime('%H:%M:%S', time.localtime())
        drawText(time_text, self.font_big, (255,255,255), (240,48), screen)
        drawText(weather_com_result['current_conditions']['text'], self.font_med, (255,255,255), (240,148), screen)
        drawText(weather_com_result['current_conditions']['moon_phase']['text'], self.font_small, (255,255,255), (240, 199), screen)
        drawText(weather_com_result['current_conditions']['temperature'], self.font_med, (255,255,255), (40, 260), screen)
        x = 99
        for forecast in weather_com_result['forecasts']:
          drawText(forecast['high'], self.font_small, (255,255,255), (x, 259), screen)
          drawText(forecast['low'], self.font_small, (255,255,255), (x, 289), screen)
          x = x + 40

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
