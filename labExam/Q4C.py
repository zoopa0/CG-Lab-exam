
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Lab Exam Canvas")
    screen.fill((255, 255, 255))  
    ###triangle is here

    pygame.draw.polygon(screen, (0,0,255),(250,0),(125,250),(325,250))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F1:
                    running = False

        pygame.display.flip()

    pygame.quit()

