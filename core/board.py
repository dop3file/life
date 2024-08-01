from dataclasses import dataclass
from typing import Type

from pygame import Vector2

from config import Config
from generation import GenerationBase, GenerationRules
from utils import Cell


class BoardList(list):
    def __getitem__(self, index):
        try:
            if isinstance(index, slice):
                return [super(BoardList, self).__getitem__(i) for i in range(*index.indices(len(self)))]
            else:
                return super(BoardList, self).__getitem__(index)
        except (IndexError, TypeError):
            return BoardList([])


class Board:
    def __init__(self, config: Config, generation_rules: GenerationRules):
        self._board = BoardList(
            BoardList([Cell(alive=False, future=False) for _ in range(config.col)]) for _ in range(config.row)
        )
        self.generation = GenerationBase(self._board, generation_rules)

    def update_cell(self, position: Vector2):
        self._board[int(position.y)][int(position.x)].action()

    def next_generation(self) -> None:
        self.generation.next_generation()

    @property
    def board(self) -> list[list[Cell]]:
        return self._board




