import pygame
import random
from DATA.SCRIPTS.profs import *
from sys import exit

class Main_game():
    def __init__(self, peruzzi_level, alberto_level, canedo_level):
        #DANDO LOAD NAS IMAGEMS---------------------- ---------------------- ---------------------- ---------------------- ----------------------
        self.font = pygame.font.Font('DATA/FONTS/fnaf_font.ttf', 30)
        self.aumento = 1.3
        self.porta = pygame.image.load('DATA/IMG/porta.png')
        self.porta_e = pygame.transform.scale(self.porta, (int(480*self.aumento), int(360*self.aumento)))
        self.porta_d = pygame.transform.flip(self.porta, True, False)
        self.porta_d = pygame.transform.scale(self.porta_d, (int((480*self.aumento)+50), int(360*self.aumento)))
        self.flecha = pygame.image.load('DATA/IMG/flip.png')
        self.flecha = pygame.transform.scale(self.flecha, (238, 50))
        self.img_alessandro_hur = pygame.image.load('DATA/IMG/alessandro_hur.png')
        self.img_alessandro_hur = pygame.transform.scale(self.img_alessandro_hur, (100, 100))
        
        #VARIAVEIS LOCAIS ---------------------- ---------------------- ---------------------- ---------------------- ----------------------
        #VARIÁVEIS CHECK ANIMATRONICS
        self.ativar_peruzinho = False
        self.ativar_alberto = False
        self.ativar_canedo = False
        
        #MP3  ---------------------- ---------------------- ---------------------- ---------------------- ----------------------
        self.music_box = pygame.mixer.Sound('DATA/MP3/music_box.mp3')
        self.jumpscare_som = pygame.mixer.Sound('DATA/MP3/bluezao.mp3')
        
        #OBJETOS
        self.office = Office()
        self.camera = Camera()
        
        #ATIVAR ANIMATRONICS
        if peruzzi_level != 0:
            self.ativar_peruzinho = True
            self.peruzzi = Peruzinho(peruzzi_level)
        if alberto_level != 0:
            self.ativar_alberto = True
            self.alberto = Alberto(alberto_level)
        if canedo_level != 0:
            self.ativar_canedo = True
            self.canedo = Canedo(canedo_level)
        
        #VARIAVEIS GERAIS
        self.AM = ['PM', 'AM']
        self.horas = [12,1,2,3,4,5]
        self.index_horas = 0
        self.index_AM = 0
        self.tempo_hora = 0
        self.bateria = 100
        self.tempo_consumo_bateria = 5000
        self.tempo_bateria = None
        self.x_camera = 0
        self.direction = 0
        self.cont = 0
        self.camera_flip = False
        self.camera_flip_check = False
        self.porta_e_status = False
        self.porta_d_status = False
        self.luz_e_status = False
        self.luz_d_status = False
        self.index = 0
        self.morte = False
        self.morte_peruzzi = False
        self.morte_alberto = False
        self.morte_canedo = False
        self.sem_energia = False
        self.game_over = False
        self.finalizar = False
        
        self.desligar_luzes = False
        self.tempo_random_sem_luz = random.randint(7000,15000)
        self.tempo_random_alessandro = random.randint(5000,10000)
        self.tempo_alessandro = None
        self.tempo_sem_luz = None
        
        self.tempo_jumpscare = None
    
    def play(self, mouse, tempo, screen, left):
        #CODIGO ---------------------- ---------------------- ---------------------- ---------------------- ----------------------
        if self.bateria <= 0:
            self.sem_energia = True
        
        if self.tempo_hora == 0:
            self.tempo_hora = tempo
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    self.porta_e_status = porta_lights_func(self.porta_e_status)
                    
                if event.key == pygame.K_d:
                    self.porta_d_status = porta_lights_func(self.porta_d_status)
                    
                if event.key == pygame.K_z:
                    self.luz_e_status = porta_lights_func(self.luz_e_status)
                    
                if event.key == pygame.K_c:
                    self.luz_d_status = porta_lights_func(self.luz_d_status)
                
                
            if event.type == pygame.KEYUP:
                self.direction = 0
                
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        if mouse[0] > 800 and self.morte == False:
            self.direction = 1
        elif mouse[0] < 200 and self.morte == False:
            self.direction = 2
        else:
            self.direction = 0
            
        if self.direction == 1 and self.x_camera > -275:
            self.x_camera -= 5
        if self.direction == 2 and self.x_camera < 0:
            self.x_camera += 5
        
        if left and self.cont == 0 and self.morte == False and self.sem_energia == False:
            if self.x_camera > -90:
                if mouse[0] > 0 and mouse[0] < 91 and mouse[1] > 244 and mouse[1] < 304:
                    self.cont = 1
                    self.porta_e_status = porta_lights_func(self.porta_e_status)
                if mouse[0] > 0 and mouse[0] < 91 and mouse[1] > 336 and mouse[1] < 400:
                    self.cont = 1
                    self.luz_e_status = porta_lights_func(self.luz_e_status)
                        
            if self.x_camera < -190 :
                if mouse[0] > 915 and mouse[0] < 1000 and mouse[1] > 244 and mouse[1] < 334:
                    self.cont = 1
                    self.porta_d_status = porta_lights_func(self.porta_d_status)
                if mouse[0] > 915 and mouse[0] < 1000 and mouse[1] > 336 and mouse[1] < 400:
                    self.cont = 1
                    self.luz_d_status = porta_lights_func(self.luz_d_status)
        if left == False:
            self.cont = 0
            
        if self.sem_energia == False:
            if self.ativar_peruzinho:
                self.morte_peruzzi = self.peruzzi.IA(tempo, self.camera_flip, self.porta_e_status)
                self.check_peruzzi = self.peruzzi.check_office()
            if self.ativar_alberto and self.morte == False:
                self.morte_alberto = self.alberto.IA(tempo, self.camera_flip)
                self.check_alberto = self.alberto.check_office(tempo, self.porta_e_status)
            if self.ativar_canedo and self.morte == False:
                self.morte_canedo = self.canedo.IA(tempo, self.camera_flip, self.porta_d_status)
                self.check_canedo = self.canedo.check_office()
            
        if self.morte_alberto or self.morte_peruzzi or self.morte_canedo:
            self.morte = True
            
        
        if ((mouse[1] > 600 and mouse[0] < 550 and mouse[0] > 394) and self.morte == False or self.camera_flip == True and self.morte == False and self.camera_flip_check == False) and self.sem_energia == False:
            self.camera_flip = True
            
            if left:
                if mouse[0] > 704 and mouse[0] < 738 and mouse[1] > 589 and mouse[1] < 608:
                    self.index = 0
                elif mouse[0] > 747 and mouse[0] < 784 and mouse[1] > 521 and mouse[1] < 540:
                    self.index = 1
                elif mouse[0] > 853 and mouse[0] < 890 and mouse[1] > 521 and mouse[1] < 540:
                    self.index = 2
                elif mouse[0] > 903 and mouse[0] < 943 and mouse[1] > 478 and mouse[1] < 498:
                    self.index = 3
                elif mouse[0] > 842 and mouse[0] < 882 and mouse[1] > 477 and mouse[1] < 497:
                    self.index = 4
                elif mouse[0] > 694 and mouse[0] < 734 and mouse[1] > 466 and mouse[1] < 486:
                    self.index = 5
                    
                    
            self.camera.ativar_camera(screen, self.index)
            if self.ativar_alberto:
                self.alberto.update(screen, self.index, self.x_camera, tempo)
            self.camera.cam2c_door(screen, self.index)
            if self.ativar_peruzinho:
                if self.check_peruzzi == False and self.ativar_peruzinho:
                    self.peruzzi.update(screen,self.index, self.x_camera)
            if self.ativar_canedo:
                if self.check_canedo == False and self.ativar_canedo:
                    self.canedo.update(screen, self.index, self.x_camera)
                    
            self.direction = 0
            if tempo >= self.tempo_camera + 400 and mouse[1] > 600 and mouse[0] < 600 and mouse[0] > 394 and self.morte == False:
                self.camera_flip = False
        else:
            self.tempo_camera = pygame.time.get_ticks()
            self.office.update(self.x_camera, self.luz_e_status, self.luz_d_status, screen, self.sem_energia, self.desligar_luzes)
            if self.sem_energia == False:
                if self.ativar_peruzinho:
                    if self.check_peruzzi == True and self.luz_e_status == True:
                        self.peruzzi.update(screen,self.index, self.x_camera)
                if self.ativar_canedo:
                    if self.check_canedo == True and self.luz_d_status == True:
                        self.canedo.update(screen,self.index, self.x_camera)
                screen.blit(self.flecha, (400, 600))
                if self.porta_e_status == True and self.camera_flip == False:
                    screen.blit(self.porta_e, (self.x_camera-150, 110))
                if self.porta_d_status == True and self.camera_flip == False:
                    screen.blit(self.porta_d, (self.x_camera+750, 130))
            

        if self.morte_peruzzi:
            if self.ativar_peruzinho:
                self.game_over = self.peruzzi.jumpscare(screen, tempo)
                
        if self.morte_alberto:
            if self.ativar_alberto:
                self.game_over = self.alberto.jumpscare(screen, tempo, self.x_camera)
                
        if self.morte_canedo:
            if self.ativar_canedo:
                self.game_over = self.canedo.jumpscare(screen, tempo)
        
        
        if self.sem_energia == True:
            self.game_over = self.no_energy(screen, self.x_camera, tempo)
            self.porta_d_status = False
            self.porta_e_status = False
            self.luz_d_status = False
            self.luz_e_status = False
        
        #HUD ---------------------- ---------------------- ---------------------- ---------------------- ----------------------
        self.TEXT, self.finalizar = self.atualizar_tempo(tempo)
        if self.TEXT != None:
            screen.blit(self.TEXT, (890, 50))
        
        if self.sem_energia == False:
            self.tempo_consumo_bateria = self.atualizar_consumo_bateria()
            self.atualizar_bateria(tempo)
            self.bateria_texto = self.font.render(str(self.bateria), True, (255, 255, 255))
            screen.blit(self.bateria_texto, (100, 600))
        
        if self.game_over == True:
            return True
        
    def atualizar_tempo(self, tempo):
        if tempo - self.tempo_hora >= 68000:
            self.index_horas += 1
            self.tempo_hora = tempo
            if self.ativar_alberto:
                self.alberto.ia_level += 1
            if self.ativar_canedo:
                self.canedo.ia_level += 1
            if self.ativar_peruzinho:
                self.peruzzi.ia_level += 1
        if self.index_horas >= 1:
            self.index_AM = 1
        if self.index_horas == 6:
            return None,True
        return self.font.render(str(self.horas[self.index_horas])+str(self.AM[self.index_AM]), True, (255, 255, 255)), False
       
    def atualizar_consumo_bateria(self):
        self.tempo_consumo_bateria_inicial = 7000
        
        if self.porta_d_status == True:
            self.tempo_consumo_bateria_inicial -= 700
            
        if self.porta_e_status == True:
            self.tempo_consumo_bateria_inicial -= 700
            
        if self.luz_d_status == True:
            self.tempo_consumo_bateria_inicial -= 700
            
        if self.luz_e_status == True:
            self.tempo_consumo_bateria_inicial -= 700
            
        if self.camera_flip == True:
            self.tempo_consumo_bateria_inicial -= 700
            
        return self.tempo_consumo_bateria_inicial
                 
    def atualizar_bateria(self, tempo):
        if self.tempo_bateria == None:
            self.tempo_bateria = tempo
            
        if tempo - self.tempo_bateria >= self.tempo_consumo_bateria:
            self.tempo_bateria = tempo
            self.bateria -= 1
            
    def no_energy(self, screen, x_camera, tempo):
        if self.tempo_sem_luz == None:
            self.tempo_sem_luz = tempo
        
        if tempo - self.tempo_sem_luz >= self.tempo_random_sem_luz:
            self.desligar_luzes = True
            self.music_box.stop()
            if self.tempo_alessandro == None:
                self.tempo_alessandro = tempo
            if tempo - self.tempo_alessandro >= self.tempo_random_alessandro:
                if self.tempo_jumpscare == None:
                    self.tempo_jumpscare = tempo
                if tempo - self.tempo_jumpscare <= 4000:
                    self.jumpscare_som.play(0)
                    screen.blit(self.img_alessandro_hur, (300,100))
                else:
                    self.jumpscare_som.stop()
                    return True
            
        else:
            self.music_box.play(0)
            screen.blit(self.img_alessandro_hur, (x_camera+123, 260))
            
        return False
        
    def create_menu_object(self):
        return True
    
    
    def vitoria_game(self):
        if self.finalizar == True:
            return True
        else:
            return False

    def __del__(self):
        print('Deletado')
        
        
class Camera():
    def __init__(self):
        self.map = pygame.image.load('DATA/IMG/cam_map_nobg.png')
        #self.cam1a = pygame.transform.scale(self.cam1a, (1000,660))
        self.lista_lugares = [pygame.image.load('DATA/IMG/cam1a.png'), pygame.image.load('DATA/IMG/cam2a.png') ,
                              pygame.image.load('DATA/IMG/cam3a.png'), pygame.image.load('DATA/IMG/cam1b.png') , 
                              pygame.image.load('DATA/IMG/cam1c.png'), pygame.image.load('DATA/IMG/cam2c.png')]
        self.porta = pygame.image.load('DATA/IMG/cam2c_door.png')
        self.porta = pygame.transform.scale(self.porta, (1000,660))
        self.lista_lugares_trans = []
        for i in self.lista_lugares:
            i = pygame.transform.scale(i, (1000,660))
            self.lista_lugares_trans.append(i)
        
        
    def ativar_camera(self, screen, index):
        screen.blit(self.lista_lugares_trans[index], (0,0))
        screen.blit(self.map, (600,400))
        
    def cam2c_door(self, screen, index):
        if index == 5:
            screen.blit(self.porta, (0,0))
    
def porta_lights_func(status):
    if status == False:
        status = True
        return status

    if status == True:
        status = False
        return status

class Office():
    def __init__(self):
        self.lista_background = [pygame.image.load('DATA/IMG/bg.png'), pygame.image.load('DATA/IMG/bg_lights_e.png'),
                                 pygame.image.load('DATA/IMG/bg_lights_d.png'), pygame.image.load('DATA/IMG/bg_lights_e_d.png')]
        self.img_sem_energia = pygame.image.load('DATA/IMG/bg_sem_energia.png')
        self.img_desligar = pygame.image.load('DATA/IMG/preto.png')
        self.img_desligar = pygame.transform.scale(self.img_desligar, (2000,2000))
    
    def check(self, luz_e_status, luz_d_status):
        if luz_e_status and luz_d_status:
            return self.lista_background[3]
        
        if luz_e_status and luz_d_status == False:
            return self.lista_background[1]
        
        if luz_d_status:
            return self.lista_background[2]
        
        return self.lista_background[0]
    
    def update(self, x_camera, luz_e_status, luz_d_status, screen, bateria_situacao, desligar):
        if bateria_situacao == False:
            self.img = self.check(luz_e_status, luz_d_status)
            screen.blit(self.img, (x_camera, 0))
        elif desligar == False:
            screen.blit(self.img_sem_energia, (x_camera, 0))
        else:
            screen.blit(self.img_desligar, (x_camera, 0))