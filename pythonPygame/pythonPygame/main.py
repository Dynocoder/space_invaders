import pygame
import random
import time
import math

pygame.init()

# resolution
winX = 800
winY = 600


# Icon and Title
window = pygame.display.set_mode((winX, winY))
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("space-invaders.png")
pygame.display.set_icon(icon)


# Background
background = pygame.image.load("background.png")


# player image
playerImg = pygame.image.load("spaceship.png")
playerX = 370
playerY = 480
playerX_Change = 0


# enemy image
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0, 736)
enemyY = 35
enemyX_Change = 2
enemyY_Change = 32
visible = True


# enemy function


def enemy(x, y):
    window.blit(enemyImg, (x, y))


# Bullet
bulletImg = pygame.image.load("bullet.png")
bulletY_Change = 10
bulletY = 480
bulletX = 0
bullet_state = "ready"
currentY = 0


# Explosion
explosionImg = pygame.image.load("explosion1.png")


def explode(x, y):
    window.blit(explosionImg, (enemyX, enemyY))



# collision


def has_collided(enemyX, bulletX, enemyY, bulletY):
    global visible
    collision_dist = math.sqrt(math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2))
    if collision_dist < 35:
        return True
    else:
        return False


def bullet(x, y):
    global bulletY
    window.blit(bulletImg, (x+16, y+10))
    bulletY -= bulletY_Change



# player function

def player(x, y):
    window.blit(playerImg, (x, y))

# score
score = 0

font = pygame.font.Font(None, 40)
scoretext = font.render("Score : " + str(score), True, (255, 255, 255))


# Game Over
font = pygame.font.Font(None, 95)

gameOverText = font.render("GAME OVER", True, (255, 255, 255))
gameover = False

running = True

while running:

    window.fill((0, 0, 0))
    # Initialize Background
    window.blit(background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Movement mechs
        if event.type == pygame.KEYDOWN:
            # Space key pressed
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                bullet_state = "fire"
            # Movement Keys (a) pressed
            if event.key == pygame.K_a:
                playerX_Change = -4
            # Movement Keys (d) pressed
            if event.key == pygame.K_d:
                playerX_Change = 4
        # Movement key (a) and (d) released
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_Change = 0
                # Fire key space pressed
            if event.type == pygame.K_SPACE:
                bullet_state = "ready"
    # Bullet
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        bullet(bulletX, bulletY)


    # Bullet Collision
    if has_collided(enemyX, bulletX, enemyY, bulletY) is True:
        bulletY = 480
        bullet_state = "ready"
        enemyX = random.randint(0, 736)
        score += 1
        scoretext = font.render("Score : " + str(score), True, (255, 255, 255))


    # Player out of bound and movement

    playerX += playerX_Change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736
    player(playerX, playerY)

    # Enemy Movement/Spawning
    enemy(enemyX, enemyY)

    # Enemy out of bound and Movement
    enemyX += enemyX_Change
    if enemyX <= 0:
        enemyX_Change = 2
        enemyY += enemyY_Change
    if enemyX >= 736:
        enemyX_Change = -2
        enemyY += enemyY_Change
    # Game Over
    if enemyY >= 420:
        window.blit(gameOverText, (200, 200))
        gameover = True
        time.sleep(3)

    if gameover:
        time.sleep(3)
        running = False



    # Score
    window.blit(scoretext, (10, 10))

    pygame.display.update()
