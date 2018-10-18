# -*- coding: utf-8 -*-

import pygame
import sprites
import explosions
from math import *
from random import randint
import sounds

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.size = randint(16, 128)
        self.scale = (self.size, self.size)

        self.resistance = self.size
        self.health = self.resistance
        self.damage = self.health/2
        self.velocity = 3
        self.maximum_speed = 2

        self.score = self.size

        self.spriteID = randint(0,4)
        self.sprite = sprites.asteroidlist[self.spriteID]
        self.sprite = pygame.transform.scale(self.sprite, self.scale)

        self.rect = self.sprite.get_rect()
        self.x, self.y = self.rect.center

        self.oldx = self.x
        self.oldy = self.y

        top_or_bottom = randint(0,1)
        left_or_right = randint(0,1)

        if top_or_bottom == 0:
            self.rect.centerx = randint(-223,0)
        elif top_or_bottom == 1:
            self.rect.centerx = randint(992,1215)

        if left_or_right == 0:
            self.rect.centery = randint(-223,0)
        elif left_or_right == 1:
            self.rect.centery = randint(736,959)

        # Note intervalle: les bordures ont une largeur de 32 pixels -> apparition au moins en 33

        self.angle = randint(0,360)               # Génère un angle aléatoire
        self.vx = self.velocity * sin(radians(self.angle))    # Calcul de vx en fonction de cet angle
        self.vy = self.velocity * cos(radians(self.angle))    # Calcul de vy en fonction de cet angle

        sprites.asteroid_spritelist.add(self)
        sprites.all_spritelist.add(self)

    def collision(self, Bullet):
        self.health -= Bullet.damage
        if self.health < self.resistance/2:
            if self.health <= 0:
                Bullet.parent.score += self.size
                self.explode()
            self.sprite = sprites.asteroidlist_broken[self.spriteID]
            self.sprite = self.sprite = pygame.transform.scale(self.sprite, (self.size, self.size))

    def explode(self):
        explosions.Explosion1("gold", self.rect.center, self.size)
        sounds.explosion_object.play()
        sprites.asteroid_spritelist.remove(self)
        sprites.all_spritelist.remove(self)

    def avoid_monotony(self):
        if round(self.vx, 0) == 0:
            self.vx = 1
        if round(self.vy, 0) == 0:
            self.vy = 1

    def avoid_drift(self):
        if self.rect.x < -224 or self.rect.x > 1216:
            self.rect.x = randint(-223,0)
        if self.rect.y < -224 or self.rect.y > 960:
            self.rect.y = randint(-223,0)

    def update(self):
        self.rect = self.sprite.get_rect(center=self.rect.center)

        self.avoid_monotony()
        self.avoid_drift()

        self.oldx = self.rect.x
        self.oldy = self.rect.y

        self.rect.x += self.vx
        self.rect.y += self.vy
