#Any pytest file name should start with 'test_' or end with "_test"
#anything you need to write in pytest, it should be in function
#whenever you declare function, method name always should star with "test_"
import pytest

#Fixture: we can define anywhere in the program


@pytest.mark.smoke
@pytest.mark.xfail #This will run, but not show the result
def test_firstprogram1(setup):
    print("hello")
#@pytest.mark.skip #Skipping this test case
def test_secondprogram():
    a = 5
    b = 6
    assert a+6 == 10
