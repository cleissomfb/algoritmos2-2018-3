"""Exercicio com pygame."""
import pygame
from estrela import Estrela
import random
from nave import Nave

estrelas = []
rastros = []
num_estrelas = 300
num_rastros = 5
vel_mult = 2
nave = Nave()
rastrocontrol = Nave()
nave_espacial = pygame.image.load("./imgs/nave.png")


GREY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def criacao(param):
    """Metodo de criacao de estrela."""
    if param == 0:
        x = random.randint(0, 800)
    elif param == 1:
        x = 800
    y = random.randint(0, 600)
    vel = random.randint(1, 3)

    estrela = Estrela()
    estrela.set_coord_x(x)
    estrela.set_coord_y(y)
    estrela.set_vel(vel)

    return estrela


def instancia_estrelas():
    """Instancia uma quantidade de estrelas."""
    global num_estrelas
    qtd = 0
    while qtd < num_estrelas:
        estrelas.append(criacao(0))
        qtd += 1


def instancia_nave():
    """Instancia uma nave."""
    nave = Nave()
    nave.set_x = 100
    nave.set_y = 100


def main():
    """Metodo main do projeto."""
    global num_estrelas
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    rodando = True

    instancia_estrelas()
    instancia_nave()
    clock = pygame.time.Clock()
    while rodando:
        clock.tick(60)
        for event in pygame.event.get():
            x = 0
            y = 0
            print(event)

            if pygame.key.get_pressed()[pygame.K_UP]:
                print("K_UP = True")
                y = -5
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                print("K_DOWN = True")
                y = 5
            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                print("K_RIGHT = True")
                x = 5
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                print("K_LEFT = True")
                x = -5

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    rodando = False

        if nave.get_y() >= 0 and nave.get_y() <= 600:
            print("Entrou em draw", y)
            print(nave.get_y())
            nave.set_y(nave.get_y() + y)
            if nave.get_y() < 0:
                nave.set_y(0)
            if nave.get_y() > 600 - 50:
                nave.set_y(600 - 50)
            print(nave.get_y())

        if nave.get_x() >= 0 and nave.get_x() <= 800:
            print("Entrou em draw", x)
            print(nave.get_x())
            nave.set_x(nave.get_x() + x)
            if nave.get_x() < 0:
                nave.set_x(0)
            if nave.get_x() > 800 - 80:
                nave.set_x(800 - 80)
            print(nave.get_x())
        qtd = 0
        pygame.draw.rect(screen, BLACK, [0, 0, 800, 600],)
        screen.blit(pygame.transform.scale(nave_espacial, (80, 50)), (nave.get_x(), nave.get_y()))
        while qtd < num_estrelas:
            estrelas[qtd].set_coord_x(estrelas[qtd].get_x()-(estrelas[qtd].get_vel() * vel_mult))
            if estrelas[qtd].get_x() <= 0:
                estrelas[qtd] = criacao(1)
            pygame.draw.rect(screen, GREY, [estrelas[qtd].get_x(), estrelas[qtd].get_y(), estrelas[qtd].get_vel(), estrelas[qtd].get_vel()],)
            qtd += 1

        pygame.display.flip()


if __name__ == "__main__":
    # call the main function
    main()
