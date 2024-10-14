import unittest
from unittest.mock import Mock, call


class TestMock(unittest.TestCase):
    def test_mock(self):
        m0, m1 = Mock(), Mock()
        m = Mock()
        m.m0, m.m1 = m0, m1

        m0()
        m1()

        assert m.mock_calls == [call.m0(), call.m1()]

    def test_mock_order_not_satisfied(self):
        m0, m1 = Mock(), Mock()
        m = Mock()
        m.m0, m.m1 = m0, m1

        m1()
        m0()

        assert m.mock_calls != [call.m0(), call.m1()]

    def test_mock_calls_not_satisfied(self):
        m0, m1 = Mock(), Mock()
        m = Mock()
        m.m0, m.m1 = m0, m1

        m0()

        assert m.mock_calls != [call.m0(), call.m1()]
