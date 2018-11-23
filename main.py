import pygame
from objeto import Carro
from random import randrange

#Definindo cores
PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
AMARELO = (255,255,0)
AZUL = (0,0,255)

ImagemFundo = pygame.image.load('fundo.png')

#criação da tela
pygame.init()

LARGURA = 800
ALTURA = 600
pontos = 0
fonte = pygame.font.SysFont("comicsansms", 30)
fonteFim= pygame.font.SysFont("comicsansms", 70)
tela = pygame.display.set_mode([LARGURA, ALTURA])
pygame.display.set_caption("Bit Race")#Nome do projeto
mouse = pygame.mouse# encurta o nome
mouse.set_visible(False)# esconde o ponteiro
clock = pygame.time.Clock()


todosObjetos = pygame.sprite.Group()
carro = Carro(400, 420)
todosObjetos.add(carro)


def bloco(blocox, blocoy, blocow, blocoh, color):#
    return pygame.draw.rect(tela, color, [blocox, blocoy, blocow, blocoh])

bloco_iniciox = randrange(0, LARGURA)
bloco_inicioy = ALTURA #a partir de qual altura vai cair
bloco_vel = 7 #velocidade
bloco_larg = 60 #tamanho do objeto
bloco_larg2 = 60 #tamanho do objeto
bloco_alt = 60#tamanho do objeto

morreu = False
sair = False

todosObjetos.draw(tela)
while not sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    while not morreu:
        filaEventos = pygame.event.get()

        azul = bloco(bloco_iniciox, bloco_inicioy, bloco_larg, bloco_alt, AZUL)

        # percorre a fila de eventos
        for event in filaEventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    carro.andarEsq()
                if event.key == pygame.K_RIGHT:
                    carro.andarDir()

        if carro.colide(azul):
            carro.kill()
            todosObjetos.remove(carro)
            morreu = True

        tela.blit(ImagemFundo, (0,0))
        azul = bloco(bloco_iniciox, bloco_inicioy, bloco_larg, bloco_alt, AZUL)

        bloco_inicioy += bloco_vel

        if bloco_inicioy > ALTURA:
            bloco_inicioy = 0 - bloco_alt
            bloco_iniciox = randrange(0, LARGURA)

        if bloco_inicioy == 500:
            pontos += 1

        todosObjetos.draw(tela)
        tela.blit(fonte.render("Pontos: " + str(pontos), True, (AZUL)), (0, 0))
        pygame.display.update()
        clock.tick(60)


    tela.fill(BRANCO)
    tela.blit(fonteFim.render("Perdeu", True, (PRETO)), (290, 200))
    tela.blit(fonteFim.render("Pontos: " + str(pontos), True, (PRETO)), (255, 300))
    pygame.display.update()