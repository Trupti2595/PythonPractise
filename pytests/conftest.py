import pytest


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will be execute last")

@pytest.fixture()
def dataload():
    print("User Profile data is being created")
    return ["Trupti", "Bansod", "7350488054"]

@pytest.fixture(params= ["chrome", "Firefox"])
def crossbrowser(request):
    return request.param


