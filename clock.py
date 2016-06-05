import scene, pygame, time, pywapi, threading
import wiringpi

weather_com_result = []
wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(18,2)
wiringpi.pwmWrite(18, 999)

def updateWeather():
  global weather_com_result
  while True:
    weather_com_result = pywapi.get_weather_from_weather_com('75056', 'imperial')
    print(weather_com_result)
    time.sleep(60)

weatherThread = threading.Thread(target=updateWeather, args=())
weatherThread.setDaemon(True)
weatherThread.start()

def drawText(text, font, color, center, screen):
  surface = font.render(text, True, color)
  rect = surface.get_rect(center=center)
  screen.blit(surface, rect)

class TitleScene(scene.SceneBase):
    pygame.font.init()
    font_big = pygame.font.Font('digital-7 (mono).ttf', 220)
    font_med = pygame.font.Font(None, 110)
    font_small = pygame.font.Font(None, 40)
    brightStart = time.time()

    def __init__(self):
        scene.SceneBase.__init__(self)
    
    def ProcessInput(self, events, pressed_keys):
        for event in events:
            wiringpi.pwmWrite(18, 1023)
            self.brightStart = time.time()
            pygame.mouse.set_visible(True)
    
    def Update(self):
        if (time.time() - self.brightStart > 5):
            wiringpi.pwmWrite(18, 100)
            pygame.mouse.set_visible(False)
    
    def Render(self, screen):
        screen.fill((0, 0, 0))
        time_text  = time.strftime('%H:%M', time.localtime())
        drawText(time_text, self.font_big, (255,255,255), (240,68), screen)
        drawText(weather_com_result['current_conditions']['text'], self.font_med, (255,255,255), (240,208), screen)
#        drawText(weather_com_result['current_conditions']['moon_phase']['text'], self.font_small, (255,255,255), (240, 199), screen)
        drawText(weather_com_result['current_conditions']['temperature'], self.font_med, (255,255,255), (40, 289), screen)
        x = 129
        for forecast in weather_com_result['forecasts']:
          drawText(forecast['high'], self.font_small, (255,255,255), (x, 279), screen)
          drawText(forecast['low'], self.font_small, (255,255,255), (x, 302), screen)
          x = x + 40

