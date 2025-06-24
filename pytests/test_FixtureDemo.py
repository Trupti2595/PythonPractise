import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixturedemo(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo1(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo2(self):
        print("I will execute steps in fixture demo")

    def test_fixturedemo3(self):
        print("I will execute steps in fixture demo")
