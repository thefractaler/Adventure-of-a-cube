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
# 	credit.py
#	Clement Blaudeau       
#	******	       
#------------------------------
#	Fichier simple pour l'Display 
#	des crédits
#------------------------------


import pygame
from pygame.locals import *
import general

class Credits:
	def __init__(self):
		self.e = 2
		
	def Display(self, window):
		image = pygame.image.load("../images/credits.png").convert_alpha()
		_continue = 1
		while _continue:
			pygame.display.flip()
			window.blit(image, (0,0))
			for event in pygame.event.get():
				if event.type == QUIT:
					_continue = 0
				if event.type == KEYDOWN:
					_continue = 0
