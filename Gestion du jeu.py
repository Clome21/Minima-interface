# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:33:10 2018

@author: utilisateurPC
"""
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from Minima_prop import Ui_Minima_Accueil
from Partie import Partie
from Constantes import Constante
import Save_Load as sl

class MonAppli(QtWidgets.QMainWindow):
    """
    Classe permettant le lien entre l'IHM et le reste du code
    """
    def __init__(self):
        """
        initialise les variable de jeu
        
        Paramètres
        ----------
        
        Return
        ------
        
        Other Paramètre
        ---------------
        
        tr_en_crs  : int
            Le numéro du tour en cours.
            
        tr_Hn_en_crs : int
            Le numéro du tour de l'attaquant en cours.
            
        nbtour : int
            le nombre total de tour que comprend une partie
            
        
        Obj : None Type
            L'objet que l'on séléctione grâce à un double-clic
        
        L_pos : liste
            Liste des coordonnées sur lesquelles il est possible de placer un obj
        
        l : int
            variable permettant de controler l'affichage dans le conteneur
            
        pos_souris_x_bouger, pos_souris_y_bouger : int
            Les coordonnées d'un double-clic droit de la souris
            
        pos_souris_x, pos_souris_y : int
            Les coordonnées d'un double-clic gauche de la souris
        
        """
        super().__init__()

        self.setMouseTracking(True)

        # Configuration de l'interface utilisateur.

        self.ui = Ui_Minima_Accueil()
        self.ui.setupUi(self)
        
        self.tr_en_crs =0
        self.tr_Hn_en_crs = 0
        self.nbtour=Constante.nbt
        self.Obj = None
        self.L_pos = []

        self.l = "i"
         
        self.pos_souris_x=int
        self.pos_souris_y=int
        
        self.pos_souris_x_bouger=int
        self.pos_souris_y_bouger=int

        self.ui.Button_Ready.clicked.connect(self.jeu)
        self.ui.Button_Ready.clicked.connect( self.ui.Button_Ready.hide)
        self.ui.Button_Ready.clicked.connect( self.generer)
        self.ui.Button_Ready.clicked.connect(self.simuler)
        self.ui.Button_Ready.clicked.connect(self.ui.info.show)                  
        self.ui.Bouton_Findetour.clicked.connect(self.simuler) 
        self.ui.Bouton_Findetour.clicked.connect(self.jeu)
        
#-------------------place un batiment
       
        self.ui.Button_Foreuse.clicked.connect(self.active_for)        
        self.ui.Button_Panneau_Solaire.clicked.connect(self.active_PS)       
        self.ui.Button_J_D_B_Fermer.clicked.connect(self.raz)
        
#-------------------production unité
        self.ui.Button_Robot_Combat.clicked.connect(self.active_RC)                
        self.ui.Button_Robot_Ouvrier.clicked.connect(self.active_RO)        
        self.ui.Button_Scorpion.clicked.connect(self.active_Sc)        
        self.ui.Button_J_A_Fermer.clicked.connect(self.raz)                
        self.ui.Button_J_D_U_Fermer.clicked.connect(self.raz)

#-------------------gestion de la sauvegarde et du chargement
        

        self.ui.nom_sauvegarde.returnPressed.connect(self.ui.groupBox_Sauvegarde.hide)
        self.ui.nom_sauvegarde.returnPressed.connect(self.sauvegarde)      

        self.ui.nom_charger.returnPressed.connect(self.ui.groupBox_Charger.hide)
        self.ui.nom_charger.returnPressed.connect(self.charger)
        


    def sauvegarde(self):
        """
        Permet la sauvegarde dans un fichier texte de la partie en cours. Fait le lien avec la fonction Save de la classe Save_Load en récupérant le nom choisi par
        le joueur.
        
        Paramètres
        ----------
        
        Return
        ------
        """
        name = self.ui.nom_sauvegarde.text()
        name = str(name)
        name = name + ".txt"
        self.ui.nom_sauvegarde.clear()
        self.Save = sl.Save(name,self.carte,self)
        self.ui.groupBox_Jeu.show()
        
    def charger (self):
         """
         Permet de charger une partie préalablement sauvegardée grâce à un nom donné par le joueur. Fait le lien avec la fonction Load de la classe Save_Load.
        
         Paramètres
         ----------
        
         Return
         ------
         """
         name = self.ui.nom_charger.text()
         name = str(name)
         name = name + ".txt"
         self.ui.nom_charger.clear()
         self.Load = sl.Load(name,self)
         if type(self.Load.Nme) != int : 
            self.ui.groupBox_Jeu.show()
            self.carte = self.Load.Lcarte
            self.ui.Chargement.show()            
            self.mise_en_place()
    
    def mise_en_place(self):
        """
        Permet de mettre en place une partie que le joueur souhaite charger. Mets à jour le conteneur, tous les compteurs LCD, le joueur qui doit jouer
        
        Paramètres
        ----------
        
        Return
         ------
        """
        self.maj_compteur_ressources()
        self.affiche_Jr_en_crs(self.carte.TrHn.Jr_en_crs)
        self.ui.Button_Ready.hide()
        self.ui.info.show()
        self.__xmax = Constante.xL
        self.__ymax = Constante.yL
        self.Epp = self.carte.Epp

        self.H = self.carte.H
        self.L= self.carte.L

        self.x_inf_b = (self.__xmax - self.L )//2 +1
        self.x_sup_b= (self.__xmax + self.L )//2 -1
        self.y_inf_b =  (self.__ymax - self.H )//2 +1
        self.y_sup_b = (self.__ymax + self.H)//2 -1
        
        self.x_inf = (self.__xmax )//2 -1
        self.x_sup = (self.__xmax)//2 +2
        self.y_inf =  (self.__ymax)//2 - 1
        self.y_sup = (self.__ymax)//2 +2
        
        self.jeu()
       

    def nom_sauvegarde (self):
        """
        Permet au joueur de choisir un nom de sauvegarde
        
        Paramètres
        ----------
        
        Return
        name : string
            Le nom de sauvegarde choisi par le joueur
        """
        name = self.ui.nom_sauvegarde.text()
        name = str(name)
        name = name + ".txt"
        self.ui.nom_sauvegarde.clear()
        return name

    def generer(self):
        """
        Permet de generer la partie avec les paramètres choisi par le joueur
        
        Paramètres
        ----------
        
        Return
         ------
        """
        self.partie = Partie(self.ui.nb_IA_facile_choisi(),self.ui.nb_Hn_choisi(),self)
        self.carte=self.partie.carte
        self.ui.lcdNumber_Metal.display(self.partie.L_joueur[0].metal_tot)
        self.ui.lcdNumber_Energie.display(self.partie.L_joueur[0].energie_tot)
        self.__xmax = Constante.xmax
        self.__ymax = Constante.ymax
        self.Epp = Constante.Ep_app

        self.H=Constante.H_Z_Constructible
        self.L=Constante.L_Z_Constructible

        self.x_inf_b = (self.__xmax - self.L )//2 +1
        self.x_sup_b= (self.__xmax + self.L )//2 -1
        self.y_inf_b =  (self.__ymax - self.H )//2 +1
        self.y_sup_b = (self.__ymax + self.H)//2 -1
        
        self.x_inf = (self.__xmax )//2 -1
        self.x_sup = (self.__xmax)//2 +2
        self.y_inf =  (self.__ymax)//2 - 1
        self.y_sup = (self.__ymax)//2 +2
            
        
    def active_for(self):
        """
        Met à jour la variable l pour afficher l'objet désiré. Met également à jour les coordonnées du double-clic de la souris
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.l = "pbf"
        self.pos_souris_x=int
        self.pos_souris_y=int
        

    def active_PS(self):
        """
        Met à jour la variable l pour afficher l'objet désiré. Met également à jour les coordonnées du double-clic de la souris
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.l = "pbp"
        self.pos_souris_x=int
        self.pos_souris_y=int
        
        
    def active_RO(self):
        """
        Met à jour la variable l pour afficher l'objet désiré. Met également à jour les coordonnées du double-clic de la souris
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.l = "puro"
        self.pos_souris_x=int
        self.pos_souris_y=int
        
    
    def active_RC(self):
        """
        Met à jour la variable l pour afficher l'objet désiré. Met également à jour les coordonnées du double-clic de la souris
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.l = "purc"
        self.pos_souris_x=int
        self.pos_souris_y=int
        
    
    def active_Sc(self):
        """
        Met à jour la variable l pour afficher l'objet désiré. Met également à jour les coordonnées du double-clic de la souris
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.l = "pus"
        self.pos_souris_x = int
        self.pos_souris_y = int

        
    def mouseDoubleClickEvent(self, event):
        """
        Surcharge de la méthode mouseDoubleClickEvent adaptée pour l'utilisation de fonction supplémentaire
        
        Paramètre
        ---------
        event : Qevent
            variable de base de la méthode mouseDoubleClickEvent
            
        Return
        ------
        """
        if event.button() == QtCore.Qt.LeftButton :
            self.pos_souris_x=int((event.x()/36))
            self.pos_souris_y=int((event.y()/36))
            self.bouger_poss_u()
            self.plac_PS()
            self.plac_for()
            self.plac_RC()
            self.plac_RO()
            self.plac_Sc()
            self.info_obj()

        if event.button() == QtCore.Qt.RightButton :
            self.pos_souris_x_bouger=int((event.x()/36))
            self.pos_souris_y_bouger=int((event.y()/36))
            self.bouger_u()
               
    
    def info_obj(self):
        """
        Met à jour l'affichage des informations du groupbox info de l'IHM lors du double-clic sur un objet
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if type(self.pos_souris_x) == int:
            Obj = self.carte.ss_carte[self.pos_souris_x][self.pos_souris_y]

            if Obj != ' ' and Obj != '/' :
                
                if Obj.T_car()[-1]== 'M':
                    sante = str(Obj.valeur)
                    nom = "Metal"
                    appartenance = " "
                    statut = "Ressource"
                    sante_max = " "
                else :
                    sante_max = str(Obj._max)              
                    sante = str(Obj.sante)
                    if Obj.T_car()[0] == 'D':
                        appartenance = "Défenseur"  
                        if Obj.T_car()[2] == 'U':
                            statut = "Unité"
                            if str(Obj.T_car()[4:6]) == 'RC':
                                nom = ("Robot de combat " + str(Obj.T_car()[6::]))
                            if str(Obj.T_car()[4:6]) == 'RO':
                                nom = ("Robot ouvrier " + str(Obj.T_car()[6::]))
                        if Obj.T_car()[2] == 'B':
                            statut = "Batiment"
                            if str(Obj.T_car()[4:6]) == 'QG':
                                nom = "QG"
                            if str(Obj.T_car()[4:5]) == 'P':
                                nom = "Panneau solaire"
                            if str(Obj.T_car()[4:5]) == 'F':
                                nom = "Foreuse"
                        
                    
                    elif Obj.T_car()[0:4] == "AI_0":
                        sante = str(Obj.sante)
                        nom = ("Scorpion 0" + str(Obj.T_car()[10::]))
                        appartenance = ("AI 0 n°" + str(Obj.T_car()[5]))
                        statut = "Unité"
    
                    elif Obj.T_car()[0:4] == "AI_1":
                        sante = str(Obj.sante)
                        nom = ("Scorpion 1" + str(Obj.T_car()[10::]))
                        appartenance = ("AI 1 n°" + str(Obj.T_car()[5]))
                        statut = "Unité"
    
                    
                    elif Obj.T_car()[0:2] == "AH":
                        sante = str(Obj.sante)
                        nom = ("Scorpion "+ str(Obj.T_car()[7::]))
                        appartenance = ("Attaquant Humain " + str(Obj.T_car()[2]))
                        statut = "Unité"

                position = str(Obj.coords)
                
                self.ui.textBrowser_nomUn.setText(nom)
                self.ui.textBrowser_appartenanceUn.setText(appartenance)
                self.ui.textBrowser_statutUn.setText(statut)
                self.ui.textBrowser_positionUn.setText(position)
                self.ui.textBrowser_santeUn.setText(sante + "/" + sante_max)
            else :
                self.ui.textBrowser_nomUn.clear()
                self.ui.textBrowser_appartenanceUn.clear()
                self.ui.textBrowser_statutUn.clear()
                self.ui.textBrowser_positionUn.clear()
                self.ui.textBrowser_santeUn.clear()
        
    def raz(self):
        """
        Réinitialise la variable l pour suprimer, dans le conteneur, l'affichage de placement et des déplacements possibles
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.l = 1
        self.paintEvent(2)
        self.ui.conteneur.update()
    
    def bouger_u(self):
        """
        Permet de déplacer une unité. Fait le lien avec la méthode bouger de l'unité sélectionnée.
        
        Paramètres
        ----------
        
        Return
        ------        
        """

        if self.Obj.T_car()[2] == 'U' or self.Obj.T_car()[4] == 'U':
                if type(self.pos_souris_x_bouger) == int:
                    self.Obj.bouger(self.pos_souris_x_bouger,self.pos_souris_y_bouger)
                    self.pos_souris_x_bouger = int
                    self.pos_souris_y_bouger = int
            
                    self.raz()
                
                
    def bouger_poss_u(self):
        
        """
        Permet vérifier si il est possible de déplacer une unité. 
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if type(self.pos_souris_x) == int:
            Obj = self.carte.ss_carte[self.pos_souris_x][self.pos_souris_y]

            if Obj != ' ' and Obj != '/':
                Jr_en_crs = self.carte.TrHn.Jr_en_crs
                role =self.carte.L_joueur[ Jr_en_crs ]._role
                role_unit = Obj.T_car()
                if Obj.T_car()[2] == 'U' and role[0:2] == "DH":
                    # déplacement des unités du défenseur humain autorisé
                    self.Obj = Obj
                    self.l="bg"
                    self.paintEvent(2)
                    self.ui.conteneur.update()
                elif Obj.T_car()[4] == 'U' and role[0:3] == role_unit[0:3]:
                    # déplacement des unités de l'attaquant humain autorisé
                    self.Obj = Obj
                    self.l="bg"
                    self.paintEvent(2)
                    self.ui.conteneur.update()
    
    def activation_boutons(self):
        """
        Permet d'activer ou desactiver les boutons .Button_Panneau_Solaire,Button_Foreuse,Button_Robot_Combat,Button_Robot_Ouvrier,Button_Scorpion suivant le nombre de 
        ressource disponible.
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if (self.carte.L_joueur[0].metal_tot>=Constante.cout_M_P and self.carte.L_joueur[0].energie_tot>=Constante.cout_E_P):
            self.ui.Button_Panneau_Solaire.setEnabled(True)
        else:
            self.ui.Button_Panneau_Solaire.setEnabled(False)
            
        if (self.carte.L_joueur[0].metal_tot>=Constante.cout_M_F and self.carte.L_joueur[0].energie_tot>=Constante.cout_E_F):
            self.ui.Button_Foreuse.setEnabled(True)
        else:
            self.ui.Button_Foreuse.setEnabled(False)
        if (self.carte.L_joueur[0].metal_tot>=Constante.cout_M_RC and self.carte.L_joueur[0].energie_tot>=Constante.cout_E_RC):
             self.ui.Button_Robot_Combat.setEnabled(True)
        else:
            self.ui.Button_Robot_Combat.setEnabled(False)
        if (self.carte.L_joueur[0].metal_tot>=Constante.cout_M_RO and self.carte.L_joueur[0].energie_tot>=Constante.cout_E_RO):
            self.ui.Button_Robot_Ouvrier.setEnabled(True)
        else:
            self.ui.Button_Robot_Ouvrier.setEnabled(False)
        
        no_jr_en_crs = self.carte.TrHn.Jr_en_crs
        Jr_en_crs = self.carte.L_joueur[no_jr_en_crs]

        if Jr_en_crs._role[0] == 'A' and Jr_en_crs.nbe_unite_restantes >= 1:
            self.ui.Button_Scorpion.setEnabled(True)
        else:
            self.ui.Button_Scorpion.setEnabled(False)
        
    def maj_compteur_ressources(self):
        """
        Permet de mettre à jour les LCD number de L'IHM avec la variable correspondante.
        
        Paramètres
        ----------
        
        Return
        ------        
        """

        self.ui.lcdNumber_Metal.display(self.carte.L_joueur[0].metal_tot)
        self.ui.lcdNumber_Energie.display(self.carte.L_joueur[0].energie_tot)
        self.ui.lcdNumber_Tours_restant.display(self.nbtour-self.carte.tr_actuel)
        self.ui.lcdNumber_Unitdispo.display(int(self.carte.L_joueur[self.carte.TrHn.Jr_en_crs].nbe_unite_restantes))
        

    def plac_RC(self):
        """
        Permet de placer un robot de combat, fait le lien avec la méthode production_unite_defense_combat de la classe Un_tour_Hn
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if self.l == "purc" and self.pos_souris_x != int:
            self.carte.TrHn.production_unite_defense_combat(self.pos_souris_x,self.pos_souris_y)
            self.activation_boutons()
            self.maj_compteur_ressources()
            self.paintEvent(2)
            self.ui.conteneur.update()
        
    def plac_RO(self):
        """
        Permet de placer un robot ouvrier, fait le lien avec la méthode production_unite_defense_production de la classe Un_tour_Hn
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if self.l == "puro" and self.pos_souris_x != int:
            self.carte.TrHn.production_unite_defense_production(self.pos_souris_x,self.pos_souris_y)
            self.activation_boutons()
            self.maj_compteur_ressources()
            self.paintEvent(2)
            self.ui.conteneur.update()
        
    def plac_for(self):
        """
        Permet de placer une foreuse, fait le lien avec la méthode placer_une_foreuse de la classe Un_tour_Hn
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if self.l == "pbf" and self.pos_souris_x != int:
            self.carte.TrHn.placer_une_foreuse(self.pos_souris_x,self.pos_souris_y) 
            self.activation_boutons()
            self.maj_compteur_ressources()
            self.paintEvent(2)
            self.ui.conteneur.update()


    def plac_PS(self):
        """
        Permet de placer un panneau solaire, fait le lien avec la méthode placer_Panneau_solaire de la classe Un_tour_Hn
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if self.l == "pbp" and self.pos_souris_x != int:
            self.carte.TrHn.placer_un_Panneau_solaire(self.pos_souris_x,self.pos_souris_y)
            self.activation_boutons()
            self.maj_compteur_ressources()
            self.paintEvent(2)
            self.ui.conteneur.update()
        
    def plac_Sc(self):
        """
        Permet de placer un scorpion, fait le lien avec la méthode production_unite_attaque_Hn de la classe Un_tour_Hn
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        if self.l == "pus" and self.pos_souris_x != int:
            self.carte.TrHn.production_unite_attaque_Hn(self.pos_souris_x,self.pos_souris_y)
            self.activation_boutons()
            self.paintEvent(2)
            self.ui.conteneur.update()

    def jeu(self):
        """
        Permet d'afficher la partie dans le conteneur
        
        Paramètres
        ----------
        
        Return
        ------        
        """
        self.paintEvent(2)
        self.ui.conteneur.update()
        self.l=1
        
                      
    def paintEvent(self,e):
        """
        Surchage de la méthode paintEvent adapté pour afficher des objets à un moment précis
        
        Paramètres
        ----------
        e: int 
            variable de base de la méthode paintEvent
        
        Return
        ------        
        """
        qp = QtGui.QPainter()
        qp.begin(self)

        if self.l!= "i":
            self.affiche_map(qp)
            self.affiche_jeu(qp)
        if type(self.l) != int and self.l[0:2]== "pb":    
            self.affiche_L_pos_bat(qp)
        if type(self.l) != int and self.l[0:2] == "pu":   
            if self.l == "pus":
                self.affiche_L_pos_a(qp)
            else:
                self.affiche_L_pos_u(qp)
        if self.l=="bg":
            try : 
                zone = self.Obj.zonecbt
                self.affiche_bouger_cbt(qp,zone)
            except Exception:
                zone = self.Obj.capmvt
                self.affiche_bouger_ressource(qp,zone)
        qp.end()

        
    def affiche_L_pos_a(self,qp):
        """
        Permet d'afficher la zone sur laquelle il est possible de placer un scorpion
        
        Paramètres
        ----------
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        
        Return
        ------        
        """
        L_Ht = self.carte.TrHn.placement_pos(0,self.Epp + 1,(self.__ymax -self.H)//2,(self.__ymax + self.H )//2,' ')            
        L_Bas = self.carte.TrHn.placement_pos(self.__xmax-1-self.Epp,self.__xmax,(self.__ymax -self.H)//2,(self.__ymax + self.H )//2,' ')        
        L_Gche = self.carte.TrHn.placement_pos((self.__xmax - self.L )//2 , (self.__xmax + self.L )//2,0,self.Epp+1,' ')        
        L_Dte = self.carte.TrHn.placement_pos((self.__xmax - self.L )//2, (self.__xmax + self.L )//2,self.__ymax -1-self.Epp,self.__ymax,' ')
        
        L_pos = L_Ht + L_Bas + L_Gche + L_Dte 
        for i in L_pos:
            self.dessin_L_pos(qp,i[0],i[1])

    def affiche_bouger_cbt(self,qp,zone):
        """
        Permet d'afficher la zone sur laquelle il est possible de déplacer un robot de combat et indique quelle unité adverse peut être attaquée.
        
        Paramètres
        ----------
        
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
            
        zone: liste
            Contient l'ensemble des coordonné où le déplacement est autorisé.
        
        Return
        ----
        """
        Ennemi = None
        self.L_pos=self.Obj.mvt_poss()
        for i in self.L_pos:
            x,y = i
            x_inf = max(0,int(-zone) + x)
            x_sup = min(self.Obj._carte.dims[0]-1, int(zone) + x)
            y_inf = max(0,int(-zone) + y)
            y_sup = min(self.Obj._carte.dims[1]-1, int(zone) + y)
        
            A = self.Obj._carte.ss_carte[x_inf:x_sup+1,y_inf:y_sup+1]
            if self.Obj.T_car()[0] == 'D':
                U,r_min_u = self.Obj.chx_ennemi_rec(A,x,y)
                Ennemi = U
            else: 
                U,r_min_u,B,r_min_b = self.Obj.chx_ennemi_rec(A,x,y)
                if U != None or B != None:
                    if r_min_b > r_min_u:
                        Ennemi = U
                    else:
                        Ennemi = B
            self.dessin_L_pos(qp,x,y)
            if Ennemi != None:  
                X,Y = Ennemi.coords
                self.dessin_interet(qp,X,Y)
        Ennemi = None
        x,y = self.Obj.coords
        x_inf = max(0,int(-zone) + x)
        x_sup = min(self.Obj._carte.dims[0]-1, int(zone) + x)
        y_inf = max(0,int(-zone) + y)
        y_sup = min(self.Obj._carte.dims[1]-1, int(zone) + y)
        
        A = self.Obj._carte.ss_carte[x_inf:x_sup+1,y_inf:y_sup+1]
        if self.Obj.T_car()[0] == 'D':
            U,r_min_u = self.Obj.chx_ennemi_rec(A,x,y)
            Ennemi = U
        else: 
            U,r_min_u,B,r_min_b = self.Obj.chx_ennemi_rec(A,x,y)
            if U != None or B != None:
                if r_min_b > r_min_u:
                    Ennemi = U
                else:
                    Ennemi = B
        if Ennemi != None:  
            X,Y = Ennemi.coords
            self.dessin_interet_proche(qp,X,Y)

    def affiche_bouger_ressource(self,qp,zone):
        """
        Permet d'afficher la zone sur laquelle il est possible de déplacer un robot ouvrier et indique quelle ressource peut être collectée
        
        Paramètres
        ----------
        
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
            
        zone: liste
            Contient l'ensemble des coordonné où le déplacement est autorisé.
        
        Return
        ----
        """

        Ress = None
        self.L_pos=self.Obj.mvt_poss()
        for i in self.L_pos:
            x,y = i
            Ress = self.Obj.chx_ressources(x,y)
            self.dessin_L_pos(qp,x,y)
            if Ress != None:
                X,Y = Ress.coords
                self.dessin_interet(qp,X,Y)
        x,y = self.Obj.coords
        Ress = self.Obj.chx_ressources(x,y)
        if Ress != None:
            X,Y = Ress.coords
            self.dessin_interet_proche(qp,X,Y)

        
    def affiche_L_pos_bat(self,qp):
        """
        Permet d'afficher la zone sur laquelle il est possible de placer un batîment
        
        Paramètres
        ----------
        
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
            
        
        Return
        ----
        """
        self.L_pos = self.carte.TrHn.placement_pos_bat(self.x_inf_b,self.x_sup_b,self.y_inf_b,self.y_sup_b,' ')
        for i in self.L_pos:
            self.dessin_L_pos(qp,i[0],i[1])
            
    def affiche_L_pos_u(self,qp):
        """
        Permet d'afficher la zone sur laquelle il est possible de placer une unité
        
        Paramètres
        ----------
        
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
            
        
        Return
        ----
        """
        L_pos = self.carte.TrHn.placement_pos(self.x_inf,self.x_sup,self.y_inf,self.y_sup,' ')
        for i in L_pos:
            self.dessin_L_pos(qp,i[0],i[1])
          
    def affiche_map(self,qp):
        """
        Permet d'afficher la zone de jeu dans le conteneur
        
        Paramètres
        ----------
        
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
            
        
        Return
        ----
        """
        for i in range(self.__xmax):
            for j in range(self.__ymax):  
                
                if self.carte.ss_carte[i][j] == '/':
                    self.dessin_mur(qp,i,j)
                elif i == (self.__xmax - self.L )//2 or i == (self.__xmax + self.L )//2-1:
                    if j<= self.Epp or j >=self.__ymax - self.Epp-1 :
                        self.dessin_zone_ap(qp,i,j)
                    else:
                        self.dessin_case(qp,i,j)                       
                    
                
                elif i >= (self.__xmax - self.L )//2+1 and i < (self.__xmax + self.L )//2-1 :
                    if j >= (self.__ymax -self.H)//2 +1 and j< (self.__ymax + self.H )//2-1:
                        self.dessin_zone_c(qp,i,j)
                    elif j<= self.Epp or j >=self.__ymax - self.Epp-1 :
                        self.dessin_zone_ap(qp,i,j)
                    else:
                        self.dessin_case(qp,i,j)
                
                elif i<= self.Epp or i >= self.__xmax - 1 - self.Epp :
                    if j >= (self.__ymax -self.H)//2  and j< (self.__ymax + self.H )//2+1:
                        self.dessin_zone_ap(qp,i,j)
                    else:
                        self.dessin_case(qp,i,j)
                 
                else:
                    self.dessin_case(qp,i,j)
                
  
    def affiche_jeu(self,qp):
        """
        Permet d'afficher les objets du jeu dans le conteneur
        
        Paramètres
        ----------
        
        qp : QtGui.QPainter
            variable permettant le dessin dans le conteneur
            
        
        Return
        ----
        """

        for Obj in self.carte : 
            if Obj.T_car()[-1]== 'M':
                self.dessin_metal(qp,Obj)
               
            elif Obj.T_car()[0] == 'D':
                if Obj.car() == 'RC':
                    self.dessin_Robot_combat(qp,Obj)

                elif Obj.car() == 'RO':
                    self.dessin_Robot_ouvrier(qp,Obj)
                
                elif Obj.T_car()[-2:] == "QG":
                    self.dessin_QG(qp,Obj)
                
                elif Obj.T_car()[-2:-1] == "P":
                    self.dessin_Panneau_Solaire(qp,Obj) 

                elif Obj.T_car()[-2:-1] == "F":
                    self.dessin_Foreuse(qp,Obj)
                
            else : 
                if Obj.T_car()[0:2] == "AH":
                    if Obj.T_car()[2] == "0":
                        
                        self.dessin_Scorpion0(qp,Obj)
                    if Obj.T_car()[2] == "1":
                        
                        self.dessin_Scorpion1(qp,Obj)                    
                    if Obj.T_car()[2] == "2":
                        
                        self.dessin_Scorpion2(qp,Obj)                    
                    if Obj.T_car()[2] == "3":
                        
                        self.dessin_Scorpion3(qp,Obj)

                elif Obj.T_car()[0:2] == "AI":
                    
                    if Obj.T_car()[5] == "0":
                        self.dessin_Scorpion0(qp,Obj)
                    if Obj.T_car()[5] == "1":
                        self.dessin_Scorpion1(qp,Obj)                    
                    if Obj.T_car()[5] == "2":
                        self.dessin_Scorpion2(qp,Obj)                    
                    if Obj.T_car()[5] == "3":
                        self.dessin_Scorpion3(qp,Obj)

                
    def affiche_Jr_en_crs(self,k):
        """
        Permet d'afficher dans la fenêtre principale quel joueur doit jouer
        
        Paramètres
        ----------
        
        k : int
            numéro du joueur qui doit jouer
            
        
        Return
        ----
        """
        
        if k == 0:
            self.ui.Attaquant.hide()
            self.ui.Defenseur.show()
            self.ui.tr_defenseur_text.show()
            
        if k==1:
            self.ui.Attaquant.show()
            self.ui.Defenseur.hide()
            self.ui.tr_defenseur_text.hide()
            self.ui.tr_attaquant_1_text.show()

        if k==2:
            self.ui.tr_attaquant_1_text.hide()
            self.ui.tr_attaquant_2_text.show()

        if k==3:
            self.ui.tr_attaquant_2_text.hide()
            self.ui.tr_attaquant_3_text.show()
       
        if k==4:
            self.ui.tr_attaquant_3_text.hide()
            self.ui.tr_attaquant_4_text.show()

            
    def dessin_case(self,QPainter,i,j):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        QPainter.setPen(QtGui.QColor(0,100,0))
        QPainter.drawRect(i*36,j*36, 36, 36)

    def dessin_zone_c(self,QPainter,i,j):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        QPainter.setPen(QtCore.Qt.lightGray)
        QPainter.drawRect(i*36,j*36, 36, 36)
        
    def dessin_zone_ap(self,QPainter,i,j):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        QPainter.setPen(QtCore.Qt.red)
        QPainter.drawRect(i*36,j*36, 36, 36)
        
    def dessin_mur(self,QPainter,i,j):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(i*36,j*36, 36, 36)
        QPainter.fillRect(u,QtCore.Qt.black)
    
    def dessin_Scorpion0(self,QPainter,Scorpion):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Scorpion.x*36,Scorpion.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(50,50,200))
        
    def dessin_Scorpion1(self,QPainter,Scorpion):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Scorpion.x*36,Scorpion.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(0,66,0))
        
    def dessin_Scorpion2(self,QPainter,Scorpion):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Scorpion.x*36,Scorpion.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(66,0,0))
        
    def dessin_Scorpion3(self,QPainter,Scorpion):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Scorpion.x*36,Scorpion.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(0,0,66))

    def dessin_metal (self,QPainter,metal):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(metal.x*36,metal.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(192,192,192))
        
    def dessin_Robot_combat(self,QPainter,Robot_combat):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Robot_combat.x*36,Robot_combat.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(150,20,60))

    def dessin_Robot_ouvrier(self,QPainter,Robot_ouvrier):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Robot_ouvrier.x*36,Robot_ouvrier.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(155,20,147))
    
    def dessin_QG(self,QPainter,QG):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(QG.x*36,QG.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(135,206,235))

    def dessin_Foreuse(self,QPainter,Foreuse):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Foreuse.x*36,Foreuse.y*36,36,36)
        QPainter.fillRect(u,QtGui.QColor(255,140,0))
        
    def dessin_Panneau_Solaire(self,QPainter,Panneau_Solaire):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        u = QtCore.QRectF(Panneau_Solaire.x*36,Panneau_Solaire.y*36,36,36)
        QPainter.fillRect(u,QtGui.QColor(255,215,0))
        
    def dessin_L_pos(self,qp,x,y):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        qp.setPen(QtGui.QColor(0,0,0))
        u=QtCore.QRectF(x*36, y*36, 36,36)
        qp.fillRect(u,QtGui.QColor(0,255,0))
        qp.drawRect(u)
        
    def dessin_interet(self,qp,x,y):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        qp.setPen(QtGui.QColor(255,0,0))
        u=QtCore.QRectF(x*36, y*36, 36,36)
        qp.drawRect(u)

    def dessin_interet_proche(self,qp,x,y):
        """
        Permet d'afficher un rectangle dans le conteneur
        
        Paramètres
        ----------
        
        QPainter : QtGui.QPainter
            variable permettant le dessin dans le conteneur
        i,j : coordonnées indiquant où doit etre dessiné le rectangle dans le conteneur
            
        
        Return
        ----
        """
        qp.setPen(QtGui.QColor(255,255,255))
        u=QtCore.QRectF(x*36, y*36, 36,36)
        qp.drawRect(u)        
    
    def simuler(self):
        """
        Permet selon le joueur en cours d'appeler les méthodes adaptées au déroulement d'un tour. Efface également les informations contenu dans le groupbox Info.
        
        Paramètres
        ----------
                           
        Return
        ----
        """
        self.ui.textBrowser_nomUn.clear()
        self.ui.textBrowser_appartenanceUn.clear()
        self.ui.textBrowser_statutUn.clear()
        self.ui.textBrowser_positionUn.clear()
        self.ui.textBrowser_santeUn.clear()
        if self.tr_en_crs == 0:
            self.carte.simuler()
        elif self.tr_Hn_en_crs == 0: 
            self.carte.TrHn.deb_unTourHn()
        elif self.tr_Hn_en_crs == 1:
            self.carte.TrHn.fin_unTourHn()
        return(None)


        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()
