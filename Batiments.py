from abc import ABC, abstractmethod

class Batiment(ABC):
    """
    Classe décrivant les comportement par défaut des batiments. Peut-être 
    utilisée en l'état ou sous classée pour définir des comportements différents.
    """
    def __init__(self, abscisse, ordonnee, cart,capacite=20):
        """
        Crée un Batiment aux coordonnées désirées.
        
        Paramètres
        ----------
        abscisse, ordonnée: int
            Les coordonnées auxquelles le batiment sera créé.
            
        capacité: int
            niveau de santé maximal du batiment. Vaut 20 par défaut.
        """
        self._max = capacite
        self.__sante = 20
        self._carte = cart
        self.coords = abscisse, ordonnee
        self.rayon_hit_box=0,5
        self._carte.ss_carte[abscisse][ordonnee] = self
        self._carte.append(self)

    def __str__(self):
        """
        Affiche l'état courant du batiment.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
        """
        return "%r : position (%i, %i) etat %i/%i"%(
            self.T_car(), self.x, self.y,
            self.sante, self._max
            )
    
    def car(self):
        """
        Renvoie l'identifiant de l'espèce de l'animal.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère représentant l'animal.
        """
        return 'B' 
    
    
    def affichage(self):
        print(str(self))

#    def attaquer(self):
#        """
#        Le batiment perd un niveau de sante si attaque par ennemie
#        """

    @property
    def coords(self):
        """
        coords: tuple
            Les coordonnées du batiment sur le plateau de jeu
        """
        return self.__coords

    @property
    def x(self):
        """
        x: nombre entier
            Abscisse du batiment
        """
        return self.coords[0]

    @property
    def y(self):
        """
        y: nombre entier
            Ordonné du batiment
        """
        return self.coords[1]

    @coords.setter
    def coords(self, nouv_coords):
        """
        Met à jour les coordonnées du batiment.
        Garantit qu'ils arrivent dans la zone définie par
        la map self._cart.
    
        Paramètres
        ----------
        nouv_coords : tuple représentant les coordonnées auquelles 
                      le batiment essaie de se rendre.
        """
        x, y = nouv_coords
        x = min(x, self._carte.dims[0]-1)
        x = max(x, 0)
        y = min(y, self._carte.dims[1]-1)
        y = max(y, 0)
        self.__coords = (x, y)

    @property
    def sante(self):
        """
        sante: float
            Le niveau de santé du batiment. Si ce niveau arrive à 0 le batiment
            est marqué comme détruit et sera retiré du plateau de jeu
        """
        return self.__sante
    
    @sante.setter
    def sante(self, value):
        """
        Met à jour le niveau de santé du batiment. Garantit que la valeur arrive 
        dans l'intervalle [0, self._max]. Met à 0 les valeurs négatives, ne
        fait rien pour les valeurs trop grandes.
        """
        if value <= self._max:
            self.__sante = value
        if value <= 0:  # <= car certaines cases enlèvent plus de 1 en santé
            value = 0   # ce qui gèrera les décès plus tard
    
    @abstractmethod
    def dessin(self,QPainter):
        ...
            
class QG(Batiment):
    """
    Classe spécialisant Batiments pour représenter le QG.
    """
    def __init__(self, x, y, cart):
        self.name = "QG"
        super().__init__(x, y, cart)
        self.sante = self._max


    def car(self):
        return 'Q '
    
    def T_car(self):
        return("D_B_QG")
    
    def disparition(self):
        print("%s est mort! \n"%(self.T_car()))
        x,y = self.coords
        self._carte.remove(self)
        self._carte.ss_carte[x][y] = ' '
        self._carte.L_joueur[0]._liste_bat[0].remove(self)
        
    
    def dessin(self,QPainter):
        
        QPainter.setPen(QtCore.Qt.red)
        x,y = self.coords
        Painter.drawRect(x,y, 10, 10)



class Panneau_solaire(Batiment):
    
    Id=0
    """
    Classe spécialisant Batiments pour représenter le panneau solaire.
    """
    def __init__(self, x, y, cart):
        super().__init__(x, y, cart)
        self.name = "Panneau_solaire"
        self.sante = self._max
        self.id = Panneau_solaire.Id
        Panneau_solaire.Id += 1

    def T_car(self):
        return("D_B_P%i"%( self.id ))
        
    def car(self):
        return 'P '
    
    def disparition(self):
        print("%s est mort! \n"%(self.T_car()))
        x,y = self.coords
        self._carte.remove(self)
        self._carte.ss_carte[x][y] = ' '
        self._carte.L_joueur[0]._liste_bat[1].remove(self)

    
class Foreuse(Batiment):
    
    Id=0
    """
    Classe spécialisant Batiments pour représenter le panneau solaire.
    """
    def __init__(self, x, y, cart):
        super().__init__(x, y, cart)
        self.name = "Foreuse"
        self.sante = self._max
        self.id = Foreuse.Id
        Foreuse.Id += 1

    def car(self):
        return 'F '
    
    def T_car(self):
        return("D_B_F%i"%( self.id ))
    
    def disparition(self):
        print("%s est mort! \n"%(self.T_car()))
        x,y = self.coords
        self._carte.remove(self)
        self._carte.ss_carte[x][y] = ' '
        self._carte.L_joueur[0]._liste_bat[2].remove(self)
        

            
            
            
            
            
