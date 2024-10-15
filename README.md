# Doublex + Expects vs Unittest

## Stubs

### Doublex + Expects:

- There is a `Stub` class that can be used to create a `Stub` object.
- If you don't define the behaviour of the `stub`, it will return `None` by default.
- You can define on the fly and in a really simple way the behaviour of the stub.
- You can easily raise an exception when the `stub` is called.

### Unittest:

- You have to use the `Mock` class to create a `Stub` object.
- You have to use the `MagicMock` class to define the behaviour of the stub.
- You have to use the `Mock` and the `side_effect` attribute to raise an exception when the stub is called.

## Spies

### Doublex + Expects:

- There is a `Spy` class that can be used to create a `spy` object.
- You can easily verify if the `spy` has been called.
- You can validate with which values or how many times the `spy` was called.

### Unittest:

- You have to use the `Mock` class to create a `spy` object.
- You have to use the `MagicMock` class to define the behaviour of the `spy`.
- You have to use `assert_called` in the method to validate if the `Spy` was called.
- You have to use `assert_called_with` in the method to validate the values with which the `spy` was called.
    
## Mocks

### Doublex + Expects:

- There is a `Mock` class that can be used to create a `mock` object.
- You can easily define the order and the calls of the `mock` should be called.

### Unittest:
    
- You have to use the `Mock` class to create a `mock` object.
- You have to use `mock_calls` to know the calls of the `mock`.
- It's hard to use.
- It's quite difficult to verify if the Mock has been satified.
