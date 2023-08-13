import pygame
import random
from PIL import Image

class Peruzinho():
    def __init__(self, level):
        if level == -1:
            self.ia_level = 0
        else:
            self.ia_level = level
        self.caminho_lista = {0: 'cam1a',1: 'cam2a',2: 'cam3a',3: 'cam1b',4: 'cam1c'}
        self.lista_sprites = [pygame.image.load('DATA/IMG/peruzzi_base.png'), pygame.image.load('DATA/IMG/peruzzi_base.png'), 
                              pygame.image.load('DATA/IMG/peruzzi_base.png'), pygame.image.load('DATA/IMG/peruzzi_base.png'),
                              pygame.image.load('DATA/IMG/peruzzi_base.png'), pygame.image.load('DATA/IMG/peruzzi_porta.png')]
        
        self.jumpscare_img = pygame.image.load('DATA/IMG/peruzzi_base.png')
        self.jumpscare_img = pygame.transform.scale(self.jumpscare_img, (500,500))
        self.lista_posicoes = [(50,50), (50,50), (50,50), (50,50), (50,50)]
        self.posicao = 0
        self.ultimo_tempo = 0
        self.jumpscare_check = False
        self.tempo = None
        self.jumpscare_som = pygame.mixer.Sound('DATA/MP3/bluezao.mp3')
        
    def check_office(self):
        if self.posicao >= 5:
            return True
        return False
    
    def update(self, screen, index, x_camera):
        if index in self.caminho_lista and self.posicao == index:
            screen.blit(self.lista_sprites[index], self.lista_posicoes[index])
        if self.posicao == 5 and self.jumpscare_check == False:
            self.y_imagem = 260
            screen.blit(self.lista_sprites[5], (x_camera+323, self.y_imagem))
    
    def IA(self, tempo, camera, porta):
        self.random = random.randrange(0,20)
        if self.ultimo_tempo == 0:
            self.ultimo_tempo = tempo
            
        if tempo - self.ultimo_tempo >= 5000 and self.jumpscare_check == False:
            self.ultimo_tempo = tempo
            if self.random <= self.ia_level:
                if porta == True:
                    if random.randrange(0,20) < 10:
                        self.posicao = 2
                    else:
                        self.posicao = 3
                elif camera == True and self.posicao == 5:
                    self.jumpscare_check = True
                if self.posicao <= 4:
                    self.posicao += 1
        
        elif self.jumpscare_check == True:
            return True

        return False
    
    def jumpscare(self, screen, tempo):
        if self.tempo == None:
            self.tempo = tempo
        if tempo - self.tempo <= 4000:
            self.jumpscare_som.play(0)
            screen.blit(self.jumpscare_img, (300,100))
        else:
            self.jumpscare_som.stop()
            return True
        
        
class Canedo():
    def __init__(self, level):
        self.ia_level = level
        self.caminho_lista = {0: 'cam1a',1: 'cam2a',2: 'cam3a',3: 'cam1b',4: 'cam1c'}
        self.lista_sprites = [pygame.image.load('DATA/IMG/canedo.png'), pygame.image.load('DATA/IMG/canedo.png'), 
                              pygame.image.load('DATA/IMG/canedo.png'), pygame.image.load('DATA/IMG/canedo.png'),
                              pygame.image.load('DATA/IMG/canedo.png'), pygame.image.load('DATA/IMG/canedo_porta.png')]
        
        self.jumpscare_img = pygame.image.load('DATA/IMG/canedo_porta.png')
        self.jumpscare_img = pygame.transform.scale(self.jumpscare_img, (500,500))
        self.lista_posicoes = [(150,150), (150,150), (150,150), (150,150), (150,150)]
        self.posicao = 0
        self.ultimo_tempo = 0
        self.jumpscare_check = False
        self.tempo = None
        self.jumpscare_som = pygame.mixer.Sound('DATA/MP3/bluezao.mp3')
        
    def check_office(self):
        if self.posicao >= 5:
            return True
        return False
    
    def update(self, screen, index, x_camera):
        if index in self.caminho_lista and self.posicao == index:
            screen.blit(self.lista_sprites[index], self.lista_posicoes[index])
        if self.posicao == 5 and self.jumpscare_check == False:
            self.y_imagem = 280
            screen.blit(self.lista_sprites[5], (x_camera+873, self.y_imagem))
    
    def IA(self, tempo, camera, porta):
        self.random = random.randrange(0,20)
        if self.ultimo_tempo == 0:
            self.ultimo_tempo = tempo
            
        if tempo - self.ultimo_tempo >= 5000 and self.jumpscare_check == False:
            self.ultimo_tempo = tempo
            if self.random <= self.ia_level:
                if porta == True:
                    if random.randrange(0,20) < 10:
                        self.posicao = 2
                    else:
                        self.posicao = 3
                elif camera == True and self.posicao == 5:
                    self.jumpscare_check = True
                if self.posicao <= 4:
                    self.posicao += 1
        
        elif self.jumpscare_check == True:
            return True

        return False
    
    def jumpscare(self, screen, tempo):
        if self.tempo == None:
            self.tempo = tempo
        if tempo - self.tempo <= 4000:
            self.jumpscare_som.play(0)
            screen.blit(self.jumpscare_img, (300,100))
        else:
            self.jumpscare_som.stop()
            return True
        
        
class Alberto():
    def __init__(self, level):
        self.ia_level = level
            
        self.caminho_lista = {4: 'cam1c', 5: 'cam2c'}
        self.scale_img_alberto = pygame.image.load('DATA/IMG/alberto.png')
        self.scale_img_alberto = pygame.transform.scale(self.scale_img_alberto, (self.scale_img_alberto.get_width()*2,self.scale_img_alberto.get_height()*2))
        self.lista_sprites = [pygame.image.load('DATA/IMG/alberto.png'),self.scale_img_alberto
                            ,self.scale_img_alberto,self.scale_img_alberto]
        
        self.jumpscare_img = pygame.image.load('DATA/IMG/alberto.png')
        self.jumpscare_img = pygame.transform.scale(self.jumpscare_img, (300,300))
        self.lista_posicoes = [(33,447), (63,347), (73,347), (120,347)]
        self.estagios = 0
        self.ultimo_tempo = 0
        self.jumpscare_check = False
        self.tempo = None
        
        self.gif_img = Image.open('DATA/GIFS/alberto_correndo.gif')
        self.y_form = 200
        self.x_form = 510
        self.correndo_camera_ligada = False
        self.ataque = False
        self.camera_update_check = None
        self.tempo_ataque = None
        
        self.current_frame = 0
        self.tempo_frame = 0
        
        self.tempo = None
        self.tempo_jumpscare = None
        
        self.jumpscare_check = False
                    
    def update(self, screen, index, x_camera, tempo):
        if index in self.caminho_lista and index == 5 and self.estagios < 4:
            screen.blit(self.lista_sprites[self.estagios], self.lista_posicoes[self.estagios])
        elif index in self.caminho_lista and index == 4 and self.estagios == 4 and self.ataque != True and self.camera_update_check == True:
            self.running(tempo, screen)
            self.correndo_camera_ligada = True
        elif self.correndo_camera_ligada == True:
            self.ataque = True
            
            
    def check_office(self, tempo, porta):
        if self.estagios == 4 and self.ataque != True:
            if self.tempo_ataque == None:
                self.tempo_ataque = tempo
            if tempo - self.tempo_ataque >= 7000: 
                self.ataque = True
        if self.ataque == True:
            if porta == True:
                self.tempo_ataque = None
                self.ultimo_tempo = tempo
                self.ataque = False
                self.estagios = 0
                self.camera_update_check = None
                self.tempo_frame = 0
                self.tempo_jumpscare = None
                self.y_form = 200
                self.x_form = 510
                self.correndo_camera_ligada = False
                self.tempo = None
                
            if self.tempo == None:
                self.tempo = tempo
            if tempo - self.tempo >= 4000:
                self.jumpscare_check = True
                return True
            
        return False
        
            
    def IA(self, tempo, camera_flip):
        self.camera_update_check = camera_flip
        if self.ultimo_tempo == 0:
            self.ultimo_tempo = tempo
            
        if tempo - self.ultimo_tempo >= 5000 and self.jumpscare_check == False:
            self.random = random.randrange(0,20)
            self.ultimo_tempo = tempo
            if self.random <= self.ia_level and camera_flip == False:
                if self.estagios <= 3:
                    self.estagios += 1
                    
        if self.jumpscare_check == True:
            return True
        return False
    
    def running(self, tempo, screen):
        self.frame = self.pil_to_game(self.get_gif_frame(self.gif_img, self.current_frame))
        if self.tempo_frame + 160 < tempo:
            self.current_frame = (self.current_frame + 1) % self.gif_img.n_frames
            self.tempo_frame = tempo
        self.frame = pygame.transform.scale(self.frame, (135,135))
        # formula y = x + (y/1.2)
        self.y_form += 1
        self.x_form -= 0.1
        screen.blit(self.frame, (self.x_form , self.y_form))
        
    def jumpscare(self, screen, tempo, camera_x):
        if self.tempo_jumpscare == None:
            self.tempo_jumpscare = tempo
        if tempo - self.tempo_jumpscare <= 4000:
            screen.blit(self.jumpscare_img, (camera_x + 123 , 170))
        else:
            return True
    
    def pil_to_game(self, img):
        data = img.tobytes("raw", 'RGBA')
        return pygame.image.fromstring(data, img.size, 'RGBA')

    def get_gif_frame(self, img, frame):
        img.seek(frame)
        return  img.convert('RGBA')