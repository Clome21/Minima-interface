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

    def __init__(self, nb_ia , nb_hn = 1,IHM = 0):
        
        """
        Permet de créer la partie, à partir du nombre de joueurs (humains et IA)
        mis en entrée.
        
    Paramètres
    ----------
        nb_ia: int
            Le nombre de joueurs IA.
        
        nb_hn : int
            Le nombre de joueurs humains.
        """
        self.IHM = IHM
        self.L_joueur = [Joueur('DH')]
        self.nb_hn = nb_hn 
        Posdisp = [ str(k) for k in range(self.nb_hn+nb_ia)]
        while self.nb_hn > 0:
            self.L_joueur.append(Joueur('AH'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            self.nb_hn -= 1
        
        nb_ia_0, nb_ia_1, nb_ia_2 = self.choix_niveau(nb_ia)
        
        while nb_ia_0 > 0:
            self.L_joueur.append(Joueur('AI_0_'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            nb_ia_0 -= 1
            
        while nb_ia_1 > 0:
            self.L_joueur.append(Joueur('AI_1_'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            nb_ia_1 -= 1
            
        while nb_ia_2 > 0:
            self.L_joueur.append(Joueur('AI_2_'+Posdisp[0]))
            Posdisp = Posdisp[1:]
            nb_ia_2 -= 1
            
        self.mise_en_place()
        self.carte = Map.Map(self.L_joueur,0,self.IHM)
    
    def mise_en_place(self):
        """
        Méthode exécutant les ajustements de base pour débuter la partie, sur chaque
        joueur.
        """

        self.L_joueur[0].metal_tot, self.L_joueur[0].energie_tot = Constante.metal_tot, Constante.energie_tot
    
    def choix_niveau(self,nb_ia):
        """
        Permet au joueur humain de choisir le niveau de difficulté de l'IA.
        
        Paramètres
        ----------
        
        nb_ia: int
            Le nombre de joueurs IA.
        
        Renvoie 
        ---------
            
        nb_ia_i (i entre 0 et 2) : int
            Le nombre d'IA de niveau i, choisies par le joueur humain.         
        
    
                """
        nb_ia_0 = nb_ia
        nb_ia_1 = 0
        nb_ia_2 = 0
                
        return(nb_ia_0, nb_ia_1, nb_ia_2)
            


if __name__ == "__main__":
    Game = Partie(4,)
    Game.carte.simuler()
