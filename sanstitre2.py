# -*- coding: utf-8 -*-
"""
Created on Thu Apr 19 22:33:10 2018

@author: utilisateurPC
"""
import sys
from PyQt5 import QtGui, QtCore, QtWidgets
from Minima import Ui_Minima_Accueil
from Partie import Partie
from Un_Tour_Joueur import Un_Tour_Du_Joueur
from Joueur import Joueur
from Constantes import Constante
from Map import Map

class MonAppli(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        # Configuration de l'interface utilisateur.

        self.ui = Ui_Minima_Accueil()

        self.ui.setupUi(self)
        self.ui.Bouton_Generer.clicked.connect(self.generer)
        self.ui.Bouton_Findetour.clicked.connect(self.un_Tour)

        self.partie = Partie(1,1)  
        self.ui.lcdNumber_Metal.display(self.partie.L_joueur[0].metal_tot)
        self.ui.lcdNumber_Energie.display(self.partie.L_joueur[0].energie_tot)
        

            
        
#    def dessin_grille(self) :
#        p=QtGui.QPainter(self)
#        p.setBrush(QtGui.QBrush(QtCore.Qt.SolidPattern))
#        # Dessin de la grille
#        largeur_case=self.width()//3
#        hauteur_case=self.height()//3
#        for i in range(4) :
#            p.drawLine(0,i*hauteur_case,self.width(),i*hauteur_case)
#            p.drawLine(i*largeur_case,0,i*largeur_case,self.height())    
    
    def un_Tour(self):
        self.partie.carte.simuler()
        self.paintEvent(self.partie)
        self.ui.conteneur.update()
    
    def paintEvent(self, e):
        qp = QtGui.QPainter()
        qp.begin(self)
        self.affiche_jeu(qp) # une méthode à définir
        qp.end()
    
    def affiche_jeu(self,qp):
        
        
        for obj in self.partie.L_joueur[1]._liste_unite:
            if obj.car() == 'S':
                self.dessin_Scorpion(qp,obj)
        
        for obj in self.partie.L_joueur[0]._liste_unite:
            if obj.car() == 'RC':
                self.dessin_Robot_combat(qp,obj)
        
        for obj in self.partie.L_joueur[0]._liste_unite:
            if obj.car() == 'QG':
                self.dessin_QG(qp,obj)
            if obj.car() == 'F':
                self.dessin_Foreuse(qp,obj)
            if obj.car() == 'P':
                self.dessin_Panneau_Solaire(qp,obj)            
            
                
    def dessin_Scorpion(self,QPainter,Scorpion):
        QPainter.setPen(QtCore.Qt.red)
        QPainter.drawEllipse(Scorpion.x,Scorpion.y, 10, 10)
        
    def dessin_Scorp(self,QPainter):
        QPainter.setPen(QtCore.Qt.red)
        QPainter.drawEllipse(100,100, 100, 100)
       
    def dessin_Robot_combat(self,QPainter,Robot_combat):
        QPainter.setPen(QtCore.Qt.green)
        QPainter.drawRect(Robot_combat.x,Robot_combat.y,10,10)
    
    def dessin_QG(self,QPainter,QG):
        QPainter.setPen(QtCore.Qt.red)
        QPainter.drawRect(QG.x,QG.y,100,100)
                
    def dessin_Foreuse(self,QPainter,Foreuse):
        QPainter.setPen(QtCore.Qt.blue)
        QPainter.drawRect(Foreuse.x,Foreuse.y,10,10)
        
    def dessin_Panneau_Solaire(self,QPainter,Panneau_Solaire):
        QPainter.setPen(QtCore.Qt.yellow)
        QPainter.drawRect(Panneau_Solaire.x,Panneau_Solaire.y,10,10)
    

            
    
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