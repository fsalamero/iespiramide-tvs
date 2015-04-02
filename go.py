#! /usr/bin/env python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------
# go.py
# Proyector de información del IES Pirámide. Versión 0.4
#-------------------------------------------------------------------

import os
import sys
import time
import glob
import pygame
from pygame.locals import *


# Inicializar PyGame y crear la Surface del proyector
pygame.init()
visor = pygame.display.set_mode((960, 720), FULLSCREEN)
pygame.mouse.set_visible(False)

# Crear un reloj para controlar la animación
reloj = pygame.time.Clock()

# Cambiar al directorio actual
directorio_actual = os.path.dirname(os.path.abspath(__file__))
os.chdir(directorio_actual)
sys.path.insert(0, directorio_actual)

# Función que obtiene la imagen a partir de un archivo
def convertir_a_imagen(archivo):
    return pygame.image.load(archivo).convert()

# Función que recoge las imágenes que hay en el interior de una carpeta
def elementos(carpeta):
    # Mirar si existen ficheros
    if os.path.exists(carpeta):
        lista = [carpeta + '/../0000.jpg'] + sorted(glob.glob(carpeta + '/*.jpg'))
    else:
        lista = []
    return  lista

# El bucle de la animación
while True:
    lista = sorted(glob.glob("Attachments/*.jpg"))
    dia = time.strftime("%d%m")
    lista = lista + elementos("Dias/" + dia)
    lista = lista + elementos("Efemerides/" + dia)
    if time.strftime("%A") == 'Wednesday':
        lista = lista + sorted(glob.glob("Verde/*.jpg"))
    lista = map(convertir_a_imagen, lista)

    # Gestionar los eventos
    for evento in pygame.event.get():
        if evento.type == QUIT or \
                            evento.type == KEYDOWN and evento.key == K_ESCAPE:
            pygame.quit()
            sys.exit()

    for diapositiva in lista:
        # Gestionar los eventos
        for evento in pygame.event.get():
            if evento.type == QUIT or \
                            evento.type == KEYDOWN and evento.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        # Dibujar la diapositiva
        visor.blit(diapositiva, (0, 0))

        # Mostrar la animación
        pygame.display.update()

        #Fijar la animación a 1 fps
        reloj.tick(0.15)
        #reloj.tick(0.04)
