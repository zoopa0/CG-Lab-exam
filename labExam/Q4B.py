 
import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 400))
    pygame.display.set_caption("Lab Exam Canvas")
    screen.fill((255, 255, 255))  
    ########### here is the line
    pygame.draw.line(screen, (255, 0, 0), (50, 50), (200, 50), 3)
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

if __name__ == "__main__":
    main()