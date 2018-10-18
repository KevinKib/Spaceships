# -*- coding: utf-8 -*-

import math

def Bounce(Player, Wall):
    # Valeurs--------------------------------------------------------------------
    RotateConstantX = Player.rect.centerx - (Player.scale[0] / 2) - Player.rect.x
    RotateConstantY = Player.rect.centery - (Player.scale[1] / 2) - Player.rect.y
    # Player.health -= 50 ?
    facteur = 0.75  # permet de réduire la vitesse lorsqu'on touche un mur

    # Conditions pour détecter la zone
    Top = Player.oldy + Player.scale[1] - 6 - RotateConstantY < Wall.rect.y
    Bottom = Player.oldy >= Wall.rect.y + Wall.scale[1] - 6 - RotateConstantY
    Left = Player.oldx + Player.scale[0] - 6 - RotateConstantX < Wall.rect.x
    Right = Player.oldx > Wall.rect.x + Wall.scale[0] - 6 - RotateConstantX

    # Système de collision
    if Left:
        Player.vx = -Player.vx
        Player.rect.x = Player.oldx
        Player.vx = Player.vx * facteur
    elif Right:
        Player.vx = -Player.vx
        Player.rect.x = Wall.rect.right
        Player.vx = Player.vx * facteur
    elif Top:
        Player.vy = -Player.vy
        Player.rect.y = Player.oldy
        Player.vy = Player.vy * facteur
    elif Bottom:
        Player.vy = -Player.vy
        Player.rect.y = Player.oldy
        Player.vy = Player.vy * facteur


def Bounce_asteroids(Asteroid, Wall):
    # Valeurs--------------------------------------------------------------------
    RotateConstantX = Asteroid.rect.centerx - (Asteroid.scale[0] / 2) - Asteroid.rect.x
    RotateConstantY = Asteroid.rect.centery - (Asteroid.scale[1] / 2) - Asteroid.rect.y

    # Conditions pour détecter la zone
    Top = Asteroid.oldy + Asteroid.scale[1] - 6 - RotateConstantY < Wall.rect.y
    Bottom = Asteroid.oldy >= Wall.rect.y + Wall.scale[1] - 6 - RotateConstantY
    Left = Asteroid.oldx + Asteroid.scale[0] - 6 - RotateConstantX < Wall.rect.x
    Right = Asteroid.oldx > Wall.rect.x + Wall.scale[0] - 6 - RotateConstantX

    # Système de collision
    if Left:
        Asteroid.vx = -Asteroid.vx
        Asteroid.rect.x = Asteroid.oldx
    elif Right:
        Asteroid.vx = -Asteroid.vx
        Asteroid.rect.x = Wall.rect.right
    elif Top:
        Asteroid.vy = -Asteroid.vy
        Asteroid.rect.y = Asteroid.oldy
    elif Bottom:
        Asteroid.vy = -Asteroid.vy
        Asteroid.rect.y = Asteroid.oldy


def Bounce_players_old(Player1, Player2):
    facteur = 0.75  # permet de réduire la vitesse lorsqu'on touche un mur

    def invert_vx():
        Player1.vx = -Player1.vx
        Player1.rect.x = Player1.oldx
        Player1.vx = Player1.vx * facteur

        Player2.vx = -Player2.vx
        Player2.rect.x = Player2.oldx
        Player2.vx = Player2.vx * facteur

    def invert_vy():
        Player1.vy = -Player1.vy
        Player1.rect.y = Player1.oldy
        Player1.vy = Player1.vy * facteur

        Player2.vy = -Player2.vy
        Player2.rect.y = Player2.oldy
        Player2.vy = Player2.vy * facteur

    def exchange_vx():
        Player1.vx = Player2.vx
        Player1.rect.x = Player1.oldx
        Player1.vx = Player1.vx * facteur

        Player2.vx = Player1.vx
        Player2.rect.x = Player2.oldx
        Player2.vx = Player2.vx * facteur

    def exchange_vy():
        Player1.vy = Player2.vy
        Player1.rect.y = Player1.oldy
        Player1.vy = Player1.vy * facteur

        Player2.vy = Player1.vy
        Player2.rect.y = Player2.oldy
        Player2.vy = Player2.vy * facteur


    if (Player1.vx >= 0 and Player2.vx < 0) or (Player1.vx < 0 and Player2.vx >= 0):
        invert_vx()

    if (Player1.vy >= 0 and Player2.vy < 0) or (Player1.vy < 0 and Player2.vy >= 0):
        invert_vy()

    if (Player1.vx >= 0 and Player2.vx >= 0) or (Player1.vx < 0 and Player2.vx < 0):
        exchange_vx()

    if (Player1.vy >= 0 and Player2.vy >= 0) or (Player1.vy < 0 and Player2.vy < 0):
        exchange_vy()


def Bounce_players(Player1, Player2):
    vectorx = Player1.rect.centerx - Player2.rect.centerx
    vectory = Player1.rect.centery - Player2.rect.centery
    vector = (vectorx, vectory)

    n = math.sqrt(vectorx ** 2 + vectory ** 2)

    if n == 0:
        n = 0.000001

    vectorx = vectorx / n
    vectory = vectory / n

    speed = 1

    Player1.vx += vectorx * speed
    Player1.vy += vectory * speed

    Player2.vx += -vectorx * speed
    Player2.vy += -vectory * speed

    if abs(Player1.vx) >= Player1.maximum_speed:
        Player1.vx = Player1.maximum_speed * math.copysign(1.0, Player1.vx)
    if abs(Player1.vy) >= Player1.maximum_speed:
        Player1.vy = Player1.maximum_speed * math.copysign(1.0, Player1.vy)

    if abs(Player2.vx) >= Player2.maximum_speed:
        Player2.vx = Player2.maximum_speed * math.copysign(1.0, Player2.vx)
    if abs(Player2.vy) >= Player2.maximum_speed:
        Player2.vy = Player2.maximum_speed * math.copysign(1.0, Player2.vy)