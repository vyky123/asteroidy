#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 17 12:49:52 2018

@author: vyk35227
"""

from math import sin, cos, radians, pi
from random import randint
import pyglet

window = pyglet.window.Window()
batch = pyglet.graphics.Batch() #věcička pro efektivní vykreslování
seznam = list()

class Lod(object):
    def __init__(self, obrazek, x=None, y=None, r=None, rychlost=10,
                 window=window, batch=batch):
        self.image = pyglet.image.load("fries.png")
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)
        if x:
            self._x = x
        else:
            self._x = randint(0, window.width)
        self.sprite.x = self._x

        if y:
            self._y = self.sprite.y = y
        else:
            self._y = randint(0, window.height)
        self.sprite.y = self._y

        if r:
            self._rotation = r
        else:
            self._rotation = randint(0, 360)
        self.sprite.rotation = self._rotation
        
        self._rychlost = rychlost
        seznam.append(self)

    def tiktak(self, t):
        self.sprite.x = self.sprite.x + self._rychlost*t*sin(pi*self._rotation/180)
        self._x = self.sprite.x
        self.sprite.y = self.sprite.y + self._rychlost*t*cos(pi*self._rotation/180)
        self._y = self.sprite.y

@window.event
def on_draw():
    window.clear()
    batch.draw()
        
trpaslik = Lod("fries.png", rychlost = 30)
enterprise = Lod("fries.png", rychlost = 50)
falcon = Lod("fries.png", rychlost = 60)

def tiktak(t):
    for lod in seznam:
        lod.tiktak(t)
    #trpaslik.tiktak(t)
    #enterprise.tiktak(t)
    #falcon.tiktak(t)

print(trpaslik._x, trpaslik._y)
print(enterprise._x, enterprise._y)
print(falcon._x, falcon._y)

pyglet.clock.schedule_interval(tiktak, 1/25)

pyglet.app.run()

