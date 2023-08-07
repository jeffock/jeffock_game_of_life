import time
import pygame
import numpy as np

COLOR_BG = (10,10,10)
COLOR_GRID = (40,40,40)
COLOR_APHASE = (170,170,170)
COLOR_MPHASE = (200,200,200)
COLOR_IPHASE = (255,255,255)

def update(screen, cells, size, traits, progress=False):
    # 0 is dead 1 is alive
    updated_cells = np.zeros((cells.shape[0], cells.shape[1]))
    updated_traits = traits.copy()

    for row, col in np.ndindex(cells.shape):
        # num alive touching: 
        alive = np.sum(cells[row-1:row+2, col-1:col+2]) - cells[row, col]
        color = COLOR_BG if cells[row, col] == 0 else COLOR_IPHASE
        
        # etc. rest of logic
        if cells[row, col] == 1:
            trait = traits[row, col]

            feed = feed_check(trait)
            move = move_check(trait)

            if feed == 0:
                # decide who feeds
            elif feed == 1:
                # do nothing
            else:
                # cooperate
            
            # make sure to edit the traits as well when moving
            # original tile can remain the same but new tile must update
            # cannot move onto occupied tile
            if move == 0:
                # +x
            elif move == 1:
                # -x
            elif move == 2:
                # +y
            elif move == 3:
                # -y
            else:
                # don't move

            # mutate
            for i, v in enumerate(trait):
                random_num = np.random.randint(1, 101)
                plusminus = np.random.randint(1, 3)
                
                if i == 0 and plusminus == 1:
                    trait[i] = v + (v*0.1)
                    trait[1] = trait[1] - (v*0.1)
                elif i == 0 and plusminus == 2:
                    trait[i] = v - (v*0.1)
                    trait[1[ = trait[1] + (v*0.1)

                if i == 2 and plusminus == 1:
                    trait[i] = v + (v*0.1)
                elif i == 2 and plusminus == 2:
                    trait[i] = v - (v*0.1)

                if i == 3 and plusminus == 1:
                    trait[i] = v + 1
                elif i == 3 and plusminus == 2:
                    trait[i] = v - 1
                
                if i == 4 and plusminus == 1:
                    trait[i] = v + 1
                elif i == 4 and plusminus == 2:
                    trait[i] = v - 1

                if i == 5 and plusminus == 1:
                    trait[i] = v + 1
                elif i == 5 and plusminus == 2:
                    trait[i] = v - 1
            
            updated_traits[row, col] = trait

        pygame.draw.rect(screen, color, (col*size, row*size, size-1, size-1))

    return updated_cells, updated_traits

def feed_check(trait):
    # 0 = compete, 1 = ignore, 2 = coop
    output = 1

    return output

def move_check(trait):
    # 0 = +x, 1 = -x, 2 = +y, 3 = -y, 4 = no movement
    output = 4

    return output

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))

    cells = np.zeros((60, 80))

    # coop, feed, ignore, ignoret, movef, moves, phasec
    trait_defaults = np.array([0.5, 0.5, 0.1, 3, 1, 1, 0.5])
    traits = np.array([[trait_defaults.copy() for i in range(80)] for j in range(60)])

    screen.fill(COLOR_GRID)
    update(screen, cells, 10, traits)

    pygame.display.flip()
    pygame.display.update()

    running = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    update(screen, cells, 10, traits)
                    pygame.display.update()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cells[pos[1] // 10, pos[0] // 10] = 1
                update(screen, cells, 10, traits)
                pygame.display.update()

        screen.fill(COLOR_GRID)

        if running:
            cells, traits = update(screen, cells, 10, traits, progress=True)
            pygame.display.update()

        time.sleep(0.001)

if __name__ == '__main__':
    main()

