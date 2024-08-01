from core.board import Board
from core.config import Config
from core.game import Game
from core.generation import GenerationRules


if __name__ == "__main__":
    config = Config()
    game = Game(
        config,
        Board(
            config,
            GenerationRules(
                survive=(0, 1, 2, 3, 4, 5, 6, 7, 8),
                born=(1, )
            )
        )
    )
    game.run()