class Ressource(object):
    """
     Classe décrivant les comportement par défaut des ressources. Peut-être 
    utilisée en l'état ou sous classée pour définir des comportements différents.
    """
    def __init__(self, abscisse, ordonnee, cart,valeur):
        """
        Crée une ressource aux coordonnées désirées.
        
        Paramètres
        ----------
        abscisse, ordonnée: int
            Les coordonnées auxquelles la ressource sera créé.
            
        """
        
        self._cart = cart
        self.coords = abscisse, ordonnee
        self.valeur= valeur
        self._cart.append(self)
        self._cart.ss_carte[abscisse][ordonnee]= self


    def __str__(self):
        """
        Affiche l'état courant de la ressource.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        s: str
            La chaîne de caractères qui sera affichée via ''print''
        """
        return "%s: position (%i, %i) valeur %i"%(
            self.car(), self.x, self.y,self.valeur)
        
        
            
    def car(self):
        """
        Renvoie l'identifiant du type de ressource.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère représentant la ressource.
        """
        return 'R'   
    
    def affichage(self):
        """
        """
        print(str(self))

    @property
    def coords(self):
        """
        coords: tuple
            Les coordonnées de la ressource sur le plateau de jeu
        """
        return self.__coords

    @property
    def x(self):
        """
        x: nombre entier
            Abscisse de la ressource
        """
        return self.coords[0]

    @property
    def y(self):
        """
        y: nombre entier
            Abscisse de la ressource
        """
        return self.coords[1]
    
    @coords.setter
    def coords(self, nouv_coords):
        """
        Met à jour les coordonnées de la ressource.
        Garantit qu'elles arrivent dans la zone définie par
        la carte self._cart.
    
        Paramètres
        ----------
        nouv_coords : tuple représentant les coordonnées auquelles 
                      la ressource sera.
        """

        x, y = nouv_coords
        x = min(x, self._cart.dims[0]-1)
        x = max(x, 0)
        y = min(y, self._cart.dims[1]-1)
        y = max(y, 0)
        self.__coords = (x, y)
    
    def disparition(self):
        x,y = self.coords
        self._cart.remove(self)
        self._cart.ss_carte[x][y] = ' '
        
        
    
class metal(Ressource):
    """
    Classe décrivant les comportement par défaut de la ressource metal
    """
    def __init__(self, x, y, cart,valeur):
        super().__init__(x, y, cart,valeur)
        self.name = "metal"
    
    def car(self):
        """
        Renvoie le symbole identifiant le métal.
        
        Paramètres
        ----------
        Aucun
        
        Renvoie
        -------
        c: str
            Le caractère représentant le métal.
        """
        return 'M '
    
    def T_car(self):
        """Méthode contenant l'ensemble des informations permettant d'identifier le batiment.
        Dans l'ordre : 
            N : le rôle du joueur possédant l'objet. Ici, le joueur neutre.
            R : le type global de l'objet. Ici, ressource.
            M : le role de l'objet. Ici, Métal.

            
        Paramètres : 
        -------------
        Aucun.
        
        Renvoie : 
        ----------
        'N_R_M': str
            La chaîne de caractère identifiant la ressource.
            
        """
        return('N_R_M')





