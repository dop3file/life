import pygame
from pygame import Surface, Vector2
from pygame.color import THECOLORS

from core.board import Board
from core.config import Config
from core.ui import UIFactory


class Game:
    def __init__(self, config: Config, board: Board):
        self.config = config
        self.board = board
        pygame.init()
        self.screen = pygame.display.set_mode([config.width, config.height])

    def draw_border_rect(self, screen: Surface, position: Vector2, is_alive: bool) -> None:
        pygame.draw.rect(
            screen,
            THECOLORS["black"] if is_alive else THECOLORS["white"],
            (position.x, position.y, self.config.cell_size, self.config.cell_size),
            0
        )

    def draw_line(self, screen: Surface, start: Vector2, end: Vector2) -> None:
        pygame.draw.line(screen, THECOLORS["black"], start, end)

    def draw_board(self):
        board = self.board.board
        for y in range(len(board)):
            for x in range(len(board[0])):
                self.draw_border_rect(
                    self.screen,
                    Vector2(y=y * self.config.cell_size, x=x * self.config.cell_size),
                    board[y][x].alive
                )

    def draw_borders(self):
        board = self.board.board
        for x in range(1, self.config.col):
            self.draw_line(
                screen=self.screen,
                start=Vector2(x=x * self.config.cell_size, y=0),
                end=Vector2(x=x * self.config.cell_size, y=self.config.cell_size * self.config.row)
            )

        for y in range(1, self.config.row + 1):
            self.draw_line(
                screen=self.screen,
                start=Vector2(x=0, y=y * self.config.cell_size),
                end=Vector2(x=self.config.cell_size * self.config.width, y=y * self.config.cell_size)
            )

    def run(self):
        start_button = UIFactory().create_start_button()
        clear_button = UIFactory().create_clear_button()
        starting = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if start_button.is_clicked(event.pos, event.button):
                        start_button.click()
                        starting = start_button.state
                        start_button.update_text_by_state(lambda state: "Старт" if not state else "Стоп")
                    elif clear_button.is_clicked(event.pos, event.button):
                        clear_button.click()
                        self.board.clear_board()
                    else:
                        if event.pos[1] <= self.config.cell_size * self.config.row:
                            self.board.update_cell(
                                position=Vector2(
                                    x=event.pos[0] // self.config.cell_size,
                                    y=event.pos[1] // self.config.cell_size
                                )
                            )

            self.screen.fill((255, 255, 255))
            self.draw_board()
            self.draw_borders()
            start_button.draw(self.screen)
            clear_button.draw(self.screen)
            if starting:
                self.board.next_generation()
                pygame.time.wait(100)
            pygame.display.flip()
