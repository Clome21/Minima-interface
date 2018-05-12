# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Minima.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys
from Constantes import Constante
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Minima_Accueil(object):
    

    
    def setupUi(self, Minima_Accueil):
        
        

        x,y = Constante.xmax, Constante.ymax
        
        Minima_Accueil.setObjectName("Minima_Accueil")
        Minima_Accueil.resize(1240, 813)
        self.centralwidget = QtWidgets.QWidget(Minima_Accueil)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_Accueil = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Accueil.setEnabled(True)
        self.groupBox_Accueil.setGeometry(QtCore.QRect(210, 50, 631, 541))
        self.groupBox_Accueil.setTitle("")
        self.groupBox_Accueil.setObjectName("groupBox_Accueil")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_Accueil)
        self.textBrowser.setGeometry(QtCore.QRect(20, 30, 591, 171))
        self.textBrowser.setObjectName("textBrowser")
        self.Button_Ac_Jouer = QtWidgets.QPushButton(self.groupBox_Accueil)
        self.Button_Ac_Jouer.setGeometry(QtCore.QRect(120, 210, 351, 101))
        self.Button_Ac_Jouer.setObjectName("Button_Ac_Jouer")
        self.Button_Ac_Quitter = QtWidgets.QPushButton(self.groupBox_Accueil)
        self.Button_Ac_Quitter.setGeometry(QtCore.QRect(120, 430, 351, 91))
        self.Button_Ac_Quitter.setObjectName("Button_Ac_Quitter")
        self.Button_Ac_Charger = QtWidgets.QPushButton(self.groupBox_Accueil)
        self.Button_Ac_Charger.setGeometry(QtCore.QRect(120, 320, 351, 101))
        self.Button_Ac_Charger.setObjectName("Button_Ac_Charger")
        
        
        self.groupBox_Jeu = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Jeu.hide()
        self.groupBox_Jeu.setGeometry(QtCore.QRect(0, 0, 2000, 1000))
        self.groupBox_Jeu.setAutoFillBackground(False)
        self.groupBox_Jeu.setTitle("")
        self.groupBox_Jeu.setObjectName("groupBox_Jeu")
        
        self.conteneur = QtWidgets.QWidget(  self.groupBox_Jeu)
        self.conteneur.setGeometry(QtCore.QRect(0,100, x*36,y*36))
        self.conteneur.setStyleSheet("")
        self.conteneur.setObjectName("conteneur")
        
        self.Button_Ready = QtWidgets.QPushButton(self.groupBox_Jeu)
        self.Button_Ready.setGeometry(QtCore.QRect(50,100, 500, 300))
        self.Button_Ready.setObjectName("Button_Ready")
        self.Button_Ready.clicked.connect(self.Button_Ready.hide)


        
        self.textBrowser_Tours_restants = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.textBrowser_Tours_restants.setGeometry(QtCore.QRect(660, 30, 191, 31))
        self.textBrowser_Tours_restants.setObjectName("textBrowser_Tours_restants")
        self.lcdNumber_Tours_restant = QtWidgets.QLCDNumber(self.groupBox_Jeu)
        self.lcdNumber_Tours_restant.setGeometry(QtCore.QRect(720, 30, 61, 31))
        self.lcdNumber_Tours_restant.setObjectName("lcdNumber_Tours_restant")
        self.textBrowser_Metal = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.textBrowser_Metal.setGeometry(QtCore.QRect(660, 70, 201, 31))
        self.textBrowser_Metal.setObjectName("textBrowser_Metal")
        self.lcdNumber_Metal = QtWidgets.QLCDNumber(self.groupBox_Jeu)
        self.lcdNumber_Metal.setGeometry(QtCore.QRect(780, 70, 71, 31))
        self.lcdNumber_Metal.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber_Metal.setObjectName("lcdNumber_Metal")
        self.textBrowser_Energie = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.textBrowser_Energie.setGeometry(QtCore.QRect(660, 110, 201, 31))
        self.textBrowser_Energie.setObjectName("textBrowser_Energie")
        self.lcdNumber_Energie = QtWidgets.QLCDNumber(self.groupBox_Jeu)
        self.lcdNumber_Energie.setGeometry(QtCore.QRect(790, 110, 71, 31))
        self.lcdNumber_Energie.setObjectName("lcdNumber_Energie")
        self.Defenseur = QtWidgets.QGroupBox(self.groupBox_Jeu)
        self.Defenseur.setGeometry(QtCore.QRect(10, 560, 451, 171))
        self.Defenseur.setObjectName("Defenseur")
        self.pushButton = QtWidgets.QPushButton(self.Defenseur)
        self.pushButton.setGeometry(QtCore.QRect(0, 30, 91, 28))
        self.pushButton.setObjectName("pushButton")
        self.scrollArea = QtWidgets.QScrollArea(self.Defenseur)
        self.scrollArea.hide()
        self.scrollArea.setGeometry(QtCore.QRect(0, 100, 171, 81))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 152, 77))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.Button_Foreuse = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button_Foreuse.setGeometry(QtCore.QRect(0, 0, 121, 28))
        self.Button_Foreuse.setObjectName("Button_Foreuse")
        self.Button_Panneau_Solaire = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button_Panneau_Solaire.setGeometry(QtCore.QRect(0, 30, 121, 28))
        self.Button_Panneau_Solaire.setObjectName("Button_Panneau_Solaire")
        self.Button_J_D_B_Fermer = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.Button_J_D_B_Fermer.setGeometry(QtCore.QRect(120, 0, 31, 28))
        self.Button_J_D_B_Fermer.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Images/croix_rouge.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_J_D_B_Fermer.setIcon(icon)
        self.Button_J_D_B_Fermer.setObjectName("Button_J_D_B_Fermer")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_2 = QtWidgets.QPushButton(self.Defenseur)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 30, 91, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.Defenseur)
        self.scrollArea_2.hide()
        self.scrollArea_2.setGeometry(QtCore.QRect(220, 100, 171, 81))
        self.scrollArea_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.scrollArea_2.setAutoFillBackground(False)
        self.scrollArea_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setProperty("toolTipDuration", -1)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 152, 77))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.Button_Robot_Ouvrier = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_Robot_Ouvrier.setGeometry(QtCore.QRect(0, 30, 111, 28))
        self.Button_Robot_Ouvrier.setObjectName("Button_Robot_Ouvrier")
        self.Button_J_D_U_Fermer = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_J_D_U_Fermer.setGeometry(QtCore.QRect(120, 0, 31, 28))
        self.Button_J_D_U_Fermer.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Images/croix_rouge.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        self.Button_J_D_U_Fermer.setIcon(icon1)
        self.Button_J_D_U_Fermer.setObjectName("Button_J_D_U_Fermer")
        self.Button_Robot_Combat = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.Button_Robot_Combat.setGeometry(QtCore.QRect(0, 0, 111, 28))
        self.Button_Robot_Combat.setObjectName("Button_Robot_Combat")
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.Attaquant = QtWidgets.QGroupBox(self.groupBox_Jeu)
        self.Attaquant.setGeometry(QtCore.QRect(430, 560, 361, 131))
        self.Attaquant.setObjectName("Attaquant")
        self.Jeu_A_Unitees = QtWidgets.QPushButton(self.Attaquant)
        self.Jeu_A_Unitees.setGeometry(QtCore.QRect(0, 30, 91, 28))
        self.Jeu_A_Unitees.setObjectName("Jeu_A_Unitees")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.Attaquant)
        self.scrollArea_3.hide()
        self.scrollArea_3.setGeometry(QtCore.QRect(0, 70, 151, 51))
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 132, 47))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.Button_Scorpion = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Button_Scorpion.setGeometry(QtCore.QRect(0, 0, 91, 28))
        self.Button_Scorpion.setObjectName("Button_Scorpion")
        self.Button_J_A_Fermer = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
        self.Button_J_A_Fermer.setGeometry(QtCore.QRect(100, 0, 31, 28))
        self.Button_J_A_Fermer.setText("")
        self.Button_J_A_Fermer.setIcon(icon)
        self.Button_J_A_Fermer.setObjectName("Button_J_A_Fermer")
        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
        self.textBrowser_U_dispo = QtWidgets.QTextBrowser(self.Attaquant)
        self.textBrowser_U_dispo.setGeometry(QtCore.QRect(90, 30, 101, 31))
        self.textBrowser_U_dispo.setObjectName("textBrowser_U_dispo")
        self.lcdNumber_Unitdispo = QtWidgets.QLCDNumber(self.Attaquant)
        self.lcdNumber_Unitdispo.setGeometry(QtCore.QRect(170, 30, 81, 31))
        self.lcdNumber_Unitdispo.setObjectName("lcdNumber_Unitdispo")
        self.Bouton_Jeu_Quitter = QtWidgets.QPushButton(self.groupBox_Jeu)
        self.Bouton_Jeu_Quitter.setGeometry(QtCore.QRect(900, 720, 91, 28))
        self.Bouton_Jeu_Quitter.setObjectName("Bouton_Jeu_Quitter")
        self.Bouton_Generer = QtWidgets.QPushButton(self.groupBox_Jeu)
        self.Bouton_Generer.setGeometry(QtCore.QRect(0, 740, 121, 21))
        self.Bouton_Generer.setObjectName("Bouton_Generer")
        self.Bouton_Findetour = QtWidgets.QPushButton(self.groupBox_Jeu)
        self.Bouton_Findetour.setGeometry(QtCore.QRect(130, 740, 91, 21))
        self.Bouton_Findetour.setObjectName("Bouton_Findetour")
        
        self.Defaite = QtWidgets.QMessageBox(self.groupBox_Jeu)
        self.Defaite.setIcon(QtWidgets.QMessageBox.Information)
        self.Defaite.setText("Les attaquants gagnent")
        self.Defaite.setWindowTitle("Fin de partie")
        self.Defaite.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.Defaite.buttonClicked.connect(self.Defaite.close)
        self.Defaite.buttonClicked.connect(Minima_Accueil.close)
        self.Defaite.hide()
        
        self.Victoire = QtWidgets.QMessageBox(self.groupBox_Jeu)
        self.Victoire.setIcon(QtWidgets.QMessageBox.Information)       
        self.Victoire.setText("Le défenseur gagne")
        self.Victoire.setWindowTitle("Fin de partie")
        self.Victoire.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.Victoire.buttonClicked.connect(self.Victoire.close)
        self.Victoire.buttonClicked.connect(Minima_Accueil.close)
        self.Victoire.hide()
         
        

        self.tr_defenseur_text = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.tr_defenseur_text.append("Tour_du_Défenseur")
        self.tr_defenseur_text.setGeometry(QtCore.QRect(660, 200, 200, 30))
        self.tr_defenseur_text.hide()
        
        self.tr_attaquant_1_text = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.tr_attaquant_1_text.append("tr_attaquant_1")
        self.tr_attaquant_1_text.setGeometry(QtCore.QRect(660, 200, 200, 30))
        self.tr_attaquant_1_text.hide()
        
        self.tr_attaquant_2_text = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.tr_attaquant_2_text.append("tr_attaquant_2")
        self.tr_attaquant_2_text.setGeometry(QtCore.QRect(660, 200, 200, 30))
        self.tr_attaquant_2_text.hide()
        
        self.tr_attaquant_3_text = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.tr_attaquant_3_text.append("tr_attaquant_3")
        self.tr_attaquant_3_text.setGeometry(QtCore.QRect(660, 200, 200, 30))
        self.tr_attaquant_3_text.hide()
        
        self.tr_attaquant_4_text = QtWidgets.QTextBrowser(self.groupBox_Jeu)
        self.tr_attaquant_4_text.append("tr_attaquant_4")
        self.tr_attaquant_4_text.setGeometry(QtCore.QRect(660, 200, 200, 30))
        self.tr_attaquant_4_text.hide()
        
        
        
        
        self.groupBox_Option = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Option.hide()
        self.groupBox_Option.setEnabled(True)
        self.groupBox_Option.setGeometry(QtCore.QRect(80, 0, 851, 651))
        self.groupBox_Option.setTitle("")
        self.groupBox_Option.setObjectName("groupBox_Option")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_Option)
        self.textBrowser_2.setGeometry(QtCore.QRect(140, 10, 201, 81))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_IA_2 = QtWidgets.QTextBrowser(self.groupBox_Option)
        self.textBrowser_IA_2.setGeometry(QtCore.QRect(0, 120, 256, 41))
        self.textBrowser_IA_2.setObjectName("textBrowser_IA_2")
        self.checkBox_Option_IA_OUI = QtWidgets.QCheckBox(self.groupBox_Option)
        self.checkBox_Option_IA_OUI.setGeometry(QtCore.QRect(260, 130, 93, 25))
        self.checkBox_Option_IA_OUI.setObjectName("checkBox_Option_IA_OUI")
        self.groupBox_Accueil_nb_IA = QtWidgets.QGroupBox(self.groupBox_Option)
        self.groupBox_Accueil_nb_IA.setEnabled(True)
        self.groupBox_Accueil_nb_IA.setGeometry(QtCore.QRect(0, 160, 301, 171))
        self.groupBox_Accueil_nb_IA.setAcceptDrops(False)
        self.groupBox_Accueil_nb_IA.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.groupBox_Accueil_nb_IA.setTitle("")
        self.groupBox_Accueil_nb_IA.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_Accueil_nb_IA.setObjectName("groupBox_Accueil_nb_IA")
        self.textBrowser_IA = QtWidgets.QTextBrowser(self.groupBox_Accueil_nb_IA)
        self.textBrowser_IA.setEnabled(True)
        self.textBrowser_IA.setGeometry(QtCore.QRect(0, 30, 151, 31))
        self.textBrowser_IA.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.textBrowser_IA.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_IA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.textBrowser_IA.setObjectName("textBrowser_IA")
        self.checkBox_IA_1 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_IA)
        self.checkBox_IA_1.setGeometry(QtCore.QRect(170, 60, 311, 25))
        self.checkBox_IA_1.setObjectName("checkBox_IA_1")
        self.checkBox_IA_2 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_IA)
        self.checkBox_IA_2.setGeometry(QtCore.QRect(170, 80, 271, 25))
        self.checkBox_IA_2.setObjectName("checkBox_IA_2")
        self.checkBox_IA_3 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_IA)
        self.checkBox_IA_3.setGeometry(QtCore.QRect(170, 100, 281, 25))
        self.checkBox_IA_3.setObjectName("checkBox_IA_3")
        self.checkBox_IA_4 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_IA)
        self.checkBox_IA_4.setGeometry(QtCore.QRect(170, 120, 281, 25))
        self.checkBox_IA_4.setObjectName("checkBox_IA_4")
        self.checkBox_IA_0 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_IA)
        self.checkBox_IA_0.setGeometry(QtCore.QRect(170, 40, 281, 20))
        self.checkBox_IA_0.setObjectName("checkBox_IA_0")
        self.Button_Retour = QtWidgets.QPushButton(self.groupBox_Option)
        self.Button_Retour.setGeometry(QtCore.QRect(10, 430, 211, 91))
        self.Button_Retour.setObjectName("Button_Retour")
        self.Button_Jouer = QtWidgets.QPushButton(self.groupBox_Option)
        self.Button_Jouer.setGeometry(QtCore.QRect(620, 430, 191, 91))
        self.Button_Jouer.setObjectName("Button_Jouer")
        self.checkBox_Option_IA_NON = QtWidgets.QCheckBox(self.groupBox_Option)
        self.checkBox_Option_IA_NON.setGeometry(QtCore.QRect(310, 130, 93, 25))
        self.checkBox_Option_IA_NON.setObjectName("checkBox_Option_IA_NON")
        self.textBrowser_Humain = QtWidgets.QTextBrowser(self.groupBox_Option)
        self.textBrowser_Humain.setGeometry(QtCore.QRect(410, 120, 256, 41))
        self.textBrowser_Humain.setObjectName("textBrowser_Humain")
        self.checkBox_Option_Humain_OUI = QtWidgets.QCheckBox(self.groupBox_Option)
        self.checkBox_Option_Humain_OUI.setGeometry(QtCore.QRect(670, 130, 93, 25))
        self.checkBox_Option_Humain_OUI.setObjectName("checkBox_Option_Humain_OUI")
        self.checkBox_Option_Hum_NON = QtWidgets.QCheckBox(self.groupBox_Option)
        self.checkBox_Option_Hum_NON.setGeometry(QtCore.QRect(720, 130, 93, 25))
        self.checkBox_Option_Hum_NON.setObjectName("checkBox_Option_Hum_NON")
        self.groupBox_Accueil_nb_humain = QtWidgets.QGroupBox(self.groupBox_Option)
        self.groupBox_Accueil_nb_humain.setEnabled(True)
        self.groupBox_Accueil_nb_humain.setGeometry(QtCore.QRect(410, 160, 301, 171))
        self.groupBox_Accueil_nb_humain.setAcceptDrops(False)
        self.groupBox_Accueil_nb_humain.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.groupBox_Accueil_nb_humain.setTitle("")
        self.groupBox_Accueil_nb_humain.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox_Accueil_nb_humain.setObjectName("groupBox_Accueil_nb_humain")
        self.textBrowser_IA_3 = QtWidgets.QTextBrowser(self.groupBox_Accueil_nb_humain)
        self.textBrowser_IA_3.setEnabled(True)
        self.textBrowser_IA_3.setGeometry(QtCore.QRect(0, 30, 151, 31))
        self.textBrowser_IA_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_IA_3.setObjectName("textBrowser_IA_3")
        self.checkBox_IA_5 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_humain)
        self.checkBox_IA_5.setGeometry(QtCore.QRect(170, 60, 311, 25))
        self.checkBox_IA_5.setObjectName("checkBox_IA_5")
        self.checkBox_IA_6 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_humain)
        self.checkBox_IA_6.setGeometry(QtCore.QRect(170, 80, 271, 25))
        self.checkBox_IA_6.setObjectName("checkBox_IA_6")
        self.checkBox_IA_7 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_humain)
        self.checkBox_IA_7.setGeometry(QtCore.QRect(170, 100, 281, 25))
        self.checkBox_IA_7.setObjectName("checkBox_IA_7")
        self.checkBox_IA_8 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_humain)
        self.checkBox_IA_8.setGeometry(QtCore.QRect(170, 120, 281, 25))
        self.checkBox_IA_8.setObjectName("checkBox_IA_8")
        self.checkBox_IA_9 = QtWidgets.QCheckBox(self.groupBox_Accueil_nb_humain)
        self.checkBox_IA_9.setGeometry(QtCore.QRect(170, 40, 421, 20))
        self.checkBox_IA_9.setObjectName("checkBox_IA_9")
        self.textBrowser_2.raise_()
        self.textBrowser_IA_2.raise_()
        self.checkBox_Option_IA_OUI.raise_()
        self.groupBox_Accueil_nb_IA.raise_()
        self.Button_Retour.raise_()
        self.Button_Jouer.raise_()
        self.checkBox_Option_IA_NON.raise_()
        self.textBrowser_Humain.raise_()
        self.checkBox_Option_Humain_OUI.raise_()
        self.checkBox_Option_Hum_NON.raise_()
        self.groupBox_Accueil_nb_humain.raise_()
        self.textBrowser.raise_()
        self.tr_defenseur_text.raise_()
        self.groupBox_Accueil.raise_()
        self.groupBox_Jeu.raise_()
        self.groupBox_Option.raise_()
        self.textBrowser.raise_()
        Minima_Accueil.setCentralWidget(self.centralwidget)
#        self.menubar = QtWidgets.QMenuBar(Minima_Accueil)
#        self.menubar.setGeometry(QtCore.QRect(0, 0, 1240, 22))
#        self.menubar.setObjectName("menubar")
#        self.menuFichier = QtWidgets.QMenu(self.menubar)
#        self.menuFichier.setObjectName("menuFichier")
#        Minima_Accueil.setMenuBar(self.menubar)
#        self.statusbar = QtWidgets.QStatusBar(Minima_Accueil)
#        self.statusbar.setObjectName("statusbar")
#        Minima_Accueil.setStatusBar(self.statusbar)
#        self.actionQuitter = QtWidgets.QAction(Minima_Accueil)
#        icon2 = QtGui.QIcon()
#        icon2.addPixmap(QtGui.QPixmap("../../Images/croix_rouge.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
#        self.actionQuitter.setIcon(icon2)
#        self.actionQuitter.setObjectName("actionQuitter")
#        self.actionSauvegarder = QtWidgets.QAction(Minima_Accueil)
#        self.actionSauvegarder.setObjectName("actionSauvegarder")
#        self.menuFichier.addAction(self.actionQuitter)
#        self.menuFichier.addAction(self.actionSauvegarder)
#        self.menubar.addAction(self.menuFichier.menuAction())

        self.retranslateUi(Minima_Accueil)
        self.Button_Ac_Quitter.clicked.connect(Minima_Accueil.close)
        self.Button_Ac_Jouer.clicked.connect(self.groupBox_Accueil.hide)
        self.Button_Ac_Jouer.clicked.connect(self.groupBox_Option.show)
        self.Button_Retour.clicked.connect(self.groupBox_Option.hide)
        self.Button_Retour.clicked.connect(self.groupBox_Accueil.show)
        self.Button_Jouer.clicked.connect(self.groupBox_Jeu.show)
        self.Button_Jouer.clicked.connect(self.groupBox_Option.hide)
        self.Bouton_Jeu_Quitter.clicked.connect(Minima_Accueil.close)
        self.checkBox_IA_1.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_1.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.checkBox_IA_1.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_2.toggled['bool'].connect(self.checkBox_IA_1.setHidden)
        self.checkBox_IA_2.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.checkBox_IA_2.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_1.setHidden)
        self.groupBox_Option.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_1.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.Button_J_A_Fermer.clicked.connect(self.scrollArea_3.hide)
        self.Jeu_A_Unitees.clicked.connect(self.scrollArea_3.show)
        self.Button_J_D_U_Fermer.clicked.connect(self.scrollArea_2.hide)
        self.pushButton_2.clicked.connect(self.scrollArea_2.show)
        self.Button_J_D_B_Fermer.clicked.connect(self.scrollArea.hide)
        self.pushButton.clicked.connect(self.scrollArea.show)
        self.checkBox_Option_IA_OUI.toggled['bool'].connect(self.groupBox_Accueil_nb_IA.setVisible)
        self.checkBox_IA_1.toggled['bool'].connect(self.checkBox_IA_0.setHidden)
        self.checkBox_IA_2.toggled['bool'].connect(self.checkBox_IA_0.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_0.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_0.setHidden)
        self.checkBox_IA_0.toggled['bool'].connect(self.checkBox_IA_1.setHidden)
        self.checkBox_IA_0.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_0.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.checkBox_IA_0.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_Option_Humain_OUI.toggled['bool'].connect(self.groupBox_Accueil_nb_humain.setVisible)
        self.checkBox_IA_9.toggled['bool'].connect(self.checkBox_IA_5.setHidden)
        self.checkBox_IA_9.toggled['bool'].connect(self.checkBox_IA_6.setHidden)
        self.checkBox_IA_9.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_9.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_9.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_6.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_6.toggled['bool'].connect(self.checkBox_IA_9.setHidden)
        self.checkBox_IA_6.toggled['bool'].connect(self.checkBox_IA_5.setHidden)
        self.checkBox_IA_6.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_6.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_9.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_5.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_6.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_9.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_5.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_6.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_0.toggled['bool'].connect(self.checkBox_IA_9.setHidden)
        self.checkBox_IA_1.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_2.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_6.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_5.setHidden)
        self.checkBox_IA_2.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_3.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_8.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_7.setHidden)
        self.checkBox_IA_4.toggled['bool'].connect(self.checkBox_IA_6.setHidden)
        self.checkBox_Option_IA_NON.toggled['bool'].connect(self.checkBox_IA_0.toggle)
        self.checkBox_Option_Hum_NON.toggled['bool'].connect(self.checkBox_IA_9.toggle)
        self.checkBox_IA_9.toggled['bool'].connect(self.checkBox_IA_0.setHidden)
        self.checkBox_IA_5.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_6.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_6.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.checkBox_IA_7.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_4.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_3.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_2.setHidden)
        self.checkBox_IA_8.toggled['bool'].connect(self.checkBox_IA_1.setHidden)
        self.checkBox_Option_IA_NON.toggled['bool'].connect(self.checkBox_Option_IA_OUI.setHidden)
        self.checkBox_Option_IA_OUI.toggled['bool'].connect(self.checkBox_Option_IA_NON.setHidden)
        self.checkBox_Option_Humain_OUI.toggled['bool'].connect(self.checkBox_Option_Hum_NON.setHidden)
        self.checkBox_Option_Hum_NON.toggled['bool'].connect(self.checkBox_Option_Humain_OUI.setHidden)
        self.checkBox_Option_IA_NON.toggled['bool'].connect(self.checkBox_Option_Hum_NON.setHidden)
        self.checkBox_Option_Hum_NON.toggled['bool'].connect(self.checkBox_Option_IA_NON.setHidden)
        QtCore.QMetaObject.connectSlotsByName(Minima_Accueil)

    
    

    
    
    def nb_IA_choisi(self):
        if self.checkBox_IA_0.isChecked():
            return 0
        if self.checkBox_IA_1.isChecked():
            return 2
        if self.checkBox_IA_2.isChecked():
            return 3
        if self.checkBox_IA_3.isChecked():
            return 4
        if self.checkBox_IA_4.isChecked():
            return 5
    
    def nb_Hn_choisi(self):
        if self.checkBox_IA_9.isChecked():
            return 0
        if self.checkBox_IA_5.isChecked():
            return 2
        if self.checkBox_IA_6.isChecked():
            return 3
        if self.checkBox_IA_7.isChecked():
            return 4
        if self.checkBox_IA_8.isChecked():
            return 5
    
    
    
    
    
    
    
    
    
    
    
    
    def retranslateUi(self, Minima_Accueil):
        _translate = QtCore.QCoreApplication.translate
        Minima_Accueil.setWindowTitle(_translate("Minima_Accueil", "Minima Accueil"))
        self.textBrowser.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:72pt; text-decoration: underline; color:#cd0808;\">Minima</span></p></td></tr></table></body></html>"))
        
        
        self.Button_Ac_Jouer.setText(_translate("Minima_Accueil", "Jouer"))
        self.Button_Ac_Quitter.setText(_translate("Minima_Accueil", "Quitter"))
        self.Button_Ac_Charger.setText(_translate("Minima_Accueil", "Charger"))
        self.textBrowser_Tours_restants.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Il reste                  à survivre </span></p></td></tr></table></body></html>"))
        self.textBrowser_Metal.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Métal disponible</span></p></td></tr></table></body></html>"))
        self.textBrowser_Energie.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Energie disponible</span></p></td></tr></table></body></html>"))
        self.Defenseur.setTitle(_translate("Minima_Accueil", "Défenseur"))
        self.pushButton.setText(_translate("Minima_Accueil", "Batiments"))
        self.Button_Foreuse.setText(_translate("Minima_Accueil", "Foreuse"))
        self.Button_Panneau_Solaire.setText(_translate("Minima_Accueil", "Panneau Solaire"))
        self.pushButton_2.setText(_translate("Minima_Accueil", "Unitées"))
        self.Button_Robot_Ouvrier.setText(_translate("Minima_Accueil", "Robot Ouvrier"))
        self.Button_Robot_Combat.setText(_translate("Minima_Accueil", "Robot Combat"))
        self.Attaquant.setTitle(_translate("Minima_Accueil", "Attaquant"))
        self.Jeu_A_Unitees.setText(_translate("Minima_Accueil", "Unitées"))
        self.Button_Scorpion.setText(_translate("Minima_Accueil", "Scorpion"))
        self.textBrowser_U_dispo.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">disponibles</span></p></td></tr></table></body></html>"))
        self.Bouton_Jeu_Quitter.setText(_translate("Minima_Accueil", "Quitter"))
        self.Bouton_Generer.setText(_translate("Minima_Accueil", "Génerer"))
        self.Button_Ready.setText(_translate("Minima_Accueil", "Ready" ))
        self.Button_Ready.setStyleSheet("QPushButton {font: 100pt Times New Roman}")
        self.Bouton_Findetour.setText(_translate("Minima_Accueil", "Fin de tour"))
        self.textBrowser_2.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:36pt; text-decoration: underline;\">Options</span></p></td></tr></table></body></html>"))
        self.textBrowser_IA_2.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Jouer contre un IA ?</span></p></td></tr></table></body></html>"))
        self.checkBox_Option_IA_OUI.setText(_translate("Minima_Accueil", "OUI"))
        self.textBrowser_IA.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Choix du nombre d\'IA</span></p></td></tr></table></body></html>"))
        self.checkBox_IA_1.setText(_translate("Minima_Accueil", "1"))
        self.checkBox_IA_2.setText(_translate("Minima_Accueil", "2"))
        self.checkBox_IA_3.setText(_translate("Minima_Accueil", "3"))
        self.checkBox_IA_4.setText(_translate("Minima_Accueil", "4"))
        self.checkBox_IA_0.setText(_translate("Minima_Accueil", "0"))
        self.Button_Retour.setText(_translate("Minima_Accueil", "Retour"))
        self.Button_Jouer.setText(_translate("Minima_Accueil", "Jouer"))
        self.checkBox_Option_IA_NON.setText(_translate("Minima_Accueil", "NON"))
        self.textBrowser_Humain.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Jouer contre un humain ?</span></p></td></tr></table></body></html>"))
        self.checkBox_Option_Humain_OUI.setText(_translate("Minima_Accueil", "OUI"))
        self.checkBox_Option_Hum_NON.setText(_translate("Minima_Accueil", "NON"))
        self.textBrowser_IA_3.setHtml(_translate("Minima_Accueil", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<table border=\"0\" style=\"-qt-table-type: root; margin-top:4px; margin-bottom:4px; margin-left:4px; margin-right:4px;\">\n"
"<tr>\n"
"<td style=\"border: none;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Cantarell\'; font-size:11pt;\">Choix du nombre d\'IA</span></p></td></tr></table></body></html>"))
        self.checkBox_IA_5.setText(_translate("Minima_Accueil", "1"))
        self.checkBox_IA_6.setText(_translate("Minima_Accueil", "2"))
        self.checkBox_IA_7.setText(_translate("Minima_Accueil", "3"))
        self.checkBox_IA_8.setText(_translate("Minima_Accueil", "4"))
        self.checkBox_IA_9.setText(_translate("Minima_Accueil", "0"))
#        self.menuFichier.setTitle(_translate("Minima_Accueil", "fichier"))
#        self.actionQuitter.setText(_translate("Minima_Accueil", "Quitter"))
#        self.actionQuitter.setShortcut(_translate("Minima_Accueil", "Ctrl+Q"))
#        self.actionSauvegarder.setText(_translate("Minima_Accueil", "Sauvegarder"))
        



if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    Minima_Accueil = QtWidgets.QMainWindow()
    ui = Ui_Minima_Accueil()
    ui.setupUi(Minima_Accueil,carte)
    Minima_Accueil.show()
    sys.exit(app.exec_())

