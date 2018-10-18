# -*- coding: utf-8 -*-

grid = \
            [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]


closed_list = []
open_list = []
closed_list_pos = []
open_list_pos = []

# A FAIRE: GERER IMPORT D'UNE MATRICE DEPUIS INSTANCES.PY

# SCANNER LA GRILLE
# CREER UN START_NODE POUR L'IA
# CREER UN OBJECTIF_NODE POUR LE JOUEUR
# CREER UNE CLASSIC_NODE POUR CHAQUE CELLULE ? // OU // LES PROCEDER AU FUR ET A MESURE
# JE RECOCOMMANDE PREMIERE METHODE CA SINON IL FAUT SCANNER DEUX FOIS (CREATION START/OBJECTIF ET CREATION VOISINS) ?

class Node():
    def __init__(self,position,cost):
        self.position = position
        self.x, self.y = self.position
        self.cost = cost
        self.heuristic = 0
        self.distance = 0
        self.total = self.cost + self.heuristic
        self.reachable = True

class Classic_Node(Node):
    def __init__(self,parent,position,cost):
        Node.__init__(self,position,cost)
        self.parent = parent
        self.parents = []
        self.parents.extend(self.parent.parents)
        self.parents.append(self.parent)


class Start_Node(Node):
    def __init__(self,position,cost):
        Node.__init__(self,position,cost)
        self.cost = 0
        self.parent_number = 1
        self.parents = []


class Objectif_Node(Node):
    def __init__(self,position,cost):
        Node.__init__(self,position,cost)

def distance(Node1,Node2):
    distance = abs(Node1.x - Node2.x) + abs(Node1.y - Node2.y)
    return distance

def voisins(Node):  # RETOURNE TOUS LES VOISINS D'UN NOEUD
    liste_voisins = []

    Voisin_Droite = Classic_Node(Node, (Node.x + 1, Node.y), Node.cost + 10)
    if 0 <= Voisin_Droite.x <= 30 and 0 <= Voisin_Droite.y <= 22:
        if grid[Voisin_Droite.y][Voisin_Droite.x] == 0:
            liste_voisins.append(Voisin_Droite)

    Voisin_Gauche = Classic_Node(Node, (Node.x - 1, Node.y), Node.cost + 10)
    if 0 <= Voisin_Gauche.x <= 30 and 0 <= Voisin_Gauche.y <= 22:
        if grid[Voisin_Gauche.y][Voisin_Gauche.x] == 0:
            liste_voisins.append(Voisin_Gauche)

    Voisin_Haut = Classic_Node(Node, (Node.x, Node.y - 1), Node.cost + 10)
    if 0 <= Voisin_Haut.x <= 30 and 0 <= Voisin_Haut.y <= 22:
        if grid[Voisin_Haut.y][Voisin_Haut.x] == 0:
            liste_voisins.append(Voisin_Haut)

    Voisin_Bas = Classic_Node(Node, (Node.x, Node.y + 1), Node.cost + 10)
    if 0 <= Voisin_Bas.x <= 30 and 0 <= Voisin_Bas.y <= 22:
        if grid[Voisin_Bas.y][Voisin_Bas.x] == 0:
            liste_voisins.append(Voisin_Bas)

    # CREATION DES VOISINS EN DIAGONALE / NON UTILISE POUR EVITER DE COINCER L'IA DANS LES ANGLES

    """
    Voisin_Haut_Droite = Classic_Node(Node_actuelle,(Node_actuelle.x+1,Node_actuelle.y+1),Node_actuelle.cost+14)
    if Voisin_Haut_Droite.reachable:
        liste_voisins.append(Voisin_Haut_Droite)

    Voisin_Haut_Gauche = Classic_Node(Node_actuelle,(Node_actuelle.x-1,Node_actuelle.y+1),Node_actuelle.cost+14)
    if Voisin_Haut_Gauche.reachable:
        liste_voisins.append(Voisin_Haut_Gauche)

    Voisin_Bas_Droite = Classic_Node(Node_actuelle,(Node_actuelle.x+1,Node_actuelle.y-1),Node_actuelle.cost+14)
    if Voisin_Bas_Droite.reachable:
        liste_voisins.append(Voisin_Bas_Droite)

    Voisin_Bas_Gauche = Classic_Node(Node_actuelle,(Node_actuelle.x-1,Node_actuelle.y-1),Node_actuelle.cost+14)
    if Voisin_Bas_Gauche.reachable:
        liste_voisins.append(Voisin_Bas_Gauche)
    """

    return liste_voisins


Start = Start_Node((0,0),0)
Objectif = Objectif_Node((30,22),0)
Start.heuristic = distance(Start,Objectif)
Start.distance = distance(Start,Objectif)


def shortest_path(Objectif,Start):

    open_list.append(Start)
    open_list_pos.append((Start.x,Start.y))

    iterations = 0

    while len(open_list) != 0:
        for Node in open_list:
            iterations += 1
            if Node.position == Objectif.position:
                print("CHEMIN TROUVE")
                print("Itérations: ",iterations)
                for parent in Node.parents:
                    print(Node.parents.index(parent),parent.position)
                print(len(Node.parents),Node.position)
                print(Node.parents[1].position) # C'EST CA QU'IL FAUT RENVOYER POUR ENSUITE FOCUS SUR LE CENTRE
                # IA FOCUS SUR: ( Node.parents[1].x*32+16, Node.parents[1].y*32+16 )
                position = ( Node.parents[1].x*32+16, Node.parents[1].y*32+16 )
                return(position)
            else:
                for Voisin in voisins(Node):

                    if ((Voisin.x,Voisin.y) in closed_list_pos) or ((Voisin.x,Voisin.y) in open_list_pos and Voisin.cost < Node.cost):
                        pass
                    else:
                        Voisin.distance = distance(Voisin,Objectif)
                        Voisin.heuristic = Voisin.cost + distance(Voisin,Objectif)
                        open_list_pos.append((Voisin.x,Voisin.y))
                        open_list.append(Voisin)

                closed_list.append(Node)
                closed_list_pos.append((Node.x,Node.y))
                open_list.remove(Node)
                open_list.sort(key=lambda node: node.heuristic)


shortest_path(Objectif,Start)

# GROSSE NOTE : LA LENTEUR VIENT DE OPEN LIST QUI N'EST PAS TRIEE !!!!!!!!
# IL FAUT L'ORGANISER AVEC LE COMPARATEUR, ET METTRE LE MEILLEUR RESULTAT (LE PLUS PROCHE DE L'OBJECTIF)
# EN TETE AFIN QU'IL SAGISSE DE LA NODE "PROCESSEE" EN PREMIER, ET NE PAS AVOIR A TOUT REFAIRE ALEATOIREMENT !!!

# TEMPS COMPAQ : 4'13"

# SUR NODE 100,100: 19 100 ITERATIONS AVEC TRI NODE.HEURISTIC
# SUR NODE 100,100: 21 000 ITERATIONS AVEC TRI NODE.HEURISTIC


# ORDRE :
# UPDATE GRID
# EFFECTUER A*
# LANCER L'IA SUR LE CARRE LE PLUS PROCHE