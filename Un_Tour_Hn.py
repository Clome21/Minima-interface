from Batiments import Foreuse,Panneau_solaire
from Constantes import Constante
from Unites_Hn_Defenseur import Robot_combat, Robot_Ouvrier
from Unites_Hn_Attaquant import Scorpion

import numpy as np


class Un_Tour_Joueur_Hn():

    """
    Classe gérant l'ensemble des méthodes et des variables consacrées à l'exécution d'un tour de jeu, pour
    un joueur humain.
    """
    
    def __init__(self,carte,IHM):
        """
        Initialise les variables utilisées pour le déroulement des tours de jeu, pour un joueur
        humain.
        
        Paramètres :
        ------------
        carte : Objet Map
            L'objet Map utilisé pour la partie.
        
        """
        self.IHM = IHM
        self._carte = carte
        self.L_joueur = self._carte.L_joueur
        self.unite_disp_par_tour = 0
        
        self.__xmax = Constante.xmax
        self.__ymax = Constante.ymax  
        self.Epp = Constante.Ep_app
        self.Jr_en_crs = 0

        self.H=Constante.H_Z_Constructible
        self.L=Constante.L_Z_Constructible

        
         
    def placer_une_foreuse(self,X,Y):
        """
        Permet au joueur, s'il en a le droit, de construire le batiment Foreuse
        sur la case dont il a indiqué les coordonnées en entrée.
        Cette case doit cependant être comprise dans les emplacements de construction
        disponibles.
        Met également à jour la quantité de ressource à sa disposition.
        
        Paramètres : 
        -------------
        X,Y : int
            Les coordonnées de la case sur laquelle le joueur veut placer le batiment.
        
        Renvoie :
        ----------
        Rien.
        
        """
        if (self.L_joueur[0].metal_tot>=Constante.cout_M_F and self.L_joueur[0].energie_tot>=Constante.cout_E_F):

            x_inf_b = (self.__xmax - self.L )//2 +1
            x_sup_b = (self.__xmax + self.L )//2 -1
            y_inf_b =  (self.__ymax - self.H )//2 +1
            y_sup_b = (self.__ymax + self.H)//2 -1
    
            L_pos = self.placement_pos_bat(x_inf_b,x_sup_b,y_inf_b,y_sup_b,' ')
     
            if (X,Y) in L_pos:
                U = Foreuse(X,Y,self._carte)
                self.L_joueur[0]._liste_bat[2].append(U)
                self.L_joueur[0].metal_tot=self.L_joueur[0].metal_tot-Constante.cout_M_F
                self.L_joueur[0].energie_tot=self.L_joueur[0].energie_tot-Constante.cout_E_F
    
    

    def placer_un_Panneau_solaire(self,X,Y):
        """
        Permet au joueur, s'il en a le droit, de construire le batiment 
        Panneau solaire sur la case dont il a indiqué les coordonnées en entrée.
        Cette case doit cependant être comprise dans les emplacements de construction
        disponibles.
        Met également à jour la quantité de ressource à sa disposition.
        
        Paramètres : 
        -------------
        X,Y : int
            Les coordonnées de la case sur laquelle le joueur veut placer le batiment.
        
        Renvoie :
        ----------
        Rien.
        
        """

        if (self.L_joueur[0].metal_tot>=Constante.cout_M_P and self.L_joueur[0].energie_tot>=Constante.cout_E_P):

            x_inf_b = (self.__xmax - self.L )//2 +1
            x_sup_b = (self.__xmax + self.L )//2 -1
            y_inf_b =  (self.__ymax - self.H )//2 +1
            y_sup_b = (self.__ymax + self.H)//2 -1
    
            L_pos = self.placement_pos_bat(x_inf_b,x_sup_b,y_inf_b,y_sup_b,' ')
    
            if (X,Y) in L_pos:                
                U = Panneau_solaire(X,Y,self._carte)
                self.L_joueur[0]._liste_bat[1].append(U)
                self.L_joueur[0].metal_tot=self.L_joueur[0].metal_tot-Constante.cout_M_P
                self.L_joueur[0].energie_tot=self.L_joueur[0].energie_tot-Constante.cout_E_P


        
    def placement_pos(self,x_inf,x_sup,y_inf,y_sup,typ):
        
        """
        Indique quelles sont les cases de la carte sur lesquelles l'objet typ est présent.
        Attention : x_sup et y_sup doivent valoir la dernière ligne/ colonne que l'on souhaite contrôler + 1.
        Ici, elle est régulièrement utilisée pour déterminer les positions où un placement d'unité / de batiment
        est possible.
        
        Paramètres : 
        ------------
        x_inf : int
            La 1e ligne de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        x_sup : int
            La ligne juste après la fin de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        y_inf : int
            La 1e colonne de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        y_sup : int
            La colonne juste après la fin de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        typ : objet (souvent string ici)
            L'objet dont on veut contrôler la présence sur une portion de la carte.
        
        Renvoie :
        ----------
        L_pos : list
            L'ensemble des coordonnées sur lesquelles se trouve l'objet typ, dans la portion de carte étudiée.
        """
        
        A = self._carte.ss_carte[x_inf : x_sup , y_inf : y_sup]
        L_pos = []

        Coords = np.where( A == typ)
        for k in range(len(Coords[0])):
            i,j = Coords[0][k]+ x_inf , Coords[1][k] + y_inf
            L_pos.append((i,j))
        return(L_pos)
        
    def placement_pos_bat(self,x_inf_b,x_sup_b,y_inf_b,y_sup_b,typ):
        """
        Indique quelles sont les cases de la carte sur lesquelles l'objet typ est présent.
        Cette méthode est utilisée pour déterminer les emplacements possibles pour un batiment.
        Par rapport à placement_pos, elle supprime des cases sur lesquelles le placement d'un batiment est
        impossible.
        Attention : x_sup et y_sup doivent valoir la dernière ligne/ colonne que l'on souhaite contrôler + 1.
        
        Paramètres : 
        ------------
        x_inf : int
            La 1e ligne de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        x_sup : int
            La ligne juste après la fin de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        y_inf : int
            La 1e colonne de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        y_sup : int
            La colonne juste après la fin de la partie de la carte dont on veut contrôler la présence de l'objet typ.
        
        typ : objet (souvent string ici)
            L'objet dont on veut contrôler la présence sur une portion de la carte.
        
        Renvoie :
        ----------
        L_pos : list
            L'ensemble des coordonnées sur lesquelles se trouve l'objet typ, dans la portion de carte étudiée.
        """
        L_pos = self.placement_pos(x_inf_b,x_sup_b,y_inf_b,y_sup_b,typ)

        x_inf = (self.__xmax )//2 -1
        x_sup = (self.__xmax)//2 +2
        y_inf =  (self.__ymax)//2 - 1
        y_sup = (self.__ymax)//2 +2
        
        L_pos_imp1 = [(i,j) for i in range(x_inf,x_sup) for j in range( (self.__ymax -self.H)//2 +1, (self.__ymax + self.H)//2)]
        L_pos_imp2 = [(i,j) for i in range((self.__xmax - self.L)//2+1 , (self.__xmax + self.L)//2) for j in range(y_inf,y_sup)]
        E_pos_imp = set(L_pos_imp1 + L_pos_imp2)
        """Définit les coordonnées où placer un bâtiment est impossible"""
        E_pos = set(L_pos)
        L_pos_tot =list( E_pos - (E_pos&E_pos_imp))
        return(L_pos_tot)
    
    def production_unite_defense_combat(self,X,Y):
        """
        Produit une unité de combat pour le défenseur, si celui-ci a suffisamment de ressources,
        sur la case qu'il a indiqué en entrée.
        Cette case doit cependant être comprise dans les emplacements de production
        disponibles.
        
        Paramètres :
        ------------
        X,Y : int
            Les coordonnées de la case sur laquelle le joueur veut placer l'unité.
        
        Renvoie :
        ----------
        Rien.
        
        """
        if (self.L_joueur[0].metal_tot>=Constante.cout_M_RC and self.L_joueur[0].energie_tot>=Constante.cout_E_RC):
    
            x_inf = (self.__xmax )//2 -1
            x_sup = (self.__xmax)//2 +2
            y_inf =  (self.__ymax)//2 - 1
            y_sup = (self.__ymax)//2 +2
     
            L_pos = self.placement_pos(x_inf,x_sup,y_inf,y_sup,' ')
                    
            if (X,Y) in L_pos:
                U=Robot_combat(self.L_joueur[0]._role,self._carte,X,Y)
                self.L_joueur[0]._liste_unite.append(U)
                self.L_joueur[0].metal_tot=self.L_joueur[0].metal_tot-Constante.cout_M_P
                self.L_joueur[0].energie_tot=self.L_joueur[0].energie_tot-Constante.cout_E_P

            
    def production_unite_defense_production(self,X,Y):
        """
        Produit une unité de production pour le défenseur, si celui-ci a suffisamment de ressources,
        sur la case qu'il a indiqué en entrée.
        Cette case doit cependant être comprise dans les emplacements de production
        disponibles.
        
        Paramètres :
        ------------
        X,Y : int
            Les coordonnées de la case sur laquelle le joueur veut placer l'unité.
        
        Renvoie :
        ----------
        Rien.
        
        """
        if (self.L_joueur[0].metal_tot>=Constante.cout_M_RO and self.L_joueur[0].energie_tot>=Constante.cout_E_RO):
    
            x_inf = (self.__xmax )//2 -1
            x_sup = (self.__xmax)//2 +2
            y_inf =  (self.__ymax)//2 - 1
            y_sup = (self.__ymax)//2 +2
            L_pos = self.placement_pos(x_inf,x_sup,y_inf,y_sup,' ')
    
            if (X,Y) in L_pos:
                U=Robot_Ouvrier(self.L_joueur[0]._role,self._carte,X,Y)
                self.L_joueur[0]._liste_unite.append(U)
                self.L_joueur[0].metal_tot=self.L_joueur[0].metal_tot-Constante.cout_M_P
                self.L_joueur[0].energie_tot=self.L_joueur[0].energie_tot-Constante.cout_E_P

        
    def production_unite_attaque_Hn(self,X,Y):
        """
        Produit des unités de combat pour l'attaquant, sur la case qu'il a indiqué en
        entrée. Cette case doit cependant être comprise dans les emplacements de production
        disponibles.
        
        Paramètres :
        ------------
        X,Y : int
            Les coordonnées de la case sur laquelle le joueur veut placer l'unité.
        
        Renvoie :
        ----------
        Rien.
        
        """

        
        if self.L_joueur[self.Jr_en_crs].nbe_unite_restantes < 1:
            print("Aucune unité à placer pour ce tour. \n")
        
        else:
        
            L_Ht = self.placement_pos(0,self.Epp + 1,(self.__ymax -self.H)//2,(self.__ymax + self.H )//2,' ')
            
            L_Bas = self.placement_pos(self.__xmax-1-self.Epp,self.__xmax,(self.__ymax -self.H)//2,(self.__ymax + self.H )//2,' ')
        
            L_Gche = self.placement_pos((self.__xmax - self.L )//2 , (self.__xmax + self.L )//2,0,self.Epp+1,' ')
        
            L_Dte = self.placement_pos((self.__xmax - self.L )//2, (self.__xmax + self.L )//2,self.__ymax -1-self.Epp,self.__ymax,' ')
        
            #Sélectionne les 4 zones d'apparitions
        
            L_pos = L_Ht + L_Bas + L_Gche + L_Dte 
        
            #Sélectionne les emplacements disponibles
            if len(L_pos) == 0 :
                print("Aucune zone d'apparition d'unité disponible, étape suivante. \n")
        
            elif (X,Y) in L_pos : 
                Jr = self.L_joueur[self.Jr_en_crs]
                self.U = Scorpion(Jr._role,self._carte,X,Y,self.Jr_en_crs)
                Jr._liste_unite.append(self.U)
                Jr.nbe_unite_restantes -= 1
                self.IHM.ui.lcdNumber_Unitdispo.display(int(Jr.nbe_unite_restantes) )
                print("Nombre de scorpions disponibles : ", int(Jr.nbe_unite_restantes))


    def deb_unTourHn(self):

        """
        Effectue toutes les actions liées au début d'un tour de jeu, pour les joueurs
        humains dans la partie.
        Pour cela, après avoir vérifié que le joueur est bien humain, la méthode 
        active les options correspondantes au rôle du joueur sélectionné.
        Une fois tous les joueurs humains passés, la méthode met à jour le nombre
        d'unités disponibles pour les attaquants, puis lance le tour de jeu des
        joueurs IA.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        Rien
        """

        n = len(self.L_joueur)
        if self.Jr_en_crs < n:
            
            k = self.Jr_en_crs
            role = self.L_joueur[k]._role
            while k < n-1 and role[1] != 'H' : 
                k += 1
                role = self.L_joueur[k]._role

            if role[1] == "H" :
                self.Jr_en_crs = k
                self.IHM.tr_Hn_en_crs = 1
                print("\\\ Tour du joueur %r ///"%(role))
                if role[0] == "D":
                    self.IHM.ui.Attaquant.hide()
                    self.IHM.ui.Defenseur.show()
                    self.IHM.ui.tr_defenseur_text.show() 
                    self.IHM.ui.tr_attaquant_1_text.hide() 
                    self.IHM.ui.tr_attaquant_2_text.hide() 
                    self.IHM.ui.tr_attaquant_3_text.hide() 
                    self.IHM.ui.tr_attaquant_4_text.hide()
                    self.IHM.ui.lcdNumber_Metal.show()
                    self.IHM.ui.textBrowser_Metal.show()
                    self.IHM.ui.textBrowser_Energie.show()
                    self.IHM.ui.lcdNumber_Energie.show()
                    
                elif role[0] == "A":
                    self.IHM.ui.Attaquant.show()
                    self.IHM.ui.Defenseur.hide()
                    self.IHM.ui.tr_defenseur_text.hide() 
                    self.IHM.affiche_Jr_en_crs(self.Jr_en_crs) 
                    self.L_joueur[self.Jr_en_crs].nbe_unite_restantes += self.unite_disp_par_tour
                    self.IHM.maj_compteur_ressources()
                    self.IHM.ui.lcdNumber_Metal.hide()
                    self.IHM.ui.textBrowser_Metal.hide()
                    self.IHM.ui.textBrowser_Energie.hide()
                    self.IHM.ui.lcdNumber_Energie.hide()
                self.IHM.activation_boutons()
            else : 
                self.Jr_en_crs += 1
                self.deb_unTourHn()
                
        else : 
            self.unite_disp_par_tour += Constante.nbe_unite_ajoute
            if self.unite_disp_par_tour > min(self.L,self.H):
                self.unite_disp_par_tour = min(self.L,self.H)
            self.Jr_en_crs = 0
            self._carte.TrIA.unTourIA()
                
    def fin_unTourHn(self):
        """
        Termine le tour de jeu d'un joueur humain. Pour cela, il effectue les
        actions de toutes les unités possédées par le joueur, puis remet à zéro
        les capacités de mouvement des unités. Il passe au tour du joueur
        suivant.
        
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie :
        -----------
        Rien.
        
        """
        i = self.Jr_en_crs
        L_unite = self.L_joueur[i]._liste_unite
        for c in L_unite:
            c.action()
            role_u = c.T_car()
            k = -2
            tTyp = role_u[k:]
            while tTyp[0] not in ['R','S']:
                k = k- 1
                tTyp = role_u[k:]
            role_u = tTyp
            if role_u[0:2] == "RC":
                c.capmvt = Constante.capmvt_RC
            elif role_u[0:2] == "RO":
                c.capmvt = Constante.capmvt_RO
            elif role_u[0] == "S":
                c.capmvt = Constante.capmvt_S
        self.Jr_en_crs += 1
        self.IHM.tr_Hn_en_crs = 0
        self.IHM.simuler()

    
