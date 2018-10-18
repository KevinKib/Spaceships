# -*- coding: utf-8 -*-

import pygame
pygame.init()
pygame.mixer.init()

shoot_laser = pygame.mixer.Sound("data/sounds/shoot_laser.wav")
explosion_laser = pygame.mixer.Sound("data/sounds/explosion_laser.wav")

shoot_rocket = pygame.mixer.Sound("data/sounds/shoot_rocket.wav")
explosion_rocket = pygame.mixer.Sound("data/sounds/explosion_rocket.wav")

explosion_object = pygame.mixer.Sound("data/sounds/explosion_object.wav")

collision = pygame.mixer.Sound("data/sounds/collision.wav")

game_music = "data/sounds/game.ogg"
menu_music = "data/sounds/menu.mp3"
