import pytest


@pytest.fixture(autouse=True, scope="module")
def login():
    print("Start testing")
    yield
    print("End testing")