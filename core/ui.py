from typing import Callable

import pygame
from pygame.color import THECOLORS


class UIElement:
    def draw(self, *args, **kwargs):
        ...


class Button(UIElement):
    def __init__(self, x, y, width, height, color, text, text_color, font_size):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.text_color = text_color
        self.font = pygame.font.Font(None, font_size)
        self.rect = pygame.Rect(x, y, width, height)
        self._state = False

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, mouse_pos, mouse_pressed):
        if self.rect.collidepoint(mouse_pos) and mouse_pressed:
            return True
        return False

    def click(self) -> None:
        self._state = not self.state

    def update_text(self, text: str) -> None:
        self.text = text

    def update_text_by_state(self, callback: Callable) -> None:
        self.text = callback(self.state)

    @property
    def state(self) -> bool:
        return self._state


class UIFactory:
    @staticmethod
    def create_start_button() -> Button:
        return Button(
            x=50,
            y=700,
            width=100,
            height=50,
            color=THECOLORS["orange"],
            text_color=THECOLORS["black"],
            font_size=36,
            text="Начать"
        )