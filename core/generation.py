from dataclasses import dataclass

from utils import Point


@dataclass
class GenerationRules:
    born: tuple[int, ...]
    survive: tuple[int, ...]


class GenerationBase:
    def __init__(self, board, rules: GenerationRules):
        self.board = board
        self.rules = rules

    def next_generation(self) -> None:
        edited = []
        board = self.board
        for y in range(len(board)):
            for x in range(len(board[0])):
                count_neighbours = board[y][x].count_alive_neighbours(board, Point(x=x, y=y))
                if not board[y][x].future:
                    if count_neighbours in self.rules.born:
                        board[y][x].action_future()
                        edited.append(board[y][x])
                elif board[y][x].future:
                    if count_neighbours not in self.rules.survive:
                        board[y][x].action_future()
                        edited.append(board[y][x])
        [cell.set_alive() for cell in edited]


class GenerationB3S23(GenerationBase):
    def next_generation(self) -> None:
        ...


class GenerationB3S12345(GenerationBase):
    def next_generation(self) -> None:
        edited = []
        board = self.board
        for y in range(len(board)):
            for x in range(len(board[0])):
                count_neighbours = board[y][x].count_alive_neighbours(board, Point(x=x, y=y))
                if not board[y][x].future:
                    if count_neighbours == 3:
                        board[y][x].action_future()
                        edited.append(board[y][x])
                elif board[y][x].future:
                    if count_neighbours > 5 or count_neighbours < 1:
                        board[y][x].action_future()
                        edited.append(board[y][x])
        [cell.set_alive() for cell in edited]