import pygame


LARGURA = 600 #tamanho da largura da tela
ALTURA = 400  #tamanho da altura da tela


class Carro(pygame.sprite.Sprite):#Criação da classe: carro
    def __init__(self, x, y ):
        super().__init__()
        self.image = pygame.image.load('racecar.png').convert_alpha()#carro com imagem
        self.rect = self.image.get_rect()#armazena o retângulo da imagem em rect
        self.rect.x = x #posiciona a imagem nas coordenadas passadas como parâmetro
        self.rect.y = y
        self.x1 = x

    #método para movimentar o carro para direita
    def andarDir(self):
        self.rect.x += 50
        self.x1 = self.rect.x
        #print("andar")

    #método para movimentar o carro para esquerda
    def andarEsq(self):
        self.rect.x -= 50
        self.x1 = self.rect.x
        #print("andar")

    #método que identifica uma possivel colisão do carro com um bloco
    def colide(self, other_sprite):
        col = self.rect.colliderect(other_sprite)#vai verificar se houve colisão entre o carro e o objeto
        if col:
            del other_sprite
            return 1
        else:
            return 0
