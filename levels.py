# -*- coding: utf-8 -*-

import pygame
from random import randint

class Level:
    def __init__(self,name,file,background):
        self.name = name
        self.background = background
        self.grid = \
            [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]
        self.generate_grid(file)

        self.levelbounds = []
        class Bound:
            def __init__(self,left,top,width,height):
                self.rect = pygame.Rect(left,top,width,height)
                self.scale = (width,height)

        self.left_bound = Bound(-32,-32,32,736)
        self.levelbounds.append(self.left_bound)
        self.top_bound = Bound(-32,-32,992,32)
        self.levelbounds.append(self.top_bound)
        self.right_bound = Bound(992,-32,32,736)
        self.levelbounds.append(self.right_bound)
        self.bottom_bound = Bound(-32,736,992,32)
        self.levelbounds.append(self.bottom_bound)

    def generate_grid(self,file):
        file = open(file,"r").read()
        current_ID_read = []
        x = 0
        y = 0
        for value in file:
            if x == 31:
                x = 0
                y+= 1
            if value == ";":
                self.grid[y][x] = int("".join(current_ID_read))
                current_ID_read = []
                x += 1
            else:
                current_ID_read.append(value)

import sprites

levellist = []
Empty = Level("Arène vide","data/levels/empty.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Empty)

Level_1 = Level("Arène 1","data/levels/level1.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Level_1)
Level_2 = Level("Arène 2","data/levels/level2.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Level_2)
Level_3 = Level("Arène 3","data/levels/level3.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Level_3)
Level_4 = Level("Arène 4","data/levels/level4.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Level_4)
Level_5 = Level("Arène 5","data/levels/level5.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Level_5)

Custom_1 = Level("Niveau personnalisé 1","data/levels/custom/slot1.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Custom_1)
Custom_2 = Level("Niveau personnalisé 2","data/levels/custom/slot2.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Custom_2)
Custom_3 = Level("Niveau personnalisé 3","data/levels/custom/slot1.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Custom_3)
Custom_4 = Level("Niveau personnalisé 4","data/levels/custom/slot4.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Custom_4)
Custom_5 = Level("Niveau personnalisé 5","data/levels/custom/slot5.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Custom_5)
Custom_6 = Level("Niveau personnalisé 6","data/levels/custom/slot6.txt",sprites.backgroundlist[randint(0,4)])
levellist.append(Custom_6)