import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


# 🧾 Load high score from file (or create it if missing)
def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read().strip())
    except (FileNotFoundError, ValueError):
        return 0


# 💾 Save new high score
def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))
        file.flush()  # ✅ ensures the data is written immediately


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroid Game with High Score")
    clock = pygame.time.Clock()

    # Sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Containers
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    Player.containers = (updatable, drawable)

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0
    score = 0
    high_score = load_high_score()

    font = pygame.font.Font(None, 36)
    game_over_font = pygame.font.Font(None, 72)

    game_over = False
    game_over_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_high_score(high_score)
                pygame.quit()
                sys.exit()

        if not game_over:
            updatable.update(dt)

            # Collision detection
            for asteroid in asteroids:
                # Player collision -> Game Over
                if asteroid.collides_with(player):
                    game_over = True
                    game_over_time = pygame.time.get_ticks()

                    # ✅ Update high score first
                    if score > high_score:
                        high_score = score
                        save_high_score(high_score)

                # Shot collision -> Destroy asteroid and add points
                for shot in shots:
                    if asteroid.collides_with(shot):
                        shot.kill()
                        asteroid.split()
                        score += 10
                        if score > high_score:
                            high_score = score
                            save_high_score(high_score)

        # Draw everything
        screen.fill("black")

        # Draw scores
        score_text = font.render(f"Score: {score}", True, "white")
        high_score_text = font.render(f"Best: {high_score}", True, "yellow")
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 40))

        for obj in drawable:
            obj.draw(screen)

        # Game Over Display
        if game_over:
            text1 = game_over_font.render("GAME OVER!", True, "red")
            text2 = font.render(f"Score: {score}", True, "white")
            text3 = font.render(f"Best: {high_score}", True, "yellow")

            screen.blit(text1, text1.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 40)))
            screen.blit(text2, text2.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 10)))
            screen.blit(text3, text3.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 50)))

            # Wait 3 seconds before quitting
            if pygame.time.get_ticks() - game_over_time > 3000:
                save_high_score(high_score)  # ✅ Make sure it’s saved before quitting
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
