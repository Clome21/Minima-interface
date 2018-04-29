# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 21:17:38 2018

@author: Clément.SAWCZUK
"""

class Constante:
    """ Classe contenant l'ensemble des constantes utilisées dans le jeu.
    """
#----------------------------------------Constantes map    
    xmax = 15
    ymax = 15
    
    assert(xmax%2 !=0)
    assert(ymax%2 !=0)
    
    
# !!!! xmax, ymax doivent être impairs!

    if int(xmax/2)%2 == 0:
        L_Z_Constructible= int(xmax/2)+1
    else : 
        L_Z_Constructible= int(xmax/2)
    if int(ymax/2)%2 == 0:
        H_Z_Constructible= int(ymax/2)+1
    else:
        H_Z_Constructible= int(ymax/2)
    
#    L_Z_Constructible = 9
#    H_Z_Constructible = 11
        
    Ep_app = int(max(xmax,ymax)/20)
    
#----------------------------------------Constantes ressources de départ    
    metal_tot=20
    energie_tot=20
    nbt= 15
    spawn_ress=2
#----------------------------------------Constantes Batiments
#----------------------------------Foreuse    
    cout_M_F=2
    cout_E_F=3   
    prod_M_F=1
#----------------------------------Panneau solaire
    cout_M_P=2  
    cout_E_P=2  
    prod_E_P=3

#----------------------------------QG
    
    prod_E_QG = 1
    prod_M_QG = 1
    
    nbe_unite_ajoute = 1 #0.5
    
#----------------------------------------Constantes Unites
#-------------------------------Robot combat
    
    capmvt_RC = 1
    cout_M_RC = 3
    cout_E_RC = 3
    capcbt_RC = 4
    

#------------------------------Robot Ouvrier
    
    capmvt_RO = 2
    cout_M_RO = 2
    cout_E_RO = 2

#------------------------------Scorpion0

    capmvt_S0 = 2
    capcbt_S0 = 1
    
#-----------------------------Scorpion

    capmvt_S = 2
    capcbt_S = 1
    
    
#-------------------------------------------- Valeurs chargées
    
        
    xL = 20
    yL = 20

    if int(xL/2)%2 == 0:
        LL_Z_Constructible= int(xL/2)+1
    else : 
        LL_Z_Constructible= int(xL/2)
    if int(yL/2)%2 == 0:
        LH_Z_Constructible= int(yL/2)+1
    else:
        LH_Z_Constructible= int(yL/2)
    
#    L_Z_Constructible = 9
#    H_Z_Constructible = 11
        

    LEp_app = int(max(xL,yL)/20)
    
    
    Lnbta = 1
    Lnbt = 20
    
