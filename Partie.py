# -*- coding: utf-8 -*-
"""
Éditeur de Spyder
"""
import Map
from Joueur import Joueur
from Constantes import Constante

class Partie():
    """
    Classe mère, contenant l'ensemble des propriétés des objets intervenant dans
    le jeu.
    """

    def __init__(self, nb_ia_0, nb_ia_1=0 , nb_hn = 0,IHM = 0):
        
        """
        Permet de créer la partie, à partir du nombre de joueurs (humains et IA)
        mis en entrée.
        
    Paramètres
    ----------
        nb_ia_0: int
            Le nombre de joueurs IA de niveau 0.
            
        nb_ia_1 : int
            Le nombre de joueurs IA de niveau 1.        
        
        nb_hn : int
            Le nombre de joueurs humains.
        """
        self.IHM = IHM
        self.L_joueur = [Joueur('DH')]
        self.nb_hn = nb_hn 
        Posdisp = [ str(k) for k in range(self.nb_hn+nb_ia_0+nb_ia_1)]
        while self.nb_hn > 0:
            self.L_joueur.append(Joueur('AH'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            self.nb_hn -= 1
        
        while nb_ia_0 > 0:
            self.L_joueur.append(Joueur('AI_0_'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            nb_ia_0 -= 1
            
        while nb_ia_1 > 0:
            self.L_joueur.append(Joueur('AI_1_'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            nb_ia_1 -= 1
            
        self.mise_en_place()
        self.carte = Map.Map(self.L_joueur,0,self.IHM)
    
    def mise_en_place(self):
        """
        Méthode exécutant les ajustements de base pour débuter la partie, sur chaque
        joueur.
        """

        self.L_joueur[0].metal_tot, self.L_joueur[0].energie_tot = Constante.metal_tot, Constante.energie_tot



if __name__ == "__main__":
    Game = Partie(4,)
    Game.carte.simuler()
