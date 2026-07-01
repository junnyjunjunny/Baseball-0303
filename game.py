from typing import Any
from game_result import GameResult


class Game:
    def __init__(self):
        self._question = ""

    @property
    def question(self):
        raise AttributeError("읽을 수 없는 속성")

    @question.setter
    def question(self, value):
        self._question = value

    def guess(self, guess_number) -> GameResult | None:
        self._assert_illegal_value(guess_number)
        if guess_number == self._question:
            return GameResult(True, 3, 0)
        return None

    def _assert_illegal_value(self, guess_number: str):
        if guess_number is None:
            raise TypeError("입력이 None 입니다.")

        if len(guess_number) != 3:
            raise TypeError("3개의 숫자를 입력해주세요.")

        if not guess_number.isdigit():
            raise TypeError("숫자만 입력해주세요.")

        if self.isDuplicatedNumber(guess_number):
            raise TypeError("중복된 숫자가 있습니다.")

    def isDuplicatedNumber(self, guessNumber) -> Any:
        return guessNumber[0] == guessNumber[1] or \
            guessNumber[1] == guessNumber[2] or \
            guessNumber[2] == guessNumber[0]
