# -*- coding: utf-8 -*-
'''
Copyright (c) 2012 Clément Blaudeau
This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
'''
#------------------------------
#	text.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier utilisé pour les 
#	Displays de certains textes
#------------------------------


import general
import pygame
from pygame.locals import *

class Textes:
	def __init__(self):
		self.chrono = Chrono()
		self.score = Score()
		self.life = Life()
		self.nivtirs = NivTirs()
	
	def Display(self, time, window, sorte):
		self.chrono.Display(time, window, sorte)
		self.life.Display(window)
		self.chrono.Display(window)
		self.nivtirs.Display(window)

class Chrono:
	
	def __init__(self):
		self.temps_trop = pygame.time.get_ticks()
		self.chrono_ml = 0
		self.chrono_s = 0
		self.chrono_m = 0
		self.temps = str(self.chrono_m) + ":" + str(self.chrono_s) + ":" + str(self.chrono_ml)
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render(self.temps, 1, (255, 180, 10))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+65, 20)

	def Display(self, time, window, sorte):
		self.chrono_ml = time
		self.chrono_s = self.chrono_ml / 1000
		self.chrono_m = self.chrono_s / 60
		self.chrono_s %= 60
		self.chrono_ml %= 1000
		if self.chrono_s < 10:
			self.chrono_s = "0" + str(self.chrono_s)
		self.temps = str(self.chrono_m) + ":" + str(self.chrono_s) + ":" + str(self.chrono_ml)
		self.text = self.font.render(self.temps, 1, (255,180,10))
		if sorte == "boss":
			self.text = self.font.render(self.temps, 1, (255,10,10))
		window.blit(self.text, self.position)
		

class Score:
	
	
	def __init__(self):
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("0", 1, (255, 255, 255))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+65, 55)
		self.score = 0
		self.r = 0
		self.b = 0
		self.v = 0
		
	def CalculScore(self, lifes):
		return (self.score + (lifes * 100) - (general.tirs*2))

	def Display(self, window):
		
		self.r = self.score/2
		if self.r > 255:
			self.r = 255
			self.b = self.score/4
			if self.b > 255:
				self.b = 255
				self.v = self.score/8
				if self.v > 255:
					self.v = 255
		self.text = self.font.render(str(self.score), 1, (self.r, self.v, self.b))
		window.blit(self.text, self.position)




class Life:
	
	def __init__(self):
		self.font = pygame.font.Font(None, 36)
		self.text = self.font.render("0", 1, (255, 255, 255))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+65, 85)
		self.life = 5
		self.lifes_used = 0
		self.r = 0
		self.b = 0
		self.v = 0

	def Display(self, window):
		
		if self.life == 5:
			self.v = 255
		if self.life == 4:
			self.v = 250
			self.r = 250
		if self.life == 3:
			self.v = 200
			self.r = 255
		if self.life == 2:
			self.r = 255
			self.v = 155
		if self.life == 1:
			self.r = 255
			self.v = 50
		if self.life == 0:
			self.r = 255
			self.v = 0
		self.text = self.font.render(str(self.life), 1, (self.r, self.v, self.b))
		window.blit(self.text, self.position)


class NivTirs:
	
	def __init__(self):
		self.font = pygame.font.Font("../polices/Bank.ttf", 20)
		self.text = self.font.render("", 1, (0,0,0))
		self.position = self.text.get_rect()
		self.position = self.position.move(general.w+70, 200)

	def Display(self, window):
		chaine = ""
		i = 0
		if (general.ennemis/15 == 1):
			general.niv = 1
			i = 15
		if (general.ennemis/15 == 2):
			general.niv = 2
			i = 30
		while i < general.ennemis:
			chaine += "|"
			i += 1
		if i >= 30:
			chaine = "***"
		
		self.text = self.font.render(chaine, 1, (0, 0, 0))
		window.blit(self.text, self.position)
		self.text = self.font.render(str("Tirs : "+str(general.tirs)), 1, (0, 0, 0))
		window.blit(self.text, self.position.move(0,50))

		self.text = self.font.render(str("Bombes : "+str(general.n_bomb + 1)), 1, (0, 0, 0))
		window.blit(self.text, self.position.move(0,80))



class ModeLent:
	
	def __init__(self):
		self.font = pygame.font.Font("../polices/Bank.ttf", 20)
		self.text = self.font.render("Mode Lent", 1, (1,1,0))
		
		
	def Display(self,window):
		window.blit(self.text, (general.w+50,general.h-100))
		
	
	
	
	
	
	

