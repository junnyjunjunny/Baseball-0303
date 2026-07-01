import pytest
from game import Game


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game: Game, guessNumber: str):
    with pytest.raises(TypeError):
        game.guess(guessNumber)

@pytest.mark.parametrize("invalid_input", [None, "12", "1234", "abc", "1b3", "121"])
def test_exception_when_invalid_input(game, invalid_input : str):
    assert_illegal_argument(game, invalid_input)