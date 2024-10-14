from doublex import Spy
from doublex_expects import have_been_called, have_been_called_with
from expects import expect


class TestSpy:
    def test_spy(self):
        spy = Spy()

        spy.foo()

        expect(spy.foo).to(have_been_called)

    def test_spy_with_args(self):
        spy = Spy()

        spy.foo(1)

        expect(spy.foo).to(have_been_called_with(1))
