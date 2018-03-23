import pygame, time # Load the required library

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('mus.mp3')
pygame.mixer.music.play()
time.sleep(40)
pygame.mixer.music.stop()