# -*- coding: utf-8 -*-

import pygame
import sprites

class Explosion1(pygame.sprite.Sprite):

	def __init__(self,color,initialpos,scale):

		pygame.sprite.Sprite.__init__(self)

		if color == "blue":
			self.explosion_list = sprites.explosion1list_blue
		elif color == "gold":
			self.explosion_list = sprites.explosion1list_gold
		elif color == "green":
			self.explosion_list = sprites.explosion1list_green
		elif color == "red":
			self.explosion_list = sprites.explosion1list_red

		self.scale = scale
		self.sprite = pygame.transform.scale(self.explosion_list[0],(self.scale,self.scale))
		self.rect = self.sprite.get_rect(center=initialpos)
		self.timer = 0
		sprites.all_spritelist.add(self)
		sprites.explosion_spritelist.add(self)

	def animation(self):
		self.timer += 1
		if self.timer == 5:
			self.sprite = pygame.transform.scale(self.explosion_list[1],(self.scale,self.scale))
		elif self.timer == 10:
			self.sprite = pygame.transform.scale(self.explosion_list[2],(self.scale,self.scale))
		elif self.timer == 15:
			self.sprite = pygame.transform.scale(self.explosion_list[3],(self.scale,self.scale))
		elif self.sprite == 20:
			self.sprite = pygame.transform.scale(self.explosion_list[4],(self.scale,self.scale))
		elif self.timer == 25:
			self.sprite = pygame.transform.scale(self.explosion_list[5],(self.scale,self.scale))
		elif self.timer == 30:
			self.sprite = pygame.transform.scale(self.explosion_list[6],(self.scale,self.scale))
			sprites.all_spritelist.remove(self)
			sprites.explosion_spritelist.remove(self)


	def update(self):
		self.animation()


class Explosion2(pygame.sprite.Sprite):
	def __init__(self, color, initialpos, scale):
		pygame.sprite.Sprite.__init__(self)
		if color == "blue":
			self.explosion_list = sprites.explosion2list_blue
		elif color == "gold":
			self.explosion_list = sprites.explosion2list_gold
		elif color == "green":
			self.explosion_list = sprites.explosion2list_green
		elif color == "red":
			self.explosion_list = sprites.explosion2list_red
		self.scale = scale
		self.sprite = pygame.transform.scale(self.explosion_list[0], (self.scale, self.scale))
		self.rect = self.sprite.get_rect(center=initialpos)
		self.timer = 0
		sprites.all_spritelist.add(self)
		sprites.explosion_spritelist.add(self)

	def animation(self):
		self.timer += 1
		if self.timer == 5:
			self.sprite = pygame.transform.scale(self.explosion_list[1], (self.scale, self.scale))
		elif self.timer == 10:
			self.sprite = pygame.transform.scale(self.explosion_list[2], (self.scale, self.scale))
		elif self.timer == 15:
			self.sprite = pygame.transform.scale(self.explosion_list[3], (self.scale, self.scale))
		elif self.sprite == 20:
			self.sprite = pygame.transform.scale(self.explosion_list[4], (self.scale, self.scale))
		elif self.timer == 25:
			self.sprite = pygame.transform.scale(self.explosion_list[5], (self.scale, self.scale))
		elif self.timer == 30:
			self.sprite = pygame.transform.scale(self.explosion_list[6], (self.scale, self.scale))
			sprites.all_spritelist.remove(self)
			sprites.explosion_spritelist.remove(self)

	def update(self):
		self.animation()