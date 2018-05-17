#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 13:28:07 2018

@author: vyk35227
"""

import pyglet, math
from pyglet.window.key import MOD_CTRL, A, B, C, DOWN, UP, LEFT, RIGHT, S
from pyglet.window.mouse import LEFT as mLEFT
from pyglet.window.mouse import RIGHT as mRIGHT

window = pyglet.window.Window()

obrazek = pyglet.image.load("fries.png")
obrazek.anchor_x = obrazek.width // 2
obrazek.anchod_y = obrazek.height // 2
sprite = pyglet.sprite.Sprite(obrazek)

uhel = 30
rychlost = 10
klavesy = set()

def tiktak(t):
    sprite.x = sprite.x + rychlost*t*math.sin((uhel*math.pi)/180)
    sprite.y = sprite.y + rychlost*t*math.cos((uhel*math.pi)/180)
    
    global rychlost
    global uhel
    for sym in klavesy:
        if sym == A:
            if rychlost < 10:
                rychlost = 0
            else:
                rychlost -=10
            
        elif sym == S:
            if rychlost > 90:
                rychlost = 100
            else: 
                rychlost +=10
    

@window.event
def on_draw():
    window.clear()
    sprite.draw()
    


@window.event
def on_mouse_press(x, y, button, mod):
    global uhel
    if button == 1:
        sprite.x = x
        sprite.y = y
    elif button == 4:
        sprite.rotation = sprite.rotation + 10
        uhel += 10
    elif button == 2:
        sprite.rotation = sprite.rotation - 10
        
    
@window.event
def on_key_press(sym, mod):
    global klavesy
    klavesy.add(sym)
    
    global uhel
    global rychlost
    if sym == 65362:
        uhel = 0
        sprite.rotation = 0
    
    elif sym == 65363:
        uhel = 90
        sprite.rotation = 90
    
    elif sym == 65364:
        uhel = 180
        sprite.rotation = 180
    
    elif sym == 65361:
        uhel = 270
        sprite.rotation = -90
 
    print(sym, mod)
    
@window.event
def on_key_release(sym, mod):
    global klavesy
    klavesy.remove(sym)
        
pyglet.clock.schedule_interval(tiktak, 1/30)    

    
pyglet.app.run()
print('Hotovo!')

