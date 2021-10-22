import pygame
from sys import exit
import numpy as np
from dataclasses import dataclass

pygame.init()

WIDTH =  HEIGHT = 600

angle: float = 0

screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT))

@dataclass
class Vector3:
    x: float
    y: float
    z: float

points: np.array = np.array([
    Vector3(-50, -50, 50),
    Vector3(50, -50, 50),
    Vector3(50, 50, 50),
    Vector3(-50, 50, 50),
    Vector3(-50, -50, -50),
    Vector3(50, -50, -50),
    Vector3(50, 50, -50),
    Vector3(-50, 50, -50)
    ])

projection: np.array = np.array([
    [ 1, 0, 0 ],
    [ 0, 1, 0 ]
])

def draw():
    screen.fill((10, 10, 10))
    points2D: list[Vector3] = []

    for v in points:

        rotationZ: np.array = np.array([
            [ np.cos(angle), -np.sin(angle), 0 ],
            [ np.sin(angle), np.cos(angle), 0 ],
            [ 0, 0, 1]
        ])

        rotationX: np.array = np.array([
            [ 1, 0, 0 ],
            [ 0, np.cos(angle), -np.sin(angle) ],
            [ 0, np.sin(angle), np.cos(angle) ]
        ])

        rotationY: np.array = np.array([
            [ np.cos(angle), 0, -np.sin(angle) ],
            [ 0, 1, 0 ],
            [ np.sin(angle), 0, np.cos(angle) ]
        ])

        array_vec: np.array = np.array([v.x, v.y, v.z])
        array_vec = np.dot(rotationX, array_vec)
        array_vec = np.dot(rotationY, array_vec)
        array_vec = np.dot(rotationZ, array_vec)
        
        array_vec2D: np.array = np.dot(projection, array_vec)
        
        point: Vector3 = Vector3(array_vec2D[0], array_vec2D[1], 0)
        points2D.append(point)

        #pygame.draw.circle(screen, (250, 250, 250), (WIDTH/2 + point.x, HEIGHT/2 + point.y), 5)

    pygame.draw.polygon(screen, (200, 200, 200), [
        (WIDTH/2 + points2D[0].x, HEIGHT/2 + points2D[0].y),
        (WIDTH/2 + points2D[1].x, HEIGHT/2 + points2D[1].y),
        (WIDTH/2 + points2D[2].x, HEIGHT/2 + points2D[2].y),
        (WIDTH/2 + points2D[3].x, HEIGHT/2 + points2D[3].y)])
    
    pygame.draw.polygon(screen, (220, 220, 220), [
        (WIDTH/2 + points2D[0].x, HEIGHT/2 + points2D[0].y),
        (WIDTH/2 + points2D[4].x, HEIGHT/2 + points2D[4].y),
        (WIDTH/2 + points2D[5].x, HEIGHT/2 + points2D[5].y),
        (WIDTH/2 + points2D[1].x, HEIGHT/2 + points2D[1].y)])
    
    pygame.draw.polygon(screen, (230, 230, 230), [
        (WIDTH/2 + points2D[2].x, HEIGHT/2 + points2D[2].y),
        (WIDTH/2 + points2D[6].x, HEIGHT/2 + points2D[6].y),
        (WIDTH/2 + points2D[5].x, HEIGHT/2 + points2D[5].y),
        (WIDTH/2 + points2D[1].x, HEIGHT/2 + points2D[1].y)])
    
    pygame.draw.polygon(screen, (240, 240, 240), [
        (WIDTH/2 + points2D[3].x, HEIGHT/2 + points2D[3].y),
        (WIDTH/2 + points2D[7].x, HEIGHT/2 + points2D[7].y),
        (WIDTH/2 + points2D[4].x, HEIGHT/2 + points2D[4].y),
        (WIDTH/2 + points2D[0].x, HEIGHT/2 + points2D[0].y)])
    
    pygame.draw.polygon(screen, (190, 190, 190), [
        (WIDTH/2 + points2D[2].x, HEIGHT/2 + points2D[2].y),
        (WIDTH/2 + points2D[3].x, HEIGHT/2 + points2D[3].y),
        (WIDTH/2 + points2D[7].x, HEIGHT/2 + points2D[7].y),
        (WIDTH/2 + points2D[6].x, HEIGHT/2 + points2D[6].y)])

    pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           exit()
    
    angle += 0.0001
    draw()
