from doublex import Mock
from doublex_expects import have_been_satisfied
from expects import expect


class TestMock:
    def test_mock(self):
        with Mock() as mock:
            mock.foo(1, 2)
            mock.bar(3, 4)
            mock.baz(5, 6)

        mock.foo(1, 2)
        mock.bar(3, 4)
        mock.baz(5, 6)

        expect(mock).to(have_been_satisfied)

    def test_mock_order_not_satisfied(self):
        with Mock() as mock:
            mock.foo(1, 2)
            mock.bar(3, 4)
            mock.baz(5, 6)

        mock.bar(3, 4)
        mock.foo(1, 2)
        mock.baz(5, 6)

        expect(mock).not_to(have_been_satisfied)

    def test_mock_calls_not_satisfied(self):
        with Mock() as mock:
            mock.foo(1, 2)
            mock.bar(3, 4)
            mock.baz(5, 6)

        mock.foo(1, 2)
        mock.bar(3, 4)

        expect(mock).not_to(have_been_satisfied)
