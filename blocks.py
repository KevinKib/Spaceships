# -*- coding: utf-8 -*-

import pygame
import sprites
import explosions

blocklist = []

class Block(pygame.sprite.Sprite):

    def __init__(self,initialpos):
        pygame.sprite.Sprite.__init__(self)
        self.rect = self.sprite.get_rect()
        self.rect.x, self.rect.y = initialpos
        self.scale = (32,32)
        sprites.block_spritelist.add(self)
        sprites.all_spritelist.add(self)

    def damage(self,Bullet):
        self.health -= Bullet.damage
        if self.health < self.resistance/2:
            if self.health <= 0:
                self.destroy()
            self.sprite = self.sprite_broken

    def destroy(self):
        explosions.Explosion1("gold",self.rect.center,32)
        sprites.block_spritelist.remove(self)
        sprites.all_spritelist.remove(self)

class Empty(Block):
    def __init__(self,initialpos):
        self.ID = 0
        self.sprite = sprites.empty
        self.sprite_broken = sprites.empty
        self.resistance = 10000

        self.health = self.resistance
        Block.__init__(self,initialpos)

class Indestructible(Block):
    def __init__(self,initialpos):
        self.ID = 1
        self.sprite = sprites.indestructible
        self.sprite_broken = sprites.indestructible
        self.resistance = 10000
        self.health = self.resistance
        Block.__init__(self,initialpos)


class Destructible(Block):
    def __init__(self,initialpos):
        self.ID = 2
        self.sprite = sprites.destructible
        self.sprite_broken = sprites.destructible_broken
        self.resistance = 70
        self.health = self.resistance
        Block.__init__(self,initialpos)

blocklist.append(Empty((-32,-32)))
blocklist.append(Destructible((-32,-32)))
blocklist.append(Indestructible((-32,-32)))
