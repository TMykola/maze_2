from function import *

window = pygame.display.set_mode(size_window)
pygame.display.set_caption("MAZE")

clock = pygame.time.Clock()

hero = Hero(10,10,size_hero[0],size_hero[1],hero_image_list,3)

game = True
while game:
    events = pygame.event.get()
    window.fill(WHITE)

    for wall in wall_list:
        pygame.draw.rect(window, wall.color, wall)

    hero.move(window)

    for event in events:
        if event.type == pygame.QUIT:
            game = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                hero.walk["up"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                hero.walk["up"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                hero.walk["down"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                hero.walk["down"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                hero.walk["left"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                hero.walk["left"] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                hero.walk["right"] = True
       
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                hero.walk["right"] = False




    clock.tick(FPS)
    pygame.display.flip()