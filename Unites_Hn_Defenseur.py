# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 10:38:35 2018

@author: landaier
"""

import math 
import numpy as np
from Constantes import Constante

class Unites_Humain_Defenseur():
    """
    Classe décrivant les comportements des unités humaines, lorsque celui-ci est
    un attaquant.
    """
    def __init__(self, abscisse, ordonnee, carte, role, sante):
        """
        Crée une unité aux coordonnées désirées.
        
        Paramètres
        ----------
        abscisse, ordonnée: int
            Les coordonnées auxquelles l'unité sera créé.
            
        carte : classe Map
            La carte sur laquelle évolue l'unité.
        
        role : str
            Le rôle du joueur possédant l'unité : attaquant ou défenseur.
        
        sante : int
            La santé de l'unité sélectionnée.
        """

        self._role = role
        self.__sante = sante

        self._max = sante
        self._carte = carte
        self._carte.ss_carte[abscisse][ordonnee] = self
        self._carte.append(self)
        self.coords = abscisse, ordonnee


    def __str__(self):
        """
        Affiche l'état courant de l'unité.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''; elle comprend 
            les caractéristiques les plus importantes de l'unité sélectionnée.
        """
        return "%r : position (%i, %i) etat %i/%i"%(
            self.T_car(), self.x, self.y,
            self.sante, self._max
            )
        
    
    
    def car(self):
        """
        Renvoie l'identifiant de l'unité en question
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        'U' : str
            Le caractère représentant l'unité.
        """
        return 'U'    
    
    def affichage(self):        
        """ Affiche l'unité, selon la méthode str.
        """
        print(str(self))


    def bouger(self,X,Y):
        """
        Mouvement de l'unité, choisie par l'utilisateur. Elle a lieu dans un rayon correspondant 
        à la capacité de mouvement autour de la position courante. Utilise l'accesseur coords.
        La capacité de mouvement restante de l'unité est alors mise à jour, selon le nombre de
        cases parcourues par l'unité. Si cette capacité est supérieure à 1, le joueur humain a encore
        la possibilité de déplacer l'unité avant la fin de son tour.        
       
        Paramètres :
        ------------
        Aucun.
        
        Renvoie : 
        -----------
        Le résultat de la méthode coords.
        
        """

        if self.capmvt >= 1 :

            L_vide = self.mvt_poss()

            xi, yi = self.coords
            if (X,Y) in L_vide :
                self.capmvt -= int(math.sqrt( (X-xi)**2 + (Y-yi)**2))
                self.coords = (X, Y)
                self._carte.ss_carte[xi][yi], self._carte.ss_carte[X][Y] = self._carte.ss_carte[X][Y], self._carte.ss_carte[xi][yi]
                return(self.coords)  

    
    def mvt_poss(self):
        """ Méthode permettant de sélectionner les cases sur lesquelles 
        l'unité peut se déplacer. Ces cases doivent être vides.
        Dans un premier temps, la méthode sélectionne les cases vides et non vides
        dans la zone de déplacement de l'unité.
        Cependant, une case non vide bloque également les cases autour de celles-ci
        (pour des questions de champ de vision, ou d'impossibilité de déplacement au
        delà de l'obstacle). 
        Donc dans un second temps, la méthode retire de la liste les cases qui 
        sont bloqués par les obstacles au déplacement de l'unité.
        Les cases retirées dépendent de la position de l'unité par rapport aux obstacles.
        
        A noter : actuellement, la façon dont les cases bloquées sont choisies a été
        prévu pour des unitées dont les déplacements sont inférieurs ou égaux à 2. 
        Une MAJ pourra être faite plus tard pour corriger ce problème.
        
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        L_vide : list
            La liste contenant toutes les cases où l'unité peut se déplacer.
        
        """
        x,y = self.coords
        
        self.L_vide = []

        L_obj = []
        x_inf = max(0,int(-self.capmvt) + x)
        x_sup = min(self._carte.dims[0]-1, int(self.capmvt + x))
        y_inf = max(0,int(-self.capmvt) + y)
        y_sup = min(self._carte.dims[1]-1, int(self.capmvt + y))
        
        i = x_inf
        j = y_inf
        
        for i in range(x_inf,x_sup+1):
            for j in range(y_inf,y_sup +1):
                if self._carte.ss_carte[i,j] == ' ':
                    
                    self.L_vide.append((i,j))
                else:
                    L_obj.append((i,j))
                    
        for k in range(len(L_obj)):
            ox,oy = L_obj[k]
            L = []
            
            if ox - x <0 and oy - y <0:
                #Diag H/G
                
                L = [(ox-1,oy-1),(ox-1,oy),(ox,oy-1)]
                
            elif ox - x <0 and oy - y >0:
                
                #Diag H/D
                
                L = [(ox-1,oy+1),(ox-1,oy),(ox,oy+1)]
                
            elif ox - x >0 and oy - y <0:
                
                #Diag B/G
                
                L = [(ox,oy-1),(ox+1,oy-1),(ox+1,oy)]
                
            elif ox - x >0 and oy - y >0:
                
                #Diag B/D
                
                L = [(ox+1,oy),(ox+1,oy+1),(ox,oy+1)]
                
            elif ox == x:
                if oy < y:
                    L = [(ox,oy-1),(ox-1,oy-1),(ox+1,oy-1)]
                elif oy > y :
                    L = [(ox,oy+1),(ox-1,oy+1),(ox+1,oy+1)]
            
            elif oy == y: 
                if ox < x:
                    L = [(ox-1,oy),(ox-1,oy-1),(ox-1,oy+1)]
                elif ox > x:
                    L = [(ox+1,oy),(ox+1,oy-1),(ox+1,oy+1)]
            if len(L) != 0:
                
                E_pos_imp = set(L)
                E_pos = set(self.L_vide)
                Occ = E_pos&E_pos_imp
                self.L_vide =list( E_pos - Occ)
        
        return(self.L_vide)        


    @property
    def coords(self):
        """
       coords: tuple
           Les coordonnées de l'unité sur le plateau de jeu
           """

        return self.__coords


    @property
    def x(self):
        """
        x: nombre entier
            Abscisse de l'unité
        """
        return self.coords[0]

    @property
    def y(self):
        """
        y: nombre entier
            Ordonnée de l'unité
        """
        return self.coords[1]   

    @coords.setter
    def coords(self, nouv_coords):
        """
        Met à jour les coordonnées de l'unité.
        Garantit qu'elles arrivent dans la zone définie par
        la carte.
    
        Paramètres
        ----------
        nouv_coords : tuple représentant les coordonnées auquelles 
                      l'unité essaie de se rendre.
        """
        x, y = nouv_coords
        XM,YM = self._carte.dims
        x = min(x, XM-1)
        x = max(x,0)
        y = min(y, YM-1)
        y = max(y,0)

        self.__coords = (x, y)

    @property
    def sante(self):
        """
        sante: float
            Le niveau de santé de l'unité. Si ce niveau arrive à 0 l'unité
            est marqué comme mort et sera retiré du plateau de jeu
        """
        return self.__sante
    
    @sante.setter
    def sante(self, value):
        """
        Met à jour le niveau de santé de l'Unité. Garantit que la valeur arrive 
        dans l'intervalle [0, self._max]. Met à 0 les valeurs négatives, ne
        fait rien pour les valeurs trop grandes.
        """
        if value <= self._max:
            self.__sante = value
        if value <= 0:  
            value = 0
    

    def combat(self):
        """
        Méthode permettant à l'unité de combattre, si un objet ennemi se trouve 
        dans sa zone d'attaque.
        L'unité recherche les ennemis dans sa zone de combat et sélectionne 
        l'objet le plus proche grâce à la méthode chx_ennemi.
        Si il n'y a pas d'objet à attaquer, la méthode le signale.
        Si il y a bien un objet, la méthode signale quel est l'objet blessé par l'unité.
        Cet objet perd alors de la vie, et est supprimé si sa santé devient nulle 
        ou négative.
        Si cet objet détruit est le QG, la variable V_atta, désignant la victoire ou non
        des attaquants, passe à 1. Les attaquants gagnent alors.
        
        Paramètres : 
        ------------
        Aucun.
        
        Renvoie :
        ----------
        Rien.
        
        """

        Ennemi = self.chx_ennemi()
        if Ennemi != None:
            print( "%s a blessé %s"%(self.T_car(), Ennemi.T_car() ) )
            Ennemi.sante = Ennemi.sante - self.capcbt
            if Ennemi.sante <= 0:
                role = Ennemi.T_car()
                Ennemi.disparition()
                if role[-2] + role[-1] == 'QG':
                    self._carte.V_atta = 1

        else :
            print("%s n'a blessé personne"%(self.T_car()) )
 
    
    def chx_ennemi(self):
        """
        Méthode sélectionnant l'objet ennemi le plus proche de l'unité.
        Elle parcourt les cases dans le rayon d'attaque de l'unité, et sélectionne
        les objets ennemis dans ce rayon.
        Elle sélectionne en priorité les unités ennemis les plus proches; mais si
        un batiment ennemi est plus proche de l'unité que les autres unités ennemis, 
        l'unité en train de combattre attaquera alors le batiment.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie :
        ----------
        Ennemi : Objet (Unité ou Batiment)
            L'ennemi le plus proche de l'unité en train de combattre.
        
        """

        x,y = self.coords
        x_inf = max(0,int(-self.zonecbt + x))
        x_sup = min(self._carte.dims[0]-1, int(self.zonecbt + x))
        y_inf = max(0,int(-self.zonecbt + y))
        y_sup = min(self._carte.dims[1]-1, int(self.zonecbt + y))
        

        
        Ennemi = None
        R_plus_petit_unit = self.zonecbt +1
        R_plus_petit_bat = self.zonecbt + 1
        
        
        for i in range(x_inf,x_sup+1):
            for j in range(y_inf,y_sup+1):
                Obj = self._carte.ss_carte[i][j]
                if Obj != ' ' and Obj !='/' and Obj.T_car()[0] == 'D':
                    R_Obj = math.sqrt((x-i)**2 + (y-j)**2)
                    
                    if Obj.T_car()[2] == 'U' and R_Obj < R_plus_petit_unit:
                        R_plus_petit_unit = R_Obj
                        Ennemi = Obj
                        
                    if Obj.T_car()[2] == 'B' and R_Obj < min(R_plus_petit_bat,R_plus_petit_unit):
                        R_plus_petit_bat = R_Obj
                        Ennemi = Obj
        
        return(Ennemi)
    
    def chx_ennemi_rec(self,A,x,y):
        """
        Méthode sélectionnant l'objet ennemi le plus proche de l'unité, de façon
        récursive.
        Cette méthode se base sur la technique de "Diviser pour régner". Elle sélectionne
        la sous-carte contenant les cases dans le rayon de combat de l'unité.
        Elle coupe ensuite cette sous-carte en quatres carrés plus petits, jusqu'à
        ce que ce carré soit de taille (1,1).
        Elle détermine alors si l'unité sur cette case est un batiment, ou une unité,
        et renvoie alors sa distance par rapport à l'unité combattante.
        
        Elle compare ensuite les distances des unités (et des batiments) par rapport
        à l'unité combattante, et renvoie l'unité ennemie la plus proche, sa distance
        par rapport à l'unité combattante, le batiment ennemi le plus proche, et sa
        distance par rapport à l'unité combattante.
        
        Paramètres
        ----------
        A : array
            Sous-carte contenant une partie (la totalité au départ) des cases 
            dans le rayon de combat de l'unité combattante.
            
        x,y : int
            Abscisse et ordonnée de l'unité combattante.
        
        Renvoie :
        ----------
        umin : Objet Unité 
            L'unité ennemie la plus proche de l'unité combattante.
            
        r_min_u : float
            La distance entre l'unité ennemie la plus proche de l'unité
            combattante et l'unité combattante.
        
        """
        if np.shape(A) == (1,1):
            v = A[0,0]
            if v == ' ' or v == '/':
                return((None,self.zonecbt+1))
            elif v.T_car()[0] == 'A':
                i,j = v.coords
                R = math.sqrt((x-i)**2+(y-j)**2)
                return(v,R)
            else:
                return(None,self.zonecbt+1)

        elif np.shape(A) == (0,0) or A.tolist() == [] or A.tolist()[0] == []:
            print("OK")
            return(None,self.zonecbt+1)

        else : 
            l,c = np.shape(A)
            A1 = A[l//2:,c//2:]
            A2 = A[l//2:,:c//2]
            A3 = A[:l//2,c//2:]
            A4 = A[:l//2,:c//2]
            
            U1,ru1= self.chx_ennemi_rec(A1,x,y)
            U2,ru2 = self.chx_ennemi_rec(A2,x,y)
            U3,ru3 = self.chx_ennemi_rec(A3,x,y)
            U4,ru4 = self.chx_ennemi_rec(A4,x,y)
            
            Lu = [ru1,ru2,ru3,ru4]
            LU = [U1,U2,U3,U4]
            
            r_min_u = min(Lu)
            umin = LU[ Lu.index(r_min_u) ]
            
            return(umin,r_min_u)
            
    def combat_rec(self):
        """
        
        Méthode permettant à l'unité de combattre, si un objet ennemi se trouve 
        dans sa zone d'attaque.
        Elle sélectionne les cases de la sous-carte correspondant à la zone d'attaque
        de l'unité combattante, et applique la méthode chx_ennemi_rec pour trouver
        le batiment et l'unité ennemie les plus proches. Cette dernière méthode est
        récursive.
        Si il n'y a pas d'objet à attaquer, la méthode le signale.
        Si il y a bien un objet, la méthode sélectionne lequel des deux est le plus
        proche de l'unité combattante. Cet objet est alors blessé : il perd de la vie, 
        et est supprimé si sa santé devient nulle ou négative.
        Si cet objet détruit est le QG, la variable V_atta, désignant la victoire ou non
        des attaquants, passe à 1. Les attaquants gagnent alors.
        La méthode signale également quel est l'objet blessé par l'unité.
        
        Paramètres :
        ------------
        Aucun.
        
        Renvoie :
        ---------
        Rien.
        
        """
        x,y = self.coords
        x_inf = max(0,int(-self.zonecbt + x))
        x_sup = min(self._carte.dims[0]-1, int(self.zonecbt + x))
        y_inf = max(0,int(-self.zonecbt + y))
        y_sup = min(self._carte.dims[1]-1, int(self.zonecbt + y))
        
        A = self._carte.ss_carte[x_inf:x_sup+1,y_inf:y_sup+1]
        
        U,r_min_u = self.chx_ennemi_rec(A,x,y)
        
        if U == None :
            print("%s n'a blessé personne"%(self.T_car()) )
        else:
            Ennemi = U
            
            print( "%s a blessé %s"%(self.T_car(), Ennemi.T_car() ) )
            Ennemi.sante = Ennemi.sante - self.capcbt
            if Ennemi.sante <= 0:
                Ennemi.disparition()


    def disparition(self):
        """ Méthode permettant de détruire l'unité. Elle supprime celui-ci
        de l'ensemble des listes/arrays où l'unité est stockée.
        
        Paramètres : 
        ------------
        Aucun.
        
        Renvoie :
        ---------
        Rien.
        
        """
        print("%s est mort! \n"%(self.T_car()))
        x,y = self.coords
        self._carte.remove(self)
        self._carte.ss_carte[x][y] = ' '
        self._carte.L_joueur[0]._liste_unite.remove(self)
    
    def chx_ressources(self,x,y):
        """
        Sélectionne la ressource la plus proche dans la zone de capture du robot ouvrier.
        
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie :
        ----------
        Ress : Objet Ressource (ou None).
            La ressource la plus proche de l'unité.
        
        """
        x_inf = max(0, int(-self.zonecap + x))
        x_sup = min(self._carte.dims[0]-1, int(self.zonecap + x))
        y_inf = max(0,int(-self.zonecap + y))
        y_sup = min(self._carte.dims[1]-1, int(self.zonecap + y))
        
        Ress = None
        R_plus_petit = self.zonecap +1
        
        for i in range(x_inf,x_sup+1):
            for j in range(y_inf,y_sup+1):
                Obj = self._carte.ss_carte[i][j]
                if Obj != ' ' and Obj !='/' and Obj.T_car()[-1] == 'M':
                    R_Obj = math.sqrt((x-i)**2 + (y-j)**2)
                    if  R_Obj < R_plus_petit:
                        R_plus_petit = R_Obj
                        Ress = Obj
                    
        return(Ress)
    
    def capture_ressources(self):
        """
        Permet la capture d'une ressource, si celle-ci se trouve à la portée du robot ouvrier.
        
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie : 
        ----------
        Rien.
        
        """
        x,y = self.coords
        Ress = self.chx_ressources(x,y)
        if Ress != None:
            print("%s a trouvé du métal! Sa valeur est de %r."%(self.T_car(),Ress.valeur))
            self._carte.L_joueur[0].metal_tot += Ress.valeur
            Ress.disparition()

    
class Robot_combat(Unites_Humain_Defenseur):
    """
    Classe spécialisant Unites_Humain_Defenseur pour représenter un Robot
    de combat.
    """
    Id = 0
    def __init__(self, role, carte,x,y):
        """Permet d'initialiser l'unité.
            
    Paramètres
    ----------
    
    role : str
    Le rôle du joueur possèdant l'unité
            
    carte : classe Map
    La carte sur laquelle évolue l'unité.

    x, y : int
    Les coordonnées de l'unité en abscisse et en ordonnée

        """
        self.__sante = 20
        super().__init__(x,y,carte,role,self.__sante)
        self.id = Robot_combat.Id
        Robot_combat.Id += 1
        self.num_joueur = 0

        self.capmvt = Constante.capmvt_RC
        self.capcbt = Constante.capcbt_RC
        self.zonecbt = math.sqrt(2)
    
    
    def car(self):
        """
        Méthode permettant d'afficher le robot de combat sur la carte. Elle renvoie le symbole associé à 
        ce robot.
        
        Paramètres :
        -------------
        Aucun.
        
        Renvoie : 
        ----------
        'RC' : str
            Le symbole associé.
        """
        return "RC"

    
    def T_car(self):
        """Méthode contenant l'ensemble des informations permettant d'identifier l'unité.
        Dans l'ordre : 
            self._role : le rôle du joueur possédant l'objet. Ici, le défenseur.
            U : le type global de l'objet. Ici, Unité.
            RC : le role de l'objet. Ici, Robot de Combat.
            self.id : l'identifiant de l'objet, afin de le différencier des autres
            robots de combat.
        
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie : 
        ----------
       'D_U_RC' + 'Id' : str
            La chaîne de caractère identifiant l'unité.
        """ 
        return "D_U_RC%i"%( self.id )
    

    def action(self):
        """ Méthode définissant l'action de l'unité, après s'être déplacée.
        Pour un robot de combat, cette action est une action de combat.
        
        A noter : il existe deux méthodes pour cette action de combat : une 
        méthode itérative, et une méthode récursive.
        
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie :
        ----------
        Rien.
        
        """
        self.combat_rec()
        return(None)
    
class Robot_Ouvrier(Unites_Humain_Defenseur):
    Id = 0
    def __init__(self, role, carte,x,y, L_ennemi = []):
        """Permet d'initialiser l'unité.
            
    Paramètres
    ----------
    
    role : str
    Le rôle du joueur possèdant l'unité
            
    carte : classe Map
    La carte sur laquelle évolue l'unité.

    x, y : int
    Les coordonnées de l'unité en abscisse et en ordonnée

        """
        self.__sante = 10
        super().__init__(x,y,carte,role,self.__sante)
        self.id = Robot_Ouvrier.Id
        Robot_Ouvrier.Id += 1
        self.num_joueur = 0

        self.capmvt = Constante.capmvt_RO
        self.zonecap = math.sqrt(2)
    
    
    def car(self):
        """
        Méthode permettant d'afficher le robot de combat sur la carte. Elle renvoie le symbole associé à 
        ce robot.
        
        Paramètres :
        -------------
        Aucun.
        
        Renvoie : 
        ----------
        'RO' : str
            Le symbole associé.
        
        """
        return "RO"
    
    def T_car(self):
        """Méthode contenant l'ensemble des informations permettant d'identifier l'unité.
        Dans l'ordre : 
            self._role : le rôle du joueur possédant l'objet. Ici, le défenseur.
            U : le type global de l'objet. Ici, Unité.
            RO : le role de l'objet. Ici, Robot Ouvrier.
            self.id : l'identifiant de l'objet, afin de le différencier des autres
            robots ouvriers.
            
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie : 
        ----------
       'D_U_RO' + 'Id' : str
            La chaîne de caractère identifiant l'unité.
        """ 
        return "D_U_RO%i"%( self.id )
        
    def action(self):
        """
        Méthode définissant l'action de l'unité, après s'être déplacée.
        Pour un robot ouvrier, cette action est une tentative de capture de ressources.
        
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie :
        ----------
        Rien.
        
        """
        self.capture_ressources()
        return(None)
