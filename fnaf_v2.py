import pygame
from DATA.SCRIPTS.main_game import *
from DATA.SCRIPTS.menu import *
from sys import exit

clock = pygame.time.Clock()
pygame.init()
screen = pygame.display.set_mode((1000,660))
pygame.display.set_caption("Five Night's At Faxilink")
f = open('DATA/SAVE/save.txt', 'w')
f.close()
f = open('DATA/SAVE/save.txt', 'r')
contents = f.read()
if contents == '':
    f = open('DATA/SAVE/save.txt', 'w')
    f.write('NIGHTS:1')
    f.close()
    f = open('DATA/SAVE/save.txt', 'r')
    contents = f.read()
    f.close()
save_file = int(contents[-1])
    

def cutscene_1(tempo_cooldown, tempo, cutscene_timer):
    tela_noitada = pygame.image.load('DATA/IMG/cutscene.png')
    if cutscene_timer - (tempo - tempo_cooldown) <= 0:
        tempo_cooldown = None
        return  True
    else:
        screen.blit(tela_noitada, (0,0))
        return False
    
def game_over(mouse, left):
    tela_morte = pygame.image.load('DATA/IMG/game_over.png')
    screen.blit(tela_morte, (0,0))
    if left:
        if mouse[0] >= 362 and mouse[0] <= 660 and mouse[1] >= 419 and 469:
            return Menu(save_file), False
    return None, True

def vitoria():
    f = open('DATA/SAVE/save.txt', 'w')
    new_save = str(save_file + 1)
    f.write('NIGHTS:' + new_save)
    f.close()
    f = open('DATA/SAVE/save.txt', 'r')
    contents = f.read()
    f.close()
    return Menu(int(contents[-1])), False
    
    
start = False
tempo_cooldown = None
cutscene_over = False
destruir_menu = False
reiniciar = False
vitoria_check = False
menu = Menu(save_file)

while True:
    left, middle, right = pygame.mouse.get_pressed()
    mouse = pygame.mouse.get_pos()
    tempo = pygame.time.get_ticks()
    
    if start == True:
        if cutscene_over == False:
            if tempo_cooldown == None:
                tempo_cooldown = tempo
            cutscene_over = cutscene_1(tempo_cooldown, tempo, cutscene_timer=3000)
        else:
            if destruir_menu == False:
                game = menu.create_game_object()
                del menu
                destruir_menu = True
            reiniciar = game.play(mouse, tempo, screen, left)
            vitoria_check = game.vitoria_game()
            
    
    elif start == False and reiniciar == False:
        start = menu.new_game()
        menu.update(screen, mouse, left)
        
    if vitoria_check == True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        start = False
        cutscene_over = False
        tempo_cooldown = None
        destruir_menu = False
        reiniciar = False
        del game
        menu, vitoria_check = vitoria()
        
        
    if reiniciar == True:
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        start = False
        cutscene_over = False
        tempo_cooldown = None
        destruir_menu = False
        menu, reiniciar = game_over(mouse, left)
    
    pygame.display.flip()
    clock.tick(120)