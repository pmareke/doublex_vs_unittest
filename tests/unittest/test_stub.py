import unittest
from unittest.mock import MagicMock, Mock


class TestStub(unittest.TestCase):
    def test_stub(self):
        stub = Mock()
        stub.foo = MagicMock(return_value=1)

        result = stub.foo()

        self.assertEqual(result, 1)

    def test_raise_error(self):
        error_message = "Error"
        stub = Mock()
        stub.foo = Mock(side_effect=Exception((error_message)))

        try:
            stub.foo()
        except Exception as e:
            self.assertEqual(str(e), error_message)
