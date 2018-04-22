
from numpy.random import randint
from numpy.random import choice
import time
from Un_Tour_Joueur import Un_Tour_Du_Joueur
from Ressource import metal
from Batiments import Foreuse,QG,Panneau_solaire
from unites_IA_facile import Scorpion0
from unites_IA_Moyenne import Scorpion1
from Constantes import Constante
from Save_Load import Save, Load
import numpy as np
from PyQt5 import QtGui, QtCore, QtWidgets
from Minima import Ui_Minima_Accueil
class Map(list):
    """
    Classe gérant le déroulement du jeu. 
    """
    def __init__(self,L_joueur,l =0):
        self.ui=Ui_Minima_Accueil()       
        if l == 0 :
            
            
            self.__xmax = Constante.xmax
            self.__ymax = Constante.ymax  
            self.nbtour = Constante.nbt 


            self.H=Constante.H_Z_Constructible
            self.L=Constante.L_Z_Constructible
            self.Epp = Constante.Ep_app
            self.Ltr_actuel = 0
            self.L_joueur = L_joueur
            self.ss_carte = np.array([[' ' for j in range(self.__ymax)] for i in range(self.__xmax)], dtype = object)

            U = QG(int(self.__xmax/2),int(self.__ymax/2),self)
#        self.ss_carte[int(self.__xmax/2)][int(self.__ymax/2)] = U
 #       self.append(U)
            self.L_joueur[0]._liste_bat[0].append(U)
        
        else : 
            self.__xmax = Constante.xL
            self.__ymax = Constante.yL  
            self.nbtour = Constante.Lnbt
            self.Ltr_actuel = Constante.Lnbta


            self.H=Constante.LH_Z_Constructible
            self.L=Constante.LL_Z_Constructible
            self.Epp = Constante.LEp_app
            self.L_joueur = L_joueur
            self.ss_carte = np.array([[' ' for j in range(self.__ymax)] for i in range(self.__xmax)], dtype = object)

            
        self.spawn_ress=Constante.spawn_ress

        self.Tr = Un_Tour_Du_Joueur(self)

        self.V_atta = 0
      #  self.createInitObject()
      



        # Tracer les murs dans la sous-map
        for i in ( (self.__xmax - self.L )//2, (self.__xmax + self.L )//2 ):  # -1 ; -1
            #Trace les murs du haut et du bas, avec un trou au milieu de ces deux lignes.
            for j in range( (self.__ymax - self.H + 1)//2, self.__ymax//2 - 1):
                self.ss_carte[i][j] = '/'
            for j in range( self.__ymax//2 + 2, (self.__ymax + self.H - 1)//2+1):
                self.ss_carte[i][j] = '/'
        for j in ( (self.__ymax -self.H)//2 , (self.__ymax + self.H )//2 ):
            # Trace les murs de gauche et de droite, avec un trou au milieu de ces deux colonnes
            for i in range( (self.__xmax - self.L +1)//2 , self.__xmax//2 -1 ):
                self.ss_carte[i][j] = '/'
            for i in range( self.__xmax//2 + 2, (self.__xmax + self.L - 1)//2 + 2 ) :
                self.ss_carte[i][j] = '/'

          
            
#        self.L_joueur[0]._liste_bat.append(U)

        """Actuellement, carte contient l'ensemble des objets en jeu """


 #   def createInitObject(self):        
  #      self.Panneau_solaire=Panneau_solaire(0,0,self,self)
   #     self.Foreuse=Foreuse(0,0,self,self)



   
    @property
    def dims(self):
        """
        Renvoies les dimensions du plateau de jeu
        """
        return (self.__xmax, self.__ymax)
    
    @dims.setter
    def dims(self,x,y):
        self.__xmax, self.__ymax = x,y
        return(self.__xmax, self.__ymax)
    
    def __str__(self):
        """Affiche le plateau de jeu en mode texte 
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: string
            La chaîne de caractères qui sera affichée via ''print''
            
       
        """
        return self.generation_Terrain()     # Pour l'affichage sur deux caractères
    
    def generation_Terrain(self):
        """
        Conversion en chaîne avec deux caractères par case.
        """

        pos={}
        s=""
         
        for obj in self:
            pos[obj.coords]=obj.car()
        for i in range(self.__xmax):
            for j in range(self.__ymax):  
                if (i>(self.__xmax-(self.L))/2 and i<(self.__xmax+(self.L-1))/2) and (j>(self.__ymax-(self.H))/2 and j<(self.__ymax+(self.H-1))/2):
                    s += "#" #zone constructible
                elif self.ss_carte[i][j] == '/':
                    s += "/" #Mur de protection 
                elif ((i<= self.Epp ) and (j>(self.__ymax-1-self.H-(self.__ymax - self.H)/2) and (j< (self.__ymax - self.H )/2+self.H+1))) or ((i >= self.__xmax-1-self.Epp ) and (j>(self.__ymax-1-self.H-(self.__ymax - self.H)/2) and (j< (self.__ymax - self.H )/2+self.H+1))) or ((j<= self.Epp) and ((i>self.__xmax-1-self.L-(self.__xmax-self.L)/2) and (i<self.__xmax-(self.__xmax-self.L)/2+1))) or ((j>=self.__ymax-1-self.Epp) and ((i>self.__xmax-1-self.L-(self.__xmax-self.L)/2) and (i<self.__xmax-(self.__xmax-self.L)/2+1))) :
                    s +="!" #zone d'apparition des unites qui attaques   
                else:
                    s += "."
                if (i, j) in pos:
                    s += pos[(i,j)]
                else:
                    s += "  "
            s += "\n"
        return s
        
    def apparition_ressource(self):
        """
        permet de faire apparaitre une ressource de metal en dehors de la zone 
        constructible(#) et du murs de défense(/)
        """
        for z in range(int(self.spawn_ress/2)):  #spawn les ressource en generation de map
            val=randint(0,1)
            if val==0:
                i=randint(0,self.__xmax)
                j=choice([randint(0,(self.__ymax-self.H)/2),randint((self.__ymax-self.H)/2+self.H+1,self.__ymax)])
                Obj = self.ss_carte[i][j]
                while Obj != ' ' :             
                    i=randint(0,self.__xmax)
                    j=choice([randint(0,(self.__ymax-self.H)/2),randint((self.__ymax-self.H)/2+self.H+1,self.__ymax)])
                    Obj=self.ss_carte[i][j]
                U=metal(i,j,self,randint(1,5))
                self.append(U)
                self.ss_carte[i][j]=U
        
            elif val==1:
                 
                i=choice([randint(0,(self.__xmax-self.L)/2),randint((self.__xmax-self.L)/2+self.L+1,self.__xmax)])
                j=randint(0,self.__ymax)
                Obj = self.ss_carte[i][j]
                while Obj != ' ':
                    i=choice([randint(0,(self.__xmax-self.L)/2),randint((self.__xmax-self.L)/2+self.L+1,self.__xmax)])
                    j=randint(0,self.__ymax)
                    Obj = self.ss_carte[i][j]
                U=metal(i,j,self,randint(1,5))
                self.append(U)
                self.ss_carte[i][j]=U

                    
    def ressource_tot(self):
        """
        renvoie au joueur l'information su nombre de ressources qu'il possède
        """
        L_bat = self.L_joueur[0]._liste_bat
        self.L_joueur[0].energie_tot += len(L_bat[1])*Constante.prod_E_P + Constante.prod_E_QG
        self.L_joueur[0].metal_tot += len(L_bat[2])*Constante.prod_M_F + Constante.prod_M_QG

        print('energie total = ' + str(self.L_joueur[0].energie_tot))
        print('metal total = ' + str(self.L_joueur[0].metal_tot))                
        
#        self.ui.lcdNumber_Metal.display(str(self.L_joueur[0].metal_tot))
#        self.ui.lcdNumber_Energie.display(str(self.L_joueur[0].energie_tot))

    

       
            
    def simuler (self):
        """
        Contrôle l'évolution du jeu, affiche le résultat de chaque tour dans
        un terminal.
        
        Paramètres
        ----------
        Aucun

        Renvoie
        -------
        Rien  
        """
        


                    
        for t in range(self.Ltr_actuel, self.nbtour):
            self.tr_actuel = t
            print("### Tour %i ###"%(t))
                  
#            self.ui.lcdNumber_Tours_restant.display(t)
                  
#            Chx = input("Sauvegarder/Charger? (S pour sauvegarder, C pour charger, rien sinon) \n")
#            if Chx == "S":
#                name = input("Entrez le nom de la sauvegarde \n")
#                name = name + ".txt"
#                self.Save = Save(name,self)
#            elif Chx == "C":
#                name = input("Entrez le nom de votre sauvegarde \n")
#                name = name + ".txt"    
#                self.Load = Load(name)
#                break
                  
                  
            if t%5==0:
                self.apparition_ressource()

                    
            self.ressource_tot()

            self.Tr.unTour()
            print(self)
            time.sleep(0.2)
            if self.V_atta == 1:
                break
        if Chx != "C":
            
            print("Fin de partie \n")
            if len(self.L_joueur[0]._liste_bat[0]) !=0:
                print("Le défenseur gagne!")
            else:
                print("Les attaquants gagnent!")

                 
#if __name__ == "__main__":
#    carte = Map()
#    print(carte)
#    carte.simuler()
