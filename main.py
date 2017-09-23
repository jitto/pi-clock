#!/usr/bin/python

import os, scene, clock

os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDRV"] = "TSLIB"
os.environ["SDL_MOUSEDEV"] = "/dev/input/touchscreen"

scene.run_game(480, 320, .1, clock.TitleScene())
