# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:33:10 2018

@author: utilisateurPC
"""
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from Minima_prop import Ui_Minima_Accueil
#from Minima_2_fen import Ui_Minima_Accueil,Ui_Minima_Jeu
from Partie import Partie
from Un_Tour_Hn import Un_Tour_Joueur_Hn
from Unites_Hn_Defenseur import Robot_combat
from Batiments import Panneau_solaire
from Joueur import Joueur
from Constantes import Constante
from Map import Map
import time

class MonAppli(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setMouseTracking(True)

        # Configuration de l'interface utilisateur.
        self.partie = Partie(1,1)  
        self.carte=self.partie.carte
        self.ui = Ui_Minima_Accueil()
        self.ui.setupUi(self,self.carte)
        
        self.tr_actuel=0
        self.nbtour=Constante.Lnbt
        self.k=0
        
#        self.ui.Bouton_Generer.clicked.connect(self.generer)

        self.l = "i"
        self.coord="O"
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
        

#        self.ui.Button_Jouer.clicked.connect(self.test)
#        self.ui.Button_Jouer.clicked.connect(self.ui.Minima_Accueil.close)
        
        self.pos_souris_x=int
        self.pos_souris_y=int
        
        self.pos_souris_x_bouger=int
        self.pos_souris_y_bouger=int


        self.ui.Button_Ready.clicked.connect(self.jeu)
        self.ui.Button_Ready.clicked.connect( self.ui.Button_Ready.hide)
        
        
        self.ui.lcdNumber_Metal.display(self.partie.L_joueur[0].metal_tot)
        self.ui.lcdNumber_Energie.display(self.partie.L_joueur[0].energie_tot)
        
              
        self.ui.Bouton_Findetour.clicked.connect(self.tr_suivant)
        self.ui.Bouton_Findetour.clicked.connect(self.simuler) 
        self.ui.Bouton_Findetour.clicked.connect(self.jeu)
#-------------------place un batiment

        self.ui.Button_Foreuse.clicked.connect(self.plac_for)
        self.ui.Button_Foreuse.clicked.connect(self.L_pos_bat)

        
        self.ui.Button_Panneau_Solaire.clicked.connect(self.plac_PS)
        self.ui.Button_Panneau_Solaire.clicked.connect(self.L_pos_bat)
        
        self.ui.Button_J_D_B_Fermer.clicked.connect(self.raz)
        
#-------------------production unité
        
        self.ui.Button_Robot_Combat.clicked.connect(self.plac_RC)
        self.ui.Button_Robot_Combat.clicked.connect(self.L_pos_u)
        
        self.ui.Button_Robot_Ouvrier.clicked.connect(self.plac_RO)
        self.ui.Button_Robot_Ouvrier.clicked.connect(self.L_pos_u)
        
        self.ui.Bouton_Generer.clicked.connect(self.bouger_u)
        
        self.ui.Button_J_D_U_Fermer.clicked.connect(self.raz)

        



        
#    def test(self):
#        self.ui2 = Ui_Minima_Jeu(self.carte)
#        self.ui.Minima_Jeu.show()
        
    def tr_suivant(self):
        self.k+=1
        if self.k>=len(self.partie.L_joueur):
            self.k=0
            self.tr_actuel+=1

        
    def mouseDoubleClickEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton :
            self.pos_souris_x=int((event.x()/36))
            self.pos_souris_y=int((event.y()/36))
        if event.button() == QtCore.Qt.RightButton :
            self.pos_souris_x_bouger=int((event.x()/36))
            self.pos_souris_y_bouger=int((event.y()/36))
               
        
    def raz(self):
        self.l = 1
        self.paintEvent(2)
        self.ui.conteneur.update()
    
    def bouger_u(self):
        for unite in self.partie.L_joueur[0]._liste_unite:
            if (self.pos_souris_x==unite.x and self.pos_souris_y==unite.y):
                unite.bouger(self.pos_souris_x_bouger,self.pos_souris_y_bouger)
                self.l="bg"
                self.paintEvent(2)
                self.ui.conteneur.update()
    
    def activation_boutons(self):
        if (self.partie.L_joueur[0].metal_tot>=Constante.cout_M_P and self.partie.L_joueur[0].energie_tot>=Constante.cout_E_P):
            self.ui.Button_Panneau_Solaire.setEnabled(True)
        else:
            self.ui.Button_Panneau_Solaire.setEnabled(False)
            
        if (self.partie.L_joueur[0].metal_tot>=Constante.cout_M_F and self.partie.L_joueur[0].energie_tot>=Constante.cout_E_F):
            self.ui.Button_Foreuse.setEnabled(True)
        else:
            self.ui.Button_Foreuse.setEnabled(False)
        if (self.partie.L_joueur[0].metal_tot>=Constante.cout_M_RC and self.partie.L_joueur[0].energie_tot>=Constante.cout_E_RC):
             self.ui.Button_Robot_Combat.setEnabled(True)

        else:
            self.ui.Button_Robot_Combat.setEnabled(False)
            
                
                
        
        
        
    def maj_compteur_ressources(self):
        self.ui.lcdNumber_Metal.display(self.partie.L_joueur[0].metal_tot)
        self.ui.lcdNumber_Energie.display(self.partie.L_joueur[0].energie_tot)
        self.ui.lcdNumber_Tours_restant.display(self.nbtour-self.tr_actuel)


    def plac_RC(self):
        self.activation_boutons()
        self.partie.carte.TrHn.production_unite_defense_combat(self.pos_souris_x,self.pos_souris_y)
        self.maj_compteur_ressources()
        self.l=1
        self.paintEvent(2)
        self.ui.conteneur.update()
        
    def plac_RO(self):
        self.activation_boutons()
        self.partie.carte.TrHn.production_unite_defense_production(self.pos_souris_x,self.pos_souris_y)
        self.maj_compteur_ressources()
        self.l=1
        self.paintEvent(2)
        self.ui.conteneur.update()
        
    def plac_for(self):
        self.activation_boutons()
        self.partie.carte.TrHn.placer_une_foreuse(self.pos_souris_x,self.pos_souris_y) 
        self.maj_compteur_ressources()
        self.l=1
        self.paintEvent(2)
        self.ui.conteneur.update()

    
    def plac_PS(self):
        self.activation_boutons()
        self.partie.carte.TrHn.placer_un_Panneau_solaire(self.pos_souris_x,self.pos_souris_y)
        self.maj_compteur_ressources()
        self.l=1
        self.paintEvent(2)
        self.ui.conteneur.update()
        
    def plac_Sc(self):
        self.activation_boutons()
        self.partie.carte.TrHn.production_unite_attaque_Hn(self.k,self.pos_souris_x,self.pos_souris_y)
        self.maj_compteur_ressources()
        self.l=1
        self.paintEvent(2)
        self.ui.conteneur.update()

    


    def jeu(self):
        self.l=1
        self.paintEvent(2)
        self.ui.conteneur.update()
        
    def L_pos_a(self):
        self.l="ps"
        self.paintEvent(2)
        self.ui.conteneur.update()
        
    def L_pos_bouger(self):
        self.l="bg"
        self.paintEvent(2)
        self.ui.conteneur.update()
        
        
    def L_pos_u(self):
        self.l = "pu"
        self.paintEvent(2)
        self.ui.conteneur.update()
        
    def L_pos_bat(self):
        self.l = "pb"
        self.paintEvent(2)
        self.ui.conteneur.update()
        
        

    def paintEvent(self,e):
        qp = QtGui.QPainter()
        qp.begin(self)
        if self.l!= "i":
            self.affiche_map(qp)
            self.affiche_jeu(qp)# une méthode à définir
        if self.l== "pb":    
            self.affiche_L_pos_bat(qp)
        if self.l== "pu":    
            self.affiche_L_pos_u(qp)
        if self.l=="bg":
            self.affiche_L_pos_bouger(qp)
        if self.l=="ps":
            self.affiche_L_pos_a(qp)
        qp.end()
        
    def affiche_L_pos_a(self,qp):
        L_Ht = self.placement_pos(0,self.Epp + 1,(self.__ymax -self.H)//2,(self.__ymax + self.H )//2,' ')            
        L_Bas = self.placement_pos(self.__xmax-1-self.Epp,self.__xmax,(self.__ymax -self.H)//2,(self.__ymax + self.H )//2,' ')        
        L_Gche = self.placement_pos((self.__xmax - self.L )//2 , (self.__xmax + self.L )//2,0,self.Epp+1,' ')        
        L_Dte = self.placement_pos((self.__xmax - self.L )//2, (self.__xmax + self.L )//2,self.__ymax -1-self.Epp,self.__ymax,' ')
        
        L_pos = L_Ht + L_Bas + L_Gche + L_Dte 
        for i in L_pos:
                self.dessin_L_pos(qp,i[0],i[1])
        
    def affiche_L_pos_bouger(self,qp):
        for unitee in self.partie.L_joueur[0]._liste_unite:
            L_pos=unitee.mvt_poss()
            for i in L_pos:
                self.dessin_L_pos(qp,i[0],i[1])
        
    def affiche_L_pos_bat(self,qp):
        L_pos = self.partie.carte.TrHn.placement_pos_bat(self.x_inf_b,self.x_sup_b,self.y_inf_b,self.y_sup_b,' ')
        for i in L_pos:
            self.dessin_L_pos(qp,i[0],i[1])
            
    def affiche_L_pos_u(self,qp):
        L_pos = self.partie.carte.TrHn.placement_pos(self.x_inf,self.x_sup,self.y_inf,self.y_sup,' ')
        for i in L_pos:
            self.dessin_L_pos(qp,i[0],i[1])
        
        
        
        
    def affiche_map(self,qp):
        for i in range(self.__xmax):
            for j in range(self.__ymax):  
                
                if self.partie.carte.ss_carte[i][j] == '/':
                    self.dessin_mur(qp,i,j)
                elif i == (self.__xmax - self.L )//2 or i == (self.__xmax + self.L )//2-1:
                    if j<= self.Epp or j >=self.__ymax - self.Epp :
                        self.dessin_zone_ap(qp,i,j)
                    else:
                        self.dessin_case(qp,i,j)                       
                    
                
                elif i >= (self.__xmax - self.L )//2+1 and i < (self.__xmax + self.L )//2-1 :
                    if j >= (self.__ymax -self.H)//2 +1 and j< (self.__ymax + self.H )//2-1:
                        self.dessin_zone_c(qp,i,j)
                    elif j<= self.Epp or j >=self.__ymax - self.Epp :
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
        
        for k in range (len(self.partie.L_joueur)):
            if k==1:
                for obj in self.partie.L_joueur[1]._liste_unite:
                    if obj.car() == 's':
                        self.dessin_Scorpion(qp,obj)
            if k==2:
                for obj in self.partie.L_joueur[2]._liste_unite:
                    if obj.car() == 's':
                        self.dessin_Scorpion(qp,obj)
            
            if k==3:
                for obj in self.partie.L_joueur[3]._liste_unite:
                    if obj.car() == 's':
                        self.dessin_Scorpion(qp,obj)
                        
            if k==4:
                for obj in self.partie.L_joueur[4]._liste_unite:
                    if obj.car() == 's':
                        self.dessin_Scorpion(qp,obj)
            
        for obj in self.partie.L_joueur[0]._liste_unite:
            if obj.car() == 'RC':
                self.dessin_Robot_combat(qp,obj)
            
        for obj in self.partie.L_joueur[0]._liste_unite:
            if obj.car() == 'RO':
                self.dessin_Robot_ouvrier(qp,obj)
            
        for obj in self.partie.L_joueur[0]._liste_bat[0]:
            self.dessin_QG(qp,obj)
        for obj in self.partie.L_joueur[0]._liste_bat[1]:
            self.dessin_Foreuse(qp,obj)
        for obj in self.partie.L_joueur[0]._liste_bat[2]:
            self.dessin_Panneau_Solaire(qp,obj) 
            
    def dessin_case(self,QPainter,i,j):
        QPainter.setPen(QtGui.QColor(0,100,0))
        QPainter.drawRect(i*36,j*36, 36, 36)

    def dessin_zone_c(self,QPainter,i,j):
        QPainter.setPen(QtCore.Qt.lightGray)
        QPainter.drawRect(i*36,j*36, 36, 36)
        
    def dessin_zone_ap(self,QPainter,i,j):
        QPainter.setPen(QtCore.Qt.red)
        QPainter.drawRect(i*36,j*36, 36, 36)
        
    def dessin_mur(self,QPainter,i,j):
        QPainter.setPen(QtCore.Qt.blue)
        u = QtCore.QRectF(i*36,j*36, 36, 36)
        QPainter.fillRect(u,QtCore.Qt.black)
    
    def dessin_Scorpion(self,QPainter,Scorpion):
        print('S')
        u = QtCore.QRectF(Scorpion.x*36,Scorpion.y*36, 36, 36)
        QPainter.fillRect(u,QtCore.Qt.black)

        

    def dessin_Robot_combat(self,QPainter,Robot_combat):
        u = QtCore.QRectF(Robot_combat.x*36,Robot_combat.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(220,20,60))
#        QPainter.drawEllipse(Robot_combat.x*30,Robot_combat.y*30,30,30)
        
    def dessin_Robot_ouvrier(self,QPainter,Robot_ouvrier):
        u = QtCore.QRectF(Robot_ouvrier.x*36,Robot_ouvrier.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(255,20,147))
    
    def dessin_QG(self,QPainter,QG):
        u = QtCore.QRectF(QG.x*36,QG.y*36, 36, 36)
        QPainter.fillRect(u,QtGui.QColor(135,206,235))

                
    def dessin_Foreuse(self,QPainter,Foreuse):
        u = QtCore.QRectF(Foreuse.x*36,Foreuse.y*36,36,36)
        QPainter.fillRect(u,QtGui.QColor(255,140,0))

        
    def dessin_Panneau_Solaire(self,QPainter,Panneau_Solaire):
        u = QtCore.QRectF(Panneau_Solaire.x*36,Panneau_Solaire.y*36,36,36)
        QPainter.fillRect(u,QtGui.QColor(255,215,0))
        
    def dessin_L_pos(self,qp,x,y):
        qp.setPen(QtGui.QColor(0,0,0))
        u=QtCore.QRectF(x*36, y*36, 36,36)
        qp.fillRect(u,QtGui.QColor(0,255,0))
        qp.drawRect(u)
    
    def simuler(self):
        
       
            t= self.tr_actuel 
            print("### Tour %i ###"%(t))
                                    
            if t%5==0:
                self.carte.apparition_ressource()
            self.maj_compteur_ressources()
            

            self.unTourHn()
            self.unTourIA()
            
            print(self)
            time.sleep(0.2)
            
            if self.partie.carte.V_atta==1:
                print("Les attaquants gagnent!")
                
            
            if t==self.nbtour:
                print("Fin de partie")
                if len(self.partie.L_joueur[0]._liste_bat[0]) !=0:
                    print("Le défenseur gagne!")
                else:
                    print("Les attaquants gagnent!")
    def unTourIA(self):
        #n = len(self.L_joueur)
        
        role = self.partie.L_joueur[self.k]._role
        if role[1] == 'I':
            print("\\\ Tour du joueur %r ///"%(role))
            self.partie.carte.TrIA.production_unite_attaque_IA_0(self.k)
            
            self.ui.Attaquant.hide()
            self.ui.Defenseur.hide()
    
            L_unite = self.partie.L_joueur[self.k]._liste_unite
            for c in L_unite:
                print("Tour de %r \n"%(c.T_car()))
                c.bouger()
                c.action()
    
        self.partie.carte.TrIA.unite_disp_par_tour += Constante.nbe_unite_ajoute
        if self.partie.carte.TrIA.unite_disp_par_tour> min(self.L,self.H):
            self.partie.carte.TrIA.unite_disp_par_tour = min(self.L,self.H)
            
    def unTourHn(self):
        #n = len(self.L_joueur)

        role = self.partie.L_joueur[self.k]._role
        if role[1] == 'H':
            print("\\\ Tour du joueur %r ///"%(role))
        if role[0] == 'D':
            self.ui.Attaquant.hide()
            self.ui.Defenseur.show()
            #self.construction_bat()
        #self.production_unite(role,k)
        else:
            self.ui.Attaquant.show()
            self.ui.Defenseur.hide()

        
        self.partie.carte.TrHn.unite_disp_par_tour += Constante.nbe_unite_ajoute
        if self.partie.carte.TrHn.unite_disp_par_tour > min(self.L,self.H):
            self.partie.carte.TrHn.unite_disp_par_tour = min(self.L,self.H)
    
    def generer(self):
#        self.partie = Partie(self.ui.Nb_IA_Choisi(),self.ui.Nb_Humain_Choisi())
        self.partie = Partie(1,1) 
        self.ui.conteneur.update()
        print('generer')
        
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MonAppli()
    window.show()
    app.exec_()