from classes import *
from typing import List


def draw_window(win: pygame.Surface, bird: Bird, pipes: List[Pipe], base: Base, score: int, highscore: int) -> None:
    win.blit(bg_img, (0, 0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)

    bird.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score), 1, WHITE_COLOR)
    win.blit(score_label, (WIN_WIDTH - score_label.get_width() - 15, 10))

    highscore_label = STAT_FONT.render("Highscore: " + str(highscore), 1, WHITE_COLOR)
    win.blit(highscore_label, (10, 10))

    pygame.display.update()


def main() -> None:
    global WIN, HIGHSCORE
    win = WIN

    bird = Bird(230, 350)
    base = Base(FLOOR)
    pipes = [Pipe(700)]
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                bird.jump()

        bird.move()
        base.move()

        if bird.y + bird.img.get_height() - 10 >= FLOOR or bird.y < -50:
            main()

        remove_pipes = []
        add_pipe = False
        for pipe in pipes:
            pipe.move()

            if pipe.collide(bird):
                main()

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                remove_pipes.append(pipe)

        if add_pipe:
            score += 1

            if score > HIGHSCORE:
                HIGHSCORE = score

            pipes.append(Pipe(WIN_WIDTH))

        for pipe in remove_pipes:
            pipes.remove(pipe)

        draw_window(WIN, bird, pipes, base, score, HIGHSCORE)


if __name__ == '__main__':
    main()
