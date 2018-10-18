# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sprites
import explosions
import weapons
import fonts
from math import *


class Player(pygame.sprite.Sprite):
    def __init__(self,ship,Weapon):
        pygame.sprite.Sprite.__init__(self)

        self.ship = ship
        self.scale = (32,32)
        self.sprite = pygame.transform.scale(self.ship,self.scale)
        self.sprite_rotated = pygame.transform.rotate(self.sprite,0)

        self.dead = False
        self.score = 0

        self.rect = self.sprite.get_rect()
        self.x, self.y = self.rect.center

        self.oldx = self.x
        self.oldy = self.y

        self.angle = 0          # orientation du joueur

        # /// INITIALISATION DES VARIABLES RESISTANCE ET VIE DU JOUEUR
        self.resistance = 400           # résistance totale du joueur
        self.health = self.resistance    # vie du joueur: 100% à l'initialisation

        # /// INITIALISATION DES VARIABLIES DE L'ARMEMENT DU JOUEUR
        self.weapon_type = Weapon.weapon_type
        self.weapon_color = Weapon.color
        self.cooldown = 0

        # /// INITIALISATION VARIABLES DU DEPLACEMENT DU JOUEUR
        self.vx = 0         # vitesse x
        self.vy = 0         # vitesse y
        self.ax = 1         # accélération x
        self.ay = 1         # accélération y

        # /// INITIALISATION DES VARIABLES CARACTERISTIQUES DU DEPLACEMENT DU JOUEUR
        self.reactor_color = "gold"
        self.rotation_speed = 5     # vitesse de rotation
        self.acceleration = 0.3     # facteur accélération
        self.deceleration = 0.1     # facteur décélération
        self.maximum_speed = 4      # vitesse maximale

        # /// DIVERSES HORLOGES ET COMPTEURS
        self.reactor_delay = 0

        sprites.players_spritelist.add(self)
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

    def set_weapon(self,type,color):
        self.weapon_type = type
        self.weapon_color = color

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
            self.die()

    def die(self):
        sprites.all_spritelist.remove(self)
        sprites.players_spritelist.remove(self)
        explosions.Explosion1("gold",self.rect.center,32)
        self.dead = True

    def lifebar(self,screen):
        life_ratio = (self.health/self.resistance)

        start_posx = self.rect.centerx - 16
        start_posy = self.rect.centery - 32
        start_pos = (start_posx,start_posy)

        end_posx = start_posx+(32*life_ratio)
        end_posy = start_posy
        end_pos = (end_posx,end_posy)

        pygame.draw.line(screen,fonts.red,start_pos,end_pos)



    def forward(self):
        ax = self.acceleration * sin(radians(self.angle))
        ay = self.acceleration * cos(radians(self.angle))
        self.set_acceleration(ax, ay)
        self.set_speed(self.vx + self.ax, self.vy + self.ay)
        if self.vx > self.maximum_speed:
            self.set_speed(self.maximum_speed, self.vy)
        if self.vx < -self.maximum_speed:
            self.set_speed(-self.maximum_speed, self.vy)
        if self.vy > self.maximum_speed:
            self.set_speed(self.vx, self.maximum_speed)
        if self.vy < -self.maximum_speed:
            self.set_speed(self.vx, -self.maximum_speed)
        self.reactor()
    def stop(self):
        if self.vx != 0:
            if self.vx > 0:
                self.vx = round(self.vx - self.deceleration,2)
            elif self.vx < 0:
                self.vx = round(self.vx + self.deceleration,2)
        if self.vy != 0:
            if self.vy > 0:
                self.vy = round(self.vy - self.deceleration,2)
            elif self.vy < 0:
                self.vy = round(self.vy + self.deceleration,2)
    def rotate_left(self):
        self.set_angle(self.angle + self.rotation_speed)
        self.rotate_sprite()
    def rotate_right(self):
        self.set_angle(self.angle - self.rotation_speed)
        self.rotate_sprite()


    def multiplayer_controls(self,number):


        if number == "Player 1":
            keys = pygame.key.get_pressed()
            if keys[K_KP8]:
                self.forward()
            if keys[K_KP5]:
                self.stop()
            if keys[K_KP4]:
                self.rotate_left()
            if keys[K_KP6]:
                self.rotate_right()
            if keys[K_KP0]:
                self.shoot()

        # PYGAME EST EN QWERTY !!!
        elif number == "Player 2":
            keys = pygame.key.get_pressed()
            if keys[K_w]:
                self.forward()

            if keys[K_s]:
                self.stop()

            if keys[K_a]:
                self.rotate_left()

            if keys[K_d]:
                self.rotate_right()

            if keys[K_SPACE]:
                self.shoot()

    def controls(self):
        keys = pygame.key.get_pressed()

        if keys[K_UP]:
            self.forward()

        if keys[K_DOWN]:
            self.stop()

        if keys[K_LEFT]:
            self.rotate_left()

        if keys[K_RIGHT]:
            self.rotate_right()

        if keys[K_SPACE]:
            self.shoot()


    def update(self):
        self.cooldown += 1
        self.rect = self.sprite_rotated.get_rect(center=self.rect.center)

        self.oldx = self.rect.x
        self.oldy = self.rect.y

        self.rect.x += self.vx
        self.rect.y += self.vy
