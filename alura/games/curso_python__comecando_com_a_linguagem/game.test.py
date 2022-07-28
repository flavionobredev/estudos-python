import unittest
import game
import sys
import io

DEFAULT_MAX_ATTEMPTS = 10


class TestGame(unittest.TestCase):

  def test_should_return_false_if_invalid_number(self):
    sys.stdin = io.StringIO('mano raw')
    result = game.make_attempt(DEFAULT_MAX_ATTEMPTS)
    self.assertFalse(result.get('match'))
    self.assertEqual(result.get('message'),
                     'Por favor, digite um número válido.')

  def test_should_return_info_that_the_number_is_greater_than_expected(self):
    sys.stdin = io.StringIO('5')
    result = game.make_attempt(DEFAULT_MAX_ATTEMPTS)
    self.assertFalse(result.get('match'))
    self.assertEqual(result.get('message'),
                     'Quase! Você digitou um número menor.')

  def test_should_return_info_that_the_number_is_smaller_than_expected(self):
    sys.stdin = io.StringIO('31')
    result = game.make_attempt(DEFAULT_MAX_ATTEMPTS)
    self.assertFalse(result.get('match'))
    self.assertEqual(result.get('message'),
                     'Opa! Você digitou um número maior.')

  def test_should_be_success_when_match_the_expected_number(self):
    sys.stdin = io.StringIO('10')
    result = game.make_attempt(DEFAULT_MAX_ATTEMPTS)
    self.assertTrue(result.get('match'))
    self.assertEqual(result.get('message'), 'Você acertou! O número correto é 10 :)')


if __name__ == '__main__':
  unittest.main()
