#------------------------------#
#          Ennemis.py          #
#		Clement Blaudeau	   #
#			******			   #
#------------------------------#

# -*- coding: utf-8 -*-


import pygame
from pygame.locals import *
from obstacles import * 
from animations import *


class Ennemis:
	
	def __init__(self):
		#variables en tous genres
		self.positions = []
		self.sortes = []
		self.vies = []
		self.tirs = []
		self.positions_tirs = []
		self.bille = pygame.image.load("images/bille.png").convert_alpha()
		self.ennemis1 = pygame.image.load("images/ennemis1.png").convert_alpha()
		self.j = 0
		self.temps = pygame.time.get_ticks()
		self.eclats = Eclat()
		self.fini = 0
		
		
		
	def NouvelEnnemi(self, sorte, x, y):
		#Ajout d'un ennemi. A faire avec les niveaux
		self.positions.append(pygame.Rect(x,y,30,30))
		self.sortes.append(sorte)
		self.vies.append(sorte * 3)
		
	def CollisionCube(self, hitbox):
		#Collision avec le cube.
		#return True or False
		i = 0
		for element in self.positions:
			if element.colliderect(hitbox):
				self.eclats.Explosion(self.positions[i],self.sortes[i] * 3)
				print self.sortes[i]
				self.vies.remove(self.vies[i])
				self.sortes.remove(self.sortes[i])
				self.positions.remove(self.positions[i])
				return True
			i+=1
		i = 0
		for element in self.positions_tirs:
			if element.colliderect(hitbox):
				self.positions_tirs.remove(element)
				self.tirs.remove(self.tirs[i])
				return True
			i+=1
		return False
		
	def CollisionsTirs(self, tirs, degats):
		#Test la colision avec les tirs
		i = 0
		for element in tirs:
			if element.top >= 0:
				for element2 in self.positions:
					if element2.colliderect(element):
						tirs.remove(element)
						self.vies[i] =- degats
						if self.vies[i] <= 0:
							self.eclats.Explosion(self.positions[i],self.sortes[i] * 3)
							print self.sortes[i]
							self.vies.remove(self.vies[i])
							self.sortes.remove(self.sortes[i])
							self.positions.remove(element2)
					i +=1
				i = 0
		
		return tirs
		
	def Deplacements(self):
		#depaclement des ennemis en fonction de leurs paterns.
		i = 0
		for element in self.sortes:
			if element == 1:
				self.positions[i] = self.positions[i].move(0,1)
			#elif element == 2:
			#elif element == 3:
			#elif element == 4:
			#elif element == 5:
			#elif element == 6:
			#elif element == 7:
			#elif element == 8:
			#elif element == 9:
			#elif element == 10:
			if self.positions[i].top > 490:
				self.vies.remove(self.vies[i])
				self.sortes.remove(self.sortes[i])
				self.positions.remove(self.positions[i])
				print "mort !"
			i+=1
			
			
	def Tir(self):
		#Tirs
		#Patern en fonction du type.
		if (pygame.time.get_ticks() - self.temps) > 500:
			self.temps = pygame.time.get_ticks()
			i = 0
			for element in self.sortes:
				if self.positions[i].bottom >= 0:
					if element == 1:
						print "			tir !"
						self.positions_tirs.append(pygame.Rect(self.positions[i].left - 5,self.positions[i].top,10,10))
						self.positions_tirs.append(pygame.Rect(self.positions[i].right + 5,self.positions[i].top,10,10))
						self.tirs.append(1)
						self.tirs.append(2)
				i += 1
				
	def Cleaner(self):
		i = 0
		for element in self.tirs:
			if self.positions_tirs[i].right < 0:
				self.positions_tirs.remove(self.positions_tirs[i])
				self.tirs.remove(self.tirs[i])
				print "Clean !"
				return 0
			elif self.positions_tirs[i].left > 640:
				self.positions_tirs.remove(self.positions_tirs[i])
				self.tirs.remove(self.tirs[i])
				print "Clean !"
				return 0
			i+=1
			
				
	def Affichage(self, fenetre):
		#Scrool, 
		#Affichage
		self.Cleaner()
		i = 0
		self.j += 1
		if self.j >= 10:
			self.j = 0
			for element in self.positions:
				self.positions[i] = element.move(0,1)
				i += 1
		i = 0
		for element in self.positions_tirs:
			if self.tirs[i] == 1:
				self.positions_tirs[i] = element.move(-1,0)
			if self.tirs[i] == 2:
				self.positions_tirs[i] = element.move(1,0)
			if self.tirs[i] == 3:
				self.positions_tirs[i] = element.move(0,2)
			if self.tirs[i] == 4:
				self.positions_tirs[i] = element.move(0,-1)
			if self.tirs[i] == 5:
				self.positions_tirs[i] = element.move(1,2)
			if self.tirs[i] == 6:
				self.positions_tirs[i] = element.move(-1,2)
			if self.tirs[i] == 7:
				self.positions_tirs[i] = element.move(1,-1)
			if self.tirs[i] == 8:
				self.positions_tirs[i] = element.move(-1,-1)
			i+= 1
		
		i = 0
		
		
		for element in self.positions:
			fenetre.blit(self.ennemis1, element)
			
		for element in self.positions_tirs:
			if not (element.right > 690) and not (element.left < -10) and not (element.top < -5) and not (element.bottom > 490):
				fenetre.blit(self.bille, element)
		
		self.eclats.Affichage(fenetre)

