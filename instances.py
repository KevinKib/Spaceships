# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import levels
import collisions
import menus
import fonts

class Instance:
    def __init__(self):
        pygame.init()
        pygame.key.set_repeat()
        self.screen = pygame.display.set_mode((992,736))
        self.Clock = pygame.time.Clock()

    def loadlevel(self,Level):
        # Efface tous les anciens blocs de l'écran
        sprites.block_spritelist.empty()
        x = 0
        y = 0
        for row in Level.grid:
            for element in row:
                if element == 1:
                    blocks.Destructible((x,y))
                if element == 2:
                    blocks.Indestructible((x,y))
                x += 32
            x = 0
            y += 32

    def play_music(self):
        import sounds
        pygame.mixer.music.load(sounds.game_music)
        pygame.mixer.music.play(-1)

    def leave(self):
        import menus
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                # Efface tous les anciens joueurs de l'écran
                sprites.players_spritelist.empty()
                menus.Main().run()


class StupideIA_BETA(Instance):
    def __init__(self):
        Instance.__init__(self)
        self.Level = levels.Empty

    def update_grid(self,updated_grid):
        self.Level.grid = updated_grid

    def run(self):
        self.loadlevel(self.Level)
        self.play_music()

        import weapons
        self.Player = player.Player(sprites.shiplist_all[0][0],weapons.weaponlist[0])
        self.Player.set_position((500,500))

        self.IA = stupidAI.AI(sprites.shiplist_all[1][24])

        while True:
            self.Player.controls()
            self.leave()

            sprites.all_spritelist.update()
            self.screen.blit(self.Level.background,(0,0))

            for mur in sprites.block_spritelist:
                self.screen.blit(mur.sprite, mur.rect)

            for explosion in sprites.explosion_spritelist:
                self.screen.blit(explosion.sprite, explosion.rect)

            for Bullet in sprites.bullet_spritelist:
                for mur in sprites.block_spritelist:
                    if Bullet.rect.colliderect(mur.rect):
                        if Bullet.type != "Laser" and Bullet.color != "blue":
                            Bullet.explode()
                        mur.damage(Bullet)
                for Player in sprites.players_spritelist:
                    if Bullet.rect.colliderect(Player.rect):
                        if Bullet.parent != Player:
                            Bullet.explode()
                            Player.collision(Bullet)
                            explosions.Explosion1("gold",Player.rect.center,32)

                self.screen.blit(Bullet.sprite_rotated, Bullet.rect)


            for Player in sprites.players_spritelist:
                Player.lifebar(self.screen)
                for AI in sprites.AI_spritelist:
                    AI.lifebar(self.screen)
                    for bound in self.Level.levelbounds:
                        if Player.rect.colliderect(bound):
                            collisions.Bounce(Player,bound)
                        if AI.rect.colliderect(bound):
                            collisions.Bounce(AI,bound)

                    for block in sprites.block_spritelist:
                        if Player.rect.colliderect(block.rect):
                            collisions.Bounce(Player,block)
                        if AI.rect.colliderect(block.rect):
                            collisions.Bounce(AI, block)

            self.screen.blit(self.IA.sprite_rotated, self.IA.rect)
            self.screen.blit(Player.sprite_rotated,Player.rect)

            self.IA.focus(self.Player.rect.center)

            pygame.display.update()
            self.Clock.tick(60)


class Asteroids(Instance):
    def __init__(self,difficulty):
        Instance.__init__(self)

        # Efface tous les anciens astéroïdes affichés à l'écran
        sprites.asteroid_spritelist.empty()

        self.name = "Asteroids"
        self.level = levels.Empty

        self.asteroid_timer = 0
        self.asteroid_counter = 0
        self.asteroids_onscreen = 20

        if difficulty == "normal":
            self.asteroid_delay = 50
            self.asteroid_limit = 20

        elif difficulty == "difficult":
            self.asteroid_delay = 30
            self.asteroid_limit = 50
            self.asteroids_onscreen = 30

        elif difficulty == "survival":
            self.asteroid_delay = 30
            self.asteroid_limit = 1500
            self.asteroids_onscreen = 30

        elif difficulty == "brutal":
            self.asteroid_delay = 10
            self.asteroid_limit = 1500
            self.asteroids_onscreen = 50

        class Bound:
            def __init__(self, left, top, width, height):
                self.rect = pygame.Rect(left, top, width, height)
                self.scale = (width, height)

        self.levelbounds = []
        self.asteroidbound_left = Bound(-256, -256, 32, 736 + 2 * 256)
        self.levelbounds.append(self.asteroidbound_left)
        self.asteroidbound_top = Bound(-256, -256, 992 + 2 * 256, 32)
        self.levelbounds.append(self.asteroidbound_top)
        self.asteroidbound_right = Bound(1248, -256, -32, 736 + 2 * 256)
        self.levelbounds.append(self.asteroidbound_right)
        self.asteroidbound_bottom = Bound(-256, 992, 992 + 2 * 256, -32)
        self.levelbounds.append(self.asteroidbound_bottom)

    def asteroidfield(self):
        if self.asteroid_counter < self.asteroid_limit:
            if len(sprites.asteroid_spritelist.sprites()) < self.asteroids_onscreen:
                if self.asteroid_timer > self.asteroid_delay:
                    asteroids.Asteroid()
                    self.asteroid_timer = 0
                    self.asteroid_counter += 1
                else:
                    self.asteroid_timer += 1

    def show_score(self):
        score = fonts.font22.render("Score : "+(str(self.Player.score)),True,fonts.white)
        self.screen.blit(score,(0,0))

    def check_death(self):
        if self.Player.dead:
            end = fonts.font22.render("Votre score: " + str(self.Player.score),True,fonts.white)
            esc = fonts.font22.render("Appuyez sur Echap pour retourner au menu",True,fonts.white)
            self.screen.blit(end,(332,357))
            self.screen.blit(esc, (177, 387))

    def check_win(self):
        if len(sprites.asteroid_spritelist.sprites()) == 0:
            end = fonts.font22.render("Niveau terminé ! Votre score: " + str(self.Player.score),True,fonts.white)
            esc = fonts.font22.render("Appuyez sur Echap pour retourner au menu",True,fonts.white)
            self.screen.blit(end,(177, 357))
            self.screen.blit(esc, (177, 387))

    def run(self,Level,J1_ship,J1_weapon):
        self.loadlevel(Level)
        self.play_music()

        self.Player = player.Player(J1_ship,J1_weapon)
        self.Player.set_position((496,368))
        self.Player.set_weapon(J1_weapon.weapon_type,J1_weapon.color)

        while True:
            self.Player.controls()
            self.asteroidfield()
            self.leave()
            sprites.all_spritelist.update()

            self.screen.blit(Level.background, (0, 0))

            for Bullet in sprites.bullet_spritelist:
                self.screen.blit(Bullet.sprite_rotated, Bullet.rect)

            for Asteroid in sprites.asteroid_spritelist:
                self.screen.blit(Asteroid.sprite, Asteroid.rect)
            for Explosion in sprites.explosion_spritelist:
                self.screen.blit(Explosion.sprite, Explosion.rect)

            for Player in sprites.players_spritelist:
                for bound in Level.levelbounds:
                    if Player.rect.colliderect(bound):
                        collisions.Bounce(Player,bound)
                self.screen.blit(Player.sprite_rotated, Player.rect)
                Player.lifebar(self.screen)

            for Asteroid in sprites.asteroid_spritelist:
                for Asteroid2 in sprites.asteroid_spritelist:
                    if Asteroid != Asteroid2:
                        if Asteroid.rect.colliderect(Asteroid2.rect):
                            collisions.Bounce_players(Asteroid,Asteroid2)
                for Bullet in sprites.bullet_spritelist:
                    if Bullet.rect.colliderect(Asteroid.rect):
                        Bullet.explode()
                        Asteroid.collision(Bullet)
                for Player in sprites.players_spritelist:
                    if Player.rect.colliderect(Asteroid.rect):
                        collisions.Bounce_players(self.Player, Asteroid)
                        Player.collision(Asteroid)
                        Asteroid.explode()
                for bound in self.levelbounds:
                    if Asteroid.rect.colliderect(bound):
                        collisions.Bounce_asteroids(Asteroid, bound)


            self.show_score()
            self.check_death()

            if self.asteroid_counter == self.asteroid_limit:
                self.check_win()

            pygame.display.update()
            self.Clock.tick(60)


class PlayerVsPlayer(Instance):
    def __init__(self):
        Instance.__init__(self)

        self.name = "PlayerVsPlayer"

        # Variables non utilisées, potentielles pour un mode multijoueur 3J,4J,5J,XJ
        self.playerlist = []
        self.players = 0

    def check_death(self):
        if self.Player1.dead or self.Player2.dead:
            if self.Player1.dead:
                win = fonts.font22.render("Le Joueur 2 a gagné !",True,fonts.white)
                self.screen.blit(win,(332,357))
            if self.Player2.dead:
                win = fonts.font22.render("Le Joueur 1 a gagné !",True,fonts.white)
                self.screen.blit(win,(332,357))
            esc = fonts.font22.render("Appuyez sur Echap pour retourner au menu",True,fonts.white)
            self.screen.blit(esc, (177, 387))

    def run(self,Level,J1_ship,J1_weapon,J2_ship,J2_weapon):
        self.loadlevel(Level)
        self.play_music()

        self.Player1 = player.Player(J1_ship,J1_weapon)
        self.Player1.set_position((32,32))

        self.Player2 = player.Player(J2_ship,J2_weapon)
        self.Player2.set_position((928,672))
        self.Player2.set_angle(180)
        self.Player2.rotate_sprite()

        while True:
            self.Player1.multiplayer_controls("Player 1")
            self.Player2.multiplayer_controls("Player 2")

            self.leave()

            sprites.all_spritelist.update()
            self.screen.blit(Level.background,(0,0))

            for Bullet in sprites.bullet_spritelist:
                for Block in sprites.block_spritelist:
                    if Bullet.rect.colliderect(Block.rect):
                        if Bullet.type != "Laser" and Bullet.color != "blue":
                            Bullet.explode()
                        Block.damage(Bullet)
                for Player in sprites.players_spritelist:
                    if Bullet.rect.colliderect(Player.rect):
                        if Bullet.parent != Player:
                            Bullet.explode()
                            Player.collision(Bullet)
                            explosions.Explosion1("gold",Player.rect.center,32)


                self.screen.blit(Bullet.sprite_rotated, Bullet.rect)

            for Player in sprites.players_spritelist:
                if self.Player1.rect.colliderect(self.Player2.rect) or self.Player2.rect.colliderect(self.Player1.rect):
                    collisions.Bounce_players(self.Player1, self.Player2)
                for bound in Level.levelbounds:
                    if Player.rect.colliderect(bound):
                        collisions.Bounce(Player,bound)
                for block in sprites.block_spritelist:
                    if Player.rect.colliderect(block.rect):
                        collisions.Bounce(Player,block)




            for Block in sprites.block_spritelist:
                self.screen.blit(Block.sprite, Block.rect)

            for Explosion in sprites.explosion_spritelist:
                self.screen.blit(Explosion.sprite, Explosion.rect)

            for Player in sprites.players_spritelist:
                self.screen.blit(Player.sprite_rotated,Player.rect)
                Player.lifebar(self.screen)

            self.check_death()

            pygame.display.update()
            self.Clock.tick(60)


class LevelCreator(Instance):

    def __init__(self):
        Instance.__init__(self)
        self.grid = [
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
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]
        from random import randint
        self.background = sprites.backgroundlist[(randint(0,4))]

        self.clock = pygame.time.Clock()

        self.mouseX = 0
        self.mouseY = 0
        self.rounded_mouseX = 0
        self.rounded_mouseY = 0
        self.CurrentBlockX = 0
        self.CurrentBlockY = 0
        self.CurrentTileID = 1
        self.CurrentSlot = 0

        self.CurrentTile = blocks.blocklist[1]

        self.text_timer = -1
        self.text1 = ""
        self.text2 = ""
        self.text3 = ""
        self.text4 = ""
        self.text5 = ""

        self.print_text(180, True, "Appuyer sur H pour afficher l'aide.",
                        "F1: Sauvegarder le niveau dans l'emplacement sélectionné.",
                        "1,2,3,4,5,6: Sélectionner un emplacement")

    def inputs(self):

        def save():
            if self.CurrentSlot == 0:
                self.print_text(180, False, "Vous devez choisir un emplacement avant de sauvegarder votre fichier !")
            else:
                if self.CurrentSlot == 0:
                    file = open("data/levels/custom/temporaryslot.txt", "w")
                if self.CurrentSlot == 1:
                    file = open("data/levels/custom/slot1.txt", "w")
                if self.CurrentSlot == 2:
                    file = open("data/levels/custom/slot2.txt", "w")
                if self.CurrentSlot == 3:
                    file = open("data/levels/custom/slot3.txt", "w")
                if self.CurrentSlot == 4:
                    file = open("data/levels/custom/slot4.txt", "w")
                if self.CurrentSlot == 5:
                    file = open("data/levels/custom/slot5.txt", "w")
                if self.CurrentSlot == 6:
                    file = open("data/levels/custom/slot6.txt", "w")

                for Y in range(23):
                    for X in range(31):
                        file.write(str(self.grid[Y][X]))
                        file.write(";")
                file.close()

                self.print_text(180, False, "Niveau sauvegardé dans l'emplacement ", str(self.CurrentSlot), " !")
                self.print_text(180, True, text4="Relancez le jeu pour pouvoir y jouer.")

        def place():
            self.grid[self.CurrentBlockY][self.CurrentBlockX] = self.CurrentTile.ID

        def pick():
            self.CurrentTile.ID = self.grid[self.CurrentBlockY][self.CurrentBlockX]

        def remove():
            self.grid[self.CurrentBlockY][self.CurrentBlockX] = 0

        def increase_id():
            self.CurrentTileID += 1
            if self.CurrentTileID > len(blocks.blocklist) - 1:
                self.CurrentTileID = 1
            self.CurrentTile = blocks.blocklist[self.CurrentTileID]

        def decrease_id():
            self.CurrentTileID -= 1
            if self.CurrentTileID <= 0:
                self.CurrentTileID = len(blocks.blocklist) - 1
            self.CurrentTile = blocks.blocklist[self.CurrentTileID]

        def update_mouse_position():
            self.mouseX = event.pos[0]
            self.mouseY = event.pos[1]
            self.rounded_mouseX = (self.mouseX - (self.mouseX % 32))
            self.rounded_mouseY = (self.mouseY - (self.mouseY % 32))
            self.CurrentBlockX = int(self.rounded_mouseX / 32)
            self.CurrentBlockY = int(self.rounded_mouseY / 32)

        for event in pygame.event.get():  # Evênements dûs à l'appui d'une touche sur le clavier

            if event.type == pygame.QUIT:
                pygame.quit()

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                menus.Main().run()

            if event.type == KEYDOWN and event.key == K_F1:
                save()

            if event.type == KEYDOWN:
                if event.key == K_1:
                    self.CurrentSlot = 1
                    self.print_text(180, False, "Emplacement ", str(self.CurrentSlot), " sélectionné !")
                elif event.key == K_2:
                    self.CurrentSlot = 2
                    self.print_text(180, False, "Emplacement ", str(self.CurrentSlot), " sélectionné !")
                elif event.key == K_3:
                    self.CurrentSlot = 3
                    self.print_text(180, False, "Emplacement ", str(self.CurrentSlot), " sélectionné !")
                elif event.key == K_4:
                    self.CurrentSlot = 4
                    self.print_text(180, False, "Emplacement ", str(self.CurrentSlot), " sélectionné !")
                elif event.key == K_5:
                    self.CurrentSlot = 5
                    self.print_text(180, False, "Emplacement ", str(self.CurrentSlot), " sélectionné !")
                elif event.key == K_6:
                    self.CurrentSlot = 6
                    self.print_text(180, False, "Emplacement ", str(self.CurrentSlot), " sélectionné !")

                if event.key == K_h:
                    self.print_text(180, True, "Appuyer sur H pour afficher l'aide.",
                                    "F1: Sauvegarder le niveau dans l'emplacement sélectionné.",
                                    "1,2,3,4,5,6: Sélectionner un emplacement")

            if event.type == MOUSEMOTION:
                update_mouse_position()

            if event.type == MOUSEBUTTONDOWN:

                if event.button == 1:
                    place()

                if event.button == 2:
                    pick()

                if event.button == 3:
                    remove()

                if event.button == 4:
                    increase_id()

                if event.button == 5:
                    decrease_id()

    def display(self):

        self.screen.blit(self.background,(0,0))
        for X in range(31):
            for Y in range(23):
                self.screen.blit(blocks.blocklist[self.grid[Y][X]].sprite,(X*32,Y*32))
        self.screen.blit(blocks.blocklist[self.CurrentTile.ID].sprite, (self.rounded_mouseX, self.rounded_mouseY))

    def print_text(self, duration, linebreak=True, text1="", text2="", text3="", text4="", text5=""):
        self.text_timer = duration

        if linebreak:
            if not(text1 == ""):
                self.text1 = fonts.font22.render(text1, True, fonts.white)
            if not(text2 == ""):
                self.text2 = fonts.font22.render(text2, True, fonts.white)
            if not(text3 == ""):
                self.text3 = fonts.font22.render(text3, True, fonts.white)
            if not(text4 == ""):
                self.text4 = fonts.font22.render(text4, True, fonts.white)
            if not(text4 == ""):
                self.text5 = fonts.font22.render(text5, True, fonts.white)
        else:
            text1 = text1 + text2 + text3 + text4 + text5

            self.text1 = fonts.font22.render(text1, True, fonts.white)
            self.text2 = ""
            self.text3 = ""
            self.text4 = ""
            self.text5 = ""

    def show_text(self):
        if self.text_timer > 0:
            if not (self.text1 == ""):
                self.screen.blit(self.text1, (0, 0))
            if not (self.text2 == ""):
                self.screen.blit(self.text2, (0, 20))
            if not (self.text3 == ""):
                self.screen.blit(self.text3, (0, 40))
            if not (self.text4 == ""):
                self.screen.blit(self.text4, (0, 60))
            if not (self.text5 == ""):
                self.screen.blit(self.text5, (0, 80))

            self.text_timer -= 1

        elif self.text_timer == 0:
            self.text1 = ""
            self.text2 = ""
            self.text3 = ""
            self.text_timer = -1

    def run(self):
        self.play_music()
        while True:
            self.inputs()
            self.display()
            self.show_text()
            pygame.display.flip()
            self.clock.tick(60)

import blocks
import player
import stupidAI
import asteroids
import sprites
import explosions
