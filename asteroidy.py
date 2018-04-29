#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:28:07 2018

@author: vyk35227
"""

import pyglet, math


window = pyglet.window.Window()

def tik(t):
    had.x = had.x + t * 20
    had.y = 20 + 20 * math.sin(had.x / 5)

    
pyglet.clock.schedule_interval(tik, 1/30)    
    
def zpracuj_text(text):
   had.x = 35
   had.rotation = had.rotation + 5
    

obrazek = pyglet.image.load("had.png") 
had = pyglet.sprite.Sprite(obrazek)  
def vykresli():
    window.clear()
    had.draw()
    
obrazek2 = pyglet.image.load("had2.png")
def zmen(t):
    had.image = obrazek2
    pyglet.clock.schedule_once(zmen_zpatky, 0.2)

pyglet.clock.schedule_once(zmen, 1)
    
def zmen_zpatky(t):
    had.image = obrazek
    pyglet.clock.schedule_once(zmen, 0.2)

def klik(x, y, tlacitko, mod):
    had.x = x
    had.y = y
    
window.push_handlers(on_text = zpracuj_text, on_draw = vykresli, on_mouse_press = klik)


pyglet.app.run()
print('Hotovo!')