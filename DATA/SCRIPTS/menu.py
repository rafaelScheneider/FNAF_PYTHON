import pygame
from sys import exit
from DATA.SCRIPTS.main_game import Main_game

class Menu():
    def __init__(self, save):
        self.menu = pygame.image.load('DATA/IMG/menu.png')
        self.menu = pygame.transform.scale(self.menu, (1000 , 660))
        self.font = pygame.font.Font('DATA/FONTS/fnaf_font.ttf', 40)
        self.five = self.font.render('FIVE', True, (255, 255, 255))
        self.nights = self.font.render('NIGHTS', True, (255, 255, 255))
        self.at = self.font.render('AT', True, (255, 255, 255))
        self.faxilink = self.font.render("FAXILINK's", True, (255, 255, 255))
        self.new_game_text = self.font.render("New game", True, (255, 255, 255))
        
        
        self.static1 = pygame.image.load('DATA/IMG/static_1.png')
        self.static1 = pygame.transform.scale(self.static1, (1000 , 660))
        self.static2 = pygame.image.load('DATA/IMG/static_2.png')
        self.static2 = pygame.transform.scale(self.static2, (1000 , 660))
        self.static3 = pygame.image.load('DATA/IMG/static_3.png')
        self.static3 = pygame.transform.scale(self.static3, (1000 , 660))
        self.staticList = [self.static1, self.static2, self.static3]
        self.static_cont = 0
        self.start = False
        
        self.save = save
        self.level_IA_peruzzi = 0
        self.level_IA_alberto = 0
        if self.save == 1:
            self.level_IA_peruzzi = 1
            self.level_IA_alberto = 0
            self.level_IA_canedo = -1
        if self.save == 2:
            self.level_IA_peruzzi = 5
            self.level_IA_alberto = 1
            self.level_IA_canedo = 3
        self.x_letreiro = 100
        self.y_letreiro = 80
        
    def update(self, screen, mouse, left):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if left and mouse[0] > 100 and mouse[0] < 300 and mouse[1] > 444 and mouse[1] < 470:
            self.start = True
        
        screen.blit(self.menu, (0,0))
        screen.blit(self.five, (self.x_letreiro , self.y_letreiro + 50))
        screen.blit(self.nights, (self.x_letreiro , self.y_letreiro + 100))
        screen.blit(self.at, (self.x_letreiro , self.y_letreiro + 150))
        screen.blit(self.faxilink, (self.x_letreiro , self.y_letreiro + 200))
        screen.blit(self.new_game_text, (self.x_letreiro , self.y_letreiro + 360))
        
        screen.blit(self.staticList[self.static_cont], (0,0))
        if self.static_cont == 2:
            self.static_cont = 0
        else:
            self.static_cont += 1
        
    def new_game(self):
        return self.start

    def create_game_object(self):
        return Main_game(self.level_IA_peruzzi, self.level_IA_alberto, self.level_IA_canedo)
    
    def __del__(self):
        print('Deletado')