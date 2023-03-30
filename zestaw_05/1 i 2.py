import pygame, sys

def main():
    clock = pygame.time.Clock()
    fps = 60
    dt = 1.0 / float(fps)

    pygame.display.set_caption('Caption')

    pygame.mixer.music.load(r'music.mp3')
    pygame.mixer.music.play(-1)

    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)

    speed = [0.0, 0.0]
    accel = [5, 5]
    g = [0, 9.81]

    image = pygame.image.load(r'moon.jpg')
    image = pygame.transform.scale(image, size)

    surf_center = (
        (width - image.get_width()) / 2,
        (height - image.get_height()) / 2
    )

    screen.blit(image, surf_center)
    ball = pygame.image.load('ball.gif')
    ball = pygame.transform.scale(ball, (ball.get_width() // 2, ball.get_height() // 2))

    screen.blit(ball, (width/2, height/2))

    ballrect = ball.get_rect(center=(width/2, height/2))
    pygame.display.flip()

    while True:
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            sys.exit()

        speed[0] += g[0] * dt
        speed[1] += g[1] * dt

        if keys[pygame.K_UP]:
            speed[1] -= accel[1] * dt
        elif keys[pygame.K_DOWN]:
            speed[1] += accel[1] * dt
        elif keys[pygame.K_LEFT]:
            speed[0] -= accel[0] * dt
        elif keys[pygame.K_RIGHT]:
            speed[0] += accel[0] * dt

        ballrect = ballrect.move(speed)

        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = -speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = -speed[1]

        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    main()
