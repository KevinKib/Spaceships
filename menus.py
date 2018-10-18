# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import fonts

J1_selected_ship = "Undefined"
J1_selected_weapon = "Undefined"

J2_selected_ship = "Undefined"
J2_selected_weapon = "Undefined"

Instance = "Undefined"
Level = "Undefined"


class Menu():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((992, 736))
        pygame.display.set_caption("Spaceships - " + str(self.caption))

        self.J1 = "Undefined"
        self.J2 = "Undefined"
        self.Level = "Undefined"

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                self.interactions()
            self.screen.blit(self.image,(0,0))
            pygame.display.update()


class Main(Menu):
    def __init__(self):
        self.caption = "Menu principal"

        import sounds
        pygame.mixer.music.load(sounds.menu_music)
        pygame.mixer.music.play(-1)

        Menu.__init__(self)

        import sprites
        self.image = sprites.main

    def interactions(self):
        keys = pygame.key.get_pressed()

        if keys[K_F1]:
            GameMode().run()

        if keys[K_F2]:
            import instances
            instances.LevelCreator().run()

        if keys[K_F7]:
            import instances
            instances.StupideIA_BETA().run()

        if keys[K_ESCAPE] or keys[K_F3]:
            pygame.quit()


class GameMode(Menu):
    def __init__(self):
        self.caption = "Choix du mode de jeu"
        Menu.__init__(self)
        import sprites
        self.image = sprites.mode

    def interactions(self):
        keys = pygame.key.get_pressed()
        global Instance

        if keys[K_F1]:
            import instances
            Instance = instances.PlayerVsPlayer()
            SelectShip_J1().run()

        if keys[K_F2]:
            import instances
            GameDifficulty().run()

        if keys[K_ESCAPE]:
            Main().run()


class GameDifficulty(Menu):
    def __init__(self):
        self.caption = "Choix de la difficulté"
        Menu.__init__(self)
        import sprites
        self.image = sprites.difficulty

    def interactions(self):
        keys = pygame.key.get_pressed()
        global Instance

        if keys[K_F1]:
            import instances
            Instance = instances.Asteroids("normal")
            SelectShip_J1().run()

        if keys[K_F2]:
            import instances
            Instance = instances.Asteroids("difficult")
            SelectShip_J1().run()

        if keys[K_F3]:
            import instances
            Instance = instances.Asteroids("survival")
            SelectShip_J1().run()

        if keys[K_F7]:
            import instances
            Instance = instances.Asteroids("brutal")
            SelectShip_J1().run()

        if keys[K_ESCAPE]:
            GameMode().run()


class SelectShip_J1(Menu):
    def __init__(self):
        self.caption = "Joueur 1: Choix du vaisseau"
        Menu.__init__(self)
        import sprites
        import weapons

        self.image = sprites.J1_ship

        self.model = 0
        self.color = 0
        self.weapon_ID = 0

        J1_selected_ship = sprites.shiplist_all[self.color][self.model]
        J1_selected_weapon = weapons.weaponlist[self.weapon_ID]

        self.shown_ship = pygame.transform.scale(J1_selected_ship,(128,128))
        self.shown_weapon = pygame.transform.scale(J1_selected_weapon.sprite,(128,128))

    def interactions(self):
        keys = pygame.key.get_pressed()

        # ////////////////////////////// MODIF VAISSEAU
        if keys[K_RIGHT]:
            self.model += 1
            if self.model > 24:
                self.model = 0

        if keys[K_LEFT]:
            self.model -= 1
            if self.model < 0:
                self.model = 24

        if keys[K_UP]:
            self.color += 1
            if self.color > 4:
                self.color = 0

        if keys[K_DOWN]:
            self.color -= 1
            if self.color < 0:
                self.color = 4

        # ////////////////////////////// MODIF ARME
        if keys[K_RCTRL]:
            self.weapon_ID += 1
            if self.weapon_ID > 7:
                self.weapon_ID = 0

        if keys[K_LCTRL]:
            self.weapon_ID -= 1
            if self.weapon_ID < 0:
                self.weapon_ID = 7


        if keys[K_F1]:
            import levels
            global Instance

            if Instance.name == "Asteroids":
                Instance.run(levels.Empty,J1_selected_ship,J1_selected_weapon)
            elif Instance.name == "PlayerVsPlayer":
                SelectShip_J2().run()

        if keys[K_ESCAPE]:
            if Instance.name == "Asteroids":
                GameDifficulty().run()
            elif Instance.name == "PlayerVsPlayer":
                GameMode().run()

    def update(self):
        import sprites
        import weapons
        global J1_selected_ship
        global J1_selected_weapon

        J1_selected_ship = sprites.shiplist_all[self.color][self.model]
        self.shown_ship = pygame.transform.scale(sprites.shiplist_all[self.color][self.model], (128,128))
        J1_selected_weapon = weapons.weaponlist[self.weapon_ID]
        self.shown_weapon = pygame.transform.scale(J1_selected_weapon.sprite,(128,128))

        self.screen.blit(self.shown_ship, (345, 264))
        self.screen.blit(self.shown_weapon, (557, 261))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                self.interactions()
            self.screen.blit(self.image,(0,0))
            self.update()
            pygame.display.update()


class SelectShip_J2(Menu):
    def __init__(self):
        self.caption = "Joueur 2: Choix du vaisseau"
        Menu.__init__(self)
        import sprites
        import weapons

        self.image = sprites.J2_ship

        self.model = 0
        self.color = 0
        self.weapon_ID = 0

        J2_selected_ship = sprites.shiplist_all[self.color][self.model]
        J2_selected_weapon = weapons.weaponlist[self.weapon_ID]

        self.shown_ship = pygame.transform.scale(J1_selected_ship,(128,128))
        self.shown_weapon = pygame.transform.scale(J1_selected_weapon.sprite,(128,128))

    def interactions(self):
        keys = pygame.key.get_pressed()

        # ////////////////////////////// MODIF VAISSEAU
        if keys[K_RIGHT]:
            self.model += 1
            if self.model > 24:
                self.model = 0

        if keys[K_LEFT]:
            self.model -= 1
            if self.model < 0:
                self.model = 24

        if keys[K_UP]:
            self.color += 1
            if self.color > 4:
                self.color = 0

        if keys[K_DOWN]:
            self.color -= 1
            if self.color < 0:
                self.color = 4

        # ////////////////////////////// MODIF ARME
        if keys[K_RCTRL]:
            self.weapon_ID += 1
            if self.weapon_ID > 7:
                self.weapon_ID = 0

        if keys[K_LCTRL]:
            self.weapon_ID -= 1
            if self.weapon_ID < 0:
                self.weapon_ID = 7


        if keys[K_F1]:
            SelectLevel().run()

        if keys[K_ESCAPE]:
            SelectShip_J1().run()

    def update(self):
        import sprites
        import weapons
        global J2_selected_ship
        global J2_selected_weapon

        J2_selected_ship = sprites.shiplist_all[self.color][self.model]
        self.shown_ship = pygame.transform.scale(sprites.shiplist_all[self.color][self.model], (128,128))
        J2_selected_weapon = weapons.weaponlist[self.weapon_ID]
        self.shown_weapon = pygame.transform.scale(J2_selected_weapon.sprite,(128,128))

        self.screen.blit(self.shown_ship, (345, 264))
        self.screen.blit(self.shown_weapon, (557, 261))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                self.interactions()
            self.screen.blit(self.image,(0,0))
            self.update()
            pygame.display.update()


class SelectLevel(Menu):
    def __init__(self):
        self.caption = "Choix du niveau"
        Menu.__init__(self)
        import sprites
        self.image = sprites.level

        import levels
        self.levelID = 0
        Level = levels.levellist[self.levelID]

    def interactions(self):
        import levels
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            self.levelID +=1
            if self.levelID > len(levels.levellist)-1:
                self.levelID = 0

        if keys[K_LEFT]:
            self.levelID -=1
            if self.levelID < 0:
                self.levelID = len(levels.levellist)-1

        if keys[K_F1]:
            global Instance
            Instance.run(Level,J1_selected_ship,J1_selected_weapon,J2_selected_ship,J2_selected_weapon)

        if keys[K_ESCAPE]:
            SelectShip_J2().run()

    def update(self):
        import levels
        global Level
        Level = levels.levellist[self.levelID]
        level_name = fonts.font44.render(Level.name,True,fonts.white)
        self.screen.blit(level_name, (248,328))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                self.interactions()
            self.screen.blit(self.image,(0,0))
            self.update()
            pygame.display.update()