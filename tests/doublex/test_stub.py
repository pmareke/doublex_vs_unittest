from doublex import ANY_ARG, Stub
from expects import be_none, equal, expect, raise_error


class TestStub:
    def test_stub(self):
        with Stub() as stub:
            stub.foo().returns(1)

        result = stub.foo()

        expect(result).to(equal(1))

    def test_stub_with_args(self):
        with Stub() as stub:
            stub.foo(1).returns(1)

        result = stub.foo(1)
        none_result = stub.foo(2)

        expect(result).to(equal(1))
        expect(none_result).to(be_none)

    def test_stub_with_any_args(self):
        with Stub() as stub:
            stub.foo(ANY_ARG).returns(1)

        result = stub.foo(1)
        another_result = stub.foo(2)

        expect(result).to(equal(1))
        expect(another_result).to(equal(1))

    def test_raise_error(self):
        error_message = "Error"
        with Stub() as stub:
            stub.foo().raises(Exception(error_message))

        expect(lambda: stub.foo()).to(raise_error(Exception, error_message))
