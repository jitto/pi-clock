import scene, pygame, time, threading, sys, requests

import wiringpi

weather_com_result = None
wiringpi.wiringPiSetupGpio()  
wiringpi.pinMode(18,2)
wiringpi.pwmWrite(18, 999)

def updateWeather():
  global weather_com_result
  while True:
    try:
#      weather_com_result = pywapi.get_weather_from_weather_com('75056', 'imperial')
#      response = requests.get('https://api.weather.gov/gridpoints/FWD/85,116/forecast')
      response = requests.get('https://wttr.in/?format=j1', verify=False)
      weather_com_result = response.json()
    except:
      weather_com_result = None
      print("Unexpected error:", sys.exc_info()[0])
    time.sleep(600)

weatherThread = threading.Thread(target=updateWeather, args=())
weatherThread.setDaemon(True)
weatherThread.start()

def drawText(text, font, color, screen, **rectAttributes):
  surface = font.render(text, True, color)
  rect = surface.get_rect(**rectAttributes)
  screen.blit(surface, rect)

class TitleScene(scene.SceneBase):
    pygame.font.init()
    font_big = pygame.font.Font('digital-7 (mono).ttf', 240)
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
            backLight = 500
            if (time.localtime().tm_hour > 22 or time.localtime().tm_hour < 5):
              backLight = 1
            wiringpi.pwmWrite(18, backLight)
            pygame.mouse.set_visible(False)
   
    def Temperature(self, temperature):
        if (not temperature):
            return (255, 255, 255)
        temp = int(temperature)
        tempColor = (0, 255, 0)
        if (temp < 50):
            tempColor = (0, 255, 255)
        elif (temp > 80):
            tempColor = (255, 0, 0)
        return tempColor

    def Render(self, screen):
        screen.fill((0, 0, 0))
        color = (255, 255, 255)
        time_text  = time.strftime('%-I:%M', time.localtime())
        drawText(time_text, self.font_big, color, screen, midright=(478,68))
        weather = weather_com_result
        if (type(weather) is dict and 'current_condition' in weather):
          drawText(weather['current_condition'][0]['weatherDesc'][0]['value'], self.font_med, color, screen, center=(240,208))
          temp = str(int(weather['current_condition'][0]['temp_F']))
          drawText(temp, self.font_med, self.Temperature(temp), screen, center=(40, 289))
          x = 129
#          for forecast in weather['periods'][0:7]:
#            high = str(int(forecast['temperatureHigh']))
#            drawText(high, self.font_small, self.Temperature(high), screen, center=(x, 279))
#            low = str(int(forecast['temperatureLow']))
#            drawText(low, self.font_small, self.Temperature(low), screen, center=(x, 302))
#            x = x + 50
#          drawText("as of", self.font_small, (100, 100, 100), screen, center=(420, 279))
#          temp = weather['current_conditions']['last_updated'].split()[1]
#          drawText(temp, self.font_small, (100, 100, 100), screen, center=(420, 302))
