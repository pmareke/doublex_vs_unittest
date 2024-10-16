import unittest
from unittest.mock import MagicMock, Mock


class TestSpy(unittest.TestCase):
    def test_spy(self):
        spy = Mock()
        spy.foo = MagicMock()

        spy.foo()

        spy.foo.assert_called()

    def test_spy_with_args(self):
        spy = Mock()
        spy.foo = MagicMock()

        spy.foo(1)

        spy.foo.assert_called_with(1)

    def test_spy_with_multiple_calls(self):
        spy = Mock()
        spy.foo = MagicMock()

        spy.foo(1)
        spy.foo(2)

        self.assertEqual(spy.foo.call_count, 2)
