from pyamaze import maze
import pygame, sys, time, random


# Difficulty
# mazesize = 10
mazesize = 20
# mazesize = 30
# mazesize = 50


# Creat random Maze with multiple paths
m = maze(mazesize, mazesize)
m.CreateMaze(loopPercent=30)
# m.run()


mazecoord = m.maze_map
# Adjust size of image and border around maze
offset = 60
frameSizeX = 800
frameSizeY = 800
mul = round((frameSizeX - offset)/mazesize)


pygame.display.set_caption('Maze')
game_window = pygame.display.set_mode((frameSizeX, frameSizeY))


# Colors
black = pygame.Color(0,0,0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)


# Wall Generation
class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width,height))
        self.image.fill((white))
        self.rect = self.image.get_rect(topleft=(x, y))


walls =[]
for xy, nsew in mazecoord.items():
    # print(xy, nsew)
    for dir, bin in nsew.items():


        if dir == 'E' and bin == 0:
            xE = xy[1]*mul
            yE = (xy[0]*mul)-mul


            walls.append(Wall(xE + offset/2, yE + offset/2, 1, mul+1))


        if dir == 'W' and bin == 0:
            xW = (xy[1]*mul)-mul
            yW = (xy[0]*mul)-mul
            walls.append(Wall(xW + offset/2, yW + offset/2, 1, mul+1))


        if dir == 'N' and bin == 0:
            xN = (xy[1]*mul)-mul
            yN = (xy[0]*mul)-mul
            walls.append(Wall(xN + offset/2, yN + offset/2, mul+1, 1))


        if dir == 'S' and bin == 0:
            xS = (xy[1]*mul)-mul
            yS = xy[0]*mul
            walls.append(Wall(xS + offset/2, yS + offset/2, mul+1, 1))


class Player(pygame.sprite.Sprite):
    # def __init__(self, x, y):
    #     super().__init__()
    #     self.image = pygame.Surface((mul-2, mul-2))
    #     self.image.fill(red)
    #     self.rect = self.image.get_rect(topleft=(x, y))
    #     self.speed = 1


    # def update(self):
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         self.rect.x -= self.speed
    #     if keys[pygame.K_RIGHT]:
    #         self.rect.x += self.speed
    #     if keys[pygame.K_UP]:
    #         self.rect.y -= self.speed
    #     if keys[pygame.K_DOWN]:
    #         self.rect.y += self.speed


    #     # Check for collisions with walls
    #     wall_collisions = pygame.sprite.spritecollide(self, walls, False)
    #     for wall in wall_collisions:
    #         if self.rect.left < wall.rect.left:
    #             self.rect.right = wall.rect.left
    #         elif self.rect.right > wall.rect.right:
    #             self.rect.left = wall.rect.right
    #         elif self.rect.top < wall.rect.top:
    #             self.rect.bottom = wall.rect.top
    #         elif self.rect.bottom > wall.rect.bottom:
    #             self.rect.top = wall.rect.bottom
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((mul - 2, mul - 2))
        self.image.fill(red)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5


    def update(self):
        keys = pygame.key.get_pressed()
        movement = pygame.Vector2(0, 0)  # Track intended movement direction


        # Determine movement based on key press
        if keys[pygame.K_LEFT]:
            movement.x = -self.speed
        elif keys[pygame.K_RIGHT]:
            movement.x = self.speed
        if keys[pygame.K_UP]:
            movement.y = -self.speed
        elif keys[pygame.K_DOWN]:
            movement.y = self.speed


        # Apply movement
        self.rect.x += movement.x
        self.rect.y += movement.y


        # Check for collisions with walls
        wall_collisions = pygame.sprite.spritecollide(self, walls, False)
        for wall in wall_collisions:
            if movement.x < 0:  # Moving left
                self.rect.left = wall.rect.right
            elif movement.x > 0:  # Moving right
                self.rect.right = wall.rect.left
            elif movement.y < 0:  # Moving up
                self.rect.top = wall.rect.bottom
            elif movement.y > 0:  # Moving down
                self.rect.bottom = wall.rect.top


player = Player((offset // 2), (offset // 2))
all_sprites = pygame.sprite.Group(player, *walls)
clock = pygame.time.Clock()


# Game Loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()


    all_sprites.update()
    game_window.fill((black))
    all_sprites.draw(game_window)
    pygame.display.flip()
    clock.tick(60)


   



