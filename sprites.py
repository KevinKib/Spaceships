# -*- coding: utf-8 -*-

import pygame
pygame.init()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// IMPORTANT : CREATION DES GROUPES DE SPRITES (PYGAME)

all_spritelist = pygame.sprite.Group()
players_spritelist = pygame.sprite.Group()
AI_spritelist = pygame.sprite.Group()
bullet_spritelist = pygame.sprite.Group()
block_spritelist = pygame.sprite.Group()
powerups_spritelist = pygame.sprite.Group()
explosion_spritelist = pygame.sprite.Group()
asteroid_spritelist = pygame.sprite.Group()


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////////////// IMPORTANT : CHARGEMENT DES SPRITES (PYGAME)


# ///////////////////////////////////////////////////////////////////////////////////////// FONDS
backgroundlist = []
background_01 = pygame.image.load("data/sprites/backgrounds/1.png")
backgroundlist.append(background_01)
background_02 = pygame.image.load("data/sprites/backgrounds/2.png")
backgroundlist.append(background_02)
background_03 = pygame.image.load("data/sprites/backgrounds/3.png")
backgroundlist.append(background_03)
background_04 = pygame.image.load("data/sprites/backgrounds/4.png")
backgroundlist.append(background_04)
background_05 = pygame.image.load("data/sprites/backgrounds/5.png")
backgroundlist.append(background_05)


# ///////////////////////////////////////////////////////////////////////////////////////// MENUS
main = pygame.image.load("data/sprites/menus/main.png").convert_alpha()
mode = pygame.image.load("data/sprites/menus/mode.png").convert_alpha()
difficulty = pygame.image.load("data/sprites/menus/difficulty.png").convert_alpha()
J1_ship = pygame.image.load("data/sprites/menus/J1_ship.png").convert_alpha()
J2_ship = pygame.image.load("data/sprites/menus/J2_ship.png").convert_alpha()
level = pygame.image.load("data/sprites/menus/level.png")

# ///////////////////////////////////////////////////////////////////////////////////////// BLOCKS
empty = pygame.image.load("data/sprites/blocks/empty.png")

destructible = pygame.image.load("data/sprites/blocks/destructible.png")
destructible_broken = pygame.image.load("data/sprites/blocks/destructible_broken.png")

indestructible = pygame.image.load("data/sprites/blocks/indestructible.png")

# ///////////////////////////////////////////////////////////////////////////////////////// ASTEROIDES

# ////////////////////////////////////////// ASTEROIDES
asteroidlist = []
asteroid1 = pygame.image.load("data/sprites/asteroids/asteroid1.png").convert_alpha()
asteroidlist.append(asteroid1)
asteroid2 = pygame.image.load("data/sprites/asteroids/asteroid2.png").convert_alpha()
asteroidlist.append(asteroid2)
asteroid3 = pygame.image.load("data/sprites/asteroids/asteroid3.png").convert_alpha()
asteroidlist.append(asteroid3)
asteroid4 = pygame.image.load("data/sprites/asteroids/asteroid4.png").convert_alpha()
asteroidlist.append(asteroid4)
asteroid5 = pygame.image.load("data/sprites/asteroids/asteroid5.png").convert_alpha()
asteroidlist.append(asteroid5)

# ////////////////////////////////////////// ASTEROIDES (CASSES)
asteroidlist_broken = []
asteroid1_broken = pygame.image.load("data/sprites/asteroids/broken1.png").convert_alpha()
asteroidlist_broken.append(asteroid1_broken)
asteroid2_broken = pygame.image.load("data/sprites/asteroids/broken2.png").convert_alpha()
asteroidlist_broken.append(asteroid2_broken)
asteroid3_broken = pygame.image.load("data/sprites/asteroids/broken3.png").convert_alpha()
asteroidlist_broken.append(asteroid3_broken)
asteroid4_broken = pygame.image.load("data/sprites/asteroids/broken4.png").convert_alpha()
asteroidlist_broken.append(asteroid4_broken)
asteroid5_broken = pygame.image.load("data/sprites/asteroids/broken5.png").convert_alpha()
asteroidlist_broken.append(asteroid5_broken)



# ///////////////////////////////////////////////////////////////////////////////////////// WEAPONS
weaponlist_all = []

# ////////////////////////////////////////// ROCKETS
rocket_red = pygame.image.load("data/sprites/bullets/rockets/red.png").convert_alpha()
weaponlist_all.append(rocket_red)
rocket_green = pygame.image.load("data/sprites/bullets/rockets/green.png").convert_alpha()
weaponlist_all.append(rocket_green)
rocket_blue = pygame.image.load("data/sprites/bullets/rockets/blue.png").convert_alpha()
weaponlist_all.append(rocket_blue)
rocket_gold = pygame.image.load("data/sprites/bullets/rockets/gold.png").convert_alpha()
weaponlist_all.append(rocket_gold)

# ////////////////////////////////////////// LASERS
laser_red = pygame.image.load("data/sprites/bullets/lasers/red.png").convert_alpha()
weaponlist_all.append(laser_red)
laser_green = pygame.image.load("data/sprites/bullets/lasers/green.png").convert_alpha()
weaponlist_all.append(laser_green)
laser_blue = pygame.image.load("data/sprites/bullets/lasers/blue.png").convert_alpha()
weaponlist_all.append(laser_blue)
laser_gold = pygame.image.load("data/sprites/bullets/lasers/gold.png").convert_alpha()
weaponlist_all.append(laser_gold)



# ///////////////////////////////////////////////////////////////////////////////////////// EXPLOSION 1

# ////////////////////////////////////////// BLUE
explosion1list_blue = []
explosion1_blue_1 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase1.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_1)
explosion1_blue_2 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase2.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_2)
explosion1_blue_3 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase3.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_3)
explosion1_blue_4 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase4.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_4)
explosion1_blue_5 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase5.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_5)
explosion1_blue_6 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase6.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_6)
explosion1_blue_7 = pygame.image.load("data/sprites/explosions/explosion1/blue/phase7.png").convert_alpha()
explosion1list_blue.append(explosion1_blue_7)

# ////////////////////////////////////////// GOLD
explosion1list_gold = []
explosion1_gold_1 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase1.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_1)
explosion1_gold_2 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase2.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_2)
explosion1_gold_3 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase3.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_3)
explosion1_gold_4 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase4.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_4)
explosion1_gold_5 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase5.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_5)
explosion1_gold_6 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase6.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_6)
explosion1_gold_7 = pygame.image.load("data/sprites/explosions/explosion1/gold/phase7.png").convert_alpha()
explosion1list_gold.append(explosion1_gold_7)

# ////////////////////////////////////////// GREEN
explosion1list_green = []
explosion1_green_1 = pygame.image.load("data/sprites/explosions/explosion1/green/phase1.png").convert_alpha()
explosion1list_green.append(explosion1_green_1)
explosion1_green_2 = pygame.image.load("data/sprites/explosions/explosion1/green/phase2.png").convert_alpha()
explosion1list_green.append(explosion1_green_2)
explosion1_green_3 = pygame.image.load("data/sprites/explosions/explosion1/green/phase3.png").convert_alpha()
explosion1list_green.append(explosion1_green_3)
explosion1_green_4 = pygame.image.load("data/sprites/explosions/explosion1/green/phase4.png").convert_alpha()
explosion1list_green.append(explosion1_green_4)
explosion1_green_5 = pygame.image.load("data/sprites/explosions/explosion1/green/phase5.png").convert_alpha()
explosion1list_green.append(explosion1_green_5)
explosion1_green_6 = pygame.image.load("data/sprites/explosions/explosion1/green/phase6.png").convert_alpha()
explosion1list_green.append(explosion1_green_6)
explosion1_green_7 = pygame.image.load("data/sprites/explosions/explosion1/green/phase7.png").convert_alpha()
explosion1list_green.append(explosion1_green_7)

# ////////////////////////////////////////// BLUE
explosion1list_red = []
explosion1_red_1 = pygame.image.load("data/sprites/explosions/explosion1/red/phase1.png").convert_alpha()
explosion1list_red.append(explosion1_red_1)
explosion1_red_2 = pygame.image.load("data/sprites/explosions/explosion1/red/phase2.png").convert_alpha()
explosion1list_red.append(explosion1_red_2)
explosion1_red_3 = pygame.image.load("data/sprites/explosions/explosion1/red/phase3.png").convert_alpha()
explosion1list_red.append(explosion1_red_3)
explosion1_red_4 = pygame.image.load("data/sprites/explosions/explosion1/red/phase4.png").convert_alpha()
explosion1list_red.append(explosion1_red_4)
explosion1_red_5 = pygame.image.load("data/sprites/explosions/explosion1/red/phase5.png").convert_alpha()
explosion1list_red.append(explosion1_red_5)
explosion1_red_6 = pygame.image.load("data/sprites/explosions/explosion1/red/phase6.png").convert_alpha()
explosion1list_red.append(explosion1_red_6)
explosion1_red_7 = pygame.image.load("data/sprites/explosions/explosion1/red/phase7.png").convert_alpha()
explosion1list_red.append(explosion1_red_7)





# ///////////////////////////////////////////////////////////////////////////////////////// EXPLOSION 2

# ////////////////////////////////////////// BLUE
explosion2list_blue = []
explosion2_blue_1 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase1.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_1)
explosion2_blue_2 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase2.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_2)
explosion2_blue_3 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase3.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_3)
explosion2_blue_4 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase4.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_4)
explosion2_blue_5 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase5.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_5)
explosion2_blue_6 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase6.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_6)
explosion2_blue_7 = pygame.image.load("data/sprites/explosions/explosion2/blue/phase7.png").convert_alpha()
explosion2list_blue.append(explosion2_blue_7)

# ////////////////////////////////////////// GOLD
explosion2list_gold = []
explosion2_gold_1 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase1.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_1)
explosion2_gold_2 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase2.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_2)
explosion2_gold_3 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase3.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_3)
explosion2_gold_4 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase4.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_4)
explosion2_gold_5 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase5.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_5)
explosion2_gold_6 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase6.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_6)
explosion2_gold_7 = pygame.image.load("data/sprites/explosions/explosion2/gold/phase7.png").convert_alpha()
explosion2list_gold.append(explosion2_gold_7)

# ////////////////////////////////////////// GREEN
explosion2list_green = []
explosion2_green_1 = pygame.image.load("data/sprites/explosions/explosion2/green/phase1.png").convert_alpha()
explosion2list_green.append(explosion2_green_1)
explosion2_green_2 = pygame.image.load("data/sprites/explosions/explosion2/green/phase2.png").convert_alpha()
explosion2list_green.append(explosion2_green_2)
explosion2_green_3 = pygame.image.load("data/sprites/explosions/explosion2/green/phase3.png").convert_alpha()
explosion2list_green.append(explosion2_green_3)
explosion2_green_4 = pygame.image.load("data/sprites/explosions/explosion2/green/phase4.png").convert_alpha()
explosion2list_green.append(explosion2_green_4)
explosion2_green_5 = pygame.image.load("data/sprites/explosions/explosion2/green/phase5.png").convert_alpha()
explosion2list_green.append(explosion2_green_5)
explosion2_green_6 = pygame.image.load("data/sprites/explosions/explosion2/green/phase6.png").convert_alpha()
explosion2list_green.append(explosion2_green_6)
explosion2_green_7 = pygame.image.load("data/sprites/explosions/explosion2/green/phase7.png").convert_alpha()
explosion2list_green.append(explosion2_green_7)

# ////////////////////////////////////////// BLUE
explosion2list_red = []
explosion2_red_1 = pygame.image.load("data/sprites/explosions/explosion2/red/phase1.png").convert_alpha()
explosion2list_red.append(explosion2_red_1)
explosion2_red_2 = pygame.image.load("data/sprites/explosions/explosion2/red/phase2.png").convert_alpha()
explosion2list_red.append(explosion2_red_2)
explosion2_red_3 = pygame.image.load("data/sprites/explosions/explosion2/red/phase3.png").convert_alpha()
explosion2list_red.append(explosion2_red_3)
explosion2_red_4 = pygame.image.load("data/sprites/explosions/explosion2/red/phase4.png").convert_alpha()
explosion2list_red.append(explosion2_red_4)
explosion2_red_5 = pygame.image.load("data/sprites/explosions/explosion2/red/phase5.png").convert_alpha()
explosion2list_red.append(explosion2_red_5)
explosion2_red_6 = pygame.image.load("data/sprites/explosions/explosion2/red/phase6.png").convert_alpha()
explosion2list_red.append(explosion2_red_6)
explosion2_red_7 = pygame.image.load("data/sprites/explosions/explosion2/red/phase7.png").convert_alpha()
explosion2list_red.append(explosion2_red_7)






# ///////////////////////////////////////////////////////////////////////////////////////// BLUE SHIPS
shiplist_blue = []
ship_blue_1 = pygame.image.load("data/sprites/ships/blue/ship1.png").convert_alpha()
shiplist_blue.append(ship_blue_1)
ship_blue_2 = pygame.image.load("data/sprites/ships/blue/ship2.png").convert_alpha()
shiplist_blue.append(ship_blue_2)
ship_blue_3 = pygame.image.load("data/sprites/ships/blue/ship3.png").convert_alpha()
shiplist_blue.append(ship_blue_3)
ship_blue_4 = pygame.image.load("data/sprites/ships/blue/ship4.png").convert_alpha()
shiplist_blue.append(ship_blue_4)
ship_blue_5 = pygame.image.load("data/sprites/ships/blue/ship5.png").convert_alpha()
shiplist_blue.append(ship_blue_5)
ship_blue_6 = pygame.image.load("data/sprites/ships/blue/ship6.png").convert_alpha()
shiplist_blue.append(ship_blue_6)
ship_blue_7 = pygame.image.load("data/sprites/ships/blue/ship7.png").convert_alpha()
shiplist_blue.append(ship_blue_7)
ship_blue_8 = pygame.image.load("data/sprites/ships/blue/ship8.png").convert_alpha()
shiplist_blue.append(ship_blue_8)
ship_blue_9 = pygame.image.load("data/sprites/ships/blue/ship9.png").convert_alpha()
shiplist_blue.append(ship_blue_9)
ship_blue_10 = pygame.image.load("data/sprites/ships/blue/ship10.png").convert_alpha()
shiplist_blue.append(ship_blue_10)
ship_blue_11 = pygame.image.load("data/sprites/ships/blue/ship11.png").convert_alpha()
shiplist_blue.append(ship_blue_11)
ship_blue_12 = pygame.image.load("data/sprites/ships/blue/ship12.png").convert_alpha()
shiplist_blue.append(ship_blue_12)
ship_blue_13 = pygame.image.load("data/sprites/ships/blue/ship13.png").convert_alpha()
shiplist_blue.append(ship_blue_13)
ship_blue_14 = pygame.image.load("data/sprites/ships/blue/ship14.png").convert_alpha()
shiplist_blue.append(ship_blue_14)
ship_blue_15 = pygame.image.load("data/sprites/ships/blue/ship15.png").convert_alpha()
shiplist_blue.append(ship_blue_15)
ship_blue_16 = pygame.image.load("data/sprites/ships/blue/ship16.png").convert_alpha()
shiplist_blue.append(ship_blue_16)
ship_blue_17 = pygame.image.load("data/sprites/ships/blue/ship17.png").convert_alpha()
shiplist_blue.append(ship_blue_17)
ship_blue_18 = pygame.image.load("data/sprites/ships/blue/ship18.png").convert_alpha()
shiplist_blue.append(ship_blue_18)
ship_blue_19 = pygame.image.load("data/sprites/ships/blue/ship19.png").convert_alpha()
shiplist_blue.append(ship_blue_19)
ship_blue_20 = pygame.image.load("data/sprites/ships/blue/ship20.png").convert_alpha()
shiplist_blue.append(ship_blue_20)
ship_blue_21 = pygame.image.load("data/sprites/ships/blue/ship21.png").convert_alpha()
shiplist_blue.append(ship_blue_21)
ship_blue_22 = pygame.image.load("data/sprites/ships/blue/ship22.png").convert_alpha()
shiplist_blue.append(ship_blue_22)
ship_blue_23 = pygame.image.load("data/sprites/ships/blue/ship23.png").convert_alpha()
shiplist_blue.append(ship_blue_23)
ship_blue_24 = pygame.image.load("data/sprites/ships/blue/ship24.png").convert_alpha()
shiplist_blue.append(ship_blue_24)
ship_blue_25 = pygame.image.load("data/sprites/ships/blue/ship25.png").convert_alpha()
shiplist_blue.append(ship_blue_25)


# ///////////////////////////////////////////////////////////////////////////////////////// GREEN SHIPS
shiplist_green = []
ship_green_1 = pygame.image.load("data/sprites/ships/green/ship1.png").convert_alpha()
shiplist_green.append(ship_green_1)
ship_green_2 = pygame.image.load("data/sprites/ships/green/ship2.png").convert_alpha()
shiplist_green.append(ship_green_2)
ship_green_3 = pygame.image.load("data/sprites/ships/green/ship3.png").convert_alpha()
shiplist_green.append(ship_green_3)
ship_green_4 = pygame.image.load("data/sprites/ships/green/ship4.png").convert_alpha()
shiplist_green.append(ship_green_4)
ship_green_5 = pygame.image.load("data/sprites/ships/green/ship5.png").convert_alpha()
shiplist_green.append(ship_green_5)
ship_green_6 = pygame.image.load("data/sprites/ships/green/ship6.png").convert_alpha()
shiplist_green.append(ship_green_6)
ship_green_7 = pygame.image.load("data/sprites/ships/green/ship7.png").convert_alpha()
shiplist_green.append(ship_green_7)
ship_green_8 = pygame.image.load("data/sprites/ships/green/ship8.png").convert_alpha()
shiplist_green.append(ship_green_8)
ship_green_9 = pygame.image.load("data/sprites/ships/green/ship9.png").convert_alpha()
shiplist_green.append(ship_green_9)
ship_green_10 = pygame.image.load("data/sprites/ships/green/ship10.png").convert_alpha()
shiplist_green.append(ship_green_10)
ship_green_11 = pygame.image.load("data/sprites/ships/green/ship11.png").convert_alpha()
shiplist_green.append(ship_green_11)
ship_green_12 = pygame.image.load("data/sprites/ships/green/ship12.png").convert_alpha()
shiplist_green.append(ship_green_12)
ship_green_13 = pygame.image.load("data/sprites/ships/green/ship13.png").convert_alpha()
shiplist_green.append(ship_green_13)
ship_green_14 = pygame.image.load("data/sprites/ships/green/ship14.png").convert_alpha()
shiplist_green.append(ship_green_14)
ship_green_15 = pygame.image.load("data/sprites/ships/green/ship15.png").convert_alpha()
shiplist_green.append(ship_green_15)
ship_green_16 = pygame.image.load("data/sprites/ships/green/ship16.png").convert_alpha()
shiplist_green.append(ship_green_16)
ship_green_17 = pygame.image.load("data/sprites/ships/green/ship17.png").convert_alpha()
shiplist_green.append(ship_green_17)
ship_green_18 = pygame.image.load("data/sprites/ships/green/ship18.png").convert_alpha()
shiplist_green.append(ship_green_18)
ship_green_19 = pygame.image.load("data/sprites/ships/green/ship19.png").convert_alpha()
shiplist_green.append(ship_green_19)
ship_green_20 = pygame.image.load("data/sprites/ships/green/ship20.png").convert_alpha()
shiplist_green.append(ship_green_20)
ship_green_21 = pygame.image.load("data/sprites/ships/green/ship21.png").convert_alpha()
shiplist_green.append(ship_green_21)
ship_green_22 = pygame.image.load("data/sprites/ships/green/ship22.png").convert_alpha()
shiplist_green.append(ship_green_22)
ship_green_23 = pygame.image.load("data/sprites/ships/green/ship23.png").convert_alpha()
shiplist_green.append(ship_green_23)
ship_green_24 = pygame.image.load("data/sprites/ships/green/ship24.png").convert_alpha()
shiplist_green.append(ship_green_24)
ship_green_25 = pygame.image.load("data/sprites/ships/green/ship25.png").convert_alpha()
shiplist_green.append(ship_green_25)


# ///////////////////////////////////////////////////////////////////////////////////////// RED SHIPS
shiplist_red = []
ship_red_1 = pygame.image.load("data/sprites/ships/red/ship1.png").convert_alpha()
shiplist_red.append(ship_red_1)
ship_red_2 = pygame.image.load("data/sprites/ships/red/ship2.png").convert_alpha()
shiplist_red.append(ship_red_2)
ship_red_3 = pygame.image.load("data/sprites/ships/red/ship3.png").convert_alpha()
shiplist_red.append(ship_red_3)
ship_red_4 = pygame.image.load("data/sprites/ships/red/ship4.png").convert_alpha()
shiplist_red.append(ship_red_4)
ship_red_5 = pygame.image.load("data/sprites/ships/red/ship5.png").convert_alpha()
shiplist_red.append(ship_red_5)
ship_red_6 = pygame.image.load("data/sprites/ships/red/ship6.png").convert_alpha()
shiplist_red.append(ship_red_6)
ship_red_7 = pygame.image.load("data/sprites/ships/red/ship7.png").convert_alpha()
shiplist_red.append(ship_red_7)
ship_red_8 = pygame.image.load("data/sprites/ships/red/ship8.png").convert_alpha()
shiplist_red.append(ship_red_8)
ship_red_9 = pygame.image.load("data/sprites/ships/red/ship9.png").convert_alpha()
shiplist_red.append(ship_red_9)
ship_red_10 = pygame.image.load("data/sprites/ships/red/ship10.png").convert_alpha()
shiplist_red.append(ship_red_10)
ship_red_11 = pygame.image.load("data/sprites/ships/red/ship11.png").convert_alpha()
shiplist_red.append(ship_red_11)
ship_red_12 = pygame.image.load("data/sprites/ships/red/ship12.png").convert_alpha()
shiplist_red.append(ship_red_12)
ship_red_13 = pygame.image.load("data/sprites/ships/red/ship13.png").convert_alpha()
shiplist_red.append(ship_red_13)
ship_red_14 = pygame.image.load("data/sprites/ships/red/ship14.png").convert_alpha()
shiplist_red.append(ship_red_14)
ship_red_15 = pygame.image.load("data/sprites/ships/red/ship15.png").convert_alpha()
shiplist_red.append(ship_red_15)
ship_red_16 = pygame.image.load("data/sprites/ships/red/ship16.png").convert_alpha()
shiplist_red.append(ship_red_16)
ship_red_17 = pygame.image.load("data/sprites/ships/red/ship17.png").convert_alpha()
shiplist_red.append(ship_red_17)
ship_red_18 = pygame.image.load("data/sprites/ships/red/ship18.png").convert_alpha()
shiplist_red.append(ship_red_18)
ship_red_19 = pygame.image.load("data/sprites/ships/red/ship19.png").convert_alpha()
shiplist_red.append(ship_red_19)
ship_red_20 = pygame.image.load("data/sprites/ships/red/ship20.png").convert_alpha()
shiplist_red.append(ship_red_20)
ship_red_21 = pygame.image.load("data/sprites/ships/red/ship21.png").convert_alpha()
shiplist_red.append(ship_red_21)
ship_red_22 = pygame.image.load("data/sprites/ships/red/ship22.png").convert_alpha()
shiplist_red.append(ship_red_22)
ship_red_23 = pygame.image.load("data/sprites/ships/red/ship23.png").convert_alpha()
shiplist_red.append(ship_red_23)
ship_red_24 = pygame.image.load("data/sprites/ships/red/ship24.png").convert_alpha()
shiplist_red.append(ship_red_24)
ship_red_25 = pygame.image.load("data/sprites/ships/red/ship25.png").convert_alpha()
shiplist_red.append(ship_red_25)


# ///////////////////////////////////////////////////////////////////////////////////////// YELLOW SHIPS
shiplist_yellow = []
ship_yellow_1 = pygame.image.load("data/sprites/ships/yellow/ship1.png").convert_alpha()
shiplist_yellow.append(ship_yellow_1)
ship_yellow_2 = pygame.image.load("data/sprites/ships/yellow/ship2.png").convert_alpha()
shiplist_yellow.append(ship_yellow_2)
ship_yellow_3 = pygame.image.load("data/sprites/ships/yellow/ship3.png").convert_alpha()
shiplist_yellow.append(ship_yellow_3)
ship_yellow_4 = pygame.image.load("data/sprites/ships/yellow/ship4.png").convert_alpha()
shiplist_yellow.append(ship_yellow_4)
ship_yellow_5 = pygame.image.load("data/sprites/ships/yellow/ship5.png").convert_alpha()
shiplist_yellow.append(ship_yellow_5)
ship_yellow_6 = pygame.image.load("data/sprites/ships/yellow/ship6.png").convert_alpha()
shiplist_yellow.append(ship_yellow_6)
ship_yellow_7 = pygame.image.load("data/sprites/ships/yellow/ship7.png").convert_alpha()
shiplist_yellow.append(ship_yellow_7)
ship_yellow_8 = pygame.image.load("data/sprites/ships/yellow/ship8.png").convert_alpha()
shiplist_yellow.append(ship_yellow_8)
ship_yellow_9 = pygame.image.load("data/sprites/ships/yellow/ship9.png").convert_alpha()
shiplist_yellow.append(ship_yellow_9)
ship_yellow_10 = pygame.image.load("data/sprites/ships/yellow/ship10.png").convert_alpha()
shiplist_yellow.append(ship_yellow_10)
ship_yellow_11 = pygame.image.load("data/sprites/ships/yellow/ship11.png").convert_alpha()
shiplist_yellow.append(ship_yellow_11)
ship_yellow_12 = pygame.image.load("data/sprites/ships/yellow/ship12.png").convert_alpha()
shiplist_yellow.append(ship_yellow_12)
ship_yellow_13 = pygame.image.load("data/sprites/ships/yellow/ship13.png").convert_alpha()
shiplist_yellow.append(ship_yellow_13)
ship_yellow_14 = pygame.image.load("data/sprites/ships/yellow/ship14.png").convert_alpha()
shiplist_yellow.append(ship_yellow_14)
ship_yellow_15 = pygame.image.load("data/sprites/ships/yellow/ship15.png").convert_alpha()
shiplist_yellow.append(ship_yellow_15)
ship_yellow_16 = pygame.image.load("data/sprites/ships/yellow/ship16.png").convert_alpha()
shiplist_yellow.append(ship_yellow_16)
ship_yellow_17 = pygame.image.load("data/sprites/ships/yellow/ship17.png").convert_alpha()
shiplist_yellow.append(ship_yellow_17)
ship_yellow_18 = pygame.image.load("data/sprites/ships/yellow/ship18.png").convert_alpha()
shiplist_yellow.append(ship_yellow_18)
ship_yellow_19 = pygame.image.load("data/sprites/ships/yellow/ship19.png").convert_alpha()
shiplist_yellow.append(ship_yellow_19)
ship_yellow_20 = pygame.image.load("data/sprites/ships/yellow/ship20.png").convert_alpha()
shiplist_yellow.append(ship_yellow_20)
ship_yellow_21 = pygame.image.load("data/sprites/ships/yellow/ship21.png").convert_alpha()
shiplist_yellow.append(ship_yellow_21)
ship_yellow_22 = pygame.image.load("data/sprites/ships/yellow/ship22.png").convert_alpha()
shiplist_yellow.append(ship_yellow_22)
ship_yellow_23 = pygame.image.load("data/sprites/ships/yellow/ship23.png").convert_alpha()
shiplist_yellow.append(ship_yellow_23)
ship_yellow_24 = pygame.image.load("data/sprites/ships/yellow/ship24.png").convert_alpha()
shiplist_yellow.append(ship_yellow_24)
ship_yellow_25 = pygame.image.load("data/sprites/ships/yellow/ship25.png").convert_alpha()
shiplist_yellow.append(ship_yellow_25)


# ///////////////////////////////////////////////////////////////////////////////////////// PINK SHIPS
shiplist_pink = []
ship_pink_1 = pygame.image.load("data/sprites/ships/pink/ship1.png").convert_alpha()
shiplist_pink.append(ship_pink_1)
ship_pink_2 = pygame.image.load("data/sprites/ships/pink/ship2.png").convert_alpha()
shiplist_pink.append(ship_pink_2)
ship_pink_3 = pygame.image.load("data/sprites/ships/pink/ship3.png").convert_alpha()
shiplist_pink.append(ship_pink_3)
ship_pink_4 = pygame.image.load("data/sprites/ships/pink/ship4.png").convert_alpha()
shiplist_pink.append(ship_pink_4)
ship_pink_5 = pygame.image.load("data/sprites/ships/pink/ship5.png").convert_alpha()
shiplist_pink.append(ship_pink_5)
ship_pink_6 = pygame.image.load("data/sprites/ships/pink/ship6.png").convert_alpha()
shiplist_pink.append(ship_pink_6)
ship_pink_7 = pygame.image.load("data/sprites/ships/pink/ship7.png").convert_alpha()
shiplist_pink.append(ship_pink_7)
ship_pink_8 = pygame.image.load("data/sprites/ships/pink/ship8.png").convert_alpha()
shiplist_pink.append(ship_pink_8)
ship_pink_9 = pygame.image.load("data/sprites/ships/pink/ship9.png").convert_alpha()
shiplist_pink.append(ship_pink_9)
ship_pink_10 = pygame.image.load("data/sprites/ships/pink/ship10.png").convert_alpha()
shiplist_pink.append(ship_pink_10)
ship_pink_11 = pygame.image.load("data/sprites/ships/pink/ship11.png").convert_alpha()
shiplist_pink.append(ship_pink_11)
ship_pink_12 = pygame.image.load("data/sprites/ships/pink/ship12.png").convert_alpha()
shiplist_pink.append(ship_pink_12)
ship_pink_13 = pygame.image.load("data/sprites/ships/pink/ship13.png").convert_alpha()
shiplist_pink.append(ship_pink_13)
ship_pink_14 = pygame.image.load("data/sprites/ships/pink/ship14.png").convert_alpha()
shiplist_pink.append(ship_pink_14)
ship_pink_15 = pygame.image.load("data/sprites/ships/pink/ship15.png").convert_alpha()
shiplist_pink.append(ship_pink_15)
ship_pink_16 = pygame.image.load("data/sprites/ships/pink/ship16.png").convert_alpha()
shiplist_pink.append(ship_pink_16)
ship_pink_17 = pygame.image.load("data/sprites/ships/pink/ship17.png").convert_alpha()
shiplist_pink.append(ship_pink_17)
ship_pink_18 = pygame.image.load("data/sprites/ships/pink/ship18.png").convert_alpha()
shiplist_pink.append(ship_pink_18)
ship_pink_19 = pygame.image.load("data/sprites/ships/pink/ship19.png").convert_alpha()
shiplist_pink.append(ship_pink_19)
ship_pink_20 = pygame.image.load("data/sprites/ships/pink/ship20.png").convert_alpha()
shiplist_pink.append(ship_pink_20)
ship_pink_21 = pygame.image.load("data/sprites/ships/pink/ship21.png").convert_alpha()
shiplist_pink.append(ship_pink_21)
ship_pink_22 = pygame.image.load("data/sprites/ships/pink/ship22.png").convert_alpha()
shiplist_pink.append(ship_pink_22)
ship_pink_23 = pygame.image.load("data/sprites/ships/pink/ship23.png").convert_alpha()
shiplist_pink.append(ship_pink_23)
ship_pink_24 = pygame.image.load("data/sprites/ships/pink/ship24.png").convert_alpha()
shiplist_pink.append(ship_pink_24)
ship_pink_25 = pygame.image.load("data/sprites/ships/pink/ship25.png").convert_alpha()
shiplist_pink.append(ship_pink_25)


# ///////////////////////////////////////////////////////////////////////////////////////// ALL SHIPS
shiplist_all = [shiplist_blue, shiplist_green, shiplist_red, shiplist_yellow, shiplist_pink]




#EXPLOSIONS
#SHIPS
#BACKGROUNDS
#MURS
#PROJECTILES
#POWERUPS




