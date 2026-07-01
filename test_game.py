import pytest
from game import Game


@pytest.fixture
def game():
    return Game()


def assert_illegal_argument(game: Game, guessNumber: str):
    try:
        game.guess(guessNumber)
        pytest.fail()
    except TypeError:
        pass


def test_exception_when_invalid_input(game):
    assert_illegal_argument(game, 'None')
    assert_illegal_argument(game, "12")
    assert_illegal_argument(game, "1234")
    assert_illegal_argument(game, "abc")
    assert_illegal_argument(game, "1b3")
    assert_illegal_argument(game, "121")