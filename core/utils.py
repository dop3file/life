from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Cell:
    alive: bool
    future: bool

    def action(self) -> None:
        self.alive = not self.alive
        self.future = not self.future

    def action_future(self) -> None:
        self.future = not self.future

    def set_alive(self) -> None:
        self.alive = self.future

    def count_alive_neighbours(self, board: list[list["Cell"]], pos: Point):
        return sum(map(lambda x: x.alive, filter(lambda x: isinstance(x, Cell), [
            board[pos.y - 1][pos.x],
            board[pos.y + 1][pos.x],
            board[pos.y][pos.x + 1],
            board[pos.y][pos.x - 1],
            board[pos.y + 1][pos.x + 1],
            board[pos.y - 1][pos.x - 1],
            board[pos.y - 1][pos.x + 1],
            board[pos.y + 1][pos.x - 1],
        ])))