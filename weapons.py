# -*- coding: utf-8 -*-

import pygame
from math import *
import sprites
import explosions
import sounds

class Bullet(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

    def fire(self,angle,initialpos,parent):
        self.parent = parent

        self.sprite_rotated = pygame.transform.rotate(self.sprite,angle)
        self.rect = self.sprite.get_rect()

        distance_from_player = 20

        self.rect.center = initialpos
        self.rect.centerx = self.rect.centerx + distance_from_player * sin(radians(angle))
        self.rect.centery = self.rect.centery + distance_from_player * cos(radians(angle))

        self.vx = self.velocity * sin(radians(angle))
        self.vy = self.velocity * cos(radians(angle))

        sprites.all_spritelist.add(self)
        sprites.bullet_spritelist.add(self)

    def update(self):
        if sqrt(self.xdistance**2 + self.ydistance**2) > self.radius:
            self.explode()

        self.xdistance += abs(self.vx)
        self.ydistance += abs(self.vy)

        self.rect = self.sprite_rotated.get_rect(center=self.rect.center)
        self.rect.x += self.vx
        self.rect.y += self.vy


class Laser(Bullet):
    def __init__(self,color):
        Bullet.__init__(self)
        sounds.shoot_laser.play()

        self.weapon_type = "Laser"
        self.damage = 10
        self.velocity = 20
        self.radius = 300
        self.cooldown = 6

        if color == "blue":
            self.type = sprites.laser_blue
            self.damage = 4
        elif color == "gold":
            self.type = sprites.laser_gold
            self.cooldown = 12
            self.velocity = 15
            self.damage = 13
        elif color == "green":
            self.type = sprites.laser_green
            self.radius = 500
            self.damage = 7
        elif color == "red":
            self.type = sprites.laser_red

        self.color = color

        self.spritefile = self.type
        self.sprite = pygame.transform.scale(self.spritefile,(16,16))
        self.sprite_rotated = pygame.transform.rotate(self.sprite,0)

        self.xdistance, self.ydistance = 0,0

    def explode(self):
        explosions.Explosion1(self.color,self.rect.center,16)
        sounds.explosion_laser.play()
        sprites.bullet_spritelist.remove(self)
        sprites.all_spritelist.remove(self)


class Rocket(Bullet):
    def __init__(self,color):
        Bullet.__init__(self)
        sounds.shoot_rocket.play()

        self.weapon_type = "Rocket"
        self.damage = 70
        self.velocity = 10
        self.radius = 250
        self.cooldown = 50

        if color == "blue":
            self.type = sprites.rocket_blue
            self.velocity = 20
            self.damage = 50
            self.cooldown = 25
        elif color == "gold":
            self.type = sprites.rocket_gold
            self.damage = 170
            self.velocity = 5
            self.cooldown = 100
        elif color == "green":
            self.type = sprites.rocket_green
            self.radius = 380
            self.damage = 60
        elif color == "red":
            self.type = sprites.rocket_red

        self.color = color
        self.reactor_color = color
        self.reactor_delay = 0

        self.spritefile = self.type
        self.sprite = pygame.transform.scale(self.spritefile,(32,32))
        self.sprite_rotated = pygame.transform.rotate(self.sprite,0)

        self.xdistance, self.ydistance = 0,0

    def reactor(self):
        self.reactor_delay += 1
        if self.reactor_delay > 3:
            explosions.Explosion2(self.reactor_color,self.rect.center,16)
            self.reactor_delay = 0

    def explode(self):
        explosions.Explosion1(self.color,self.rect.center,32)
        sounds.explosion_rocket.play()
        sprites.bullet_spritelist.remove(self)
        sprites.all_spritelist.remove(self)

    def update(self):
        if sqrt(self.xdistance**2 + self.ydistance**2) > self.radius:
            self.explode()

        self.xdistance += abs(self.vx)
        self.ydistance += abs(self.vy)

        self.rect = self.sprite_rotated.get_rect(center=self.rect.center)
        self.rect.x += self.vx
        self.rect.y += self.vy

        self.reactor()


weaponlist = [Rocket("red"),Rocket("blue"),Rocket("green"),Rocket("gold"),Laser("red"),Laser("blue"),Laser("green"),Laser("gold")]