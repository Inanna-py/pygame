import pygame
import pymunk
import pymunk.pygame_util


pygame.init()

w, h = pygame.display.Info().current_w//2, pygame.display.Info().current_h//2
window = pygame.display.set_mode((w, h))
screen_pymunk = pymunk.pygame_util.DrawOptions(window)


space = pymunk.Space()
space.gravity = 0, 9.8

def new_ball(pos):
    radius = 15
    ball_mass = 10
    inercia = pymunk.moment_for_circle(ball_mass, radius*0.8, radius)
    body = pymunk.Body(ball_mass, inercia, pymunk.Body.DYNAMIC)
    body.position = pos
    ball = pymunk.Circle(body, radius)
    ball.fraction = 0.5
    ball.elasticity = 1
    space.add(body, ball)
new_ball([w//2, h//3])
segment = pymunk.Segment(space.static_body, (0, h),(w,h), 10)
segment.elasticity = 0.3
segment.fraction = 0.3
space.add(segment)


fps = 144
while True:
    events = pygame.event.get()
    space.step(1/fps)
    window.fill('#FFFFFF')
    for ev in events:
        if ev.type == pygame.QUIT:
            import sys
            sys.exit()
        if ev.type == pygame.MOUSEBUTTONDOWN:
            new_ball(ev.pos)
    space.debug_draw(screen_pymunk)
    pygame.display.flip()