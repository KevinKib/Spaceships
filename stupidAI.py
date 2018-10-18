# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sprites
import explosions
import weapons
from math import *
import fonts
class AI(pygame.sprite.Sprite):
    def __init__(self,ship):
        pygame.sprite.Sprite.__init__(self)

        self.ship = ship
        self.scale = (32,32)
        self.sprite = pygame.transform.scale(self.ship,self.scale)
        self.sprite_rotated = pygame.transform.rotate(self.sprite,0)

        self.score = 0

        self.rect = self.sprite.get_rect()
        self.x, self.y = self.rect.center

        self.oldx = self.x
        self.oldy = self.y

        self.angle = 0          # orientation du joueur

        # /// INITIALISATION DES VARIABLES RESISTANCE ET VIE DU JOUEUR
        self.resistance = 1000           # résistance totale du joueur
        self.health = self.resistance   # vie du joueur: 100% à l'initialisation

        # /// INITIALISATION DES VARIABLIES DE L'ARMEMENT DU JOUEUR
        self.weapon_type = "Laser"
        self.weapon_color = "red"
        self.cooldown = 0

        # /// INITIALISATION VARIABLES DU DEPLACEMENT DU JOUEUR
        self.vx = 0         # vitesse x
        self.vy = 0         # vitesse y
        self.ax = 1         # accélération x
        self.ay = 1         # accélération y

        # /// INITIALISATION DES VARIABLES CARACTERISTIQUES DU DEPLACEMENT DU JOUEUR
        self.reactor_color = "gold"
        self.rotation_speed = 5     # vitesse de rotation
        self.acceleration = 0.4     # facteur accélération
        self.deceleration = 0.1     # facteur décélération
        self.maximum_speed = 6      # vitesse maximale

        # /// DIVERSES HORLOGES ET COMPTEURS // A AMENAGER
        self.reactor_delay = 0

        sprites.AI_spritelist.add(self)
        sprites.all_spritelist.add(self)

    def set_position(self,position):
        self.rect.x, self.rect.y = position

    def set_angle(self,angle):
        self.angle = angle
    def rotate_sprite(self):
        self.sprite_rotated = pygame.transform.rotate(self.sprite, self.angle)

    def set_speed(self,vx,vy):
        self.vx = vx
        self.vy = vy
    def set_acceleration(self,ax,ay):
        self.ax = ax
        self.ay = ay

    def weapon_cooldown(self,weapon):
        if self.cooldown >= weapon.cooldown:
            self.cooldown = 0
            weapon.fire(self.angle,self.rect.center,self)

    def shoot(self):

        if self.weapon_type == "Rocket":
            if self.weapon_color == "blue":
                weapon = weapons.Rocket("blue")
            elif self.weapon_color == "gold":
                weapon = weapons.Rocket("gold")
            elif self.weapon_color == "green":
                weapon = weapons.Rocket("green")
            elif self.weapon_color == "red":
                weapon = weapons.Rocket("red")

        elif self.weapon_type == "Laser":
            if self.weapon_color == "blue":
                weapon = weapons.Laser("blue")
            elif self.weapon_color == "gold":
                weapon = weapons.Laser("gold")
            elif self.weapon_color == "green":
                weapon = weapons.Laser("green")
            elif self.weapon_color == "red":
                weapon = weapons.Laser("red")

        self.weapon_cooldown(weapon)

    def reactor(self):
        self.reactor_delay += 1
        if self.reactor_delay > 3:
            explosions.Explosion2(self.reactor_color,self.rect.center,16)
            self.reactor_delay = 0

    def collision(self,Object):
        self.health -= Object.damage
        if self.health <= 0:
            explosions.Explosion1("green",self.rect.center,32)

    def forward(self):
        ax = self.acceleration * sin(radians(self.angle))
        ay = self.acceleration * cos(radians(self.angle))
        self.set_acceleration(ax, ay)
        self.set_speed(self.vx + self.ax, self.vy + self.ay)
        # Limite de vitesse
        if self.vx > self.maximum_speed:
            self.set_speed(self.maximum_speed, self.vy)
        if self.vx < -self.maximum_speed:
            self.set_speed(-self.maximum_speed, self.vy)
        if self.vy > self.maximum_speed:
            self.set_speed(self.vx, self.maximum_speed)
        if self.vy < -self.maximum_speed:
            self.set_speed(self.vx, -self.maximum_speed)
        self.reactor()

    def focus(self,position):

        x,y = position
        X = abs(self.rect.x - x)
        Y = abs(self.rect.y - y)
        # Distance entre les deux vaisseaux : (Pythagore) sqrt(X+Y) POUR LE MOMENT INUTILE ?
        # IF DISTANCE < ARME.RADIUS : TIRER ?

        if X == 0:
            X = 0.0001
        if Y == 0:
            Y = 0.0001
        Teta = degrees(atan(X/Y))

        if self.rect.y <= y:
            if self.rect.x <= x:
                self.set_angle(Teta)
            elif self.rect.x > x:
                self.set_angle(270 + Teta)
        elif self.rect.y > y:
            if self.rect.x <= x:
                self.set_angle(90 + Teta)
            elif self.rect.x > x:
                self.set_angle(180 + Teta)

        self.rotate_sprite()

    def lifebar(self,screen):
        life_ratio = (self.health/self.resistance)

        start_posx = self.rect.centerx - 16
        start_posy = self.rect.centery - 32
        start_pos = (start_posx,start_posy)

        end_posx = start_posx+(32*life_ratio)
        end_posy = start_posy
        end_pos = (end_posx,end_posy)

        pygame.draw.line(screen,fonts.red,start_pos,end_pos)

    def update(self):
        self.cooldown += 1
        self.forward()
        self.shoot()

        self.rect = self.sprite_rotated.get_rect(center=self.rect.center)
        self.rect.x += self.vx
        self.rect.y += self.vy


# INSTANCES:
#   - ASTEROIDES
#       - FACILE
#       - NORMAL
#       - DIFFICILE
#       - SURVIE
#   - JOUEUR CONTRE JOUEUR
#   - JOUEUR CONTRE ORDINATEUR
#   - COURSE (récupérer des drapeaux?)