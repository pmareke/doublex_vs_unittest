# Doublex vs Unittest

## Stubs

### Doublex:

- There is a `Stub` class that can be used to create a stub object.
- You can define on the fly and in a really simple way the behaviour of the stub.
- You can easily raise an exception when the stub is called.

### UnitTest:

- You can use the `Mock` class to create a `Stub` object.

## Spies

### Doublex:

- There is a `Spy` class that can be used to create a spy object.
- You can easily verify if the spy has been called and with wich values.

### UnitTest:

- You can use the `Mock` class to create a `Spy` object.
    
## Mocks

### Doublex:

- There is a `Mock` class that can be used to create a mock object.
- You can easily define the order and the calls of the mock.

### UnitTest:
    
- You can use the `Mock` class to create a `Mock` object.
- Hard to use.
- Quite difficult to verify if the Mock has been satified.
