import pygame
import os

import utils


class EnemyExlosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(EnemyExlosion, self).__init__()
        self.sprites = []
        for _ in range(1, 17):
            file_name = os.path.join('assets', 'sprites', 'enemy-explosion',f'{_}.png')
            file_name = utils.resource_path(file_name)
            self.sprites.append(pygame.image.load(file_name).convert_alpha())

        self.atual_sprite = 0
        self.rect = self.sprites[0].get_rect(center=(x, y))

    def update(self, screen_surface):
        screen_surface.blit(self.sprites[self.atual_sprite], self.rect)
        self.atual_sprite += 1
        if self.atual_sprite == len(self.sprites):
            self.atual_sprite = 0
            self.kill()

