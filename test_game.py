import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import game


class TestCheckGuess(unittest.TestCase):
    def test_too_low(self):
        self.assertEqual(game.check_guess(50, 10), "low")

    def test_too_high(self):
        self.assertEqual(game.check_guess(50, 90), "high")

    def test_correct(self):
        self.assertEqual(game.check_guess(50, 50), "correct")


class TestPlay(unittest.TestCase):
    def test_wins_after_guesses(self):
        out = io.StringIO()
        with patch("game.random.randint", return_value=7), \
                patch("builtins.input", side_effect=["1", "9", "7"]), \
                redirect_stdout(out):
            game.play()
        text = out.getvalue()
        self.assertIn("Too low", text)
        self.assertIn("Too high", text)
        self.assertIn("You got it in 3 guesses", text)


if __name__ == "__main__":
    unittest.main()
