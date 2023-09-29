from src.app.helloer import say_hello


def test_hello(hello):
    assert say_hello() == "hello"
